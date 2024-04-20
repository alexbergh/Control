from PySide6.QtCore import QThread, QDate, Qt, QObject, QModelIndex, Signal
from PySide6.QtWidgets import QMessageBox
from .db import DB
from .inspection import Inspection
from .base_table_model import BaseTableModel
from .issues_table_model import IssueTableModel

class LoaderThread(QThread):
    finished = Signal(bool)
    updateStatus = Signal(int, int)

    def __init__(self, begin_date: QDate, end_date: QDate):
        super().__init__()
        self.begin = begin_date.toString(Qt.DateFormat.ISODate)
        self.end = end_date.addDays(1).toString(Qt.DateFormat.ISODate)
        self.inspections = []

    def run(self):
        try:
            cursor = DB.connection().cursor(prepared=True)
            query = "SELECT id FROM inspection WHERE created BETWEEN %s AND %s;"
            cursor.execute(query, (self.begin, self.end))
            data = cursor.fetchall()
            total = len(data)

            for current, id_tuple in enumerate(data, start=1):
                if self.isInterruptionRequested():
                    self.finished.emit(False)
                    return
                self.inspections.append(Inspection(id_tuple[0]))
                self.updateStatus.emit(current, total)

        except Exception as e:
            print("Error loading data:", e)  # Better to log or signal this back
        finally:
            DB.close_current()
            self.finished.emit(True)

class InspectionsTableModel(BaseTableModel):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.job = None
        self._headers = ("№", "Дата проверки", "Ступень", "Тип", "Цех", "Проверяющий", "Смена", "Активные", "Устраненные")

    def fetch(self, begin_date: QDate, end_date: QDate):
        if self.job and self.job.isRunning():
            self.job.requestInterruption()
            self.job.wait()

        self.clear()
        self.job = LoaderThread(begin_date, end_date)
        self.job.updateStatus.connect(self.updateProgress)
        self.job.finished.connect(self.loadingFinished)
        self.job.start()

    def updateProgress(self, current, total):
        # Update progress in the model, possibly as a special row
        pass

    def loadingFinished(self, success):
        if success:
            self.beginResetModel()
            self._data = self.job.inspections
            self.endResetModel()
        else:
            QMessageBox.critical(None, "Error", "Failed to load inspections.")

    def clear(self):
        self.beginResetModel()
        self._data.clear()
        self.endResetModel()

    def get_issues_model(self, index: QModelIndex) -> IssueTableModel:
        return self._data[index.row()].issues_model

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        return super().data(index, role)
