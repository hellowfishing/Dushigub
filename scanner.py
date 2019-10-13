import os
import subprocess
import webbrowser
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

def internet():
    os.system('clear')
    print(color.DARKCYAN+'''
         Checking your internet connction...'''+color.END)
    time.sleep(2)
    os.system('clear')
    subprocess.call('./inet.sh')
    time.sleep(2.3)

def yesno():
    os.system('chmod +x *')
    subprocess.call('clear', shell=True)
    print(color.BOLD+'                               WELCOME TO SCAN'+color.END)
    xz=input(color.BOLD+'< install/skip/exit/update > '+color.END).lower()
    if xz.startswith('install'):
       os.system('clear')
       print('''INSTALL''')
       time.sleep(1.9)
       os.system('clear')
       subprocess.call('./in.sh', shell=True)
       print('Okey')
    elif xz.startswith('update'):
         os.system('clear')
         os.system('apt update -y')
    elif xz.startswith('skip'):
        print('Good')
    elif xz.startswith('exit'):
        print('GoodBye')
        exit()
    else:
        os.system('clear')
        print('ERROR')
        time.sleep(0.9)
        os.system('clear')
        print('REPLAY')
        time.sleep(1)
        yesno()
internet()
yesno()

while True:
    try:
        os.system('clear')
        os.system('ip route')
        ip=input('local@ip~# ').lower()
        if ip.startswith(ip):
           os.system('clear')
           os.system('./connecting.sh')
           os.system('clear')
           time.sleep(2)
           webbrowser.open(ip)
           os.system('clear')
           time.sleep(0.7)
           os.system("nmap "+ip+" > scanner.txt")
           scan = open('scanner.txt', 'r')
           print(color.FAIL+scan.read()+color.END)
           enter=input(color.DARKCYAN+'Для продолжения нажмите Enter '+color.END)
           time.sleep(5)
           os.system('rm scanner.txt')
           print(color.DARKCYAN+'Запуск полного сканирования сети...'+color.END)
           os.system('clear')
           print(color.DARKCYAN+'Запуск DNS'+color.END)
           time.sleep(3)
           os.system('./dns.sh')
           os.system('clear')
           print(color.DARKCYAN+'Перехват трафика, идет переадресация портов с 80, на 8080'+color.END)
           time.sleep(2)
           os.system('python3 sniff.py')
           exit()



    except:
        print('GoodBye')
        exit()
