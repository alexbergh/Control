from PySide6.QtCore import QDateTime, QObject

from .db import DB
from .user import User
from .issues_table_model import IssueTableModel


class Inspection(QObject):
    def __init__(self, id: int = 0, parent: QObject = None) -> None:
        super().__init__(parent)

        assert type(id) == int

        self.id = id
        if id:
            self._load()
        else:
            self._new()

    def _new(self):
        self.work_id = "-"
        self.date = QDateTime.currentDateTime()
        self.level = User.level
        self.type = "Обход"
        self.department = User.department
        self.inspector = User.short_name()
        self.shift = User.shift
        self.issues_model = IssueTableModel(self)

    def _load(self):
        cursor = DB.connection().cursor(prepared=True)
        query = """
                SELECT *
                FROM inspection
                WHERE id = %s
                """
        params = (self.id,)

        cursor.execute(query, params)
        data = cursor.fetchone()
        cursor.close()

        self.work_id = data[1]
        self.date = QDateTime(data[2])
        self.level = data[3]
        self.type = data[4]
        self.department = data[5]
        self.inspector = data[6]
        self.shift = data[7]
        self.issues_model = IssueTableModel(self, self.id)

    def __getitem__(self, key):
        match key:
            case 0:
                return self.work_id
            case 1:
                return self.date
            case 2:
                return self.level
            case 3:
                return self.type
            case 4:
                return self.department
            case 5:
                return self.inspector
            case 6:
                return self.shift
            case 7:
                return self.work_id  # TODO: add functions to issues model
            case 8:
                return self.work_id  # TODO: add functions to issues model
            case _:
                raise BaseException()

    def date_str(self) -> str:
        return self.date.toString("dd.MM.yyyy hh:mm")
