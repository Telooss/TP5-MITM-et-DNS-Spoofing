import scapy.all as scapy

result = scapy.srp((scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst="193.250.129.0/24")), timeout=3, verbose=0)[0]

if ans:
    for element in ans:
        print("IP: {}".format(element))
        print("MAC address: {}\n".format(element))
