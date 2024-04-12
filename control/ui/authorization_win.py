from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QMessageBox

from ..structs.user import User
from .design.authorization_ui import Ui_Authorization


class AuthorizationWin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)

        self.settings = QSettings()

        self.ui.login.setText(self.settings.value("user/login", ""))
        self.ui.password.setText(self.settings.value("user/password", ""))

        self.ui.ok.clicked.connect(self.accept)
        self.ui.cancel.clicked.connect(self.reject)

    def accept(self) -> None:
        if self.ui.save_credentials.isChecked():
            self.settings.setValue("user/login", self.ui.login.text())
            self.settings.setValue("user/password", self.ui.password.text())
        else:
            self.settings.setValue("user/password", "")

        if User.login(self.ui.login.text(), self.ui.password.text()):
            return super().accept()
        else:
            QMessageBox.warning(None, "Ошибка", "Не верно указаны логин или пароль")
