# 🛡️ DataFinderPro v2.3
**Natespo Advanced Security Framework** - A modular and hybrid security auditing tool designed for Termux and Linux environments.

## 🚀 Overview
DataFinderPro is a multi-functional security tool that works in both **Root** and **Non-Root** modes. Whether you are performing a web audit, scanning for malware, or analyzing local networks, this tool provides a comprehensive suite for security enthusiasts.

---

## ✨ Features
### 🌐 1. Web Security Audit
- Checks for essential security headers (CSP, X-Frame-Options, etc.).
- Identifies missing protections on target URLs.

### 🛡️ 2. Malware & Permission Scan
- Scans files for known malware signatures (MD5).
- Detects permission-restricted files in the system.

### 🔑 3. Password Hash Cracker
- High-speed MD5 hash cracking using wordlists like `Rockyou.txt`.
- Optimized for mobile processing in Termux.

### 📡 4. Network Analysis & Port Scan (New!)
- Scans common ports (SSH, HTTP, DNS, etc.) to identify running services.
- **Root Mode:** Displays the local ARP table and device MAC addresses.

### 📶 5. Wi-Fi Password Dump (Root Only!)
- Automatically detects root access.
- Dumps saved Wi-Fi configurations and passwords from system directories.

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/zxmoon76-sys/Data-Finder-Pro.git](https://github.com/zxmoon76-sys/Data-Finder-Pro.git)
   cd Data-Finder-Pro
   pip install requests
   
python finder.py
This tool is developed for Educational Purposes only. Use it responsibly and only on systems you have permission to audit. The developer (Mamun)  is not responsible for any misuse.
