# ids.py
from scapy.all import IP
from collections import Counter

THRESHOLD = 20  # Flag any source IP that sends more than this many packets


def generate_simulated_packets():
    """Builds a simulated list of network packets for demonstration purposes."""
    packets = []
    packets += [IP(src='192.168.1.10') for _ in range(9)]
    packets += [IP(src='192.168.1.20') for _ in range(3)]
    packets += [IP(src='192.168.1.150') for _ in range(25)]
    return packets


def main():
    print("Analyzing simulated network packets...")
    packets = generate_simulated_packets()

    # Count how many packets came from each source IP
    ip_counts = Counter(pkt[IP].src for pkt in packets)

    print("Packet counts per source IP:")
    for ip, count in ip_counts.items():
        print(f" - {ip}: {count} packets")

    print("\nChecking for suspicious activity...")
    suspicious_found = False
    for ip, count in ip_counts.items():
        if count > THRESHOLD:
            print(f"!!! ALERT: Suspicious activity detected from {ip}. Packets sent: {count}")
            suspicious_found = True

    if not suspicious_found:
        print("No suspicious activity detected.")


if __name__ == '__main__':
    main()