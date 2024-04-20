from typing import Any, List, Tuple
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt


class BaseTableModel(QAbstractTableModel):
    """Base class for SQLModel"""

    def __init__(self, parent: QObject) -> None:
        super().__init__(parent)
        self._headers: Tuple[str, ...] = ()
        self._data: List[List[Any]] = []

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Vertical:
            return section
        return self._headers[section] if section < len(self._headers) else None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._data)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._headers)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid() or not (0 <= index.row() < len(self._data)) or not (0 <= index.column() < len(self._headers)):
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def get_id(self, index: QModelIndex | int) -> int:
        if isinstance(index, QModelIndex):
            row = index.row()
        elif isinstance(index, int):
            row = index
        else:
            raise ValueError("Invalid index type")

        if 0 <= row < len(self._data):
            return self._data[row][0]  # Assuming the ID is in the first column
        raise IndexError("Row index out of range")
