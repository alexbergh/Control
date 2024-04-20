from PySide6.QtCore import QObject
from .db import DB
from .base_table_model import BaseTableModel


class SimpleModel(BaseTableModel):
    """
    A simple table model for displaying data from a specified database table.
    """
    def __init__(self, table: str, parent: QObject) -> None:
        super().__init__(parent)
        self.table = self.validate_table_name(table)
        self._headers = ("Name",)
        self.load_data()

    def validate_table_name(self, table: str) -> str:
        """
        Validate the table name to prevent SQL injection. Only allow alphanumeric and underscore characters.
        """
        import re
        if re.match(r'^\w+$', table):
            return table
        else:
            raise ValueError("Invalid table name.")

    def load_data(self):
        """
        Loads data from the database table into the model.
        """
        query = "SELECT name FROM " + self.table + " ORDER BY name;"
        connection = DB.connection()
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            self.beginResetModel()
            self._data = cursor.fetchall()
            self.endResetModel()
        except Exception as e:
            print(f"Failed to fetch data: {e}")  # Consider using logging
        finally:
            cursor.close()
            