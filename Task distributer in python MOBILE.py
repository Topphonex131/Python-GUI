
# Task distributer in Python for mobile client
# This script allows a mobile client to send commands to a PC server and receive the output.
# The server must be running on the PC with the specified IP and port.
# Make sure to run the server script on the mobile or an other device with python,qpython,pydroid, etc.
# make sure to change the ip address to your PC's IP address
# this script is strictl;y for mobile devices to send commands to a PC server.



import socket

SERVER_IP = "192.168.X.X"  # ← Replace this with your PC's IP!
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

while True:
    cmd = input("Enter command to run on PC: ")
    if cmd.lower() in ['exit', 'quit']:
        break
    client.send(cmd.encode())
    result = client.recv(4096).decode()
    print("Output:\n", result)

client.close()
