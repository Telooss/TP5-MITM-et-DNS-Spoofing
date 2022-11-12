from scapy.all import *

TIMEOUT = 2
conf.verb = 0
for ip in range(0, 256):
    packet = IP(dst="10.4.1." + str(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=0.5)
    if not (reply is None):
         print(reply.dst, "is online")
    else:
         print("Timeout waiting for %s" % packet[IP].dst)

         
