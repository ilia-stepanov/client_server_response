import socket
import threading
import requests
import json


def send_json_to_cloud(json_data):
	url = 'http://34.125.211.72:5000/api/receive'
	headers = {'Content-Type': 'application/json'}
	response = requests.post(url, json=json_data, headers=headers)
	if response.status_code == 200:
		print("Data sent successfully!")
		print(response.json())
	else:
		print(f"Failed to send data. Status code: {response.status_code}")


def poll_miner(miner_ip):
    try:
        message = 'stats'
        port = 12345
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((miner_ip, port))
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        response = json.loads(response)
        response['ip'] = miner_ip
        print(f"Received response: {response}")
        send_json_to_cloud(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

        
def run_script(miner_ips):
    max_threads = 350
    threads = []
    semaphore = threading.BoundedSemaphore(value=max_threads)

    for miner_ip in miner_ips:
        thread = threading.Thread(target=poll_miner, args=(miner_ip,))
        threads.append(thread)
        thread.start()
        semaphore.acquire()

    for thread in threads:
        thread.join()
        semaphore.release()
        
if __name__ == "__main__":
     miner_ips = ['34.125.131.135', '34.125.144.20']
     run_script(miner_ips)
