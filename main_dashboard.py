from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import time
import importlib

import ui.PL_mainDashboard_ui as PL_mainDashboard

from functions import login_functions,ui_functions,animation_functions
from functions.animation_functions import fade_widget

importlib.reload(PL_mainDashboard)

class PL_mainDashboard_class(QMainWindow):
    def __init__(self, username: str, role: str, pipeliam_name : str, pipeliam_version : str):
        super().__init__()

        if hasattr(PL_mainDashboard, 'Ui_PL_mainDashboard'):
            self.ui = PL_mainDashboard.Ui_PL_mainDashboard()
            self.ui.setupUi(self)

            #pipeline internal var
            self.pipeliam_name = pipeliam_name
            self.pipeliam_version = pipeliam_version


            #login internal var
            self.username = username
            self.role = role

            #btn internal var
            self.btn_logout = self.ui.btn_logout
            self.statusbar = self.ui.statusbar

            self.btn_project = self.ui.btn_project
            self.lab_project = self.ui.lab_project

            self.btn_logout

            self.btn_logo_pipeliam = self.ui.btn_logo_pipeliam

            #frm internal var
            self.frm_menu = self.ui.frm_menu

        else:
            raise ImportError("Ui_PL_logger class not found in PL_logger_ui")


        self.setWindowTitle(f"{pipeliam_name}{pipeliam_version} // Main Dashboard -- {self.username} ({self.role})")
        self.adapt_name()
        self.setup_connections()
        self.statusbar.showMessage(f"CONNECTED AS -- {self.role} -- ", 6000)

        self.btn_logo_pipeliam.clicked.connect(animation_functions.toggle_frame_visibility(self.frm_menu,0,70,self.statusbar))

        
        

    def setup_connections(self):
        self.btn_logout.clicked.connect(lambda :self.logout())

    def adapt_name(self):
        self.welcoming = self.ui.lab_welcome
        self.welcoming.setText(f"WELCOME {self.username}")
    
    def logout(self):
        self.close()
        from logger import PL_logger_class
        self.gc = login_functions.getting_creds()
        self.path = login_functions.path_checker(self.pipeliam_name, self.pipeliam_version)
        login_functions.launch_login(self,self.pipeliam_name,self.pipeliam_version,PL_logger_class,fade_widget)
        login_functions.delete_remember(self,True)
      