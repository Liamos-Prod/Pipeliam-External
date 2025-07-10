from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, Qt
import sys
import time
import importlib

from logger import PL_logger_class
from main_dashboard import PL_mainDashboard_class
import ui.PL_splash_ui as PL_splash


from functions import login_functions
from functions.animation_functions import fade_widget

importlib.reload(PL_splash)


class PL_splash_class(QMainWindow):
    def __init__(self,pipeliam_name :str,pipeliam_version:str):
        super().__init__()

        if hasattr(PL_splash, 'Ui_PL_splash'):
            self.ui = PL_splash.Ui_PL_splash()
            self.ui.setupUi(self)

            # Splashscreen style
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # Lance la vérif après 2 sec
            self.status_bar = self.ui.statusbar
            self.update_version_label(pipeliam_version)
            QTimer.singleShot(1000, lambda : self.verify_connexions(pipeliam_name,pipeliam_version))

            self.gc = login_functions.getting_creds()
            self.path = login_functions.path_checker(pipeliam_name, pipeliam_version)
        else:
            raise ImportError("Ui_PL_splash class not found in PL_splash_ui")

    def verify_connexions(self,pipeliam_name :str,pipeliam_version:str):
        
        self.status_bar.showMessage("Loading -- Checking the credentials...", 1000)
        QTimer.singleShot(1000, lambda : self.step_check_remember(pipeliam_name,pipeliam_version))

    def step_check_remember(self,pipeliam_name,pipeliam_version):
        self.remember, self.password = login_functions.find_remember(self.path, self.gc)

        if self.remember:
            self.status_bar.showMessage("Loading -- User found, getting infos...", 1000)
            QTimer.singleShot(1000, lambda : self.step_load_user(pipeliam_name,pipeliam_version))
        else:
            self.status_bar.showMessage("Loading -- No User found, redirecting...", 1000)
            QTimer.singleShot(1000, lambda : login_functions.launch_login(self,pipeliam_name,pipeliam_version,PL_logger_class,fade_widget))

    def step_load_user(self,pipeliam_name,pipeliam_version):
        self.username, self.role = login_functions.load_remembered_user(self.path, self.password, self.gc)
        self.status_bar.showMessage(f"Welcome {self.username} -- Connexion to the Dashboard...", 1000)
        QTimer.singleShot(1000, lambda : login_functions.launch_dashboard(self,pipeliam_name,pipeliam_version,PL_mainDashboard_class,fade_widget))

    def update_version_label(self,pipeliam_version):
        self.pipeliam_version_label = self.ui.lab_version
        self.pipeliam_version_label.setText(f"VERSION {pipeliam_version.replace(".","",1)}")
