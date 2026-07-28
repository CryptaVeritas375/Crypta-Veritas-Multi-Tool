from UI import logo
from UI import chooses
from DNSLookUp import LookUP
from IpLookup import LookIP
from Dos import ICMPFlooder
from Network import main as mm
import os
def main():
    chooses()
    ch = input("> ")
    if ch == "1":
        print("Warning this method is using NSlookup!")
        DNS = input("Enter a dns: ")
        LookUP(DNS)
        os.system("pause")
        main()
        

    if ch == "2":
        Ip = input("Enter a IP: ")
        res = LookIP(Ip)
        print(res)
        os.system("pause")
        main()
    if ch == "3":
        flooder = ICMPFlooder()
        flooder.start()
        os.system("pause")
        main()
    if ch == "4":
        mm()
        os.system("pause")
        main()

main()