import os
import time

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



try:
    os.system('clear')
    os.system('ls android/')
    time.sleep(0.8)
    os.system('termux-setup-storage')
    time.sleep(0.7)
    pam=input(color.GREEN+'Какое приложение импортирвать? '+color.END)
    os.system('chmod +x android/'+pam)
    time.sleep(0.2)
    os.system('mv android/'+pam+' $HOME/Dushigub/')
    time.sleep(0.4)
    os.system('mv '+pam+' /storage/emulated/0/')
    os.system('clear')
    print(color.RED+color.BOLD+'Приложение перенесено в ваши файлы'+color.END)
    print(color.RED+color.BOLD+'Вам осталось зайти в ваши файлы...'+color.END)
    time.sleep(10)
    
except:
    print(color.FAIL+'Выход...'+color.END)
    exit()
