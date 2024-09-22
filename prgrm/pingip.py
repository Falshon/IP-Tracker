import os
import time
import ipaddress
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("")
print("")
print("                         __________.___ _______    ________   ._______________ ")
time.sleep(0.1)
print("                         \______   \   |\      \  /  _____/   |   \______    |")
time.sleep(0.1)
print("                         |     ___/   |/   |   \/   \  ___    |   ||     ___/")
time.sleep(0.1)
print("                         |    |   |   /    |    \    \_\  \   |   ||    |    ")
time.sleep(0.1)
print("                         |____|   |___\____|__  /\______  /   |___||____|    ")
time.sleep(0.1)
print("                                              \/        \/                   ")
print("")
print("")

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def main():
    clear_screen()
    ip_address = input("Enter IP address: ")  # Prompt in red
    
    if not ip_address:
        print("No IP address provided.")
        return

    if not is_valid_ip(ip_address):
        print("\033[91m" + "[-] IP address is invalid." + "\033[0m")
    else:
        response_time = (ip_address)
        if response_time is None:
            print("\033[91m" + "[-] IP address is unreachable." + "\033[0m")
        else:
            print("\033[92m" + str"[+] IP address is reachable. Response time: {response_time:.2f} ms" + "\033[0m")
choice = input("press [ENTRER] to return to the menu :")

if choice == '3':
    os.system("python prgrm/start.py")

if __name__ == "__main__":
    main()