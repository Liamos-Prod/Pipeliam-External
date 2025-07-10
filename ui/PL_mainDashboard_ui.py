# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PL_mainDashboard.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)
import utils.utils_rc

class Ui_PL_mainDashboard(object):
    def setupUi(self, PL_mainDashboard):
        if not PL_mainDashboard.objectName():
            PL_mainDashboard.setObjectName(u"PL_mainDashboard")
        PL_mainDashboard.resize(1354, 491)
        PL_mainDashboard.setStyleSheet(u"background-color: #414752;")
        self.wdg_main_admin = QWidget(PL_mainDashboard)
        self.wdg_main_admin.setObjectName(u"wdg_main_admin")
        self.horizontalLayout_3 = QHBoxLayout(self.wdg_main_admin)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.frm_menu_bar = QFrame(self.wdg_main_admin)
        self.frm_menu_bar.setObjectName(u"frm_menu_bar")
        self.frm_menu_bar.setMaximumSize(QSize(70, 16777215))
        self.frm_menu_bar.setStyleSheet(u"background-color:#313134;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.frm_menu_bar.setFrameShape(QFrame.NoFrame)
        self.frm_menu_bar.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frm_menu_bar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frm_logo = QFrame(self.frm_menu_bar)
        self.frm_logo.setObjectName(u"frm_logo")
        self.frm_logo.setMaximumSize(QSize(16777215, 70))
        self.frm_logo.setFrameShape(QFrame.NoFrame)
        self.frm_logo.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frm_logo)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_logo_pipeliam = QPushButton(self.frm_logo)
        self.btn_logo_pipeliam.setObjectName(u"btn_logo_pipeliam")
        self.btn_logo_pipeliam.setMaximumSize(QSize(150, 16777215))
        self.btn_logo_pipeliam.setStyleSheet(u"QPushButton{background-color:transparent;border:none}\n"
"\n"
"QPushButton:hovered{background-color:transparent;border:none}")
        icon = QIcon()
        icon.addFile(u":/logo/logo/logo_green.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_logo_pipeliam.setIcon(icon)
        self.btn_logo_pipeliam.setIconSize(QSize(70, 70))
        self.btn_logo_pipeliam.setChecked(False)
        self.btn_logo_pipeliam.setFlat(True)

        self.verticalLayout_6.addWidget(self.btn_logo_pipeliam)


        self.verticalLayout_5.addWidget(self.frm_logo)

        self.frm_menu_bar_main = QFrame(self.frm_menu_bar)
        self.frm_menu_bar_main.setObjectName(u"frm_menu_bar_main")
        self.frm_menu_bar_main.setFrameShape(QFrame.NoFrame)
        self.frm_menu_bar_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frm_menu_bar_main)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 332, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.btn_logout = QPushButton(self.frm_menu_bar_main)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMaximumSize(QSize(50, 16777215))
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#313134;\n"
"	icon: url(:/icons/icons/logout_h.png);\n"
"	background-color:transparent;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:transparent;\n"
"	color:#FFF;	\n"
"    icon: url(:/icons/icons/logout_h.png);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_logout.setIcon(icon1)
        self.btn_logout.setIconSize(QSize(25, 25))
        self.btn_logout.setFlat(True)

        self.verticalLayout_8.addWidget(self.btn_logout)


        self.verticalLayout_5.addWidget(self.frm_menu_bar_main)


        self.horizontalLayout_3.addWidget(self.frm_menu_bar)

        self.frm_menu = QFrame(self.wdg_main_admin)
        self.frm_menu.setObjectName(u"frm_menu")
        self.frm_menu.setMaximumSize(QSize(0, 16777215))
        self.frm_menu.setStyleSheet(u"")
        self.frm_menu.setFrameShape(QFrame.NoFrame)
        self.frm_menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frm_menu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.vs_menu_top = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.vs_menu_top)

        self.frm_menu_back = QFrame(self.frm_menu)
        self.frm_menu_back.setObjectName(u"frm_menu_back")
        self.frm_menu_back.setStyleSheet(u"background-color : #626A79;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.frm_menu_back.setFrameShape(QFrame.StyledPanel)
        self.frm_menu_back.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frm_menu_back)


        self.horizontalLayout_3.addWidget(self.frm_menu)

        self.frm_main = QFrame(self.wdg_main_admin)
        self.frm_main.setObjectName(u"frm_main")
        self.frm_main.setFrameShape(QFrame.NoFrame)
        self.frm_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frm_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_top = QFrame(self.frm_main)
        self.frm_top.setObjectName(u"frm_top")
        self.frm_top.setMaximumSize(QSize(16777215, 70))
        self.frm_top.setFrameShape(QFrame.NoFrame)
        self.frm_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frm_top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lab_welcome = QLabel(self.frm_top)
        self.lab_welcome.setObjectName(u"lab_welcome")
        font = QFont()
        font.setFamilies([u"TrendSansW00-One"])
        font.setPointSize(35)
        font.setBold(False)
        self.lab_welcome.setFont(font)
        self.lab_welcome.setStyleSheet(u"color :#37ad74")
        self.lab_welcome.setFrameShape(QFrame.NoFrame)
        self.lab_welcome.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lab_welcome)


        self.verticalLayout.addWidget(self.frm_top)

        self.frm_bot = QFrame(self.frm_main)
        self.frm_bot.setObjectName(u"frm_bot")
        self.frm_bot.setStyleSheet(u"QFrame{background-color:#626A79;border-radius:10px}")
        self.frm_bot.setFrameShape(QFrame.NoFrame)
        self.frm_bot.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_bot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frm_project = QFrame(self.frm_bot)
        self.frm_project.setObjectName(u"frm_project")
        self.frm_project.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	border-width: 5px;\n"
