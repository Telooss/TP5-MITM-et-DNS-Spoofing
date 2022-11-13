import scapy.all as scapy



print("Scan en cours [...]") 

scapy.conf.verb = 0 
ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = "10.4.1.0/24"), timeout = 2, inter = 0.1)[0]


print ("\n[*] IP - MAC") 

for snd,rcv in ans: 
	print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))

print("\n[*] Scan fini")


