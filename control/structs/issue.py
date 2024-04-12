from PySide6.QtCore import QDateTime, QObject

from .db import DB


class Issue(QObject):
    def __init__(self, id: int = 0, parent: QObject = None) -> None:
        super().__init__(parent)

        assert type(id) == int

        self.id = id
        if id:
            self._load()
        else:
            self._new()

    def _new(self):
        self.inspection_id = ""
        self.place = ""
        self.issue = ""
        self.repair_before = None
        self.responsible = ""
        self.category = ""
        self.subcategory = ""
        self.measures = ""
        self.repair_date = None
        self.repair_department = ""
        self.repair_user = ""
        self.repair_comment = ""
        self.confirmation_date = None
        self.confirmation_department = ""
        self.confirmation_user = ""
        self.confirmation_comment = ""

    def _load(self):
        cursor = DB.connection().cursor(prepared=True)
        query = """
                SELECT *
                FROM issue
                WHERE id = %s
                """
        params = (self.id,)

        cursor.execute(query, params)
        data = cursor.fetchone()
        cursor.close()

        self.inspection_id = str(data[1])
        self.place = data[2]
        self.issue = data[3]
        self.repair_before = QDateTime(data[4])
        self.responsible = data[5]
        self.category = data[6]
        self.subcategory = data[7]
        self.measures = data[8]
        self.repair_date = QDateTime(data[9])
        self.repair_department = data[10]
        self.repair_user = data[11]
        self.repair_comment = data[12]
        self.confirmation_date = QDateTime(data[13])
        self.confirmation_department = data[14]
        self.confirmation_user = data[15]
        self.confirmation_comment = data[16]

    def __getitem__(self, key):
        match key:
            case 0:
                return self.place
            case 1:
                return self.issue
            case 2:
                return self.responsible
            case 3:
                return self.repair_before
            case 4:
                return self.category
            case 5:
                return self.subcategory
            case 6:
                return self.measures
            case 7:
                if self.repair_date:
                    repair_date = self.repair_date.toString("dd.MM.yyyy hh:mm")
                    field = f"{repair_date}\n{self.repair_department} {self.repair_user}\n{self.repair_comment}"
                    return field
                return None
            case 8:
                if self.confirmation_date:
                    confirmation_date = self.confirmation_date.toString("dd.MM.yyyy hh:mm")
                    field = f"{confirmation_date}\n{self.confirmation_department} {self.confirmation_user}\n{self.confirmation_comment}"
                    return field
                return None
            case _:
                raise BaseException()

    def date_str(self) -> str:
        return self.date.toString("dd.MM.yyyy hh:mm")
