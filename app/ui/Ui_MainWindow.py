# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindows.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 838)
        self.actionSet_Table = QAction(MainWindow)
        self.actionSet_Table.setObjectName(u"actionSet_Table")
        self.actionGenerate_Table = QAction(MainWindow)
        self.actionGenerate_Table.setObjectName(u"actionGenerate_Table")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TabPane = QTabWidget(self.centralwidget)
        self.TabPane.setObjectName(u"TabPane")
        self.tabSetData = QWidget()
        self.tabSetData.setObjectName(u"tabSetData")
        self.atomos_input = QLineEdit(self.tabSetData)
        self.atomos_input.setObjectName(u"atomos_input")
        self.atomos_input.setGeometry(QRect(120, 100, 131, 22))
        self.Atomo = QLabel(self.tabSetData)
        self.Atomo.setObjectName(u"Atomo")
        self.Atomo.setGeometry(QRect(50, 100, 49, 16))
        self.addAtom = QPushButton(self.tabSetData)
        self.addAtom.setObjectName(u"addAtom")
        self.addAtom.setGeometry(QRect(260, 100, 75, 24))
        self.list_atomos = QTextBrowser(self.tabSetData)
        self.list_atomos.setObjectName(u"list_atomos")
        self.list_atomos.setGeometry(QRect(110, 140, 256, 192))
        self.Premisas = QLabel(self.tabSetData)
        self.Premisas.setObjectName(u"Premisas")
        self.Premisas.setGeometry(QRect(460, 110, 47, 13))
        self.premisas_input = QLineEdit(self.tabSetData)
        self.premisas_input.setObjectName(u"premisas_input")
        self.premisas_input.setGeometry(QRect(530, 100, 131, 22))
        self.addPremisa = QPushButton(self.tabSetData)
        self.addPremisa.setObjectName(u"addPremisa")
        self.addPremisa.setGeometry(QRect(680, 100, 75, 24))
        self.list_atomos_2 = QTextBrowser(self.tabSetData)
        self.list_atomos_2.setObjectName(u"list_atomos_2")
        self.list_atomos_2.setGeometry(QRect(460, 140, 256, 192))
        self.TabPane.addTab(self.tabSetData, "")
        self.tabTable = QWidget()
        self.tabTable.setObjectName(u"tabTable")
        self.TabPane.addTab(self.tabTable, "")

        self.verticalLayout.addWidget(self.TabPane)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 958, 22))
        self.File = QMenu(self.menubar)
        self.File.setObjectName(u"File")
        self.Exit = QMenu(self.menubar)
        self.Exit.setObjectName(u"Exit")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Exit.menuAction())
        self.File.addAction(self.actionSet_Table)
        self.File.addAction(self.actionGenerate_Table)
        self.Exit.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        self.TabPane.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TrueTables", None))
        self.actionSet_Table.setText(QCoreApplication.translate("MainWindow", u"Set Table", None))
        self.actionGenerate_Table.setText(QCoreApplication.translate("MainWindow", u"Generate Table", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.Atomo.setText(QCoreApplication.translate("MainWindow", u"Atomos", None))
        self.addAtom.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.Premisas.setText(QCoreApplication.translate("MainWindow", u"Premisas", None))
        self.addPremisa.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.TabPane.setTabText(self.TabPane.indexOf(self.tabSetData),
                                QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabPane.setTabText(self.TabPane.indexOf(self.tabTable),
                                QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.Exit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi
