# PuranaPata (پرانہ پتہ) - OSINT Investigation Tool

PuranaPata is a powerful OSINT (Open-Source Intelligence) tool designed for investigative purposes. It fetches historical snapshots of websites, compares them, scans for keywords, and provides comprehensive reports. The tool is intended for ethical use only, supporting legal investigations, cybersecurity assessments, and digital forensics.

---

## ⚖️ Ethical Considerations
PuranaPata is strictly intended for legal and ethical use. Misuse for illegal activities, privacy invasion, or surveillance is strictly prohibited. The authors and contributors are not responsible for any misuse or consequences arising from the use of this software.

## 💻 Features
- Fetch website snapshots from the Wayback Machine.
- Compare snapshots for changes with HTML diff reports.
- Scan content for specific keywords or patterns.
- Export reports to PDF, JSON, XLSX, or HTML.
- Perform domain reconnaissance (WHOIS/DNS).
- Threat intelligence integrations (VirusTotal, AbuseIPDB).
- Dynamic plugin support.
- Automation and alerting with monitoring.

---

## 🚀 Installation
1. Clone the repository:
```bash
 git clone https://github.com/MuhammadBalochh/PuranaPata.git
```
2. Navigate to the project directory:
```bash
 cd PuranaPata
```
3. Install dependencies:
```bash
 pip install -r requirements.txt
```
4. Set API keys using:
```bash
 python src/main.py --setup
```

---

## 🟢 Commands & Usage
### Fetch Snapshots
```bash
python src/main.py https://example.com --limit 5 --export pdf
```

### Keyword Scanning
```bash
python src/main.py https://example.com --keywords "admin,password"
```

### WHOIS/DNS Reconnaissance
```bash
python src/main.py --domain example.com --whois
```

### Threat Intelligence
```bash
python src/main.py --ip 192.168.1.1 --threatintel
```

### Dynamic Plugin Execution
```bash
python src/main.py --plugin custom_plugin --target example.com
```

---

## 📝 License
MIT License - Modified for Ethical Use

Copyright (c) 2025 nerd-e-pak

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The Software shall not be used for any illegal, unethical, or unauthorized activities, including but not limited to hacking, surveillance, or privacy invasion without consent.
2. This software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement.
3. The authors and contributors are not liable for any misuse or damage caused by the use of this software.
4. The use of this software in illegal operations or malicious activities is strictly prohibited. The author is not responsible for any consequences arising from such use.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

