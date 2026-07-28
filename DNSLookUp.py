import os
import json

def LookUP(dns):
    os.system("nslookup " + dns)