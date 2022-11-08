from scapy.all import *


TIMEOUT = 1
conf.verb = 0
for ip in range(0, 256):
    packet = IP(dst="10.33.16." + str(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
         print (reply.dst, "Online")
    else:
         print("Offline %s" % packet[IP].dst)

