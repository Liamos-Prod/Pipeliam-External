# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PL_logger.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import utils.utils_rc

class Ui_PL_logger(object):
    def setupUi(self, PL_logger):
        if not PL_logger.objectName():
            PL_logger.setObjectName(u"PL_logger")
        PL_logger.resize(715, 900)
        self.wdg_main = QWidget(PL_logger)
        self.wdg_main.setObjectName(u"wdg_main")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdg_main.sizePolicy().hasHeightForWidth())
        self.wdg_main.setSizePolicy(sizePolicy)
        self.wdg_main.setStyleSheet(u"background-color: #414752;")
        self.verticalLayout = QVBoxLayout(self.wdg_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_top_logger = QFrame(self.wdg_main)
        self.frm_top_logger.setObjectName(u"frm_top_logger")
        self.frm_top_logger.setMaximumSize(QSize(16777215, 300))
        self.frm_top_logger.setStyleSheet(u"")
        self.frm_top_logger.setFrameShape(QFrame.NoFrame)
        self.frm_top_logger.setFrameShadow(QFrame.Plain)
        self.frm_top_logger.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_top_logger)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frm_logo_pipeliam = QFrame(self.frm_top_logger)
        self.frm_logo_pipeliam.setObjectName(u"frm_logo_pipeliam")
        self.frm_logo_pipeliam.setFrameShape(QFrame.NoFrame)
        self.frm_logo_pipeliam.setFrameShadow(QFrame.Plain)
        self.frm_logo_pipeliam.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frm_logo_pipeliam)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, 20)
        self.btn_logo_pipeliam = QPushButton(self.frm_logo_pipeliam)
        self.btn_logo_pipeliam.setObjectName(u"btn_logo_pipeliam")
        self.btn_logo_pipeliam.setMaximumSize(QSize(16777215, 16777215))
        self.btn_logo_pipeliam.setStyleSheet(u"QPushButton{background-color:transparent;border:none}\n"
"\n"
"QPushButton:hovered{background-color:transparent;border:none}")
        icon = QIcon()
        icon.addFile(u":/logo/logo/logo_green.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_logo_pipeliam.setIcon(icon)
        self.btn_logo_pipeliam.setIconSize(QSize(150, 150))
        self.btn_logo_pipeliam.setChecked(False)
        self.btn_logo_pipeliam.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_logo_pipeliam)

        self.lab_login = QLabel(self.frm_logo_pipeliam)
        self.lab_login.setObjectName(u"lab_login")
        font = QFont()
        font.setFamilies([u"TrendSansW00-One"])
        font.setPointSize(48)
        font.setBold(False)
        self.lab_login.setFont(font)
        self.lab_login.setStyleSheet(u"color :#37ad74")
        self.lab_login.setFrameShape(QFrame.NoFrame)
        self.lab_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lab_login)


        self.horizontalLayout_3.addWidget(self.frm_logo_pipeliam)


        self.verticalLayout.addWidget(self.frm_top_logger)

        self.frame_main_logger = QFrame(self.wdg_main)
        self.frame_main_logger.setObjectName(u"frame_main_logger")
        self.frame_main_logger.setFrameShape(QFrame.NoFrame)
        self.frame_main_logger.setFrameShadow(QFrame.Plain)
        self.frame_main_logger.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main_logger)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frm_login_content = QFrame(self.frame_main_logger)
        self.frm_login_content.setObjectName(u"frm_login_content")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frm_login_content.sizePolicy().hasHeightForWidth())
        self.frm_login_content.setSizePolicy(sizePolicy1)
        self.frm_login_content.setMaximumSize(QSize(16777215, 16777215))
        self.frm_login_content.setFrameShape(QFrame.NoFrame)
        self.frm_login_content.setFrameShadow(QFrame.Plain)
        self.frm_login_content.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frm_login_content)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.lie_username = QLineEdit(self.frm_login_content)
        self.lie_username.setObjectName(u"lie_username")
        self.lie_username.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lie_username.sizePolicy().hasHeightForWidth())
        self.lie_username.setSizePolicy(sizePolicy2)
        self.lie_username.setMinimumSize(QSize(200, 100))
        self.lie_username.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"TrendSansW00-One"])
        font1.setPointSize(20)
        self.lie_username.setFont(font1)
        self.lie_username.setStyleSheet(u"border : none;\n"
"border-bottom : 2px solid #37ad74;\n"
"color : #FFF;\n"
"padding-bottom : 5px")

        self.verticalLayout_3.addWidget(self.lie_username)

        self.lie_password = QLineEdit(self.frm_login_content)
        self.lie_password.setObjectName(u"lie_password")
        self.lie_password.setMinimumSize(QSize(200, 100))
        self.lie_password.setFont(font1)
        self.lie_password.setStyleSheet(u"border : none;\n"
"border-bottom : 2px solid #37ad74;\n"
"color : #FFF;\n"
"padding-bottom : 5px")
        self.lie_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.lie_password)

        self.btn_login = QPushButton(self.frm_login_content)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(0, 100))
        self.btn_login.setFont(font1)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	background-color:#37ad74;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"	border-color : transparent;\n"
