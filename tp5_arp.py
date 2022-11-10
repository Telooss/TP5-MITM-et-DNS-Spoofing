import scapy.all as scapy

ans=scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst="10.1.4.0/24"),timeout=2, iface="enp0s8")

if ans:
    for element in ans:
        print("IP:{}".format(element))
        print("MAC address: {}\n".format(element))