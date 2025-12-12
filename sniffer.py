"""
sniffer.py - Windows Compatible Network Sniffer
Uses Scapy + Npcap to capture packets.
"""

from scapy.all import sniff, IP, TCP, UDP, wrpcap
from datetime import datetime  # fixed import

packets = []

def show_packet(pkt):
    if IP in pkt:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src = pkt[IP].src
        dst = pkt[IP].dst

        if TCP in pkt:
            proto = "TCP"
        elif UDP in pkt:
            proto = "UDP"
        else:
            proto = "IP"

        payload = bytes(pkt.payload)[:40]
        payload = " ".join(f"{b:02X}" for b in payload)

        print(f"{ts} | {src} -> {dst} | {proto} | {payload}")

        packets.append(pkt)

if __name__ == "__main__":
    print("[+] Starting packet capture on Windows...")
    sniff(prn=show_packet, count=25)
    wrpcap("capture.pcap", packets)
    print("[+] Saved capture as capture.pcap")