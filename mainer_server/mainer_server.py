import socket
import json
from create_response import create_response
	
def start_server():
	host = '0.0.0.0'
	port = 12345

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((host, port))
	server_socket.listen(1)

	print(f"Server listening on {host}:{port}")
	while True:
		client_socket = None
		try:
			client_socket, addr = server_socket.accept()
			print(f"Connection from: {addr}")

			message = client_socket.recv(1024).decode()
			print(f"Received message: {message}")

			response = create_response()
			response = json.dumps(response)
			if message == 'stats':
				client_socket.sendall(response.encode())
		except Exception as e:
			print(e)
			print(f"Received data: {client_socket.recv(1024)}")
		finally:
			if client_socket:
				client_socket.close()

if __name__ == "__main__":
    start_server()