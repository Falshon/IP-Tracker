import ipaddress
import requests
import time
from colorama import Fore, init
import subprocess
import os

init(autoreset=True)

ascii_title = """

                   ._____________    _____________________    _____  _________  ____  __._____________________ 
                   |   \______   \   \__    ___/\______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   |
                   |   ||     ___/     |    |    |       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/
                   |   ||    |         |    |    |    |   \/    |    \     \___|    |  \  |        \ |    |   |
                   |___||____|         |____|    |____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  /
                                                        \/         \/        \/        \/        \/         \/             

                                                     -o#&&*''''?d:>b\\_
                                               _o/"`''  '',,  dMF9MMMMMHo_
                                             .o&#'         ` MbHMMMMMMMMMMMHo.
                                           .o"" '            odM*$&&HMMMMMMMMMM?.
                                          '                M&ood,~'`(&##MMMMMMH  &               
                                        ?$.             MMMMMMMMMMMMMMMMMMM/HMMM|`*L
                                       |               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
                                       $H#:             *MMMMMMMMMMMMMMMMMMMMb#}'  `?
                                       ]MMH#                *##""*#MMMMMMMMMMMMM'    -              
                                       MMMMMMb_                   |MMMMMMMMMMXP'     :
                                       HMMMMMMMHo                  `MMMMMMMMT       .               
                                       ?MMMMMMMMP        IP TRACKER 9MMMMMMMM}       -
                                       -?MMMMMMM                  |MMMMMMMMM?,d-    '
                                        :|MMMMMM-                 `MMMMMMMT .M|.   :
                                         .9MMM[                    &MMMMM*' `'    .
                                          :9MMk                    `MMM#"        -
                                            &M}                     `          .-
                                             `&.                             .
                                               `~,   .                     ./
                                                   . _                  .-
                                                     '`--._,dd###pp=##'


"""

def display_title(ascii_art, delay=0.1):
    for line in ascii_art.splitlines():
        print(Fore.RED + line)
        time.sleep(delay)

display_title(ascii_title, delay=1 / ascii_title.count("\n"))

def get_location(ip):
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()

        loc = data.get("loc", " Location not found")
        if loc != " Location not found":
            latitude, longitude = loc.split(",")
        else:
            latitude = " Latitude not found"
            longitude = " Longitude not found"
        
        city = data.get("city", " City not found")
        region = data.get("region", " Region not found")
        country = data.get("country", " Country not found")
        postal = data.get("postal", " Postal code not found")
        timezone = data.get("timezone", " Timezone not found")
        org = data.get("org", " ISP not found")
        
        return (
            f"{Fore.GREEN if 'not found' not in latitude else Fore.RED} Latitude: {latitude}\n"
            f"{Fore.GREEN if 'not found' not in longitude else Fore.RED} Longitude: {longitude}\n"
            f"{Fore.GREEN if 'not found' not in city else Fore.RED} City: {city}\n"
            f"{Fore.GREEN if 'not found' not in region else Fore.RED} Region: {region}\n"
            f"{Fore.GREEN if 'not found' not in country else Fore.RED} Country: {country}\n"
            f"{Fore.GREEN if 'not found' not in postal else Fore.RED} Postal Code: {postal}\n"
            f"{Fore.GREEN if 'not found' not in timezone else Fore.RED} Timezone: {timezone}\n"
            f"{Fore.GREEN if 'not found' not in org else Fore.RED} ISP: {org}\n"
        )
    except Exception as e:
        return f"{Fore.RED} Error retrieving location: {e}"

while True:
    print(Fore.RED + "Victim's IP : ", end="") 
    ip_input = input()  

    try:
        ipaddress.ip_address(ip_input)
        print(Fore.GREEN + "This IP is valid.")
        
        location_info = get_location(ip_input)
        print(location_info)
        

        os.system('cls' if os.name == 'nt' else 'clear')


        break  
    except ValueError:
        print(Fore.RED + "This IP is invalid, try again with a good one.")

choice = input("Press [6] to return to the menu. ")

if choice == '6':
    os.system("python prgrm/start.py")

