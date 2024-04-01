from pypresence import *
from colorama import *
from pystyle import *
import time

class Banner:
    def banner():
        print(Center.XCenter(f"""
{Fore.LIGHTBLACK_EX}·▄▄▄▄   ▌ ▐· ▐ ▄      {Fore.LIGHTCYAN_EX}▄▄▄·▄▄▄  ▄▄▄ ..▄▄ · ▄▄▄ . ▐ ▄  ▄▄· ▄▄▄ .
{Fore.LIGHTBLACK_EX}██▪ ██ ▪█·█▌•█▌▐█    {Fore.LIGHTBLUE_EX}▐█ ▄█▀▄ █·▀▄.▀·▐█ ▀. ▀▄.▀·•█▌▐█▐█ ▌▪▀▄.▀·
{Fore.LIGHTBLACK_EX}▐█· ▐█▌▐█▐█•▐█▐▐▌     {Fore.LIGHTCYAN_EX}██▀·▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄▐▀▀▪▄▐█▐▐▌██ ▄▄▐▀▀▪▄
{Fore.LIGHTBLACK_EX}██. ██  ███ ██▐█▌    {Fore.LIGHTBLUE_EX}▐█▪·•▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄▄▌██▐█▌▐███▌▐█▄▄▌
{Fore.LIGHTBLACK_EX}▀▀▀▀▀• . ▀  ▀▀ █▪    {Fore.LIGHTCYAN_EX}.▀   .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀ ▀▀ █▪·▀▀▀  ▀▀▀ {Fore.RESET}"""))
        print(Center.XCenter(f"| {Fore.LIGHTBLACK_EX}Made: {Fore.LIGHTCYAN_EX}Oracle{Fore.RESET} |"))
        print(Center.XCenter(f"     | {Fore.LIGHTBLACK_EX}Team: {Fore.LIGHTCYAN_EX}Divine{Fore.LIGHTBLUE_EX}Blood{Fore.RESET} |"))
        print(Center.XCenter(f"| {Fore.LIGHTBLACK_EX}Telegram: {Fore.LIGHTCYAN_EX}t.me/TheDivineBlood{Fore.RESET} |"))


class Discord:
    def presence(clientid, state, title, details, image):
        try:
           client = Presence(clientid)
           if not state or not details or not title or not image:
                client.connect()
                presence_data = {
            "state": "https://github.com/Jinx-CrazyCode",
            "details": "DVN SPONSOR",
            "large_text": "DEVELOPER",
            }    
                client.update(**presence_data)
                print(f"{Fore.LIGHTGREEN_EX}Rich Presence Updated{Fore.RESET}")
                while True:
                    time.sleep(15)    
           
           client.connect()
           presence_data = {
            "state": state,
            "details": details,
            "large_image": image,
            "large_text": title,
           }
           client.update(**presence_data)
           print(f"{Fore.LIGHTGREEN_EX}Rich Presence Updated{Fore.RESET}")
           while True:
               time.sleep(15)
        except Exception as a:
            print(f"{Fore.RED}Impossible Set Rich Presence:{Fore.RESET} ", a)