from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import importlib

import ui.PL_logger_ui as PL_logger
import functions.login_functions as login_functions

from main_dashboard import PL_mainDashboard_class
from functions.animation_functions import fade_widget
from functions.login_functions import launch_dashboard


importlib.reload(PL_logger)

class PL_logger_class(QMainWindow):
    def __init__(self,pipeliam_name,pipeliam_version,gc,path):
        super().__init__()

        if hasattr(PL_logger, 'Ui_PL_logger'):
            self.ui = PL_logger.Ui_PL_logger()
            self.ui.setupUi(self)
            self.setWindowTitle(pipeliam_name + pipeliam_version)
        else:
            raise ImportError("Ui_PL_logger class not found in PL_logger_ui")
        self.basic_launch(path)
        self.setup_connections(gc,pipeliam_name,pipeliam_version)
        

    def setup_connections(self,gc,pipeliam_name,pipeliam_version):
        # Exemple : connecter un bouton à une fonction
        self.ui.btn_login.clicked.connect(lambda :self.handle_login(gc,pipeliam_name,pipeliam_version))
        self.ui.lie_username.returnPressed.connect(lambda: self.ui.lie_password.setFocus())
        self.ui.lie_password.returnPressed.connect(self.ui.btn_login.click)

    def basic_launch(self,path):
        self.path = path

    def handle_login(self,gc,pipeliam_name,pipeliam_version):
        self.username = self.ui.lie_username.text()
        password = self.ui.lie_password.text()
        remember_me = self.ui.chb_remember.isChecked()
        print(f"Tentative de login avec : {self.username}/{password}")

        idx_username = login_functions.getting_username(self.username,gc)
        

        if idx_username != None :
            gsheet_password = login_functions.getting_password(idx_username,gc)
            print("User Found -- Connecting...")

            if remember_me == True : 
                if gsheet_password == password :
                    self.role = login_functions.getting_role(gsheet_password,gc)
                    login_functions.password_remember(self.username,gsheet_password,self.role,remember_me,self.path)
                    print("Remember Me activated")
                    print(f"CURRENT ROLE -- {self.role}")
                    print(f"LOGIN AUTHORIZED -- Welcome {self.username}")
                    self.close()
                    launch_dashboard(self,pipeliam_name,pipeliam_version,PL_mainDashboard_class,fade_widget)
                else : 
                    print("Wrong password -- Please retry or contact @liamos_prod")
            else :
                if gsheet_password == password :
                    self.role = login_functions.getting_role(gsheet_password,gc)
                    print("Nothing Remembered")
                    print(f"CURRENT ROLE -- {self.role}")
                    print(f"LOGIN AUTHORIZED -- Welcome {self.username}")
                    self.close()
                    launch_dashboard(self,pipeliam_name,pipeliam_version,PL_mainDashboard_class,fade_widget)
                    
                else : 
                    print("Wrong password -- Please retry or contact @liamos_prod")
        else : 
            print("No User found -- Please contact @liamos_prod")