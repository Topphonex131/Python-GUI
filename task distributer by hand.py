import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import threading

class TaskDistributor:
    def __init__(self, master):
        self.master = master
        self.master.title("🧠 BRAINLINK Desktop Command Center")
        self.master.geometry("700x500")

        # Input Label
        self.command_label = ttk.Label(master, text="Enter Command:")
        self.command_label.pack(pady=5)

        # Command Entry
        self.command_entry = ttk.Entry(master, width=80)
        self.command_entry.pack(pady=5)

        # Send Button
        self.send_button = ttk.Button(master, text="Run", command=self.run_command_thread)
        self.send_button.pack(pady=5)

        # Output Label
        self.output_label = ttk.Label(master, text="Command Output:")
        self.output_label.pack(pady=5)

        # Output Box (with scroll)
        self.output_box = scrolledtext.ScrolledText(master, height=20, width=85, state='disabled', wrap='word')
        self.output_box.pack(pady=5)

    def run_command_thread(self):
        thread = threading.Thread(target=self.run_command)
        thread.start()

    def run_command(self):
        command = self.command_entry.get().strip()
        if not command:
            messagebox.showwarning("Warning", "Command cannot be empty!")
            return

        self.output_box.config(state='normal')
        self.output_box.insert(tk.END, f"\n>>> {command}\n")
        self.output_box.see(tk.END)
        self.output_box.config(state='disabled')

        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                self.output_box.config(state='normal')
                self.output_box.insert(tk.END, line)
                self.output_box.see(tk.END)
                self.output_box.config(state='disabled')
            process.wait()
        except Exception as e:
            self.output_box.config(state='normal')
            self.output_box.insert(tk.END, f"\n[ERROR] {str(e)}\n")
            self.output_box.config(state='disabled')

        self.command_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TaskDistributor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