"	border-radius: 17px;\n"
"	margin-left : 60px;\n"
"	margin-right : 60px;\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#313134;\n"
"	background-color:#FFF;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#313134;\n"
"	color:#FFF;	\n"
"    icon: url(:/icons/icons/folder_h.png);\n"
"	margin-left : 65px;\n"
"	margin-right : 65px;\n"
"	margin-top: 5px;\n"
"	margin-bottom : 5px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	color : #FFF;\n"
"}")
        self.frm_project.setFrameShape(QFrame.StyledPanel)
        self.frm_project.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_project)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_project = QPushButton(self.frm_project)
        self.btn_project.setObjectName(u"btn_project")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_project.sizePolicy().hasHeightForWidth())
        self.btn_project.setSizePolicy(sizePolicy)
        self.btn_project.setMaximumSize(QSize(16777215, 250))
        self.btn_project.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	border-width: 5px;\n"
"	border-radius: 17px;\n"
"	margin-left : 60px;\n"
"	margin-right : 60px;\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#313134;\n"
"	background-color:#FFF;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#313134;\n"
"	color:#FFF;	\n"
"    icon: url(:/icons/icons/folder_h.png);\n"
"	margin-left : 65px;\n"
"	margin-right : 65px;\n"
"	margin-top: 5px;\n"
"	margin-bottom : 5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_project.setIcon(icon2)
        self.btn_project.setIconSize(QSize(60, 60))
        self.btn_project.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_project)

        self.lab_project = QLabel(self.frm_project)
        self.lab_project.setObjectName(u"lab_project")
        self.lab_project.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setFamilies([u"TrendSansW00-One"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.lab_project.setFont(font1)
        self.lab_project.setStyleSheet(u"color :#414752;")
        self.lab_project.setFrameShape(QFrame.NoFrame)
        self.lab_project.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.lab_project)


        self.horizontalLayout_2.addWidget(self.frm_project)

        self.frm_library = QFrame(self.frm_bot)
        self.frm_library.setObjectName(u"frm_library")
        self.frm_library.setFrameShape(QFrame.StyledPanel)
        self.frm_library.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm_library)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_library = QPushButton(self.frm_library)
        self.btn_library.setObjectName(u"btn_library")
        sizePolicy.setHeightForWidth(self.btn_library.sizePolicy().hasHeightForWidth())
        self.btn_library.setSizePolicy(sizePolicy)
        self.btn_library.setMaximumSize(QSize(16777215, 250))
        self.btn_library.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	border-width: 5px;\n"
