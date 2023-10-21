import socket
import json
import time
from datetime import datetime
import random

def start_server():
	host = '0.0.0.0'
	port = 12345

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((host, port))
	server_socket.listen(1)

	print(f"Server listening on {host}:{port}")
	while True:
		client_socket, addr = server_socket.accept()
		print(f"Connection from: {addr}")

		message = client_socket.recv(1024).decode()
		print(f"Received message: {message}")

		response= {
      "STATUS": {
            "STATUS": "S",
            "when": int(time.time()),
            "Msg": "stats",
            "api_version": "1.0.0"},
      "INFO": {"miner_version": "uart_trans.1.3",
               "CompileTime": f"{str(datetime.now().strftime('%A, %B %d, %Y at %I:%M:%S %p'))}",
               "type": f"Antminer S{random.randint(1, 1000)} XP"},
      "STATS": [{"elapsed": random.randint(1, 1000),
            "hashrate": float(random.randint(50000, 1000000)),
			"rate_30m": float(random.randint(100000, 500000)),
			"rate_avg": float(random.randint(100000, 500000)),
			"rate_ideal": 141000.0,
			"rate_unit": "GH/s",
            "chain_num": 3,
            "fan_num": 4,
            "fan": [6000, 6000, 6000, 6000],             
            "hwp_total": 0.0,
            "miner-mode": 0,
            "freq-level": 100}]}
		response = json.dumps(response)
		if message == 'stats':
			client_socket.sendall(response.encode())
		client_socket.close()

if __name__ == "__main__":
    start_server()