import paramiko

# Define the connection details for the second VM
hostname = '34.125.37.209'
port = 22
username = 'iliastepanov'

# Define the command to execute on the second VM
command = 'python3 /home/iliastepanov/server.py'

# Create an SSH client
client = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure, see notes below)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the second VM
    client.connect(hostname, port, username, key_filename='/home/iliastepanov/.ssh/ssh_key')

    # Execute the command
    stdin, stdout, stderr = client.exec_command(command)

    # Print the output of the command
    print(stdout.read().decode('utf-8'))

finally:
    # Close the SSH connection
    client.close()