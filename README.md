
# Basic Network Sniffer

A simple Windows-compatible network packet sniffer built using Python, Scapy, and Npcap.  
This tool captures live network traffic, prints packet details, and saves the captured packets into a 'capture.pcap' file.


## Features

- Fully compatible with Windows
- Uses Scapy + Npcap for packet capture
- Captures IP, TCP, and UDP packets
- Displays:
  - Timestamp  
  - Source IP  
  - Destination IP  
  - Protocol  
  - Hex payload  
- Automatically saves packets to 'capture.pcap'


## Requirements
### 1. Python 3.8 or higher  
Download from: https://www.python.org/downloads/  
Make sure to check "Add Python to PATH".

### 2. Npcap (required for Windows)  
Download: https://npcap.com/dist/npcap-1.80.exe  
During installation, enable:
- WinPcap API-compatible Mode

### 3. Install Scapy  
Open CMD:

- pip install scapy
## How to run
1 . Open Command Prompt

2 . Navigate to the folder containing sniffer.py:

 - cd path\to\your\project

3 . Run the script:

 - python sniffer.py

The script will capture 25 packets and then save them to capture.pcap.
## Output image

![Screenshot 2025-12-11 204011](https://github.com/user-attachments/assets/7c841600-4cab-4a74-b1f9-4f0ad35ef320)

## Saved File

 - capture.pcap

Open it using Wireshark.
