
import socket
import sys
import threading
import queue
import time
from datetime import datetime

# ---------------------------------------------------------------------------
# Common ports -> service name (used for quick service hints)
# ---------------------------------------------------------------------------
COMMON_PORTS = {
    7: "Echo", 9: "Discard", 13: "Daytime", 17: "QOTD", 19: "Chargen",
    20: "FTP-Data", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    37: "Time", 42: "WINS", 43: "WHOIS", 49: "TACACS", 53: "DNS",
    67: "DHCP-Server", 68: "DHCP-Client", 69: "TFTP", 70: "Gopher",
    79: "Finger", 80: "HTTP", 88: "Kerberos", 102: "MS-Exchange",
    110: "POP3", 111: "RPCBind", 113: "Ident", 119: "NNTP",
    123: "NTP", 135: "MSRPC", 137: "NetBIOS-NS", 138: "NetBIOS-DGM",
    139: "NetBIOS-SSN", 143: "IMAP", 161: "SNMP", 162: "SNMP-Trap",
    177: "XDMCP", 179: "BGP", 194: "IRC", 201: "AppleTalk",
    264: "BGMP", 318: "PKIX-TimeStamp", 381: "HP-OpenView", 389: "LDAP",
    411: "Direct-Connect", 412: "Direct-Connect", 443: "HTTPS",
    445: "SMB", 464: "Kerberos-Change", 465: "SMTPS", 497: "Retrospect",
    500: "ISAKMP/IKE", 512: "Rexec", 513: "Rlogin", 514: "Syslog/Shell",
    515: "LPD/Printer", 520: "RIP", 521: "RIPng", 540: "UUCP",
    548: "AFP", 554: "RTSP", 587: "SMTP-Submission", 593: "MSRPC-HTTP",
    623: "IPMI", 631: "IPP/CUPS", 636: "LDAPS", 646: "LDP",
    691: "MS-Exchange-Routing", 860: "iSCSI", 873: "Rsync",
    902: "VMware-Server", 989: "FTPS-Data", 990: "FTPS", 993: "IMAPS",
    995: "POP3S", 1025: "MS-RPC-Alt", 1026: "MS-RPC-Alt",
    1080: "SOCKS-Proxy", 1099: "Java-RMI", 1194: "OpenVPN",
    1433: "MSSQL", 1434: "MSSQL-Monitor", 1521: "OracleDB",
    1723: "PPTP", 1755: "MS-Media-Services", 1812: "RADIUS",
    1813: "RADIUS-Acct", 1883: "MQTT", 2049: "NFS", 2082: "cPanel",
    2083: "cPanel-SSL", 2086: "WHM", 2087: "WHM-SSL", 2095: "Webmail",
    2096: "Webmail-SSL", 2181: "ZooKeeper", 2222: "SSH-Alt",
    2375: "Docker-API", 2376: "Docker-API-SSL", 2483: "Oracle-DB-Alt",
    2484: "Oracle-DB-SSL", 2601: "Zebra", 2604: "Zebra-OSPF",
    3000: "Dev-Server", 3128: "Squid-Proxy", 3260: "iSCSI-Target",
    3268: "LDAP-GC", 3269: "LDAP-GC-SSL", 3306: "MySQL",
    3307: "MySQL-Alt", 3389: "RDP", 3690: "SVN", 3724: "WoW-Server",
    3784: "Ventrilo", 4000: "ICQ", 4040: "Spark-UI", 4369: "Erlang-EPMD",
    4433: "HTTPS-Alt", 4444: "Metasploit/Backdoor", 4500: "IPSec-NAT-T",
    4664: "Google-Desktop", 4712: "Pulseaudio", 4993: "AirPlay",
    5000: "UPnP/Flask-Dev", 5001: "Synology/Slingbox",
    5060: "SIP", 5061: "SIP-TLS", 5222: "XMPP-Client",
    5269: "XMPP-Server", 5353: "mDNS", 5355: "LLMNR",
    5432: "PostgreSQL", 5555: "Android-Debug/Freeciv",
    5601: "Kibana", 5672: "AMQP/RabbitMQ", 5683: "CoAP",
    5900: "VNC", 5901: "VNC-1", 5984: "CouchDB", 5985: "WinRM-HTTP",
    5986: "WinRM-HTTPS", 6000: "X11", 6379: "Redis",
    6443: "Kubernetes-API", 6465: "SMTP-Alt", 6500: "GameSpy",
    6660: "IRC-Alt", 6661: "IRC-Alt", 6662: "IRC-Alt", 6663: "IRC-Alt",
    6664: "IRC-Alt", 6665: "IRC", 6666: "IRC", 6667: "IRC",
    6668: "IRC", 6669: "IRC", 6881: "BitTorrent", 7000: "Cassandra",
    7001: "Cassandra-SSL", 7077: "Spark-Master", 7199: "Cassandra-JMX",
    7474: "Neo4j", 7547: "TR-069/CWMP", 7687: "Neo4j-Bolt",
    8000: "HTTP-Alt", 8008: "HTTP-Alt2", 8080: "HTTP-Proxy",
    8081: "HTTP-Proxy-Alt", 8086: "InfluxDB", 8087: "Riak",
    8088: "HTTP-Alt3", 8089: "Splunk-Mgmt", 8090: "HTTP-Alt4",
    8091: "Couchbase", 8096: "Emby", 8118: "Privoxy",
    8123: "Home-Assistant", 8140: "Puppet", 8161: "ActiveMQ-Console",
    8200: "GoToMyPC/Trickle", 8222: "VMware-vCenter", 8291: "Mikrotik-Winbox",
    8332: "Bitcoin-RPC", 8333: "Bitcoin-P2P", 8443: "HTTPS-Alt",
    8500: "Consul", 8530: "WSUS", 8531: "WSUS-SSL", 8834: "Nessus",
    8880: "HTTP-Alt5", 8888: "HTTP-Alt6/Jupyter", 8983: "Solr",
    9000: "PHP-FPM/SonarQube", 9042: "Cassandra-CQL", 9060: "WebSphere-Admin",
    9092: "Kafka", 9100: "JetDirect-Printer", 9200: "Elasticsearch",
    9300: "Elasticsearch-Transport", 9418: "Git", 9999: "Urchin/Abyss",
    10000: "Webmin", 10050: "Zabbix-Agent", 10051: "Zabbix-Server",
    11211: "Memcached", 11214: "Steam-In", 11215: "Steam-Out",
    12345: "NetBus-Backdoor", 13720: "NetBackup", 15672: "RabbitMQ-Mgmt",
    17500: "Dropbox-LAN-Sync", 20000: "Usermin", 24800: "Synergy",
    25565: "Minecraft", 27017: "MongoDB", 27018: "MongoDB-Shard",
    27019: "MongoDB-Config", 28017: "MongoDB-Web", 32400: "Plex",
    33848: "Docker-Registry", 37777: "DVR-Camera", 44818: "EtherNet-IP",
    47808: "BACnet", 49152: "Windows-RPC-Dyn", 50000: "SAP",
    50070: "Hadoop-NameNode", 54321: "GameServer", 61616: "ActiveMQ-OpenWire"
}

