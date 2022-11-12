## 1. Scan réseau

Programme du scan ARP
```py
import sys
import scapy.all as scapy



print("Scan en cours [...]") 

scapy.conf.verb = 0 
ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = "10.4.1.0/24"), timeout = 2, iface = "enp0s8", inter = 0.1)


print ("\n[*] IP - MAC") 
for snd,rcv in ans: 
	print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))

print("\n[*] Scan fini")
```

Scan effectué sur le réseau 10.4.1.0/24
```
balan@victime:~/Desktop/TP5-MITM-et-DNS-Spoofing$ sudo python3 tp5_arp.py
[sudo] password for balan: 
Scan en cours [...]

[*] IP - MAC
10.4.1.10 - 0a:00:27:00:00:13
10.4.1.11 - 08:00:27:e5:71:04
10.4.1.254 - 08:00:27:f1:6b:c5

[*] Scan fini
```