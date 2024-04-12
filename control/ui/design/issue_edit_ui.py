# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'issue_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_IssueEdit(object):
    def setupUi(self, IssueEdit):
        if not IssueEdit.objectName():
            IssueEdit.setObjectName(u"IssueEdit")
        IssueEdit.resize(579, 531)
        self.verticalLayout_5 = QVBoxLayout(IssueEdit)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(IssueEdit)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.category = QComboBox(IssueEdit)
        self.category.setObjectName(u"category")

        self.horizontalLayout_5.addWidget(self.category)

        self.label_4 = QLabel(IssueEdit)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.subcategory = QComboBox(IssueEdit)
        self.subcategory.setObjectName(u"subcategory")

        self.horizontalLayout_5.addWidget(self.subcategory)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(IssueEdit)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.place = QLineEdit(IssueEdit)
        self.place.setObjectName(u"place")

        self.horizontalLayout.addWidget(self.place)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.has_issue = QGroupBox(IssueEdit)
        self.has_issue.setObjectName(u"has_issue")
        self.has_issue.setEnabled(True)
        self.has_issue.setCheckable(True)
        self.has_issue.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.has_issue)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.issue = QTextEdit(self.has_issue)
        self.issue.setObjectName(u"issue")

        self.verticalLayout.addWidget(self.issue)


        self.verticalLayout_5.addWidget(self.has_issue)

        self.groupBox_2 = QGroupBox(IssueEdit)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.measures = QPlainTextEdit(self.groupBox_2)
        self.measures.setObjectName(u"measures")

        self.verticalLayout_2.addWidget(self.measures)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.gbEesponsible = QGroupBox(IssueEdit)
        self.gbEesponsible.setObjectName(u"gbEesponsible")
        self.horizontalLayout_2 = QHBoxLayout(self.gbEesponsible)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.gbEesponsible)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.responsible = QComboBox(self.gbEesponsible)
        self.responsible.setObjectName(u"responsible")

        self.horizontalLayout_2.addWidget(self.responsible)

        self.label_5 = QLabel(self.gbEesponsible)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.repair_before = QDateTimeEdit(self.gbEesponsible)
        self.repair_before.setObjectName(u"repair_before")

        self.horizontalLayout_2.addWidget(self.repair_before)


        self.verticalLayout_5.addWidget(self.gbEesponsible)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.delete_issue = QPushButton(IssueEdit)
        self.delete_issue.setObjectName(u"delete_issue")

        self.horizontalLayout_3.addWidget(self.delete_issue)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.accept = QPushButton(IssueEdit)
        self.accept.setObjectName(u"accept")

        self.horizontalLayout_3.addWidget(self.accept)

        self.cancel = QPushButton(IssueEdit)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_3.addWidget(self.cancel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.retranslateUi(IssueEdit)

        QMetaObject.connectSlotsByName(IssueEdit)
    # setupUi

    def retranslateUi(self, IssueEdit):
        IssueEdit.setWindowTitle(QCoreApplication.translate("IssueEdit", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("IssueEdit", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("IssueEdit", u"\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("IssueEdit", u"\u041e\u0431\u044a\u0435\u043a\u0442", None))
        self.has_issue.setTitle(QCoreApplication.translate("IssueEdit", u"\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None))
        self.issue.setHtml(QCoreApplication.translate("IssueEdit", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; color:#737373;\">\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0439 \u043d\u0435 \u0432\u044b\u044f\u0432\u043b\u0435\u043d\u043e</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("IssueEdit", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.gbEesponsible.setTitle(QCoreApplication.translate("IssueEdit", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435", None))
        self.label_2.setText(QCoreApplication.translate("IssueEdit", u"\u0426\u0435\u0445", None))
        self.label_5.setText(QCoreApplication.translate("IssueEdit", u"\u0423\u0441\u0442\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u043e", None))
        self.delete_issue.setText(QCoreApplication.translate("IssueEdit", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.accept.setText(QCoreApplication.translate("IssueEdit", u"\u041e\u041a", None))
        self.cancel.setText(QCoreApplication.translate("IssueEdit", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

