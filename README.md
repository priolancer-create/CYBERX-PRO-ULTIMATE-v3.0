# CYBERX-PRO-ULTIMATE-v3.0
CYBERX PRO ULTIMATE v3.0 ADVANCED CYBERSECURITY RESEARCH TOOLKIT DEVELOPED BY: Mostafizur Rahman PLATFORM: ANDROID TERMUX DISCOVER • ANALYZE • PROTECT
।CYBERX PRO ULTIMATE v3.0
A single-file, Python-based defensive cybersecurity research toolkit designed for Android Termux and Python 3.
Use this toolkit only on systems, websites, and files that you own or are explicitly authorized to assess.
Features
System information dashboard
DNS and IP lookup
Website HTTP security-header review
TLS/SSL certificate check
Limited TCP port audit (predefined common ports)
Local password-strength estimate (password is not stored)
File SHA-256 integrity check
Basic source-code static review
Public username profile-reference generator
Catalog of 100 security tools and resources
JSON reports, activity history, and log files
Important: The 100-tool catalog is a reference list. It does not install or bundle those external tools. Availability depends on the operating system and installed software.
Requirements
Python 3
Git (only needed to clone the GitHub repository)
Android Termux, Linux, or another Python 3 environment
Internet access for DNS, HTTP, and TLS checks
The script uses Python standard-library modules; no third-party Python package is required for the current features.
Install on Android (Termux)
Open Termux and run:
pkg update -y && pkg upgrade -y
pkg install python git -y
Download from GitHub
Replace YOUR_USERNAME and YOUR_REPOSITORY with your GitHub username and repository name:
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
Run
If the Python file is named CYBERX PRO ULTIMATE v3.0.py:
python "CYBERX PRO ULTIMATE v3.0.py"
Or rename it to a shorter filename:
mv "CYBERX PRO ULTIMATE v3.0.py" cyberx_pro.py
python cyberx_pro.py
Install on Linux
sudo apt update
sudo apt install -y python3 git
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
python3 "CYBERX PRO ULTIMATE v3.0.py"
Upload the project to GitHub
First, create an empty repository on GitHub. Then, from the project folder, run:
git init
git add "CYBERX PRO ULTIMATE v3.0.py" README.md
git commit -m "Initial release: CYBERX PRO ULTIMATE v3.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
If the remote named origin already exists, update it instead:
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
Run options
Environment        Command
Termux / Android   python "CYBERX PRO ULTIMATE v3.0.py" Linux              python3 "CYBERX PRO ULTIMATE v3.0.py" After renaming     python cyberx_pro.py
Output files
When the application runs, it creates these items in the same directory as the script:
reports/ --- JSON audit reports
logs/ --- activity log
cyberx_history.json --- recent activity history
Keep generated reports and logs private if they contain information about your systems.
Menu
Dashboard / System Info
DNS & IP Lookup
Website HTTP Security Headers
TLS / SSL Certificate Check
Limited TCP Port Audit
Local Password Strength Check
File SHA-256 Integrity Check
Source Code Static Review
Public Username OSINT References
100-Tool Catalog
Activity History
Exit
Responsible use and limitations
Obtain permission before testing a website, host, or network.
The port audit checks only the predefined ports in the script; it is not a full vulnerability scan.
The source-code review uses basic pattern matching and can produce false positives or miss issues.
Generated public-profile URLs are references only; the script does not verify that profiles exist.
The password-strength feature is a simple local estimate, not a password-cracking or breach-checking service.
The tool catalog does not mean those tools are installed, available, or integrated.
Do not use this project to access accounts, devices, networks, or data without authorization.
License
Choose and add a license before publishing if you want to define how others may use, modify, and redistribute this project. Do not claim a license that you have not added.
Author
Add your GitHub username or project-maintainer details here.
