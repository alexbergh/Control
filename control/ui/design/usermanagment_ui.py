# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usermanagment.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_userManagment(object):
    def setupUi(self, userManagment):
        if not userManagment.objectName():
            userManagment.setObjectName(u"userManagment")
        userManagment.resize(1227, 689)
        self.horizontalLayout = QHBoxLayout(userManagment)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(userManagment)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tvVse = QTableView(self.tab)
        self.tvVse.setObjectName(u"tvVse")
        self.tvVse.setAlternatingRowColors(True)
        self.tvVse.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tvVse.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tvVse.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvVse.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvVse.setSortingEnabled(True)
        self.tvVse.horizontalHeader().setProperty("showSortIndicator", True)
        self.tvVse.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tvVse)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.vAdd = QPushButton(self.tab)
        self.vAdd.setObjectName(u"vAdd")

        self.horizontalLayout_2.addWidget(self.vAdd)

        self.vDel = QPushButton(self.tab)
        self.vDel.setObjectName(u"vDel")

        self.horizontalLayout_2.addWidget(self.vDel)

        self.vSave = QPushButton(self.tab)
        self.vSave.setObjectName(u"vSave")

        self.horizontalLayout_2.addWidget(self.vSave)

        self.vCancel = QPushButton(self.tab)
        self.vCancel.setObjectName(u"vCancel")

        self.horizontalLayout_2.addWidget(self.vCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tvOtchet = QTableView(self.tab_2)
        self.tvOtchet.setObjectName(u"tvOtchet")
        self.tvOtchet.setAlternatingRowColors(True)
        self.tvOtchet.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tvOtchet.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tvOtchet.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvOtchet.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvOtchet.setSortingEnabled(True)
        self.tvOtchet.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tvOtchet)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.oAdd = QPushButton(self.tab_2)
        self.oAdd.setObjectName(u"oAdd")

        self.horizontalLayout_3.addWidget(self.oAdd)

        self.oDel = QPushButton(self.tab_2)
        self.oDel.setObjectName(u"oDel")

        self.horizontalLayout_3.addWidget(self.oDel)

        self.oSave = QPushButton(self.tab_2)
        self.oSave.setObjectName(u"oSave")

        self.horizontalLayout_3.addWidget(self.oSave)

        self.oCancel = QPushButton(self.tab_2)
        self.oCancel.setObjectName(u"oCancel")

        self.horizontalLayout_3.addWidget(self.oCancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tvCeh = QTableView(self.tab_3)
        self.tvCeh.setObjectName(u"tvCeh")
        self.tvCeh.setAlternatingRowColors(True)
        self.tvCeh.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tvCeh.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tvCeh.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvCeh.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvCeh.setSortingEnabled(True)
        self.tvCeh.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tvCeh)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.cAdd = QPushButton(self.tab_3)
        self.cAdd.setObjectName(u"cAdd")

        self.horizontalLayout_4.addWidget(self.cAdd)

        self.cDel = QPushButton(self.tab_3)
        self.cDel.setObjectName(u"cDel")

        self.horizontalLayout_4.addWidget(self.cDel)

        self.cSave = QPushButton(self.tab_3)
        self.cSave.setObjectName(u"cSave")

        self.horizontalLayout_4.addWidget(self.cSave)

        self.cCancel = QPushButton(self.tab_3)
        self.cCancel.setObjectName(u"cCancel")

        self.horizontalLayout_4.addWidget(self.cCancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tvDolj = QTableView(self.tab_4)
        self.tvDolj.setObjectName(u"tvDolj")
        self.tvDolj.setAlternatingRowColors(True)
        self.tvDolj.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tvDolj.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tvDolj.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvDolj.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tvDolj.setSortingEnabled(True)
        self.tvDolj.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tvDolj)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.dAdd = QPushButton(self.tab_4)
        self.dAdd.setObjectName(u"dAdd")

        self.horizontalLayout_5.addWidget(self.dAdd)

        self.dDel = QPushButton(self.tab_4)
        self.dDel.setObjectName(u"dDel")

        self.horizontalLayout_5.addWidget(self.dDel)

        self.dSave = QPushButton(self.tab_4)
        self.dSave.setObjectName(u"dSave")

        self.horizontalLayout_5.addWidget(self.dSave)

        self.dCancel = QPushButton(self.tab_4)
        self.dCancel.setObjectName(u"dCancel")

        self.horizontalLayout_5.addWidget(self.dCancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(userManagment)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(userManagment)
    # setupUi

    def retranslateUi(self, userManagment):
        userManagment.setWindowTitle(QCoreApplication.translate("userManagment", u"Dialog", None))
        self.vAdd.setText(QCoreApplication.translate("userManagment", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.vDel.setText(QCoreApplication.translate("userManagment", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.vSave.setText(QCoreApplication.translate("userManagment", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.vCancel.setText(QCoreApplication.translate("userManagment", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("userManagment", u"\u0412\u0441\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.oAdd.setText(QCoreApplication.translate("userManagment", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.oDel.setText(QCoreApplication.translate("userManagment", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.oSave.setText(QCoreApplication.translate("userManagment", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.oCancel.setText(QCoreApplication.translate("userManagment", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("userManagment", u"\u0414\u043b\u044f \u043e\u0442\u0447\u0435\u0442\u0430", None))
        self.cAdd.setText(QCoreApplication.translate("userManagment", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cDel.setText(QCoreApplication.translate("userManagment", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.cSave.setText(QCoreApplication.translate("userManagment", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cCancel.setText(QCoreApplication.translate("userManagment", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("userManagment", u"\u0426\u0435\u0445\u0430", None))
        self.dAdd.setText(QCoreApplication.translate("userManagment", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.dDel.setText(QCoreApplication.translate("userManagment", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.dSave.setText(QCoreApplication.translate("userManagment", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.dCancel.setText(QCoreApplication.translate("userManagment", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("userManagment", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
    # retranslateUi

