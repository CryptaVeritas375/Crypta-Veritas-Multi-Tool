import requests
import json

def LookIP(Ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{Ip}")
        res.raise_for_status()
        data = res.json()

        if data.get("status") == "fail":
            print(f"Error: {data.get('message')}")
            return None

        return data
    except requests.exceptions.RequestException as e:
        print(f"IpLookUp Failed {e}")
        return None
