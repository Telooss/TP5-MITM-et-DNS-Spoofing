# TP5 - MITM et DNS Spoofing

## Installation nécessaire

````
git clone https://github.com/Telooss/TP5-MITM-et-DNS-Spoofing.git
````

Installation du langage python

````
sudo apt install python3 
````

Installation du package scapy

````
sudo apt install python3-scapy
````

## Utilisation

Accéder au répertoire ou se trouve les scripts

````
cd ~/TP5-MITM-et-DNS-Spoofing
````

Pour effectuer un scan du réseau 

````
sudo python3 scan_arp.py
````

Pour effectuer un ARP spoofing sur le réseau

````
sudo python3 ./spoof_arp.py ARP_Spoof "[MON_RESEAU]"
````

### A noté : 
si vous êtes sur windows, ouvrez votre terminal en tant qu'administrateur.