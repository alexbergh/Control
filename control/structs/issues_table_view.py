from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QModelIndex, Qt
from .base_table_view import BaseTableView
from .issues_table_model import IssueTableModel

class IssueTableView(BaseTableView):
    """
    A specialized table view for displaying issues linked to an inspection.
    """

    def __init__(self, parent: QWidget) -> None:
        """
        Initializes the IssueTableView with a specific model.
        """
        super().__init__(parent)
        self._model = IssueTableModel(self)
        self._proxy_model.setSourceModel(self._model)
        self.setDisabled(True)  # Initially disabled until data is fetched

    def change_model(self, model: IssueTableModel):
        """
        Changes the underlying model of the table view.
        """
        self._model = model
        self._proxy_model.setSourceModel(self._model)

    def fetch(self, inspection_id: int):
        """
        Fetches issues related to the specified inspection ID and updates the view.
        """
        self.setDisabled(True)  # Disable view during fetch
        self._model.fetch(inspection_id)
        self.setDisabled(False)  # Re-enable view once data is loaded

    def _double_clicked(self, index: QModelIndex):
        """
        Handles double-click events on the table view.
        """
        if not index.isValid():
            return
        # Consider what action to perform on double-click, for now, just log the index
        print(f"Double-clicked on row: {index.row()}, column: {index.column()}")
