from typing import Optional
from PySide6.QtCore import QDateTime, QObject

from .db import DB

class Issue(QObject):
    def __init__(self, id: int = 0, parent: QObject = None) -> None:
        super().__init__(parent)

        if not isinstance(id, int):
            raise ValueError("ID must be an integer")
        
        self.id = id
        if id:
            self._load()
        else:
            self._new()

    def _new(self):
        """Инициализирует новый пустой объект дела."""
        self.inspection_id = None
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
        """Загружает данные дела из базы данных по его ID."""
        try:
            with DB.connection().cursor() as cursor:
                query = "SELECT * FROM issue WHERE id = %s;"
                cursor.execute(query, (self.id,))
                data = cursor.fetchone()
        except Exception as e:
            print(f"Failed to load data for issue with ID {self.id}: {e}")
            raise

        if not data:
            raise ValueError(f"No issue found with ID {self.id}")

        attributes = [
            'inspection_id', 'place', 'issue', 'repair_before', 'responsible',
            'category', 'subcategory', 'measures', 'repair_date', 'repair_department',
            'repair_user', 'repair_comment', 'confirmation_date', 'confirmation_department',
            'confirmation_user', 'confirmation_comment'
        ]
        for attr, value in zip(attributes, data[1:]):  # skipping the first element as it's ID
            setattr(self, attr, QDateTime.fromSecsSinceEpoch(value) if "date" in attr else value)

    def __getitem__(self, key: int) -> Optional[str]:
        """Позволяет доступ к атрибутам дела по индексу."""
        field_map = {
            0: self.place,
            1: self.issue,
            2: self.responsible,
            3: self.repair_before.toString("dd.MM.yyyy hh:mm") if self.repair_before else None,
            4: self.category,
            5: self.subcategory,
            6: self.measures,
            7: (f"{self.repair_date.toString('dd.MM.yyyy hh:mm')}\n{self.repair_department} {self.repair_user}\n{self.repair_comment}"
                if self.repair_date else None),
            8: (f"{self.confirmation_date.toString('dd.MM.yyyy hh:mm')}\n{self.confirmation_department} {self.confirmation_user}\n{self.confirmation_comment}"
                if self.confirmation_date else None)
        }
        return field_map.get(key, None)

    def date_str(self) -> str:
        """Возвращает строковое представление даты."""
        return self.date.toString("dd.MM.yyyy hh:mm") if self.date else ""

