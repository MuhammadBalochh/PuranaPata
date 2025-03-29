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

