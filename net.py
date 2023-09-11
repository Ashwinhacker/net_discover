print("""
 ____    ____ _/  |_       __| _/|__|  ______  ____   ____ ___  __  ____ _______  
 /    \ _/ __ \\   __\     / __ | |  | /  ___/_/ ___\ /  _ \\  \/ /_/ __ \\_  __ \ 
|   |  \\  ___/ |  |      / /_/ | |  | \___ \ \  \___(  <_> )\   / \  ___/ |  | \/ 
|___|  / \___  >|__|      \____ | |__|/____  > \___  >\____/  \_/   \___  >|__|    
     \/      \/                \/          \/      \/                   \/         

""")
                                                                                   

from scapy.all import ARP, Ether, srp

def netdiscover(interface, network_range):
    # Create an ARP request packet
    arp = ARP(pdst=network_range)

    # Create an Ethernet frame
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')  # Broadcast MAC address

    packet = ether/arp

    # Send and receive packets
    result = srp(packet, timeout=3, iface=interface, verbose=0)[0]

    # Process the response
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    # Print the discovered hosts
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")

# Example usage
interface = 'eth0'  # Replace with your network interface
network_range = input("Enter the network range (e.g., 192.168.0.1/24): ")
netdiscover(interface, network_range)