"	border-radius: 17px;\n"
"	margin-left : 60px;\n"
"	margin-right : 60px;\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#313134;\n"
"	background-color:#FFF;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#313134;\n"
"	color:#FFF;	\n"
"    icon: url(:/icons/icons/images_h.png);\n"
"	margin-left : 65px;\n"
"	margin-right : 65px;\n"
"	margin-top: 5px;\n"
"	margin-bottom : 5px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/images.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_library.setIcon(icon3)
        self.btn_library.setIconSize(QSize(60, 60))
        self.btn_library.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_library)

        self.lab_library = QLabel(self.frm_library)
        self.lab_library.setObjectName(u"lab_library")
        self.lab_library.setMaximumSize(QSize(16777215, 60))
        self.lab_library.setFont(font1)
        self.lab_library.setStyleSheet(u"color :#414752;")
        self.lab_library.setFrameShape(QFrame.NoFrame)
        self.lab_library.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.lab_library)


        self.horizontalLayout_2.addWidget(self.frm_library)

        self.frm_team = QFrame(self.frm_bot)
        self.frm_team.setObjectName(u"frm_team")
        self.frm_team.setFrameShape(QFrame.StyledPanel)
        self.frm_team.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_team)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_team = QPushButton(self.frm_team)
        self.btn_team.setObjectName(u"btn_team")
        sizePolicy.setHeightForWidth(self.btn_team.sizePolicy().hasHeightForWidth())
        self.btn_team.setSizePolicy(sizePolicy)
        self.btn_team.setMaximumSize(QSize(16777215, 250))
        self.btn_team.setAutoFillBackground(False)
        self.btn_team.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	border-width: 5px;\n"
"	border-radius: 17px;\n"
"	margin-left : 60px;\n"
"	margin-right : 60px;\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#313134;\n"
"	background-color:#FFF;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#313134;\n"
"	color:#FFF;	\n"
"    icon: url(:/icons/icons/user_h.png);\n"
"	margin-left : 65px;\n"
"	margin-right : 65px;\n"
"	margin-top: 5px;\n"
"	margin-bottom : 5px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_team.setIcon(icon4)
        self.btn_team.setIconSize(QSize(60, 60))
        self.btn_team.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_team)

        self.lab_team = QLabel(self.frm_team)
        self.lab_team.setObjectName(u"lab_team")
        self.lab_team.setMaximumSize(QSize(16777215, 60))
        self.lab_team.setFont(font1)
        self.lab_team.setStyleSheet(u"color :#414752;")
        self.lab_team.setFrameShape(QFrame.NoFrame)
        self.lab_team.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.lab_team)


        self.horizontalLayout_2.addWidget(self.frm_team)


        self.verticalLayout.addWidget(self.frm_bot)


        self.horizontalLayout_3.addWidget(self.frm_main)

        PL_mainDashboard.setCentralWidget(self.wdg_main_admin)
        self.statusbar = QStatusBar(PL_mainDashboard)
        self.statusbar.setObjectName(u"statusbar")
        font2 = QFont()
        font2.setFamilies([u"TrendSansW00-One"])
        font2.setPointSize(8)
        self.statusbar.setFont(font2)
        self.statusbar.setStyleSheet(u"color : #FFF;background-color: #313134;")
        PL_mainDashboard.setStatusBar(self.statusbar)

        self.retranslateUi(PL_mainDashboard)

        self.btn_logo_pipeliam.setDefault(False)


        QMetaObject.connectSlotsByName(PL_mainDashboard)
    # setupUi

    def retranslateUi(self, PL_mainDashboard):
        PL_mainDashboard.setWindowTitle(QCoreApplication.translate("PL_mainDashboard", u"MainWindow", None))
        self.btn_logo_pipeliam.setText("")
#if QT_CONFIG(statustip)
        self.btn_logout.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_logout.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_logout.setText("")
        self.lab_welcome.setText(QCoreApplication.translate("PL_mainDashboard", u"WELCOME \"USER\"", None))
#if QT_CONFIG(statustip)
        self.btn_project.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_project.setText("")
        self.lab_project.setText(QCoreApplication.translate("PL_mainDashboard", u"Projects", None))
#if QT_CONFIG(statustip)
        self.btn_library.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_library.setText("")
        self.lab_library.setText(QCoreApplication.translate("PL_mainDashboard", u"Library", None))
#if QT_CONFIG(statustip)
        self.btn_team.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_team.setText("")
        self.lab_team.setText(QCoreApplication.translate("PL_mainDashboard", u"Team", None))
    # retranslateUi

