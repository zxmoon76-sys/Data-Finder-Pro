import os
import hashlib
import requests
import socket
import subprocess

# কালার কোড
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

class DataFinderPro:
    def __init__(self):
        self.headers_to_check = ["X-Frame-Options", "Content-Security-Policy", "X-Content-Type-Options"]
        self.malware_signatures = ["5d41402abc4b2a76b9719d911017c592"]
        self.common_ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 53: "DNS", 
            80: "HTTP", 443: "HTTPS", 3306: "MySQL", 8080: "Proxy"
        }

    def show_banner(self):
        banner = fr"""{CYAN}
  _____       _        ______ _           _           _____           
 |  __ \     | |      |  ____(_)         | |         |  __ \          
 | |  | | ___| |_ __ _| |__   _ _ __   __| | ___ _ __| |__) | __ ___  
 | |  | |/ _ \ __/ _` |  __| | | '_ \ / _` |/ _ \ '__|  ___/ '__/ _ \ 
 | |__| |  __/ || (_| | |    | | | | | (_| |  __/ |  | |   | | | (_) |
 |_____/ \___|\__\__,_|_|    |_|_| |_|\__,_|\___|_|  |_|   |_|  \___/ 
{YELLOW}
        [+--- Natespo Advanced Security Framework v2.3 ---+]
        [+--- Hybrid: Root & Non-Root Security Tools   ---+]
{RESET}"""
        print(banner)

    # মডিউল ১: ওয়েবসাইট অডিট
    def audit_url(self, url):
        print(f"\n{CYAN}[*] Web Audit: {url}{RESET}")
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            res = requests.get(url, timeout=10, headers=headers)
            for h in self.headers_to_check:
                status = f"{GREEN}[✔] '{h}' Found" if h in res.headers else f"{RED}[✘] '{h}' Missing"
                print(status + RESET)
        except Exception as e: print(f"{RED}[-] Error: {e}{RESET}")

    # মডিউল ২: ফাইল স্ক্যান
    def scan_file(self, path):
        try:
            with open(path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                return f"{RED}[✘] MALWARE: {path}{RESET}" if file_hash in self.malware_signatures else f"{GREEN}[✔] SAFE: {path}{RESET}"
        except PermissionError: return f"{YELLOW}[!] BYPASSING (No Permission): {path}{RESET}"
        except: return f"{RED}[-] Error: {path}{RESET}"

    # মডিউল ৩: পাসওয়ার্ড ক্র্যাকার
    def crack_hash(self, target_hash, wordlist_path):
        print(f"\n{CYAN}[*] Cracking MD5: {target_hash}{RESET}")
        try:
            with open(wordlist_path, 'r', encoding='latin-1') as f:
                for line in f:
                    word = line.strip()
                    if hashlib.md5(word.encode()).hexdigest() == target_hash:
                        return f"{GREEN}[✔] SUCCESS! Password: {word}{RESET}"
            return f"{RED}[✘] Failed: Not in wordlist.{RESET}"
        except Exception as e: return f"{RED}[-] Error: {e}{RESET}"

    # মডিউল ৪: নেটওয়ার্ক ও পোর্ট অ্যানালাইসিস (Non-Root)
    def network_analysis(self, target_ip):
        print(f"\n{CYAN}[*] Port Scanning: {target_ip}{RESET}")
        for port, service in self.common_ports.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((target_ip, port)) == 0:
                print(f"{GREEN}[✔] Port {port}: OPEN ({service}){RESET}")
            s.close()
        
        # রুট থাকলে ম্যাক অ্যাড্রেস দেখাবে
        if os.getuid() == 0:
            print(f"\n{GREEN}[+] Root detected! Fetching ARP Table...{RESET}")
            os.system('ip neigh show')

    # মডিউল ৫: ওয়াইফাই পাসওয়ার্ড ডাম্প (Root Only)
    def wifi_dump(self):
        if os.getuid() != 0:
            print(f"\n{RED}[✘] Error: This module requires ROOT access!{RESET}")
            return
        print(f"\n{CYAN}[*] Dumping Saved Wi-Fi Passwords...{RESET}")
        # ডাইরেক্ট সিস্টেম কমান্ড ব্যবহার করে ফাইল পড়ার চেষ্টা
        cmd = "su -c 'cat /data/misc/wifi/wpa_supplicant.conf || cat /data/misc/apexdata/com.android.wifi/WifiConfigStore.xml'"
        os.system(cmd)

def main():
    app = DataFinderPro()
    app.show_banner()
    
    print(f"{YELLOW}1. Web Security Audit\n2. Malware & Permission Scan\n3. Password Hash Cracker (MD5)\n4. Network Analysis (IP/Port)\n5. Wi-Fi Password Dump (Root Only){RESET}")
    
    choice = input(f"\n{CYAN}Select Option: {RESET}")
    
    if choice == "1":
        app.audit_url(input("Enter URL: "))
    elif choice == "2":
        path = input("Enter Path: ")
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for name in files: print(app.scan_file(os.path.join(root, name)))
        else: print(app.scan_file(path))
    elif choice == "3":
        print(app.crack_hash(input("Enter MD5: "), input("Enter Wordlist Path: ")))
    elif choice == "4":
        app.network_analysis(input("Enter Target IP: "))
    elif choice == "5":
        app.wifi_dump()

if __name__ == "__main__":
    main()
