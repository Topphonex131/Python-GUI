import tkinter as tk
from datetime import datetime
datetime.now()

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x200")
        self.is_24_hour = True  # Track current format

        self.label = tk.Label(self, font=("Helvetica", 48), fg="black")
        self.label.pack(expand=True)

        self.toggle_button = tk.Button(self, text="Switch to 12-hour", command=self.toggle_format)
        self.toggle_button.pack(pady=10)

        self.update_clock()

    def toggle_format(self):
        self.is_24_hour = not self.is_24_hour
        if self.is_24_hour:
            self.toggle_button.config(text="Switch to 12-hour")
        else:
            self.toggle_button.config(text="Switch to 24-hour")

    def update_clock(self):
        now = datetime.now()
        if self.is_24_hour:
            current_time = now.strftime("%H:%M:%S")
        else:
            current_time = now.strftime("%I:%M:%S %p")
        self.label.config(text=current_time)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()
# This code creates a simple digital clock using Tkinter in Python.
# It updates the time every second and displays it in a large font.
# To run this code, ensure you have Python and Tkinter installed.
# Save the code in a file named digital_clock.py and run it using Python.
# You can customize the font and size by changing the parameters in the Label widget.
# The clock will display the current time in HH:MM:SS format.
# To stop the clock, simply close the window.
# This code is a basic example and can be extended with features like changing time zones or adding
# alarms.
# Make sure to run this code in an environment that supports Tkinter, such as a local Python installation.
# If you encounter any issues, check your Python installation and ensure Tkinter is available.  