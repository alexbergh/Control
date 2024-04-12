# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ystranit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QHBoxLayout, QListView, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ystranit(object):
    def setupUi(self, ystranit):
        if not ystranit.objectName():
            ystranit.setObjectName(u"ystranit")
        ystranit.resize(711, 439)
        self.verticalLayout_3 = QVBoxLayout(ystranit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(ystranit)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pteText = QPlainTextEdit(self.groupBox)
        self.pteText.setObjectName(u"pteText")

        self.verticalLayout.addWidget(self.pteText)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(ystranit)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lvFiles = QListView(self.groupBox_2)
        self.lvFiles.setObjectName(u"lvFiles")
        self.lvFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lvFiles.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.lvFiles)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbDobavi = QPushButton(self.groupBox_2)
        self.pbDobavi.setObjectName(u"pbDobavi")

        self.horizontalLayout.addWidget(self.pbDobavi)

        self.pbYdal = QPushButton(self.groupBox_2)
        self.pbYdal.setObjectName(u"pbYdal")

        self.horizontalLayout.addWidget(self.pbYdal)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbOK = QPushButton(self.groupBox_2)
        self.pbOK.setObjectName(u"pbOK")

        self.horizontalLayout.addWidget(self.pbOK)

        self.pbCancel = QPushButton(self.groupBox_2)
        self.pbCancel.setObjectName(u"pbCancel")

        self.horizontalLayout.addWidget(self.pbCancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(ystranit)

        QMetaObject.connectSlotsByName(ystranit)
    # setupUi

    def retranslateUi(self, ystranit):
        ystranit.setWindowTitle(QCoreApplication.translate("ystranit", u"\u041e\u0442\u043c\u0435\u0442\u043a\u0430 \u043e\u0431 \u0443\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("ystranit", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ystranit", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.pbDobavi.setText(QCoreApplication.translate("ystranit", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pbYdal.setText(QCoreApplication.translate("ystranit", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pbOK.setText(QCoreApplication.translate("ystranit", u"\u041e\u041a", None))
        self.pbCancel.setText(QCoreApplication.translate("ystranit", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

