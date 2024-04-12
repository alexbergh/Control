# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'issue_add.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_IssueAdd(object):
    def setupUi(self, IssueAdd):
        if not IssueAdd.objectName():
            IssueAdd.setObjectName(u"IssueAdd")
        IssueAdd.resize(625, 556)
        self.verticalLayout_5 = QVBoxLayout(IssueAdd)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(IssueAdd)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.category = QComboBox(IssueAdd)
        self.category.setObjectName(u"category")

        self.horizontalLayout_5.addWidget(self.category)

        self.label_4 = QLabel(IssueAdd)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.subcategory = QComboBox(IssueAdd)
        self.subcategory.setObjectName(u"subcategory")

        self.horizontalLayout_5.addWidget(self.subcategory)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(IssueAdd)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.place = QLineEdit(IssueAdd)
        self.place.setObjectName(u"place")
        self.place.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.place)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.has_issue = QGroupBox(IssueAdd)
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

        self.groupBox_2 = QGroupBox(IssueAdd)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.measures = QPlainTextEdit(self.groupBox_2)
        self.measures.setObjectName(u"measures")

        self.verticalLayout_2.addWidget(self.measures)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.gbresponsible = QGroupBox(IssueAdd)
        self.gbresponsible.setObjectName(u"gbresponsible")
        self.horizontalLayout_2 = QHBoxLayout(self.gbresponsible)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.responsible = QTableView(self.gbresponsible)
        self.responsible.setObjectName(u"responsible")
        self.responsible.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.responsible.setAlternatingRowColors(True)
        self.responsible.setSelectionMode(QAbstractItemView.SingleSelection)
        self.responsible.horizontalHeader().setVisible(False)
        self.responsible.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.responsible)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.add_resp_all = QPushButton(self.gbresponsible)
        self.add_resp_all.setObjectName(u"add_resp_all")

        self.verticalLayout_4.addWidget(self.add_resp_all)

        self.add_resp = QPushButton(self.gbresponsible)
        self.add_resp.setObjectName(u"add_resp")
        self.add_resp.setStyleSheet(u"QPushButton::menu-indicator{width:0px;}")

        self.verticalLayout_4.addWidget(self.add_resp)

        self.rem_resp = QPushButton(self.gbresponsible)
        self.rem_resp.setObjectName(u"rem_resp")

        self.verticalLayout_4.addWidget(self.rem_resp)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addWidget(self.gbresponsible)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.accept = QPushButton(IssueAdd)
        self.accept.setObjectName(u"accept")

        self.horizontalLayout_3.addWidget(self.accept)

        self.cancel = QPushButton(IssueAdd)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_3.addWidget(self.cancel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.retranslateUi(IssueAdd)

        self.accept.setDefault(True)


        QMetaObject.connectSlotsByName(IssueAdd)
    # setupUi

    def retranslateUi(self, IssueAdd):
        IssueAdd.setWindowTitle(QCoreApplication.translate("IssueAdd", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("IssueAdd", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("IssueAdd", u"\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("IssueAdd", u"\u041e\u0431\u044a\u0435\u043a\u0442", None))
        self.has_issue.setTitle(QCoreApplication.translate("IssueAdd", u"\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None))
        self.issue.setPlaceholderText(QCoreApplication.translate("IssueAdd", u"\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0439 \u043d\u0435 \u0432\u044b\u044f\u0432\u043b\u0435\u043d\u043e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("IssueAdd", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.gbresponsible.setTitle(QCoreApplication.translate("IssueAdd", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435", None))
        self.add_resp_all.setText(QCoreApplication.translate("IssueAdd", u"\u0412\u0441\u0435", None))
        self.add_resp.setText(QCoreApplication.translate("IssueAdd", u"+", None))
        self.rem_resp.setText(QCoreApplication.translate("IssueAdd", u"-", None))
        self.accept.setText(QCoreApplication.translate("IssueAdd", u"\u041e\u041a", None))
        self.cancel.setText(QCoreApplication.translate("IssueAdd", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

