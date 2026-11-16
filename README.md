::: {align="center"}
# CYBERX PRO ULTIMATE v3.0

### Defensive Cybersecurity Research Toolkit

**Android Termux · Linux · Python 3**

A single-file toolkit for basic, authorized security checks and local
file analysis.
:::

------------------------------------------------------------------------

## 📌 পরিচিতি

**CYBERX PRO ULTIMATE v3.0** হলো Python 3-ভিত্তিক একটি একক-ফাইলের
প্রতিরক্ষামূলক সাইবার নিরাপত্তা গবেষণা টুলকিট। এটি Android Termux, Linux এবং
Python 3 সমর্থিত পরিবেশে চালানোর জন্য তৈরি।

> **⚠️ ব্যবহারসংক্রান্ত সতর্কতা:** নিজের মালিকানাধীন সিস্টেম, ওয়েবসাইট ও ফাইল
> পরীক্ষা করুন। অন্য কোনো সিস্টেম পরীক্ষা করার আগে মালিকের স্পষ্ট অনুমতি নিন।

## ✨ প্রধান ফিচার

  ফিচার                        বিবরণ
  ---------------------------- ------------------------------------------------
  System Dashboard             ডিভাইস ও সিস্টেমের প্রয়োজনীয় তথ্য
  DNS ও IP Lookup              ডোমেইনের DNS ও IP-সংক্রান্ত তথ্য
  HTTP Security Headers        ওয়েবসাইটের HTTP নিরাপত্তা হেডার পর্যালোচনা
  TLS/SSL Check                TLS/SSL সার্টিফিকেট পরীক্ষা
  TCP Port Audit               পূর্বনির্ধারিত সাধারণ TCP পোর্ট পরীক্ষা
  Password Strength            পাসওয়ার্ডের স্থানীয় শক্তিমাত্রা মূল্যায়ন
  SHA-256 Check                ফাইলের SHA-256 হ্যাশ তৈরি
  Source Code Review           সাধারণ প্যাটার্নের ভিত্তিতে প্রাথমিক কোড পর্যালোচনা
  Public Username References   পাবলিক প্রোফাইলের রেফারেন্স লিংক তৈরি
  Security Tools Catalog       ১০০টি নিরাপত্তা টুল ও রিসোর্সের তথ্যসূত্র
  Reports & Logs               JSON রিপোর্ট, ইতিহাস ও লগ সংরক্ষণ

**নোট:** ১০০টি টুলের ক্যাটালগটি তথ্যসূত্র মাত্র। এই প্রকল্প সেগুলো স্বয়ংক্রিয়ভাবে
ইনস্টল বা সমন্বয় করে না।

## 🧰 প্রয়োজনীয়তা

-   Android Termux অথবা Linux
-   Python 3
-   Git --- GitHub থেকে প্রজেক্ট ক্লোন করতে
-   DNS, HTTP ও TLS-ভিত্তিক পরীক্ষার জন্য ইন্টারনেট সংযোগ

বর্তমান ফিচার চালাতে Python-এর Standard Library যথেষ্ট; আলাদা তৃতীয়-পক্ষ
Python প্যাকেজ প্রয়োজন নেই।

------------------------------------------------------------------------

## 📱 Android Termux-এ ইনস্টল

### ধাপ ১ --- Termux প্রস্তুত করুন

``` bash
pkg update -y && pkg upgrade -y
pkg install python git -y
```

### ধাপ ২ --- GitHub Repository ক্লোন করুন

নিচের URL-এ `YOUR_USERNAME` ও `YOUR_REPOSITORY` নিজের তথ্য দিয়ে প্রতিস্থাপন
করুন।

``` bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### ধাপ ৩ --- টুল চালু করুন

ফাইলের নাম `CYBERX PRO ULTIMATE v3.0.py` থাকলে:

``` bash
python "CYBERX PRO ULTIMATE v3.0.py"
```

ঐচ্ছিকভাবে ফাইলের নাম ছোট করে চালাতে পারেন:

``` bash
mv "CYBERX PRO ULTIMATE v3.0.py" cyberx_pro.py
python cyberx_pro.py
```

------------------------------------------------------------------------

## 🐧 Linux-এ ইনস্টল

Debian/Ubuntu-ভিত্তিক Linux-এ:

``` bash
sudo apt update
sudo apt install -y python3 git
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
python3 "CYBERX PRO ULTIMATE v3.0.py"
```

------------------------------------------------------------------------

## ▶️ চালানোর কমান্ড --- দ্রুত দেখুন

  পরিবেশ             কমান্ড
  ------------------ -----------------------------------------
  Termux / Android   `python "CYBERX PRO ULTIMATE v3.0.py"`
  Linux              `python3 "CYBERX PRO ULTIMATE v3.0.py"`
  নাম পরিবর্তনের পর   `python cyberx_pro.py`

## 🗂️ টুলের মেনু

1.  Dashboard / System Information
2.  DNS ও IP Lookup
3.  HTTP Security Headers Check
4.  TLS / SSL Certificate Check
5.  Limited TCP Port Audit
6.  Local Password Strength Check
7.  SHA-256 File Integrity Check
8.  Basic Source Code Review
9.  Public Username OSINT References
10. Security Tools Catalog
11. Activity History
12. Exit

## 📁 তৈরি হওয়া ফাইল ও ফোল্ডার

টুল চালানোর সময় স্ক্রিপ্টের একই ডিরেক্টরিতে নিচের আইটেমগুলো তৈরি হতে পারে:

  আইটেম                   কাজ
  ----------------------- ---------------------------
  `reports/`              JSON ফরম্যাটে অডিট রিপোর্ট
  `logs/`                 কার্যক্রমের লগ
  `cyberx_history.json`   সাম্প্রতিক কার্যক্রমের ইতিহাস

রিপোর্ট ও লগে সিস্টেম-সংক্রান্ত সংবেদনশীল তথ্য থাকতে পারে। এগুলো নিরাপদে
সংরক্ষণ করুন এবং প্রকাশের আগে যাচাই করুন।

------------------------------------------------------------------------

## ☁️ GitHub-এ প্রজেক্ট আপলোড

GitHub-এ একটি খালি Repository তৈরি করে প্রজেক্ট ফোল্ডারে নিচের কমান্ড চালান:

``` bash
git init
git add "CYBERX PRO ULTIMATE v3.0.py" README.md
git commit -m "Initial release: CYBERX PRO ULTIMATE v3.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

যদি `origin` Remote আগে থেকেই যুক্ত থাকে, তাহলে `git remote add origin`-এর
বদলে চালান:

``` bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

------------------------------------------------------------------------

## 🔐 দায়িত্বশীল ব্যবহার ও সীমাবদ্ধতা

-   কোনো ওয়েবসাইট, হোস্ট বা নেটওয়ার্ক পরীক্ষা করার আগে মালিকের অনুমতি নিন।
-   TCP Port Audit কেবল স্ক্রিপ্টে নির্ধারিত পোর্ট পরীক্ষা করে; এটি পূর্ণাঙ্গ
    Vulnerability Scanner নয়।
-   Source Code Review সাধারণ প্যাটার্ন শনাক্ত করে। ভুল সতর্কতা আসতে পারে এবং
    কিছু সমস্যা শনাক্ত নাও হতে পারে।
-   Public Username Reference কেবল লিংক-রেফারেন্স তৈরি করে; সংশ্লিষ্ট
    প্রোফাইল বাস্তবে আছে কি না তা নিশ্চিত করে না।
-   Password Strength Check একটি সাধারণ স্থানীয় মূল্যায়ন; এটি পাসওয়ার্ড
    ক্র্যাকিং বা ফাঁস হওয়া পাসওয়ার্ড যাচাইয়ের সেবা নয়।
-   Security Tools Catalog-এ কোনো টুলের নাম থাকা মানেই সেটি ডিভাইসে ইনস্টল
    বা এই প্রকল্পের সঙ্গে সমন্বিত---এমন নয়।
-   অনুমতি ছাড়া অন্যের অ্যাকাউন্ট, ডিভাইস, নেটওয়ার্ক বা তথ্য ব্যবহারের চেষ্টা
    করবেন না।

## 📄 লাইসেন্স

প্রজেক্ট প্রকাশের আগে উপযুক্ত ওপেন-সোর্স লাইসেন্স যুক্ত করুন। লাইসেন্স ফাইল যুক্ত না
করা পর্যন্ত কোনো নির্দিষ্ট লাইসেন্সের দাবি করা হচ্ছে না।

## 👨‍💻 নির্মাতা ও রক্ষণাবেক্ষণ

এখানে আপনার GitHub ইউজারনেম, যোগাযোগের মাধ্যম অথবা রক্ষণাবেক্ষণকারীর তথ্য
যোগ করুন।

------------------------------------------------------------------------

::: {align="center"}
**CYBERX PRO ULTIMATE v3.0**

*দায়িত্বশীল ও অনুমোদিত সাইবার নিরাপত্তা পরীক্ষার জন্য তৈরি একটি সহায়ক টুলকিট।*
:::
