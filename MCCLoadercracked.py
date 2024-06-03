import time
from time import sleep
import os
import json
import requests
import webbrowser
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def bg1():
    os.system("")

os.system("clear")  # Use clear instead of cls

def windowtitle(a):  # Corrected function name
    os.system(f"title {a}")


windowtitle("MCC Loader Premium ^<^/^> ^| Not Authorized")
print("Bypassing authentication...")
print("Authenticated...")
windowtitle("MCC Loader Premium | authorized")  # Corrected function name
print("\nWelcome in freemuim Mode.")

bg1()

time.sleep(2)
os.system("clear")  # Use clear instead of cls

banner = r"""
       MCC Loader archives freemuim
        Cracked by @Whovale discord press enter to continue 
"""[1:]

Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)

xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb = "\033[1;39m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
dev = "\033[1;39m[\033[1;31mÃ—\033[1;39m]\033[1;39m"

pre = """
\033[1;39m



                                             
                    MCC Loader Cracked


\033[1;39m
   \033[0;31m                                          Welcome, choose any sections.

                                    \033[1;31m[\033[1;39m1\033[1;31m] \033[1;34mMinecraft                \033[1;31m[\033[1;39mSS\033[1;31m] \033[1;34mScreen Share Tools  \033[1;31m[\033[1;39m1\033[1;31m] \033[1;34mMinecraft Private
    """
print(pre)

while True:
    os.system('clear')  # Use clear instead of cls
    print(pre)
    chon = Write.Input("         [×] >>  ", Colors.red_to_purple, interval=0.0025)
    if chon == '1':
        os.system('clear')  # Use clear instead of cls
        print("                                              \033[1;39mLoading Minecraft Section..")
        exec(requests.get('https://github.com/imsmartandverycool/MCCLoader/blob/main/minecraft').text)
    elif chon == 'SS':
        os.system('clear')  # Use clear instead of cls
        print("                                            \033[1;39mLoading Screen Share Tools Section..")
        exec(requests.get('https://github.com/imsmartandverycool/MCCLoader/blob/main/SS-TOOLS').text)
