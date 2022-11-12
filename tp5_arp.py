import sys
from datetime import datetime
import scapy.all as scapy



print("[*] Scanning...") 
start_time = datetime.now()

scapy.conf.verb = 0 
ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = "10.4.1.0/24"), timeout = 2, iface = "enp0s8", inter = 0.1)


print ("\n[*] IP - MAC") 
for snd,rcv in ans: 
	print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))
stop_time = datetime.now()
total_time = stop_time - start_time 
print("\n[*] Scan Complete. Duration:", total_time)