"	border-radius: 15px;\n"
"	margin-left : 5px;\n"
"	margin-right : 5px;\n"
"	margin-top: 5px;\n"
"	margin-bottom : 5px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: none;\n"
"}")
        self.btn_login.setFlat(False)

        self.verticalLayout_3.addWidget(self.btn_login)

        self.chb_remember = QCheckBox(self.frm_login_content)
        self.chb_remember.setObjectName(u"chb_remember")
        font2 = QFont()
        font2.setFamilies([u"TrendSansW00-One"])
        font2.setPointSize(16)
        self.chb_remember.setFont(font2)
        self.chb_remember.setStyleSheet(u"QCheckBox{\n"
"	color:#FFF;\n"
"	background-color:#8B94A4;\n"
"	border-color: transparent;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    outline: none;\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/correct_h.png);\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"\n"
"	background-color : #37ad74;\n"
"	border-color : transparent;\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"")
        self.chb_remember.setCheckable(True)
        self.chb_remember.setAutoRepeat(True)
        self.chb_remember.setTristate(False)

        self.verticalLayout_3.addWidget(self.chb_remember)

        self.frm_forgotten_pwd = QFrame(self.frm_login_content)
        self.frm_forgotten_pwd.setObjectName(u"frm_forgotten_pwd")
        self.frm_forgotten_pwd.setFrameShape(QFrame.NoFrame)
        self.frm_forgotten_pwd.setFrameShadow(QFrame.Plain)
        self.frm_forgotten_pwd.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frm_forgotten_pwd)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lab_forgotten_pwd = QLabel(self.frm_forgotten_pwd)
        self.lab_forgotten_pwd.setObjectName(u"lab_forgotten_pwd")
        font3 = QFont()
        font3.setFamilies([u"TrendSansW00-One"])
        font3.setPointSize(12)
        self.lab_forgotten_pwd.setFont(font3)
        self.lab_forgotten_pwd.setStyleSheet(u"color :#37ad74")
        self.lab_forgotten_pwd.setFrameShadow(QFrame.Raised)
        self.lab_forgotten_pwd.setAlignment(Qt.AlignCenter)
        self.lab_forgotten_pwd.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.lab_forgotten_pwd)


        self.verticalLayout_3.addWidget(self.frm_forgotten_pwd)


        self.verticalLayout_2.addWidget(self.frm_login_content)

        self.frm_infos = QFrame(self.frame_main_logger)
        self.frm_infos.setObjectName(u"frm_infos")
        self.frm_infos.setMaximumSize(QSize(16777215, 50))
        self.frm_infos.setFrameShape(QFrame.NoFrame)
        self.frm_infos.setFrameShadow(QFrame.Plain)
        self.frm_infos.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frm_infos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lab_infos = QLabel(self.frm_infos)
        self.lab_infos.setObjectName(u"lab_infos")
        font4 = QFont()
        font4.setFamilies([u"TrendSansW00-One"])
        font4.setPointSize(7)
        self.lab_infos.setFont(font4)
        self.lab_infos.setStyleSheet(u"color :#37ad74")
        self.lab_infos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lab_infos)


        self.verticalLayout_2.addWidget(self.frm_infos)


        self.verticalLayout.addWidget(self.frame_main_logger)

        PL_logger.setCentralWidget(self.wdg_main)

        self.retranslateUi(PL_logger)

        self.btn_logo_pipeliam.setDefault(False)


        QMetaObject.connectSlotsByName(PL_logger)
    # setupUi

    def retranslateUi(self, PL_logger):
        PL_logger.setWindowTitle(QCoreApplication.translate("PL_logger", u"MainWindow", None))
        self.btn_logo_pipeliam.setText("")
        self.lab_login.setText(QCoreApplication.translate("PL_logger", u"Log in", None))
        self.lie_username.setPlaceholderText(QCoreApplication.translate("PL_logger", u"Username", None))
        self.lie_password.setInputMask("")
        self.lie_password.setPlaceholderText(QCoreApplication.translate("PL_logger", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("PL_logger", u"Log In", None))
        self.chb_remember.setText(QCoreApplication.translate("PL_logger", u"Keep me logged in", None))
        self.lab_forgotten_pwd.setText(QCoreApplication.translate("PL_logger", u"Forgot your password ?", None))
        self.lab_infos.setText(QCoreApplication.translate("PL_logger", u"All rights reserved to Liamos Prod\u00a9 2025", None))
    # retranslateUi

