import os
from random import choice
import time

print("")
print("")
print("                 ___________________   ________  .____       .___ _______  ___________________")
time.sleep(0.1)
print("                 \__    ___/\_____  \  \_____  \ |    |      |   |\      \ \_   _____/\_____  \  ")
time.sleep(0.1)
print("                   |    |    /   |   \  /   |   \|    |      |   |/   |   \ |    __)   /   |   \ ")
time.sleep(0.1)
print("                   |    |   /    |    \/    |    \    |___   |   /    |    \|     \   /    |     ")
time.sleep(0.1)
print("                   |____|   \_______  /\_______  /_______ \  |___\____|__  /\___  /   \_______  /")
time.sleep(0.1)
print("                                    \/         \/        \/              \/     \/            \/ ")


print("")
print("")
time.sleep(0.1)
print("                                                 About us :)")
print("")
time.sleep(0.1)
print("                                      ------------------------------")
time.sleep(0.1)
print("                                         Version        : v1.0")
time.sleep(0.1)
print("                                         Platforme      : Windows (termux soon)")
time.sleep(0.1)
print("                                         langage        : python")
time.sleep(0.1)
print("                                         Developper     : Falshon")
time.sleep(0.1)
print('                                         Github         : https://github.com/Falshon')
time.sleep(0.1)
print("                                     -------------------------------")
print("")
print("")

choice = input("Press [6] to main menu.")

if choice == '6' :
    os.system("python prgrm/start.py")