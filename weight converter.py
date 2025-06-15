import tkinter as tk
from tkinter import ttk
import time

# Conversion dictionaries
to_kg = {
    "pg": 1e-12, "ng": 1e-9, "ug": 1e-6,
    "mg": 1e-3, "g": 1e-3, "kg": 1, "t": 1e3
}
from_kg = {
    "pg": 1e12, "ng": 1e9, "ug": 1e6,
    "mg": 1e3, "g": 1e3, "kg": 1, "t": 1e-3
}
units = list(to_kg.keys())

# Main window
root = tk.Tk()
root.title("⚖️ Ultra Weight Converter")
root.geometry("500x400")
root.configure(bg="#0f0f0f")
root.resizable(False, False)

# Animate title glow
def glow():
    colors = ["#39FF14", "#00FFFF", "#FF00FF", "#FF4500"]
    i = 0
    def change():
        nonlocal i
        title_label.config(fg=colors[i])
        i = (i + 1) % len(colors)
        root.after(500, change)
    change()

# Convert function
def convert():
    try:
        weight = float(weight_entry.get())
        if weight <= 0:
            result_label.config(text="Weight must be > 0", fg="red")
            return
        from_unit = from_unit_combo.get()
        to_unit = to_unit_combo.get()
        weight_in_kg = weight * to_kg[from_unit]
        converted = weight_in_kg * from_kg[to_unit]
        result_label.config(text=f"{weight} {from_unit} = {converted:.8f} {to_unit}", fg="#39FF14")
    except ValueError:
        result_label.config(text="Invalid input", fg="red")

# Clear fields
def clear():
    weight_entry.delete(0, tk.END)
    result_label.config(text="")
    from_unit_combo.set(units[0])
    to_unit_combo.set(units[1])

# Live preview
def live_preview(*args):
    try:
        weight = float(weight_entry.get())
        if weight <= 0:
            result_label.config(text="")
            return
        from_unit = from_unit_combo.get()
        to_unit = to_unit_combo.get()
        kg = weight * to_kg[from_unit]
        converted = kg * from_kg[to_unit]
        result_label.config(text=f"{weight} {from_unit} = {converted:.8f} {to_unit}", fg="gray")
    except:
        result_label.config(text="")

# Fonts
title_font = ("Consolas", 20, "bold")
text_font = ("Segoe UI", 12)
button_font = ("Segoe UI", 10, "bold")

# Title
title_label = tk.Label(root, text="⚖️ Ultra Weight Converter", font=title_font, bg="#0f0f0f")
title_label.pack(pady=15)
glow()

# Weight input
tk.Label(root, text="Enter weight:", font=text_font, fg="white", bg="#0f0f0f").pack()
weight_entry = tk.Entry(root, font=("Consolas", 14), justify="center")
weight_entry.pack(pady=8)
weight_entry.bind("<KeyRelease>", live_preview)

# Unit selection
unit_frame = tk.Frame(root, bg="#0f0f0f")
unit_frame.pack(pady=5)

from_unit_combo = ttk.Combobox(unit_frame, values=units, state="readonly", width=5)
from_unit_combo.set(units[0])
from_unit_combo.pack(side=tk.LEFT, padx=20)
from_unit_combo.bind("<<ComboboxSelected>>", live_preview)

to_unit_combo = ttk.Combobox(unit_frame, values=units, state="readonly", width=5)
to_unit_combo.set(units[1])
to_unit_combo.pack(side=tk.RIGHT, padx=20)
to_unit_combo.bind("<<ComboboxSelected>>", live_preview)

# Buttons
button_frame = tk.Frame(root, bg="#0f0f0f")
button_frame.pack(pady=15)

convert_btn = tk.Button(button_frame, text="🔁 Convert", font=button_font, bg="#222", fg="white", padx=15, pady=5, command=convert)
convert_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(button_frame, text="🧹 Clear", font=button_font, bg="#444", fg="white", padx=15, pady=5, command=clear)
clear_btn.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Courier", 14), bg="#0f0f0f", fg="white")
result_label.pack(pady=15)

# Run app
root.mainloop()
