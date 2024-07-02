import socket
import threading

SERVER_IP = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 12345
BUFFER_SIZE = 1024

clients = []

def handle_client(sock):
    while True:
        try:
            message, client_address = sock.recvfrom(BUFFER_SIZE)
            print(f"Received message from {client_address}: {message.decode()}")
            if client_address not in clients:
                clients.append(client_address)
            broadcast_message(sock, message, client_address)
        except Exception as e:
            print(f"An error occurred: {e}")
            sock.close()
            break

def broadcast_message(sock, message, sender_address):
    for client in clients:
        if client != sender_address:
            sock.sendto(message, client)

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((SERVER_IP, SERVER_PORT))
    print(f"Server started on {SERVER_IP}:{SERVER_PORT}")

    while True:
        handle_client(server_sock)

    server_sock.close()

if __name__ == "__main__":
    main()
