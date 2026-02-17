import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import threading

# ---------------- CONFIGURACIÓN ----------------
HOST = "0.0.0.0"   # Accept connections from other machines
PORT = 5050
MAX_THREADS = 10
LOG_FILE = "server_log.txt"

# Lock to make file writing thread-safe
log_lock = threading.Lock()
# ------------------------------------------------


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def handle_client(client_socket, client_address):
    print("CLIENT CONNECTED:", client_address)  # 👈 FIRST print

    try:
        client_socket.settimeout(5)

        data = client_socket.recv(1024)
        if not data:
            print("NO DATA RECEIVED")  # 👈 optional
            return

        message = data.decode("utf-8").strip()
        print("RECEIVED:", message)  # 👈 SECOND print

        last_char = message[-1]
        count = message.count(last_char)
        prime_result = "sí" if is_prime(count) else "no"

        response = f"{count} {prime_result}\n"
        client_socket.sendall(response.encode("utf-8"))
        print("SENT RESPONSE:", response.strip())  # 👈 THIRD print

        client_socket.shutdown(socket.SHUT_WR)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} | {client_address[0]} | {message} | {count} | {prime_result}\n"

        with log_lock:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)

    except socket.timeout:
        print(f"TIMEOUT FROM {client_address}")

    finally:
        client_socket.close()
        print("CONNECTION CLOSED")  # 👈 FOURTH print




def start_server():
    print(f"Starting TCP server on port {PORT}...")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Server is running and waiting for connections...")

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        while True:
            client_socket, client_address = server_socket.accept()
            executor.submit(handle_client, client_socket, client_address)


if __name__ == "__main__":
    start_server()
