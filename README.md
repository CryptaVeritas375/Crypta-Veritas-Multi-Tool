# Crypta Veritas - Mini Multi tool
A Python-based collection of network reconnaissance and testing utilities featuring an interactive terminal interface.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%2FLinux%2FmacOS-lightgrey.svg)

## Overview

Crypta Veritas is an open-source network toolkit designed for educational purposes and authorized penetration testing. It provides a unified interface for DNS resolution, IP geolocation, ICMP flooding, and port scanning operations.

## Features

| Tool | Description | Requirements |
|------|-------------|--------------|
| **DNS Lookup** | Resolve domain names using system nslookup | None |
| **IP Lookup** | Geolocation lookup via ip-api.com | Internet connection |
| **ICMP Flooder** | Multi-threaded ICMP packet flooding | Root/Admin privileges |
| **XMAP Port Scanner** | Fast multi-threaded TCP port scanner with banner grabbing | None |

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Dependencies

## Clone & Setup

git clone https://github.com/yourusername/crypta-veritas.git
cd crypta-veritas
python main.py
pip install -r requirements.txt
python main.py

## Usage
Launch the main menu interface:

# Windows
python main.py or py main.py

# Linux/macOS (ICMP Flooder requires sudo)
sudo python3 main.py

## Menu Options

--------------------------------------------------------------------------
|    [1]. DNS Lookup | [2]. IpLook UP | [3]. ICMP Flood | [4]. portScann | 
--------------------------------------------------------------------------

## 1. DNS Lookup
Performs DNS resolution using the system's nslookup command.

Input: Domain name (e.g., example.com)

Example:


Enter a dns: google.com
Server:  192.168.1.1
Address: 192.168.1.1#53

Non-authoritative answer:
Name:   google.com
Address: 142.250.80.46

## 2. IP Lookup
Retrieves geolocation data for any IP address using the ip-api.com service.

Input: IP address (e.g., 8.8.8.8)

Returns:

Country, Region, City
ISP and Organization
Latitude/Longitude
Timezone
AS number
Example:

Enter a IP: 8.8.8.8
{'status': 'success', 'country': 'United States', 'region': 'CA', 
 'city': 'Mountain View', 'isp': 'Google LLC', ...}

## 3. ICMP Flooder
Sends high-volume ICMP echo requests to a target. Requires root/admin privileges.

Configuration Options:

Target IP address
Number of threads (default: 10)
Delay between packets in seconds (default: 0.001, use 0 for max speed)
Features:

Randomized ICMP packet IDs and payloads
Real-time packet counter
Multi-threaded for maximum throughput
Example:

==================================================
       ICMP Flooder - Interactive Setup
==================================================

[?] Enter target IP: 192.168.1.1
[?] Number of threads [default: 10]: 50
[?] Delay between packets in seconds [default: 0.001]: 0

==================================================
Target:  192.168.1.1
Threads: 50
Delay:   0s
==================================================

[?] Start flooding? [Y/n]: y

[*] Starting ICMP flood...
[*] Press Ctrl+C to stop

[+] Packets sent: 152847 | Target: 192.168.1.1


## 4. XMAP Port Scanner
Fast TCP port scanner with service banner detection.

Configuration Options:

Target IP address
Starting port (default: 1)
Ending port (default: 100)
Features:

Multi-threaded scanning
Service banner grabbing
Colored output (open/closed/filtered status)
Example:


==================================================
              XMAP - Port Scanner
==================================================

[?] Enter IP to scan: 192.168.1.1
[?] Start port [default: 1]: 1
[?] End port [default: 100]: 1000

[*] Scanning 192.168.1.1 ports 1-1000 with 100 threads...

[+] Port 22 is open! Banner: SSH-2.0-OpenSSH_8.2p1
[+] Port 80 is open! Banner: HTTP/1.1 200 OK
[+] Port 443 is open! Banner: 

[*] Scan complete. Time elapsed: 5.23 seconds
[*] Open ports found: 3

## Files

crypta-veritas/
├── main.py          # Main entry point and menu system
├── UI.py            # User interface functions and display
├── Network.py       # XMAP port scanner implementation
├── Dos.py           # ICMP flooder implementation
├── DNSLookUp.py     # DNS resolution module
├── IpLookup.py      # IP geolocation module
└── README.md        # This file

Module Descriptions
main.py
Entry point that displays the main menu and routes user selections to the appropriate modules.

UI.py
Contains display functions including:

logo() - Displays the Crypta Veritas ASCII banner
menu() - Displays the main menu interface
Network.py
Implements the XMAP port scanner with:

Multi-threaded TCP connection testing
Socket timeout handling
Service banner grabbing
Colored terminal output
Dos.py
ICMP flooding implementation featuring:

Raw socket creation
ICMP packet construction with checksum calculation
Thread-safe packet counting
Interactive configuration prompts
DNSLookUp.py
Simple wrapper around system nslookup command for DNS resolution.

IpLookup.py
Uses ip-api.com JSON API for IP geolocation data retrieval.

Important Notes
Privileges
ICMP Flooder requires root/administrator privileges to create raw sockets
Other tools work with standard user privileges
Legal Disclaimer
These tools are provided for educational purposes and authorized testing only. Unauthorized use of these tools against systems you do not own or have explicit permission to test is illegal. The author assumes no liability for misuse.
