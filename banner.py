import os
from colored import fg, bg, attr

os.system('clear')

red = fg('red')
blue = fg('blue')
green = fg('green')
yellow = fg('yellow')
violet = fg('violet')
reset = attr('reset')

def banner():
    print(red + """
 ____  _          _ ____       _       _     
|  _ \(_)_  _____| |  _ \ __ _| |_ ___| |__  
| |_) | \ \/ / _ \ | |_) / _` | __/ __| |_ \ 
|  __/| |>  <  __/ |  __/ (_| | |_ (__| | | |
|_|   |_/_/\_\___|_|_|   \__,_|\__\___|_| |_|v1.0                                              

""" + reset)
    print(green + '[Author: Ashutosh Singh Patel]')
    print('[User: BetterBy0x01]')
    print('[Github: github.com/BetterBy0x01]\n' + reset)