from PySide6.QtWidgets import QApplication
import sys

from splash import PL_splash_class

pipeliam_name = "PIPELIAM"
pipeliam_version = ".0.3"

def launch_splash():
    app = QApplication(sys.argv)
    splash = PL_splash_class(pipeliam_name,pipeliam_version)
    splash.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    launch_splash()