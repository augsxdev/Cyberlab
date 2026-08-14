# CYBERLAB

> *"Observe. Analyze. Control."*

---

# STATUS

> **⚠️ PROJECT UNDER DEVELOPMENT**

CyberLab is currently being built from scratch.

The architecture, modules, API and desktop interface are under active development and may change frequently.

<img align="right" width="280" src="star.jpg">

---

# ABOUT

CyberLab is a modular cybersecurity framework focused on network analysis, reconnaissance and infrastructure auditing.

Designed for learning, research and software engineering, the project combines a **Python backend** with a modern **C# WPF desktop interface**.

### Current Features

- Network Discovery
- TCP Port Scanner
- Hostname Resolution
- DNS Lookup
- Operating System Detection
- Service Identification
- Security Alerts
- Report Generation
- Desktop Dashboard

<br><br>

---

<img align="left" width="250" src="mordendo crucifixo.jpg">

# ROADMAP

### Core

- [x] Project Structure
- [x] Main Application
- [x] TCP Scanner
- [x] Reports Module
- [x] Alerts Module
- [x] Utilities
- [ ] Network Discovery
- [ ] Hostname Detection
- [ ] DNS Resolution
- [ ] Service Detection
- [ ] Banner Grabbing
- [ ] Operating System Detection

### Infrastructure

- [ ] SQLite Database
- [ ] REST API
- [ ] Logging
- [ ] Configuration System

### Desktop

- [ ] CyberLab Desktop
- [ ] Dashboard
- [ ] Scan History
- [ ] Real-Time Monitoring

<br><br><br><br><br><br><br><br>

---

# PROJECT STRUCTURE

```text
CyberLab/
│
├── api/
├── assets/
├── core/
│   ├── __init__.py
│   ├── alerts.py
│   ├── banner.py
│   ├── dns.py
│   ├── hostname.py
│   ├── network.py
│   ├── osdetect.py
│   ├── ports.py
│   ├── reports.py
│   ├── scanner.py
│   ├── services.py
│   └── utils.py
│
├── database/
├── frontend/
│   └── CyberLab.Desktop/
│
├── logs/
├── reports/
│
├── main.py
├── requirements.txt
└── README.md
```

---

<img align="right" width="300" src="catspider.jpg">

# TECHNOLOGY STACK

### Backend

- Python 3
- Socket
- SQLite *(planned)*
- FastAPI *(planned)*

### Frontend

- C#
- .NET 8
- WPF (XAML)

### Version Control

- Git
- GitHub

<br><br><br><br>

---

# OBJECTIVE

CyberLab aims to become a complete cybersecurity platform capable of:

- Discovering active devices
- Identifying Hostnames
- Detecting Operating Systems
- Enumerating Services
- Detecting Security Risks
- Generating Reports
- Monitoring Networks
- Providing a Modern Desktop Experience

---

# DEVELOPMENT

This repository is **actively under development**.

Expect frequent commits, refactoring and new modules over time.

The architecture follows a modular design to keep every component independent and scalable.

---

<p align="center">

<img width="170" src="star.jpg">

# CYBERLAB

### **WATCH • ANALYZE • CONTROL**

*"Built for learning. Designed for security."*


# CyberLab

MVP defensivo para inventário e análise de uma rede privada autorizada. Inclui API FastAPI, SQLite, scanner TCP limitado e uma interface WPF inicial em .NET 8.

> Use somente em sistemas e redes para os quais você tem autorização. A API rejeita alvos públicos e exige confirmação explícita de consentimento.

## Execução do backend

```powershell
cd CyberLab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Documentação: `http://127.0.0.1:8000/docs`

Exemplo de scan autorizado:

```powershell
Invoke-RestMethod -Method Post http://127.0.0.1:8000/api/scan -ContentType application/json -Body '{"target":"127.0.0.1","ports":[80,443],"consent":true}'
```

## Interface desktop

Com o backend em execução:

```powershell
cd frontend\CyberLab.Desktop
dotnet run
```

## Escopo deste MVP

- Scan TCP de portas comuns; banners simples.
- Descoberta limitada a redes privadas com até 254 hosts.
- Alertas de postura (não são exploração nem confirmação de vulnerabilidade).
- Histórico SQLite e exportação JSON, TXT e CSV.

Próximos passos: implementar ARP/MAC e fabricante com `scapy`, detecção de SO baseada em Nmap com consentimento e relatórios PDF.


</p>
