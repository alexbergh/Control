from PySide6.QtCore import QDateTime, QObject
from .db import DB
from .user import User
from .issues_table_model import IssueTableModel


class Inspection(QObject):
    def __init__(self, id: int = 0, parent: QObject = None) -> None:
        super().__init__(parent)
        if not isinstance(id, int):
            raise TypeError("id must be an integer")

        self.id = id
        self._initialize()

        def _initialize(self):
        if self.id:
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
        query = """
                SELECT work_id, date, level, type, department, inspector, shift
                FROM inspection
                WHERE id = %s
                """
        params = (self.id,)
        with DB.connection().cursor(prepared=True) as cursor:
            cursor.execute(query, params)
            data = cursor.fetchone()
            if data:
                self._set_attributes_from_data(data)
            else:
                raise ValueError("No inspection found with ID:", self.id)

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

    def _set_attributes_from_data(self, data):
        (self.work_id, db_date, self.level, self.type, self.department, self.inspector, self.shift) = data
        self.date = QDateTime.fromString(db_date, "yyyy-MM-dd HH:mm:ss")
        self.issues_model = IssueTableModel(self, self.id)

    def __getitem__(self, key):
        attributes = [
            self.work_id, self.date, self.level, self.type,
            self.department, self.inspector, self.shift
        ]
        try:
            return attributes[key]
        except IndexError:
            raise IndexError("Index out of range for inspection attributes")

    def date_str(self) -> str:
        return self.date.toString("dd.MM.yyyy hh:mm")
