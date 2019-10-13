import os
import time
import webbrowser
import subprocess
import disclaimer
import commands


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

def dushigub():
    os.system('clear')
    disclaimer.DISCLAIMER()
    os.system('chmod +x *')
    os.system('clear')
    print('Для помощи пиши help!')
    time.sleep(3)
    os.system('clear')
    time.sleep(0.3)
    commands.welcome()
    
dushigub()
