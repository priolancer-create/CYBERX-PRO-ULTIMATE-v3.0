#!/usr/bin/env python3
# ============================================================
# CYBERX PRO ULTIMATE v3.0
# Single-file defensive cybersecurity research toolkit
# Android Termux / Python 3
# Use only on systems you own or are explicitly authorized to test.
# ============================================================

import os
import sys
import re
import ssl
import json
import time
import socket
import hashlib
import getpass
import platform
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

APP_NAME = "CYBERX PRO ULTIMATE"
VERSION = "3.0"
BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "reports"
LOG_DIR = BASE_DIR / "logs"
DB_FILE = BASE_DIR / "cyberx_history.json"

# The catalog documents 100 well-known tools. Availability depends on OS,
# architecture, dependencies, and the user's authorization.
TOOL_CATALOG = [
    ("Nmap", "Network discovery and port auditing", "External / optional"),
    ("Masscan", "High-speed port scanner", "External / not bundled"),
    ("Amass", "Attack-surface discovery", "External / not bundled"),
    ("Subfinder", "Subdomain discovery", "External / not bundled"),
    ("Assetfinder", "Asset discovery", "External / not bundled"),
    ("theHarvester", "Public-source reconnaissance", "External / not bundled"),
    ("Recon-ng", "Reconnaissance framework", "External / not bundled"),
    ("SpiderFoot", "OSINT automation", "External / not bundled"),
    ("Maltego", "Relationship analysis", "External / not bundled"),
    ("Whois", "Domain registration lookup", "Optional CLI"),
    ("Burp Suite", "Web application testing proxy", "Desktop / external"),
    ("OWASP ZAP", "Web application security testing", "External"),
    ("Nikto", "Web server assessment", "External"),
    ("Wapiti", "Web vulnerability assessment", "External"),
    ("WhatWeb", "Website technology identification", "External"),
    ("Wappalyzer", "Website technology identification", "External"),
    ("Nuclei", "Template-based security checks", "External"),
    ("WPScan", "WordPress security assessment", "External"),
    ("Feroxbuster", "Content discovery", "External"),
    ("Gobuster", "Content discovery", "External"),
    ("Wireshark", "Packet analysis", "Desktop / external"),
    ("tcpdump", "Packet capture and analysis", "Optional CLI"),
    ("Bettercap", "Network security research", "External"),
    ("Zeek", "Network monitoring", "External"),
    ("Suricata", "Network intrusion detection", "External"),
    ("Snort", "Network intrusion detection", "External"),
    ("Netcat", "Network diagnostics", "Optional CLI"),
    ("Socat", "Network communication diagnostics", "External"),
    ("OpenVAS", "Vulnerability assessment", "Server / external"),
    ("Greenbone", "Vulnerability management", "Server / external"),
    ("John the Ripper", "Password hash auditing", "External"),
    ("Hashcat", "Password hash auditing", "External"),
    ("Hydra", "Authentication testing", "Not bundled"),
    ("CeWL", "Wordlist generation", "External"),
    ("Crunch", "Wordlist generation", "External"),
    ("KeePassXC", "Password management", "Desktop / external"),
    ("Gitleaks", "Secret detection in repositories", "External"),
    ("TruffleHog", "Secret detection", "External"),
    ("detect-secrets", "Secret scanning", "External"),
    ("Have I Been Pwned", "Breach-awareness lookup", "Web service"),
    ("Autopsy", "Digital forensics", "Desktop / external"),
    ("The Sleuth Kit", "Filesystem forensics", "External"),
    ("Volatility", "Memory forensics", "External"),
    ("FTK Imager", "Forensic imaging", "Desktop / external"),
    ("ExifTool", "Metadata inspection", "Optional CLI"),
    ("Binwalk", "Firmware analysis", "External"),
    ("Foremost", "File carving", "External"),
    ("PhotoRec", "File recovery", "External"),
    ("YARA", "Pattern-based file analysis", "External"),
    ("Ghidra", "Reverse engineering", "Desktop / external"),
    ("IDA Free", "Binary analysis", "Desktop / external"),
    ("Radare2", "Reverse engineering", "External"),
    ("JADX", "Android package analysis", "External"),
    ("Apktool", "Android package resource analysis", "External"),
    ("Frida", "Application security research", "External"),
    ("GDB", "Debugging", "Optional CLI"),
    ("x64dbg", "Binary debugging", "Windows / external"),
    ("Detect It Easy", "File identification", "Desktop / external"),
    ("CAPA", "Executable capability analysis", "External"),
    ("Sherlock", "Public username OSINT", "External"),
    ("Maigret", "Public username OSINT", "External"),
    ("PhoneInfoga", "Phone-number OSINT", "External"),
    ("GHunt", "Public exposure research", "External"),
    ("Holehe", "Public account exposure checks", "External"),
    ("OSINT Framework", "OSINT resource directory", "Web resource"),
    ("Google Dorks", "Public search research", "Manual / web"),
    ("ScoutSuite", "Cloud security auditing", "External"),
    ("Prowler", "Cloud security assessment", "External"),
    ("Checkov", "Infrastructure-as-code scanning", "External"),
    ("Trivy", "Container vulnerability scanning", "External"),
    ("Grype", "Software vulnerability scanning", "External"),
    ("Semgrep", "Static code analysis", "External"),
    ("Bandit", "Python security analysis", "External"),
    ("MobSF", "Mobile application security", "Server / external"),
    ("testssl.sh", "TLS configuration assessment", "External"),
    ("SSLyze", "TLS configuration assessment", "External"),
    ("Metasploit Framework", "Authorized penetration testing", "Not bundled"),
    ("Kali Linux", "Security testing distribution", "Separate OS"),
    ("Parrot Security OS", "Security testing distribution", "Separate OS"),
    ("Security Onion", "Security monitoring platform", "Separate OS"),
    ("SET", "Security awareness simulation", "External"),
    ("Caldera", "Adversary emulation", "Controlled lab only"),
    ("Atomic Red Team", "Defensive control testing", "Controlled lab"),
    ("MITRE ATT&CK", "Threat knowledge base", "Reference"),
    ("Prelude Operator", "Security validation", "External"),
    ("BloodHound CE", "Directory security analysis", "External"),
    ("Python", "Security automation", "Available in Termux"),
    ("Scapy", "Packet analysis and crafting", "Python package"),
    ("Requests", "HTTP client library", "Python package"),
    ("SQLMap", "SQL injection testing", "External / authorized only"),
    ("OWASP Dependency-Check", "Dependency vulnerability checks", "External"),
    ("Snyk", "Software security analysis", "External service"),
    ("SonarQube", "Code quality and security", "Server / external"),
    ("Checkmarx", "Static application security testing", "Commercial"),
    ("DefectDojo", "Vulnerability management", "Server / external"),
    ("OpenSSL", "Cryptographic and TLS utilities", "Optional CLI"),
    ("DNSViz", "DNSSEC visualization", "Web service"),
    ("testssl.sh", "TLS assessment", "External"),
    ("Lynis", "System security auditing", "External"),
    ("ClamAV", "Antivirus scanning", "External"),
    ("Rkhunter", "Rootkit checks", "Linux / external"),
    ("Fail2ban", "Host intrusion prevention", "Linux server"),
    ("UFW", "Host firewall management", "Linux / external"),
]
# Keep the public catalog at exactly 100 entries.
TOOL_CATALOG = TOOL_CATALOG[:100]

