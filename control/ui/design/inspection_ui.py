# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inspection.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Inspection(object):
    def setupUi(self, Inspection):
        if not Inspection.objectName():
            Inspection.setObjectName(u"Inspection")
        Inspection.resize(1050, 514)
        self.verticalLayout_3 = QVBoxLayout(Inspection)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Inspection)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.inspection_id = QLabel(Inspection)
        self.inspection_id.setObjectName(u"inspection_id")

        self.horizontalLayout_3.addWidget(self.inspection_id)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Inspection)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.inspection_date = QLabel(Inspection)
        self.inspection_date.setObjectName(u"inspection_date")

        self.horizontalLayout_4.addWidget(self.inspection_date)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Inspection)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.department = QLabel(Inspection)
        self.department.setObjectName(u"department")

        self.horizontalLayout.addWidget(self.department)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Inspection)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.inspector = QLabel(Inspection)
        self.inspector.setObjectName(u"inspector")

        self.horizontalLayout_2.addWidget(self.inspector)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(Inspection)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.level = QLabel(Inspection)
        self.level.setObjectName(u"level")

        self.horizontalLayout_6.addWidget(self.level)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(Inspection)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.inspection_type = QComboBox(Inspection)
        self.inspection_type.setObjectName(u"inspection_type")

        self.horizontalLayout_7.addWidget(self.inspection_type)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(Inspection)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.shift = QComboBox(Inspection)
        self.shift.addItem("")
        self.shift.addItem("")
        self.shift.addItem("")
        self.shift.addItem("")
        self.shift.addItem("")
        self.shift.addItem("")
        self.shift.addItem("")
        self.shift.setObjectName(u"shift")

        self.horizontalLayout_8.addWidget(self.shift)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.groupBox = QGroupBox(Inspection)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.issues_layout = QVBoxLayout()
        self.issues_layout.setObjectName(u"issues_layout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.add_issue_button = QPushButton(self.groupBox)
        self.add_issue_button.setObjectName(u"add_issue_button")

        self.horizontalLayout_10.addWidget(self.add_issue_button)

        self.remove_issue_button = QPushButton(self.groupBox)
        self.remove_issue_button.setObjectName(u"remove_issue_button")

        self.horizontalLayout_10.addWidget(self.remove_issue_button)


        self.issues_layout.addLayout(self.horizontalLayout_10)


        self.verticalLayout_4.addLayout(self.issues_layout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.ok = QPushButton(Inspection)
        self.ok.setObjectName(u"ok")

        self.horizontalLayout_11.addWidget(self.ok)

        self.cancel = QPushButton(Inspection)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_11.addWidget(self.cancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)


        self.retranslateUi(Inspection)

        QMetaObject.connectSlotsByName(Inspection)
    # setupUi

    def retranslateUi(self, Inspection):
        Inspection.setWindowTitle(QCoreApplication.translate("Inspection", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443", None))
        self.label.setText(QCoreApplication.translate("Inspection", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.inspection_id.setText(QCoreApplication.translate("Inspection", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Inspection", u"\u0414\u0430\u0442\u0430", None))
        self.inspection_date.setText(QCoreApplication.translate("Inspection", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Inspection", u"\u0426\u0435\u0445", None))
        self.department.setText(QCoreApplication.translate("Inspection", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Inspection", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u044e\u0449\u0438\u0439", None))
        self.inspector.setText(QCoreApplication.translate("Inspection", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Inspection", u"\u0421\u0442\u0443\u043f\u0435\u043d\u044c", None))
        self.level.setText(QCoreApplication.translate("Inspection", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Inspection", u"\u0422\u0438\u043f", None))
        self.label_11.setText(QCoreApplication.translate("Inspection", u"\u0421\u043c\u0435\u043d\u0430", None))
        self.shift.setItemText(0, QCoreApplication.translate("Inspection", u"0", None))
        self.shift.setItemText(1, QCoreApplication.translate("Inspection", u"1", None))
        self.shift.setItemText(2, QCoreApplication.translate("Inspection", u"2", None))
        self.shift.setItemText(3, QCoreApplication.translate("Inspection", u"3", None))
        self.shift.setItemText(4, QCoreApplication.translate("Inspection", u"4", None))
        self.shift.setItemText(5, QCoreApplication.translate("Inspection", u"5", None))
        self.shift.setItemText(6, QCoreApplication.translate("Inspection", u"6", None))

        self.groupBox.setTitle(QCoreApplication.translate("Inspection", u"\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f", None))
        self.add_issue_button.setText(QCoreApplication.translate("Inspection", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.remove_issue_button.setText(QCoreApplication.translate("Inspection", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.ok.setText(QCoreApplication.translate("Inspection", u"\u041e\u041a", None))
        self.cancel.setText(QCoreApplication.translate("Inspection", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

