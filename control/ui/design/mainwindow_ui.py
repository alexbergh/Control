# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 624)
        self.action_change_password = QAction(MainWindow)
        self.action_change_password.setObjectName(u"action_change_password")
        self.action_change_password.setEnabled(False)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_user_settings = QAction(MainWindow)
        self.action_user_settings.setObjectName(u"action_user_settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.begin_date = QDateEdit(self.groupBox)
        self.begin_date.setObjectName(u"begin_date")
        self.begin_date.setMinimumSize(QSize(90, 0))
        self.begin_date.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.begin_date)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.end_date = QDateEdit(self.groupBox)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(90, 0))
        self.end_date.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.end_date)

        self.select_dates = QPushButton(self.groupBox)
        self.select_dates.setObjectName(u"select_dates")
        self.select_dates.setMaximumSize(QSize(20, 23))

        self.horizontalLayout.addWidget(self.select_dates)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.split_view = QRadioButton(self.groupBox_2)
        self.split_view.setObjectName(u"split_view")
        self.split_view.setChecked(True)

        self.horizontalLayout_4.addWidget(self.split_view)

        self.join_view = QRadioButton(self.groupBox_2)
        self.join_view.setObjectName(u"join_view")

        self.horizontalLayout_4.addWidget(self.join_view)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.horizontalSpacer = QSpacerItem(13, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.open_instruction = QPushButton(self.centralwidget)
        self.open_instruction.setObjectName(u"open_instruction")

        self.horizontalLayout_3.addWidget(self.open_instruction)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.authorization = QPushButton(self.centralwidget)
        self.authorization.setObjectName(u"authorization")

        self.horizontalLayout_2.addWidget(self.authorization)

        self.add_inspection = QPushButton(self.centralwidget)
        self.add_inspection.setObjectName(u"add_inspection")

        self.horizontalLayout_2.addWidget(self.add_inspection)

        self.exit_app = QPushButton(self.centralwidget)
        self.exit_app.setObjectName(u"exit_app")

        self.horizontalLayout_2.addWidget(self.exit_app)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 968, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_reports = QMenu(self.menubar)
        self.menu_reports.setObjectName(u"menu_reports")
        self.menu_inspectors = QMenu(self.menubar)
        self.menu_inspectors.setObjectName(u"menu_inspectors")
        self.menu_responsible = QMenu(self.menubar)
        self.menu_responsible.setObjectName(u"menu_responsible")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_inspectors.menuAction())
        self.menubar.addAction(self.menu_responsible.menuAction())
        self.menubar.addAction(self.menu_reports.menuAction())
        self.menu.addAction(self.action_user_settings)
        self.menu.addAction(self.action_change_password)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u043f\u0440\u043e\u0432\u0435\u0440\u043e\u043a", None))
        self.action_change_password.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435", None))
        self.action_user_settings.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e", None))
        self.select_dates.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0432\u0438\u0434", None))
        self.split_view.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0439", None))
        self.join_view.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0435\u043d\u043d\u044b\u0439", None))
        self.open_instruction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.authorization.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.add_inspection.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.exit_app.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_reports.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.menu_inspectors.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u044e\u0449\u0438\u0439", None))
        self.menu_responsible.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439", None))
    # retranslateUi

