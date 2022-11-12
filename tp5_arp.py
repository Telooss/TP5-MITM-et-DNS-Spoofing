import scapy.all as scapy

result = scapy.srp((scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst="10.4.1.0/24")), timeout=3, verbose=0)[0]

print("Online IPs:")
ip=[]
mac=[]
for sent, received in result:
    ip.append(received.psrc)
    mac.append(received.hwsrc)
