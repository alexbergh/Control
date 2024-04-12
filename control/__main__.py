import sys

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtTest import QTest
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

from .files import resources_rc  # implicit use
from .structs.db import DB
from .ui.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)

    QCoreApplication.setOrganizationName("UGRES")
    QCoreApplication.setApplicationName("Control")

    splash = QSplashScreen(QPixmap(":/images/logo.jpg"))
    splash.show()

    splash.showMessage("Connecting to DB", Qt.AlignmentFlag.AlignBottom |
                       Qt.AlignmentFlag.AlignHCenter)

    # QTest.qWait(1000)

    DB()  # init DB

    splash.showMessage(DB.status, Qt.AlignmentFlag.AlignBottom |
                       Qt.AlignmentFlag.AlignHCenter)

    # QTest.qWait(1000)

    if not DB.is_valid:
        QTest.qWait(1000)
        sys.exit(0)

    widget = MainWindow()
    splash.finish(widget)
    widget.show()
    exit_code = app.exec()

    DB.close()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
