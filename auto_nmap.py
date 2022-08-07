from pyfiglet import Figlet
import colorama
from colorama import Fore, Back, Style
import os

while True:
    colorama.init()
    f = Figlet(font='roman')
    print(Fore.CYAN)
    print (f.renderText('Auto Nmap'))
    print("Project Owner By Adolfus#1250\n")
    
    soru = int(input("1 - Search Vuln Ports\n2 - Search Port Versions\nChoose a Number Above : "))
    
    ip = input("Enter Target İp : ")
    
    if soru == 1:
        print(Fore.GREEN)
        print("Searchin Vuln Ports")
        os.system("nmap -sS -Pn --script vuln " + ip )
    
    if soru == 2:
        print(Fore.GREEN)
        print("Search Port Versions !!")
        os.system("nmap -sS -sV -Pn " + ip)

    