SAFE_PORTS = [21, 22, 25, 53, 80, 110, 143, 443, 445, 8080, 8443]
USER_AGENT = "CyberX-Pro-Ultimate/3.0 (defensive-security-audit)"


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def color(text, code):
    return f"\033[{code}m{text}\033[0m"


def banner():
    print(color(r"""
   ______ __   __ ____  ______ ____  __  __
  / ____// /  / // __ \/ ____// __ \/ / / /
 / /    / /__/ // /_/ / /    / /_/ / /_/ /
/ /___ / __  // ____/ /___ / _, _/ __  /
\____//_/ /_//_/     \____//_/ |_/_/ /_/
          PRO ULTIMATE  v3.0
""", "36;1"))
    print(color("  DEFENSIVE SECURITY RESEARCH • TERMUX EDITION", "32;1"))
    print(color("  Authorized systems and controlled labs only", "33"))
    print("-" * 62)


def ensure_dirs():
    REPORT_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)
    if not DB_FILE.exists():
        DB_FILE.write_text("[]", encoding="utf-8")


def log_event(action, target="", status="INFO", details=""):
    record = {
        "time": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "target": target,
        "status": status,
        "details": details,
    }
    try:
        data = json.loads(DB_FILE.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            data = []
    except Exception:
        data = []
    data.append(record)
    DB_FILE.write_text(json.dumps(data[-500:], indent=2, ensure_ascii=False), encoding="utf-8")
    with (LOG_DIR / "cyberx.log").open("a", encoding="utf-8") as f:
        f.write(f"{record['time']} | {status} | {action} | {target} | {details}\n")


def save_report(title, target, results):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = re.sub(r"[^a-zA-Z0-9_-]+", "_", title).strip("_") or "report"
    path = REPORT_DIR / f"{safe_title}_{stamp}.json"
    report = {
        "application": APP_NAME,
        "version": VERSION,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "title": title,
        "target": target,
        "notice": "Authorized defensive testing only.",
        "results": results,
    }
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(color(f"\n[+] Report saved: {path}", "32"))
    log_event("report_saved", target, "OK", str(path))
    return path


def pause():
    input(color("\nPress Enter to return to the menu...", "33"))


def valid_host(value):
    value = value.strip()
    if not value or len(value) > 253 or any(c.isspace() for c in value):
        return False
    if value.startswith("http://") or value.startswith("https://"):
        return False
    if "/" in value or "\\" in value or "@" in value:
        return False
    try:
        socket.inet_pton(socket.AF_INET, value)
        return True
    except OSError:
        pass
    try:
        socket.inet_pton(socket.AF_INET6, value)
        return True
    except OSError:
        pass
    if value.endswith("."):
        value = value[:-1]
    labels = value.split(".")
    return all(
        label and len(label) <= 63
        and re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?", label)
        for label in labels
    )


def normalize_url(value):
    value = value.strip()
    if not value.startswith(("http://", "https://")):
        value = "https://" + value
    from urllib.parse import urlparse
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not valid_host(parsed.hostname or ""):
        raise ValueError("Enter a valid HTTP/HTTPS URL.")
    if parsed.username or parsed.password:
        raise ValueError("Username/password must not be included in the URL.")
    return value, parsed


def authorization_gate():
    print(color("\nAuthorization Notice", "33;1"))
    print("Test only your own devices/websites or targets you have explicit written permission to assess.")
    answer = input("Are you authorized to test this target? (yes/no): ").strip().lower()
    if answer not in ("yes", "y"):
        print(color("Test cancelled.", "31"))
        return False
    return True


def dns_lookup():
    host = input("Domain/IP (e.g. example.com): ").strip()
    if not valid_host(host):
        print(color("Invalid hostname/IP.", "31"))
        return
    try:
        records = socket.getaddrinfo(host, None)
        ips = sorted({item[4][0] for item in records})
        print(color("\nDNS / Address Results:", "32;1"))
        for ip in ips:
            print("  •", ip)
        save_report("dns_lookup", host, {"addresses": ips})
        log_event("dns_lookup", host, "OK", f"{len(ips)} addresses")
    except Exception as exc:
        print(color(f"DNS lookup failed: {exc}", "31"))
        log_event("dns_lookup", host, "ERROR", str(exc))


def http_headers_check():
    raw = input("Your own/authorized website URL: ").strip()
    try:
        url, parsed = normalize_url(raw)
    except Exception as exc:
        print(color(str(exc), "31"))
        return
    if not authorization_gate():
        return
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            headers = dict(response.headers.items())
            status = response.status
            final_url = response.geturl()
        wanted = [
            "Content-Security-Policy", "Strict-Transport-Security",
            "X-Content-Type-Options", "X-Frame-Options",
            "Referrer-Policy", "Permissions-Policy",
        ]
        print(color(f"\nHTTP status: {status}", "32"))
        print("Final URL:", final_url)
        for name in wanted:
            value = headers.get(name)
            mark = "PRESENT" if value else "MISSING"
            print(f"{name:32} {mark}" + (f" — {value}" if value else ""))
        results = {"status": status, "final_url": final_url, "headers": headers,
                   "missing_security_headers": [h for h in wanted if not headers.get(h)]}
        save_report("http_headers", parsed.hostname, results)
        log_event("http_headers", parsed.hostname, "OK", f"HTTP {status}")
    except urllib.error.HTTPError as exc:
        print(color(f"HTTP error: {exc.code}", "31"))
    except Exception as exc:
        print(color(f"Request failed: {exc}", "31"))


def tls_check():
    host = input("Your own/authorized HTTPS domain: ").strip()
    if not valid_host(host):
        print(color("Invalid hostname.", "31"))
        return
    if not authorization_gate():
        return
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=8) as raw_sock:
            with context.wrap_socket(raw_sock, server_hostname=host) as sock:
                cert = sock.getpeercert()
                cipher = sock.cipher()
                version = sock.version()
        result = {
            "tls_version": version,
            "cipher": cipher,
            "subject": cert.get("subject"),
            "issuer": cert.get("issuer"),
            "not_before": cert.get("notBefore"),
            "not_after": cert.get("notAfter"),
            "subject_alt_name": cert.get("subjectAltName"),
        }
        print(color("\nTLS connection verified", "32;1"))
        print("TLS version:", version)
        print("Cipher:", cipher)
        print("Certificate expires:", cert.get("notAfter", "Unknown"))
        save_report("tls_check", host, result)
        log_event("tls_check", host, "OK", version or "")
    except Exception as exc:
        print(color(f"TLS check failed: {exc}", "31"))
        log_event("tls_check", host, "ERROR", str(exc))


