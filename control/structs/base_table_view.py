import re
from PySide6.QtWidgets import QTableView, QWidget
from PySide6.QtCore import QSortFilterProxyModel, QModelIndex


class BaseTableView(QTableView):
    """Base class for views"""

    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        self._filters: Dict[int, Set[str]] = {}

        # Set up table view behavior
        self._setup_view()
        self._setup_model(parent)

        # Connect signals
        self.clicked.connect(self._clicked)
        self.doubleClicked.connect(self._double_clicked)

        # behavior
    def _setup_view(self):
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.setVerticalScrollMode(QTableView.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollMode(QTableView.ScrollMode.ScrollPerPixel)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.horizontalHeader().setStretchLastSection(True)

    def _setup_model(self, parent: QWidget | None):
        self._proxy_model = QSortFilterProxyModel(parent)
        self.setModel(self._proxy_model)

        self.clicked.connect(self._clicked)
        self.doubleClicked.connect(self._double_clicked)

    # virtual
    def _clicked(self, index: QModelIndex):
        pass

    # virtual
    def _double_clicked(self, index: QModelIndex):
        pass

    def apply_filter(self):
        filter_string = ""
        for column, filters in self._filters.items():
            if filters:
                combined = "(" + "|".join(filters) + ")"
                filter_string += f"(col({column}) {combined}) & "
        if filter_string:
            self._proxy_model.setFilterRegExp(filter_string[:-3])

    def add_to_filter(self, column: int, re_filter: str):
        if column not in self._filters:
            self._filters[column] = set()
        self._filters[column].add(re_filter)
        self.apply_filter()

    def remove_from_filter(self, column: int, re_filter: str):
        if column in self._filters and re_filter in self._filters[column]:
            self._filters[column].remove(re_filter)
            if not self._filters[column]:
                del self._filters[column]
        self.apply_filter()

    def set_filter(self, column: int, re_filter: Set[str]):
        self._filters[column] = re_filter
        self.apply_filter()

    def clear_filter(self, column: int):
        if column in self._filters:
            self._filters.pop(column)
        self.apply_filter()
