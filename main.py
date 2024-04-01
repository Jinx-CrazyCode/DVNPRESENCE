import lib.lib as D
import os
from colorama import *
os.system("cls")
D.Banner.banner()

id = input(f"{Fore.LIGHTCYAN_EX}Insert your ClientID: {Fore.RESET}")
state = input(f"{Fore.LIGHTBLUE_EX}Insert State Presence: {Fore.RESET}")
title = input(f"{Fore.LIGHTCYAN_EX}Insert Title Presence: {Fore.RESET}")
detail = input(f"{Fore.LIGHTBLUE_EX}Insert Details Presence: {Fore.RESET}")
logo = input(f"{Fore.LIGHTCYAN_EX}Insert url Logo Presence(512x512): {Fore.RESET}")
D.Discord.presence(id, state,title, detail, logo)