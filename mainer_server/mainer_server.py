import socket
import json

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
            "when": 1689666370,
            "Msg": "stats",
            "api_version": "1.0.0"},
      "INFO": {"miner_version": "uart_trans.1.3",
               "CompileTime": "Mon Oct 17 13:13:09 CST 2022",
               "type": "Antminer S19 XP"},
      "STATS": [{"elapsed": 928,
            "hashrate": 142408.75,
			"rate_30m": 141365.18,
			"rate_avg": 141399.98,
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