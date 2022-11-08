import scapy.all as scapy

ans=scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst="10.33.19.0/22"),timeout=2, iface="wlan0")




for element in ans:
        print("IP:{}".format(element[1].psrc))
        print("MAC address: {}\n".format(element[1].hwsrc))

