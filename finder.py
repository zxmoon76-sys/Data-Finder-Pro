#!/usr/bin/env python3
import os
import time
import requests
import socket
import re
from urllib.parse import urlparse

# কালার কোড
G = '\033[1;32m'
Y = '\033[1;33m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;36m'
W = '\033[0m'

def banner():
    os.system('clear')
    print(f"{C}")
    print(r"    ██████╗  █████╗ ████████╗ █████╗     ██████╗ ██████╗  ██████╗")
    print(r"    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗")
    print(r"    ██║  ██║███████║   ██║   ███████║    ██████╔╝██████╔╝██║   ██║")
    print(r"    ██║  ██║██╔══██║   ██║   ██╔══██║    ██╔═══╝ ██╔══██╗██║   ██║")
    print(r"    ██████╔╝██║  ██║   ██║   ██║  ██║    ██║     ██║  ██║╚██████╔╝")
    print(r"    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝")
    print(f"           {Y}[ ULTIMATE VULNERABILITY & DATA SCANNER ] - BY: MAMUN{W}")
    print(f"{B}    --------------------------------------------------------------{W}")

def vul_check(url):
    print(f"\n{Y}[*] Deep Vulnerability Scan & Fuzzing Started...{W}")
    report = f"\n--- Vuln Report for {url} ---"
    
    # ১. হেডার অ্যানালাইসিস (Security Gap)
    try:
        res = requests.get(url, timeout=5)
        headers = res.headers
        print(f"{B}[+] Server: {headers.get('Server', 'Hidden')}{W}")
        
        vulnerabilities = {
            'X-Frame-Options': 'Clickjacking Attack',
            'X-XSS-Protection': 'Cross-Site Scripting (XSS)',
            'Content-Security-Policy': 'Data Injection'
        }
        
        for h, risk in vulnerabilities.items():
            if h not in headers:
                print(f"{R}[!] WARNING: {h} is MISSING! Risk: {risk}{W}")
                report += f"\n- Missing {h}: Risk {risk}"
    except:
        print(f"{R}[!] Connection error during header check.{W}")

    # ২. অটোমেটেড ফিউজিং / পেলোড টেস্টিং (Simple Payload Test)
    print(f"{Y}[*] Testing Payloads on Target...{W}")
    payloads = ["' OR 1=1 --", "<script>alert(1)</script>", "../etc/passwd"]
    
    for p in payloads:
        try:
            test_url = f"{url}?id={p}" if "?" not in url else f"{url}&test={p}"
            r = requests.get(test_url, timeout=5)
            if r.status_code == 500:
                print(f"{R}[FOUND] Possible Vulnerability with payload: {p}{W}")
                report += f"\n- Potential Bug with payload: {p}"
            else:
                print(f"{G}[SAFE] Payload {p} blocked/ignored.{W}")
        except:
            pass
    return report

def save_report(data):
    with open("final_report.txt", "a") as f:
        f.write(data + "\n")
    print(f"\n{G}[+] Full Report Saved to final_report.txt{W}")

def main():
    banner()
    print(f"{G}[1]{W} Full Security Audit (Vuln + Fuzzing + IP)")
    print(f"{G}[2]{W} Read Saved Reports")
    print(f"{R}[3]{W} Exit")
    
    choice = input(f"\n{C}Select Option: {W}")
    
    if choice == '1':
        target = input(f"\n{B}Enter URL (e.g. https://google.com): {W}")
        if not target.startswith("http"): target = "https://" + target
        
        # IP & Port (সিম্পল ভার্সন)
        domain = urlparse(target).netloc
        try:
            ip = socket.gethostbyname(domain)
            print(f"{G}[+] Resolved IP: {ip}{W}")
        except: pass
        
        # ভালনারেবিলিটি ও পেলোড চেক
        v_report = vul_check(target)
        save_report(v_report)
        
        name = input(f"\n{B}Enter Name for Lab Record: {W}")
        print(f"\n{G}[SUCCESS] Mission Accomplished, Mamun!{W}")
        
    elif choice == '2':
        if os.path.exists("final_report.txt"):
            os.system("cat final_report.txt")
        else: print(f"{R}No reports yet.{W}")
        input("\nPress Enter...")
        main()
        
    elif choice == '3':
        exit()

if __name__ == "__main__":
    main()
