import os

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

def DISCLAIMER():
    print(color.FAIL+color.BOLD+'''
                            DISCLAIMER
                   '''+color.END)
    print(color.WARNING+'Данное приложение не создано с целью каких либо атак!'+color.END)
    print(color.WARNING+'Приложение лишь ознакомит вас с хакингом, не применяйте приложение во вред!'+color.END)
    print(color.WARNING+'Я не несу ответственность за ваши действия.'+color.END)
    print(color.RED+color.BOLD+'Нажимая Y, вы соглашаетесь с тем, что не будете использовать приложение во вред!'+color.END)
    query = input(color.FAIL + "[*] Y/N: " + color.END).lower()
    if query.startswith('n'):
       print(color.BLUE + "GOODBAU" + color.END)
    if query.startswith('y'):
       print()
    else:
        exit()
