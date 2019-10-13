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

print('Что запускать?')
print('Голосовой помощник - [1]')
print('Ручное управление - [2]')
sta=input('~# ')
while True:
    if sta.startswith('1'):
        os.system('python3 dushigub.py')
    if sta.startswith('2'):
        os.system('python3 sherman.py')
