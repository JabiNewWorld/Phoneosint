import os
import sys
import time

os.system("clear")

os.system("sudo apt upgrade")

os.system("sudo apt update")

os.system("sudo apt install python3-pip")

os.system("python3 -m pip install colorama")

os.system("sudo apt install figlet")
os.system("clear")
Py = input("deseas seguir y(si) o n(no) :")
if Py == 'y':   
    print("**OK SEGUIRE INSTALNDO**")   
else:
    exit
os.system("figlet YA ACABAMOS")
time.sleep(3)
sys.exit()
