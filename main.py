import os
import subprocess
from socket import socket
from pystyle import *
from banner import banner
import sys

color_code = {
    "reset": "\033[0m",  
    "underline": "\033[04m", 
    "green": "\033[32m",     
    "yellow": "\033[93m",    
    "red": "\033[31m",       
    "cyan": "\033[36m",     
    "bold": "\033[01m",        
    "pink": "\033[95m",
    "url_l": "\033[36m",       
    "li_g": "\033[92m",      
    "f_cl": "\033[0m",
    "dark": "\033[90m",     
}
os.system("clear")
os.system("cls")

alignment = "{:>50}".format(banner)
colored_banner = Colorate.Horizontal(Colors.red_to_yellow, alignment)
print(colored_banner)
select = input(f'{color_code["red"]}[+]{color_code["bold"]} выбрать >{color_code["yellow"]} ')

if select == '1':
  subprocess.run(['python', 'search/base.py'])

elif select == '2':
  subprocess.run(['python', 'search/number.py'])
    
elif select == '3':
  subprocess.run(['python', 'search/tokenbot.py'])
    
elif select == '4':
  subprocess.run(['python', 'search/discord.py'])

elif select == '5':
  subprocess.run(['python', 'search/fullname.py'])

elif select == '6':
  subprocess.run(['python', 'search/telegram.py'])

elif select == '7':
  subprocess.run(['python', 'search/password.py'])

elif select == '8':
  subprocess.run(['python', 'search/ip.py'])

elif select == '9':
  subprocess.run(['python', 'search/auto.py'])

elif select == '10':
  subprocess.run(['python', 'search/vk.py'])

elif select == '11':
  subprocess.run(['python', 'tool/banword.py'])

elif select == '12':
  subprocess.run(['python', 'tool/bomber.py'])

elif select == '13':
  subprocess.run(['python', 'tool/snoser.py'])

elif select == '14':
  subprocess.run(['python', 'tool/stealer.py'])

elif select == '15':
  subprocess.run(['python', 'tool/obfuscate.py'])

elif select == '16':
  subprocess.run(['python', 'tool/ddos.py'])

elif select == '17':
  subprocess.run(['python', 'tool/parsing.py'])

elif select == '18':
  subprocess.run(['python', 'tool/deepfake.py'])

elif select == '19':
 print(Colorate.Horizontal(Colors.red_to_white, (""" 
     .
     channel @forever1termux
     dev @levelstorm
     release 11.12.2024
     .
""").strip()))

elif select == '20':
  exit()





