from typing import Any
from threading import Thread, Event
from mysql.connector import PoolError

from PySide6.QtCore import QObject, QModelIndex, QPersistentModelIndex, QDate, Qt, QCoreApplication
from PySide6.QtWidgets import QMessageBox

from .db import DB
from .inspection import Inspection

from .base_table_model import BaseTableModel
from .issues_table_model import IssueTableModel


class LoaderThread(Thread):
    """Loader for inspections. Can be stopped at any time to break loading"""

    def __init__(self, begin_date: QDate, end_date: QDate):
        super().__init__()
        self._stop_event = Event()
        self.begin = begin_date.toString(Qt.DateFormat.ISODate)
        self.end = end_date.addDays(1).toString(Qt.DateFormat.ISODate)
        self.current = 0
        self.total = 0
        self.inspections = []
        self.status = False

    def stop(self):
        self._stop_event.set()

    def run(self):
        try:
            cursor = DB.connection().cursor(prepared=True)
        except PoolError:
            print("Ошибка", "Превышен лимит запрсов")
            return

        query = """
                SELECT
                    id
                FROM
                    inspection
                WHERE created BETWEEN %s AND %s;
                """
        params = (self.begin, self.end)
        cursor.execute(query, params)
        data: list = cursor.fetchall()

        self.total = len(data)
        for id in data:
            self.current += 1
            self.inspections.append(Inspection(id[0]))
            if self._stop_event.is_set():
                break

        DB.close_current()
        self.status = True


class InspectionsTableModel(BaseTableModel):
    def __init__(self, parent: QObject) -> None:
        super().__init__(parent)
        self.job = None
        self._headers = (
            "№",
            "Дата проверки",
            "Ступень",
            "Тип",
            "Цех",
            "Проверяющий",
            "Смена",
            "Активные",
            "Устраненные",
        )

    def fetch(self, begin_date: QDate, end_date: QDate):
        if not DB.is_available():
            QMessageBox.critical(None, "Ошибка", "Превышен лимит запрсов. Дождитесь завршения предыдущего запроса.")
            return False

        self.clear()
        self._data = [[""] * len(self._headers)]

        if self.job and self.job.is_alive():
            self.job.stop()

        self.job = LoaderThread(begin_date, end_date)
        self.job.start()

        while self.job.is_alive():
            self.beginResetModel()
            self._data[0][0] = "Загрузка"
            if self.job.current:
                self._data[0][1] = f"{self.job.current}"
                self._data[0][2] = f"из"
                self._data[0][3] = f"{self.job.total}"
            self.endResetModel()

            self.job.join(0.01)
            QCoreApplication.processEvents()

        self.beginResetModel()
        self._data = self.job.inspections
        self.endResetModel()
        return self.job.status

    def clear(self):
        self.beginResetModel()
        self._data.clear()
        self.endResetModel()

    def get_issues_model(self, index: QModelIndex) -> IssueTableModel:
        return self._data[index.row()].issues_model

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        # TODO: fill with color
        return super().data(index, role)

    def setData(self, index: QModelIndex | QPersistentModelIndex, value: Any, role: int = ...) -> bool:
        return super().setData(index, value, role)

    def get_id(self, index: QModelIndex | int) -> int:
        return self._data[index.row()].id
