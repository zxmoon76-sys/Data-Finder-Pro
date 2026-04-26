import os
import hashlib
import requests
import socket

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

    def show_banner(self):
        # সিনট্যাক্স এরর ঠিক করতে r বসানো হয়েছে
        banner = fr"""{CYAN}
  _____       _        ______ _           _           _____           
 |  __ \     | |      |  ____(_)         | |         |  __ \          
 | |  | | ___| |_ __ _| |__   _ _ __   __| | ___ _ __| |__) | __ ___  
 | |  | |/ _ \ __/ _` |  __| | | '_ \ / _` |/ _ \ '__|  ___/ '__/ _ \ 
 | |__| |  __/ || (_| | |    | | | | | (_| |  __/ |  | |   | | | (_) |
 |_____/ \___|\__\__,_|_|    |_|_| |_|\__,_|\___|_|  |_|   |_|  \___/ 
{YELLOW}
        [+--- Natespo Advanced Security Framework v2.1 ---+]
        [+--- Added Module: Password Cracker Logic     ---+]
{RESET}"""
        print(banner)

    # মডিউল ১: ওয়েবসাইট অডিট (NuGet Logic)
    def audit_url(self, url):
        print(f"\n{CYAN}[*] Web Audit: {url}{RESET}")
        try:
            res = requests.get(url, timeout=5)
            for h in self.headers_to_check:
                if h in res.headers:
                    print(f"{GREEN}[✔] Secure: '{h}' found.{RESET}")
                else:
                    print(f"{RED}[✘] Missing: '{h}'!{RESET}")
        except:
            print(f"{RED}[-] Error: Connection Failed.{RESET}")

    # মডিউল ২: ফাইল ও পারমিশন স্ক্যান (Bypass Logic)
    def scan_file(self, path):
        try:
            with open(path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in self.malware_signatures:
                    return f"{RED}[✘] MALWARE: {path}{RESET}"
                return f"{GREEN}[✔] SAFE: {path}{RESET}"
        except PermissionError:
            return f"{YELLOW}[!] BYPASSING: Permission Denied for {path}{RESET}"
        except:
            return f"{RED}[-] Error scanning: {path}{RESET}"

    # মডিউল ৩: পাসওয়ার্ড ক্র্যাকার (Rockyou.txt Logic)
    def crack_hash(self, target_hash, wordlist_path):
        print(f"\n{CYAN}[*] Cracking MD5 Hash: {target_hash}{RESET}")
        print(f"{YELLOW}[*] Using Wordlist: {wordlist_path}{RESET}\n")
        try:
            count = 0
            with open(wordlist_path, 'r', encoding='latin-1') as f:
                for line in f:
                    word = line.strip()
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                    count += 1
                    if count % 100000 == 0:
                        print(f"[*] Checked {count} passwords...", end='\r')
                    
                    if hashed_word == target_hash:
                        return f"\n{GREEN}[✔] SUCCESS! Password Found: {word}{RESET}"
            return f"\n{RED}[✘] Failed: Password not found in worldist.{RESET}"
        except FileNotFoundError:
            return f"{RED}[-] Error: Rockyou.txt not found at the given path.{RESET}"

def main():
    app = DataFinderPro()
    app.show_banner()
    
    print(f"{YELLOW}1. Web Security Audit")
    print("2. Malware & Permission Scan")
    print(f"3. Password Hash Cracker (MD5){RESET}")
    
    choice = input(f"\n{CYAN}Select Option: {RESET}")
    
    if choice == "1":
        target = input("Enter URL: ")
        app.audit_url(target)
    elif choice == "2":
        path = input("Enter Path: ")
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for name in files:
                    print(app.scan_file(os.path.join(root, name)))
        else:
            print(app.scan_file(path))
    elif choice == "3":
        t_hash = input("Enter MD5 Hash: ")
        w_path = input("Enter Rockyou.txt Path: ")
        print(app.crack_hash(t_hash, w_path))

if __name__ == "__main__":
    main()
