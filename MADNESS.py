import requests
import os
import json

logo = """

\x1b[0;31;40███╗   ███╗ ████████╗ ██████╗ ███╗   ██╗█████████╗███████╗███████╗
\x1b[0;31;40████╗ ████║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝
\x1b[0;31;40██╔████╔██║███████║██║  ██║██╔██╗ ██║█████╗  ███████╗███████╗
\x1b[0;31;40██║╚██╔╝██║██╔══██║██║  ██║██║╚██╗██ ██╔══╝  ╚════██║╚════██║
\x1b[0;31;40██║ ╚═╝ ██║██║       ║████████║ ╚████║███████╗█████████    ██████
\x1b[0;31;40╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
                             


"""



while True:
         os.system("title MADNESS")
         os.system("cls")
         print ("logo")
         print ("[1] FlameGRAVE DDos Tool")
         print ("[2] MadSpam SMS & Call Bomber")
         print ("[3] IP Address Lookup Tools")
         print (" ")
         x = input("Option: ")

if x  == "1":
      os.system("cls")
      print ("FlameGRAVE\n")
      ip = input("Enter Target IP: ")
      port = input("Enter Target IP Port (1-65535): ")
