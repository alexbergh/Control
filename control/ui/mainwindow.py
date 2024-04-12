from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtCore import QDate, QSettings, QTimer
from PySide6.QtGui import QIcon, QAction

from control.structs.db import DB
from control.structs.inspections_table_view import InspectionsTableView
from control.structs.issues_table_view import IssueTableView
from control.structs.user import User

from .authorization_win import AuthorizationWin
from .inspection_win import InspectionWin
from .design.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = QSettings()

        # fill all menus
        select_dates_menu = QMenu(self.ui.select_dates)
        select_dates_menu.addAction("За прошлый день", lambda: self.change_selected_dates_days(1))
        select_dates_menu.addAction("За последние 7 дней", lambda: self.change_selected_dates_days(7))
        select_dates_menu.addAction("За последние 30 дней", lambda: self.change_selected_dates_days(30))
        select_dates_menu.addAction("За последние 180 дней", lambda: self.change_selected_dates_days(180))
        select_dates_menu.addAction("За прошлую неделю", self.change_selected_dates_last_week)
        select_dates_menu.addAction("За прошлый месяц", self.change_selected_dates_last_month)
        select_dates_menu.addAction("За прошлый год", self.change_selected_dates_last_year)
        self.ui.select_dates.setMenu(select_dates_menu)

        menu_local_reports = self.ui.menu_reports.addMenu("Местные отчеты")
        menu_local_reports.addAction(QIcon(":/icons/off_excel.png"),
                                     "Результаты контроля ВК СУОТППЭБ",
                                     self.show_auth_window)
        menu_local_reports.addAction(QIcon(":/icons/off_excel.png"),
                                     "Общий итог единоличных проверок за период",
                                     self.show_auth_window)
        menu_local_reports.addAction(QIcon(":/icons/off_excel.png"),
                                     "Анализ устранения 3 ст. контроля за год",
                                     self.show_auth_window)
        menu_local_reports.addAction(QIcon(":/icons/off_excel.png"),
                                     "Информация о результатах проверок за период",
                                     self.show_auth_window)
        menu_local_reports.addAction(QIcon(":/icons/off_excel.png"),
                                     "Общая информация за период",
                                     self.show_auth_window)
        menu_local_reports.addAction(QIcon(":/icons/off_excel.png"),
                                     "Отчет по соревнованиям вахт",
                                     self.show_auth_window)

        menu_irao_reports = self.ui.menu_reports.addMenu("Отчеты для ИНТЕР РАО")
        menu_irao_reports.addAction(QIcon(":/icons/off_excel.png"),
                                    "Итоговый отчет за выбранный период",
                                    self.show_auth_window)

        menu_report_templates = self.ui.menu_reports.addMenu("Шаблоны")
        menu_report_templates.addAction(QIcon(":/icons/off_word.png"),
                                        "Шаблон ППРМ",
                                        self.show_auth_window)

        # menu inspectors
        cursor = DB.connection().cursor()
        query = """SELECT name FROM department WHERE inspector is TRUE ORDER BY name"""
        cursor.execute(query)

        for row in cursor.fetchall():
            action = QAction(row[0], self.ui.menu_inspectors)
            action.setCheckable(True)
            action.triggered.connect(self.set_inspector_filter)
            self.ui.menu_inspectors.addAction(action)

        # menu responsible
        cursor = DB.connection().cursor()
        query = """SELECT name FROM department WHERE responsible is TRUE ORDER BY name"""
        cursor.execute(query)

        for row in cursor.fetchall():
            action = QAction(row[0], self.ui.menu_responsible)
            action.setCheckable(True)
            action.triggered.connect(self.set_responsible_filter)
            self.ui.menu_responsible.addAction(action)

        # tabels
        self.issues = IssueTableView(self)
        self.inspections_table_view = InspectionsTableView(self.issues, self)

        self.ui.splitter.addWidget(self.inspections_table_view)
        self.ui.splitter.addWidget(self.issues)

        # TODO: remove later
        # self.setWindowState(Qt.WindowMaximized)
        self.ui.splitter.restoreState(self.settings.value("splitter/data"))
        self.ui.splitter.splitterMoved.connect(
            lambda: self.settings.setValue("splitter/data", self.ui.splitter.saveState()))

        # TODO: fix connections
        # connections
        self.ui.begin_date.dateChanged.connect(self.apply_filters)
        self.ui.end_date.dateChanged.connect(self.apply_filters)

        # self.ui.inspections.doubleClicked.connect(self.show_auth_window)

        self.ui.action_change_password.triggered.connect(self.show_auth_window)
        self.ui.action_user_settings.triggered.connect(self.show_auth_window)
        self.ui.action_exit.triggered.connect(self.close)

        self.ui.authorization.clicked.connect(self.show_auth_window)
        self.ui.add_inspection.clicked.connect(self.show_inspection_window)
        self.ui.exit_app.clicked.connect(self.close)

        # update dates to load info
        self.change_selected_dates_days(130)
        self.update_timer = QTimer(self)
        self.update_timer.setInterval(5*60*1000)  # every 5 minute
        self.update_timer.timeout.connect(self.timer_update)

    def timer_update(self):
        if self.settings.value("fetch/auto"):
            self.ui.end_date.setDate(QDate.currentDate())

    # ---------------- filters ----------------
    def set_inspector_filter(self):
        sender: QAction = self.sender()
        if sender.isChecked():
            self.inspections_table_view.add_to_filter(4, sender.text())
        else:
            self.inspections_table_view.remove_from_filter(4, sender.text())

    def set_responsible_filter(self):
        sender: QAction = self.sender()
        if sender.isChecked():
            self.inspections_table_view.add_to_filter(7, sender.text())
            self.inspections_table_view.add_to_filter(8, sender.text())
        else:
            self.inspections_table_view.remove_from_filter(7, sender.text())
            self.inspections_table_view.remove_from_filter(8, sender.text())

    def apply_filters(self):
        self.settings.setValue("fetch/auto", self.ui.end_date.date() >= QDate.currentDate())
        begin = self.ui.begin_date.date()
        end = self.ui.end_date.date()
        self.inspections_table_view.fetch(begin, end)

    # ---------------- select dates ----------------
    def change_selected_dates_days(self, days: int):
        begin_date = QDate.currentDate().addDays(-days)
        end_date = QDate.currentDate()
        self.ui.begin_date.setDate(begin_date)
        self.ui.end_date.setDate(end_date)

    def change_selected_dates_last_week(self):
        date = QDate.currentDate().addDays(-7)
        day_of_week = QDate.dayOfWeek(date)
        begin_date = date.addDays(-day_of_week)
        end_date = begin_date.addDays(6)
        self.ui.begin_date.setDate(begin_date)
        self.ui.end_date.setDate(end_date)

    def change_selected_dates_last_month(self):
        date = QDate.currentDate().addMonths(-1)
        begin_date = QDate(date.year(), date.month(), 1)
        end_date = begin_date.addMonths(1).addDays(-1)
        self.ui.begin_date.setDate(begin_date)
        self.ui.end_date.setDate(end_date)

    def change_selected_dates_last_year(self):
        date = QDate.currentDate().addYears(-1)
        begin_date = QDate(date.year(), 1, 1)
        end_date = begin_date.addYears(1).addDays(-1)
        self.ui.begin_date.setDate(begin_date)
        self.ui.end_date.setDate(end_date)

    # ---------------- show windows ----------------
    def show_auth_window(self):
        if (AuthorizationWin(self).exec()):
            title = self.windowTitle().split(" - ")[0]
            self.setWindowTitle(
                title + " - " + User.department + " " + User.short_name())

    def show_inspection_window(self):
        if (InspectionWin(parent=self).exec()):
            print("ok")
        else:
            print("false")
