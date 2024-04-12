# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        if not Authorization.objectName():
            Authorization.setObjectName(u"Authorization")
        Authorization.resize(363, 226)
        Authorization.setMinimumSize(QSize(363, 226))
        Authorization.setMaximumSize(QSize(363, 226))
        self.verticalLayout_3 = QVBoxLayout(Authorization)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Authorization)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login = QLineEdit(self.groupBox)
        self.login.setObjectName(u"login")
        self.login.setMaxLength(64)
        self.login.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.login)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Authorization)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.password = QLineEdit(self.groupBox_2)
        self.password.setObjectName(u"password")
        self.password.setMaxLength(64)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.password)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_credentials = QCheckBox(self.groupBox_2)
        self.save_credentials.setObjectName(u"save_credentials")
        self.save_credentials.setChecked(True)

        self.horizontalLayout.addWidget(self.save_credentials)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.ok = QPushButton(Authorization)
        self.ok.setObjectName(u"ok")

        self.horizontalLayout_2.addWidget(self.ok)

        self.cancel = QPushButton(Authorization)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Authorization)

        self.ok.setDefault(True)


        QMetaObject.connectSlotsByName(Authorization)
    # setupUi

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QCoreApplication.translate("Authorization", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("Authorization", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Authorization", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c 64 \u0441\u0438\u043c\u0432\u043e\u043b\u0430", None))
        self.save_credentials.setText(QCoreApplication.translate("Authorization", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c", None))
        self.ok.setText(QCoreApplication.translate("Authorization", u"\u041e\u041a", None))
        self.cancel.setText(QCoreApplication.translate("Authorization", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

