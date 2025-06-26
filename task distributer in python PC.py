
# Task Distributor in Python for PC
# This script allows a PC to act as a server that listens for commands from clients (like mobile devices).
# The server executes the commands and sends back the output.
# you can send commands like pip install, git clone, etc., and it will execute them on the PC.
# Make sure to run this script on the PC where you want to execute commands.



import socket
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess

HOST = socket.gethostbyname(socket.gethostname())
PORT = 2000

clients = []

class TaskDistributor:
    def __init__(self, master):
        self.master = master
        self.master.title("🧠 BRAINLINK Desktop Server")
        self.master.geometry("750x500")

        ttk.Label(master, text=f"PC IP: {HOST}  Port: {PORT}").pack(pady=5)

        self.output_box = scrolledtext.ScrolledText(master, height=25, width=90, state='disabled')
        self.output_box.pack(pady=5)

        server_thread = threading.Thread(target=self.start_server, daemon=True)
        server_thread.start()

    def log(self, message):
        self.output_box.config(state='normal')
        self.output_box.insert(tk.END, message + '\n')
        self.output_box.see(tk.END)
        self.output_box.config(state='disabled')

    def handle_client(self, client_socket, address):
        self.log(f"[CONNECTED] {address}")
        while True:
            try:
                command = client_socket.recv(1024).decode()
                if not command:
                    break
                self.log(f"[COMMAND from {address}] {command}")

                result = subprocess.getoutput(command)
                client_socket.send(result.encode())
                self.log(f"[RESULT SENT]")
            except:
                break
        self.log(f"[DISCONNECTED] {address}")
        client_socket.close()

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)
        self.log(f"[LISTENING] Server started on {HOST}:{PORT}")
        while True:
            client_socket, addr = server.accept()
            clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket, addr), daemon=True).start()

def main():
    root = tk.Tk()
    app = TaskDistributor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