print_lock = threading.Lock()
results = []
results_lock = threading.Lock()


def banner():
    print(r"""
__  ____  __    _    ____
\ \/ /  \/  |  / \  |  _ \
 \  /| |\/| | / _ \ | |_) |
 /  \| |  | |/ ___ \|  __/
/_/\_\_|  |_/_/   \_\_|

        XMAP - MADE BY CRYPTA VERITAS
""")


def ask(prompt, default=None, cast=str):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            return cast(raw)
        except ValueError:
            print(f"  [!] Invalid value, please try again.")


def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"[!] Could not resolve host: {target}")
        sys.exit(1)


def grab_banner(sock):
    try:
        sock.settimeout(1.0)
        data = sock.recv(1024)
        if data:
            return data.decode(errors="ignore").strip().replace("\n", " ")[:80]
    except Exception:
        pass
    return ""


def scan_port(ip, port, timeout, grab):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                service = COMMON_PORTS.get(port, "unknown")
                banner_text = ""
                if grab:
                    banner_text = grab_banner(s)
                with results_lock:
                    results.append((port, service, banner_text))
                with print_lock:
                    line = f"  [+] Port {port:<6} OPEN   service: {service:<12}"
                    if banner_text:
                        line += f" banner: {banner_text}"
                    print(line)
    except Exception:
        pass


def worker(ip, timeout, grab, q):
    while not q.empty():
        try:
            port = q.get_nowait()
        except queue.Empty:
            return
        scan_port(ip, port, timeout, grab)
        q.task_done()


def parse_port_range(text, default_start=1, default_end=1024):
    text = text.strip()
    if text == "":
        return default_start, default_end
    if "-" in text:
        a, b = text.split("-", 1)
        return int(a.strip()), int(b.strip())
    p = int(text)
    return p, p


def main():
    banner()

    target = ask("Target IP or hostname: ")
    ip = resolve_target(target)
    print(f"[*] Resolved target: {target} -> {ip}")

    port_range_raw = input("Port range (e.g. 1-1024, default 1-1024): ")
    start_port, end_port = parse_port_range(port_range_raw)
    if start_port > end_port or start_port < 1 or end_port > 65535:
        print("[!] Invalid port range.")
        sys.exit(1)

    threads = ask("Number of threads (default 100): ", default=100, cast=int)
    timeout = ask("Socket timeout in seconds (default 0.5): ", default=0.5, cast=float)

    grab_raw = input("Attempt banner grabbing? (y/N): ").strip().lower()
    grab = grab_raw == "y"

    print(f"\n[*] Starting XMAP scan on {ip}")
    print(f"[*] Ports: {start_port}-{end_port}  Threads: {threads}  Timeout: {timeout}s")
    print(f"[*] Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    start_time = time.time()

    q = queue.Queue()
    for port in range(start_port, end_port + 1):
        q.put(port)

    thread_list = []
    for _ in range(min(threads, end_port - start_port + 1)):
        t = threading.Thread(target=worker, args=(ip, timeout, grab, q))
        t.daemon = True
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    elapsed = time.time() - start_time

    print("-" * 60)
    print(f"[*] Scan finished in {elapsed:.2f} seconds")
    print(f"[*] Open ports found: {len(results)}")

    if results:
        results.sort(key=lambda r: r[0])
        print("\nSummary:")
        for port, service, banner_text in results:
            line = f"  {port}/tcp  open  {service}"
            if banner_text:
                line += f"  ({banner_text})"
            print(line)

        save = input("\nSave results to file? (y/N): ").strip().lower()
        if save == "y":
            filename = input("Filename (default xmap_results.txt): ").strip() or "xmap_results.txt"
            with open(filename, "w") as f:
                f.write(f"XMAP scan report for {ip} ({target})\n")
                f.write(f"Scanned range: {start_port}-{end_port}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("-" * 60 + "\n")
                for port, service, banner_text in results:
                    f.write(f"{port}/tcp open {service} {banner_text}\n")
            print(f"[*] Results saved to {filename}")
    else:
        print("[*] No open ports found in the given range.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit(0)