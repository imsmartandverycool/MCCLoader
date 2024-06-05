import time
from time import sleep
import os
import json
import requests
import webbrowser
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

# Function to configure terminal settings
def bg1():
    os.system("")

# Clear the terminal
os.system("clear")  # Use 'clear' instead of 'cls' for Unix-based systems

# Function to set the terminal window title
def windowtitle(a):
    os.system(f"title {a}")

# Set initial window title and print messages
windowtitle("MCC Loader Premium ^<^/^> ^| Not Authorized")
print("Bypassing authentication...")
print("Authenticated...")
windowtitle("MCC Loader Premium | Authorized")
print("\nWelcome to freemium Mode.")

# Configure terminal settings
bg1()

# Pause for 2 seconds
time.sleep(2)

# Clear the terminal
os.system("clear")  # Use 'clear' instead of 'cls'

# Define and display the banner
banner = r"""
       MCC Loader archives freemium
        Cracked by @Whovale discord press enter to continue 
"""[1:]

Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)

# Define color codes
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
dev = "\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

# Define the main menu prompt
pre = """
\033[1;39m

                                             
                    MCC Loader Cracked


\033[1;39m
   \033[0;31m                                          Welcome, choose any section.

                                    \033[1;31m[\033[1;39m1\033[1;31m] \033[1;34mMinecraft                \033[1;31m[\033[1;39mSS\033[1;31m] \033[1;34mScreen Share Tools  
"""
print(pre)

# Main loop to handle user input
while True:
    os.system('clear')  # Use 'clear' instead of 'cls'
    print(pre)
    chon = Write.Input("         [×] >>  ", Colors.red_to_purple, interval=0.0025)
    if chon == '1':
        os.system('clear')  # Use 'clear' instead of 'cls'
        print("                                              \033[1;39mLoading Minecraft Section..")
        # Fetch and execute the Minecraft section script
        exec(requests.get('https://raw.githubusercontent.com/imsmartandverycool/MCCLoader/main/minecraft').text)
    elif chon == 'SS':
        os.system('clear')  # Use 'clear' instead of 'cls'
        print("                                            \033[1;39mLoading Screen Share Tools Section..")
        # Fetch and execute the Screen Share Tools section script
        exec(requests.get('https://raw.githubusercontent.com/imsmartandverycool/MCCLoader/main/SS-TOOLS').text)
