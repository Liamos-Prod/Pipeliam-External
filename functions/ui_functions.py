import sys
import os

def button_and_label_highlight(btn,lab):
    lab.setStyleSheet()

def show_message_status_bar(statusbar,message=None):
    statusbar.showMessage("COMMAND LAUNCHED : "+message+" ",10000)