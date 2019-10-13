import socket, threading, time, subprocess, os
import requests

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

subprocess.call("clear")

key = 8194
shuntdown = False
join = False

def receving (name, sock):
    while not shuntdown:
        try:
            while True:
                data, addr = sock.recvfrom(4079)

                decrypt = ""; k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                print(decrypt)
                # END

                time.sleep(0.2)
        except:
            pass

host = ''
port = 0

name_server=input(color.DARKCYAN+color.BOLD+'ip-server: '+color.END)
print(color.FAIL+'Ожидайте, идет подключение...'+color.END)
print(color.FAIL+'Default port 7495'+color.END)

server = (name_server,7495)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while True:
    while shuntdown == False:
        if join == False:
            alias=input('Name: ')
            os.system('clear')
            s.sendto(("["+color.DARKCYAN+color.BOLD+alias+color.END+"] =>"+color.OKGREEN+" online "+color.END).encode("utf-8"),server)
            join = True
        else:
            try:
                time.sleep(0.5)
                message = input(color.CYAN+alias+color.END+"-> ")

                crypt = ""
                for i in message:
                    crypt += chr(ord(i)^key)
                message = crypt

                if message != "":
                    time.sleep(0.1)
                    s.sendto(("\n]"+color.RED+color.BOLD+alias +color.END+"] :: "+message).encode("utf-8"),server)
                time.sleep(0.2)
            except:
                s.sendto(("["+color.OKGREEN+color.BOLD+alias+color.END+"] <="+color.RED+" offline "+color.END).encode("utf-8"),server)
                time.sleep(0.1)
                print("Выход")
                time.sleep(0.2)
                shuntdown = True
                exit()

    rT.join()
    s.close()