def limited_port_audit():
    host = input("Your own/authorized host/IP: ").strip()
    if not valid_host(host):
        print(color("Invalid hostname/IP.", "31"))
        return
    if not authorization_gate():
        return
    print("This safe audit checks only a limited set of common TCP ports:")
    print(", ".join(map(str, SAFE_PORTS)))
    confirm = input("Proceed? (yes/no): ").strip().lower()
    if confirm not in ("yes", "y"):
        return
    opened, checked = [], []
    print(color("\nStarting TCP connection audit...", "36"))
    for port in SAFE_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.7)
        try:
            code = sock.connect_ex((host, port))
            state = "OPEN" if code == 0 else "CLOSED/FILTERED"
            checked.append({"port": port, "state": state})
            if code == 0:
                opened.append(port)
                print(color(f"  {port:5} OPEN", "32"))
            else:
                print(f"  {port:5} closed/filtered")
        except OSError as exc:
            checked.append({"port": port, "state": "ERROR", "error": str(exc)})
            print(f"  {port:5} error")
        finally:
            sock.close()
        time.sleep(0.15)
    save_report("limited_tcp_audit", host, {"checked": checked, "open_ports": opened})
    log_event("limited_tcp_audit", host, "OK", f"open={opened}")


def password_strength():
    print("This is a local strength check for your own password only.")
    password = getpass.getpass("Password (hidden on screen and not stored): ")
    if not password:
        print("Empty input.")
        return
    score = 0
    checks = {
        "At least 12 characters": len(password) >= 12,
        "Uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"\d", password)),
        "Symbol": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
    for label, passed in checks.items():
        print(f"[{'OK' if passed else '--'}] {label}")
        score += int(passed)
    common = {"password", "123456789", "qwerty123", "admin123", "letmein"}
    if password.lower() in common:
        score = 0
        print(color("Warning: This is a very common password.", "31"))
    grade = "Weak" if score <= 2 else "Fair" if score <= 3 else "Strong" if score == 4 else "Very strong"
    print(color(f"\nStrength estimate: {grade}", "32" if score >= 4 else "33"))
    log_event("password_strength", "LOCAL ONLY", "OK", grade)
    password = None


def file_integrity():
    raw = input("Full path to your own file: ").strip()
    path = Path(raw).expanduser()
    if not path.is_file():
        print(color("File not found.", "31"))
        return
    sha256 = hashlib.sha256()
    size = 0
    try:
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                size += len(chunk)
                sha256.update(chunk)
        stat = path.stat()
        result = {
            "file_name": path.name,
            "size_bytes": size,
            "modified_time": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "sha256": sha256.hexdigest(),
        }
        print(color("\nFile integrity information", "32;1"))
        for key, value in result.items():
            print(f"{key}: {value}")
        save_report("file_integrity", str(path), result)
        log_event("file_integrity", str(path), "OK", result["sha256"])
    except Exception as exc:
        print(color(f"File analysis failed: {exc}", "31"))


def source_code_audit():
    raw = input("Path to your own source code file (.py/.js/.html/.php): ").strip()
    path = Path(raw).expanduser()
    if not path.is_file():
        print(color("File not found.", "31"))
        return
    try:
        text_data = path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        print(color(str(exc), "31"))
        return
    rules = [
        ("Possible hardcoded secret", re.compile(r"""(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['"][^'"]{6,}['"]""")),
        ("Dangerous eval usage", re.compile(r"\beval\s*\(")),
        ("Possible disabled TLS verification", re.compile(r"(?i)verify\s*=\s*False")),
        ("Possible unsafe shell execution", re.compile(r"(?i)(shell\s*=\s*True|os\.system\s*\()")),
        ("Possible SQL string concatenation", re.compile(r"""(?i)(execute|cursor\.execute)\s*\([^)]*(\+\s*|%s?\s*%)""")),
    ]
    findings = []
    lines = text_data.splitlines()
    for number, line in enumerate(lines, 1):
        for label, pattern in rules:
            if pattern.search(line):
                findings.append({"line": number, "finding": label, "snippet": line.strip()[:180]})
    print(color(f"\nStatic review: {len(findings)} potential finding(s)", "33;1"))
    for item in findings[:100]:
        print(f"L{item['line']}: {item['finding']} — {item['snippet']}")
    if not findings:
        print(color("No matches found by this basic rule set. This does not guarantee security.", "32"))
    save_report("source_code_review", str(path), {"findings": findings, "lines_checked": len(lines)})
    log_event("source_code_review", str(path), "OK", f"{len(findings)} findings")


def username_osint_guidance():
    username = input("Public username (public information research only): ").strip()
    if not re.fullmatch(r"[A-Za-z0-9_.-]{2,40}", username):
        print(color("Invalid username format.", "31"))
        return
    urls = [
        f"https://github.com/{username}",
        f"https://www.reddit.com/user/{username}/",
        f"https://www.instagram.com/{username}/",
        f"https://x.com/{username}",
    ]
    print(color("\nManual public-profile references (existence not verified):", "36;1"))
    for url in urls:
        print(" •", url)
    print("Private accounts, login walls, and personal information are not bypassed.")
    save_report("public_username_references", username, {"reference_urls": urls, "verified": False})
    log_event("public_username_references", username, "OK", "URLs generated; not verified")


def tool_catalog():
    print(color("\n100-TOOL INTEGRATION CATALOG", "36;1"))
    for index, (name, purpose, status) in enumerate(TOOL_CATALOG, 1):
        print(f"{index:03}. {name:<25} | {purpose} [{status}]")
    print(f"\nTotal catalog entries: {len(TOOL_CATALOG)}")
    print("A catalog entry does not mean the tool is installed or executable from this Python file.")
    save_report("tool_catalog", "LOCAL", {"tools": [
        {"name": n, "purpose": p, "status": s} for n, p, s in TOOL_CATALOG
    ]})


def history_view():
    try:
        data = json.loads(DB_FILE.read_text(encoding="utf-8"))
        if not data:
            print("No activity history yet.")
            return
        print(color("\nLatest 20 Activities", "36;1"))
        for item in data[-20:][::-1]:
            print(f"{item.get('time','')} | {item.get('action','')} | "
                  f"{item.get('target','')} | {item.get('status','')}")
    except Exception as exc:
        print(color(f"History read error: {exc}", "31"))


def system_info():
    info = {
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "architecture": platform.machine(),
        "hostname": socket.gethostname(),
        "base_directory": str(BASE_DIR),
    }
    print(color("\nSystem information", "36;1"))
    for k, v in info.items():
        print(f"{k}: {v}")
    log_event("system_info", "LOCAL", "OK", platform.platform())


def main_menu():
    ensure_dirs()
    while True:
        clear()
        banner()
        print("""
 [01] Dashboard / System Info
 [02] DNS & IP Lookup
 [03] Website HTTP Security Headers
 [04] TLS / SSL Certificate Check
 [05] Limited TCP Port Audit (authorized only)
 [06] Local Password Strength Check
 [07] File SHA-256 Integrity Check
 [08] Source Code Static Review
 [09] Public Username OSINT References
 [10] 100-Tool Catalog
 [11] Activity History
 [12] Exit
""")
        choice = input(color("CYBERX@Termux >> ", "32;1")).strip()
        if choice == "1":
            system_info()
        elif choice == "2":
            dns_lookup()
        elif choice == "3":
            http_headers_check()
        elif choice == "4":
            tls_check()
        elif choice == "5":
            limited_port_audit()
        elif choice == "6":
            password_strength()
        elif choice == "7":
            file_integrity()
        elif choice == "8":
            source_code_audit()
        elif choice == "9":
            username_osint_guidance()
        elif choice == "10":
            tool_catalog()
        elif choice == "11":
            history_view()
        elif choice == "12":
            print(color("\nCYBERX PRO  is shutting down. Stay safe.", "32"))
            break
        else:
            print(color("Select a valid option.", "31"))
        pause()


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(color("\nOperation interrupted by user.", "33"))
    except Exception as error:
        print(color(f"\nUnexpected error: {error}", "31"))
