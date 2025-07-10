# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PL_splash.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import utils.utils_rc

class Ui_PL_splash(object):
    def setupUi(self, PL_splash):
        if not PL_splash.objectName():
            PL_splash.setObjectName(u"PL_splash")
        PL_splash.resize(733, 355)
        PL_splash.setStyleSheet(u"background-color: #313134;")
        self.wdg_main = QWidget(PL_splash)
        self.wdg_main.setObjectName(u"wdg_main")
        self.wdg_main.setStyleSheet(u"background-color: #414752;")
        self.horizontalLayout = QHBoxLayout(self.wdg_main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frm_logo = QFrame(self.wdg_main)
        self.frm_logo.setObjectName(u"frm_logo")
        self.frm_logo.setMaximumSize(QSize(200, 16777215))
        self.frm_logo.setFrameShape(QFrame.NoFrame)
        self.frm_logo.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frm_logo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_logo_pipeliam = QPushButton(self.frm_logo)
        self.btn_logo_pipeliam.setObjectName(u"btn_logo_pipeliam")
        self.btn_logo_pipeliam.setMaximumSize(QSize(16777215, 16777215))
        self.btn_logo_pipeliam.setStyleSheet(u"QPushButton{background-color:transparent;border:none}\n"
"\n"
"QPushButton:hovered{background-color:transparent;border:none}")
        icon = QIcon()
        icon.addFile(u":/logo/logo/logo_green.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_logo_pipeliam.setIcon(icon)
        self.btn_logo_pipeliam.setIconSize(QSize(300, 300))
        self.btn_logo_pipeliam.setChecked(False)
        self.btn_logo_pipeliam.setFlat(True)

        self.verticalLayout.addWidget(self.btn_logo_pipeliam)


        self.horizontalLayout.addWidget(self.frm_logo)

        self.frm_infos = QFrame(self.wdg_main)
        self.frm_infos.setObjectName(u"frm_infos")
        self.frm_infos.setFrameShape(QFrame.NoFrame)
        self.frm_infos.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frm_infos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lab_name = QLabel(self.frm_infos)
        self.lab_name.setObjectName(u"lab_name")
        self.lab_name.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"TrendSansW00-One"])
        font.setPointSize(48)
        font.setBold(False)
        self.lab_name.setFont(font)
        self.lab_name.setStyleSheet(u"color :#37ad74;\n"
"background-color : transparent")
        self.lab_name.setFrameShape(QFrame.NoFrame)
        self.lab_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lab_name)

        self.lab_version = QLabel(self.frm_infos)
        self.lab_version.setObjectName(u"lab_version")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_version.sizePolicy().hasHeightForWidth())
        self.lab_version.setSizePolicy(sizePolicy)
        self.lab_version.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"TrendSansW00-One"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.lab_version.setFont(font1)
        self.lab_version.setStyleSheet(u"color :#37ad74;\n"
"background-color : transparent")
        self.lab_version.setFrameShape(QFrame.NoFrame)
        self.lab_version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lab_version)

        self.lab_text = QLabel(self.frm_infos)
        self.lab_text.setObjectName(u"lab_text")
        self.lab_text.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"TrendSansW00-One"])
        font2.setPointSize(26)
        font2.setBold(False)
        self.lab_text.setFont(font2)
        self.lab_text.setStyleSheet(u"color :#37ad74;\n"
"background-color : transparent")
        self.lab_text.setFrameShape(QFrame.NoFrame)
        self.lab_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lab_text)


        self.horizontalLayout.addWidget(self.frm_infos)

        PL_splash.setCentralWidget(self.wdg_main)
        self.statusbar = QStatusBar(PL_splash)
        self.statusbar.setObjectName(u"statusbar")
        font3 = QFont()
        font3.setFamilies([u"TrendSansW00-One"])
        font3.setPointSize(8)
        self.statusbar.setFont(font3)
        self.statusbar.setStyleSheet(u"color : #FFF;")
        PL_splash.setStatusBar(self.statusbar)

        self.retranslateUi(PL_splash)

        self.btn_logo_pipeliam.setDefault(False)


        QMetaObject.connectSlotsByName(PL_splash)
    # setupUi

    def retranslateUi(self, PL_splash):
        PL_splash.setWindowTitle(QCoreApplication.translate("PL_splash", u"MainWindow", None))
        self.btn_logo_pipeliam.setText("")
        self.lab_name.setText(QCoreApplication.translate("PL_splash", u"Pipeliam", None))
        self.lab_version.setText(QCoreApplication.translate("PL_splash", u"Version 0.1", None))
        self.lab_text.setText(QCoreApplication.translate("PL_splash", u"3D Pipeline tool", None))
    # retranslateUi

