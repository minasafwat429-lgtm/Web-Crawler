# 🔍 Web Crawler - Simple Link Extractor

A lightweight, recursive web crawler that extracts and visits all internal links from any website. Perfect for website mapping, link analysis, and SEO audits.

## ✨ Features

- 🚀 Recursive crawling through all internal pages
- 🛡️ Automatic duplicate URL prevention
- ⚡ Timeout protection (10 seconds)
- 🎯 Domain-restricted crawling (stays within target site)
- 📝 Clean console output with real-time URL printing
- 🔧 Command-line interface for easy usage

## 📋 Requirements

- Python 3.6 or higher
- Internet connection

## 🛠️ Installation

```bash
# Clone or download the script
# Then install dependencies
pip install -r requirements.txt
```
## 🚀 Usage
```bash
python web_crawler.py -u https://example.com

 Options
Option	Description
-u, --url	Target website URL to crawl
-h, --help	Show help message
```
## Example
```bash
python web_crawler.py -u https://python.org
##Output:

text
[+] Starting crawl on: https://python.org

https://python.org
https://python.org/about
https://python.org/downloads
https://python.org/doc
https://python.org/community
...
```

##⚠️ Limitations
Does not execute JavaScript (links from dynamic content won't be found)

Single-threaded (sequential crawling)

No robots.txt compliance

HTTP only (no HTTPS certificate validation issues)

##📝 Notes
The crawler only follows internal links (same domain)

Fragments/anchors (#section) are automatically removed

Duplicate URLs are skipped automatically

##🧪 Tested On
Linux (Ubuntu, Debian)

Windows 10/11

macOS

##🤝 Contributing
Feel free to fork, modify, and submit pull requests!

##👨‍💻 Author
Mina Safwat

##⭐ Support
If you find this tool useful, give it a star on GitHub!
