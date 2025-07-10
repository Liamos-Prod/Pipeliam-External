import os
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials


sheet_id = "YourSheetID"


def path_checker(name,version): #runs a simple function to see if you have the folder Pipeliam
    path = Path.home()/f"{name}{version}"
    if os.path.exists(path) :
        None
    else : 
        os.mkdir(path)

    print(path)
    return path

def password_remember(username,password,current_role,checked,path):
    remember_me = "remember_me.txt"
    path_to_remember_me = os.path.join(str(path)+"/"+remember_me)
    if checked == True :
        if os.path.exists(path_to_remember_me) :
            print('TXT -- File already there')
        else :
            with open(path_to_remember_me,'w') as file :
                file.write(username+"\n"+password)
                print("TXT -- File created")
            file.close()

def find_remember(path,gc):
    remember_me = "remember_me.txt"
    line_list =[]
    state = False
    password_value = "NO PWD"
    path_to_remember_me = os.path.join(str(path)+"/"+remember_me)
    if os.path.exists(path_to_remember_me):
        with open(path_to_remember_me) as file :
            for line in file : 
                line_list.append(line)


     
        sh = gc.open_by_key(sheet_id)
        worksheet = sh.sheet1
        
        line_username_casefold = line_list[0].strip().casefold()
        line_password = line_list[1].strip()

        username_col = worksheet.col_values(2)


        for idx,val in enumerate(username_col,start=1) :
            if val.casefold() == line_username_casefold  :
                password_row = idx
                password_col = worksheet.find("PASSWORD").col
                password_value = worksheet.cell(password_row,password_col).value
                if password_value == line_password :
                    state = True

                else : 
                    None
            else :
                None
        file.close()       
        
    else :
        None
    return state, password_value
    

def getting_creds():
    
    SERVICE_ACCOUNT_FILE = "./YOURCREDS.json"
    scopes=["https://www.googleapis.com/auth/spreadsheets"]

    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=scopes)

    gc = gspread.authorize(creds)
    print("Credentials authorised -- You are connected ")
    return gc

def get_worksheet(gc):
    sh = gc.open_by_key(sheet_id)
    worksheet = sh.sheet1
    return worksheet

def getting_username(username : str,gc):

    username_casefold = username.casefold()
    username_col = get_worksheet(gc).col_values(2)
    for idx, val in enumerate(username_col, start=1):
        if val.casefold() == username_casefold:
            return idx

def getting_password(idx,gc):
    row = idx
    col_password = get_worksheet(gc).find("PASSWORD").col
    current_password = get_worksheet(gc).cell(row, col_password).value
    return current_password

def getting_role(password: str,gc):

    password_row = get_worksheet(gc).find(password).row
    role_col = get_worksheet(gc).find("ROLE").col
    current_role = get_worksheet(gc).cell(password_row, role_col).value
    return current_role

def load_remembered_user(path,password,gc):
    # Simule un .txt ou json contenant les infos
    with open(f"{path}/remember_me.txt", "r") as f:
        lines = f.read().splitlines()
    username = lines[0]
    role = getting_role(password,gc)
    return username, role

def launch_dashboard(self,pipeliam_name,pipeliam_version,PL_mainDashboard_class,fade_widget):
    self.close()
    self.main_window = PL_mainDashboard_class(self.username, self.role,pipeliam_name,pipeliam_version)
    fade_widget(self.main_window, fade_in=True)
    self.main_window.show()

def launch_login(self,pipeliam_name,pipeliam_version,PL_logger_class,fade_widget):
    self.close()
    self.login_window = PL_logger_class(pipeliam_name,pipeliam_version,self.gc,self.path)
    fade_widget(self.login_window, fade_in=True)
    self.login_window.show()

def delete_remember(self,logout : bool):
    remember_me = str(self.path)+"/"+"remember_me.txt"
    if logout == True : 
        if os.path.exists(remember_me):
            os.remove(remember_me)
        else : 
            print("No File to delete -- Either no remember me ticked or deleted by mistake")



