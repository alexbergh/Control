import re
from PySide6.QtWidgets import QTableView, QWidget
from PySide6.QtCore import QSortFilterProxyModel, QModelIndex


class BaseTableView(QTableView):
    """Base class for views"""

    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        self._filters = {}

        # behavior
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.setVerticalScrollMode(QTableView.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollMode(QTableView.ScrollMode.ScrollPerPixel)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.horizontalHeader().setStretchLastSection(True)

        self._proxy_model = QSortFilterProxyModel(parent)
        self.setModel(self._proxy_model)

        self.clicked.connect(self._clicked)
        self.doubleClicked.connect(self._double_clicked)

    # virtual
    def _clicked(self, index: QModelIndex):
        Ellipsis

    # virtual
    def _double_clicked(self, index: QModelIndex):
        Ellipsis

    def apply_filter(self):
        for row in range(self._proxy_model.rowCount()):
            hidden = False
            for column in self._filters:
                data = self._proxy_model.index(row, column).data()
                column_filter = "(" + "|".join(self._filters[column]) + ")"
                if self._filters[column] and data and not re.search(column_filter, data):
                    hidden = True
                self.setRowHidden(row, hidden)

    def add_to_filter(self, column: int, re_filter: str):
        if column not in self._filters:
            self._filters[column] = set()
        self._filters[column].add(re_filter)
        self.apply_filter()

    def remove_from_filter(self, column: int, re_filter: str):
        self._filters[column].remove(re_filter)
        self.apply_filter()

    def set_filter(self, column: int, re_filter: str):
        self._filters[column] = {re_filter}
        self.apply_filter()

    def clear_filter(self, column: int):
        self._filters[column].clear()
        self.apply_filter()
