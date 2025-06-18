#clicker game with tkinter gui
import tkinter as tk

#initial value 
score = 0
click_value = 1
upgrade_cost = 10

#define click function
def click():
    global score
    score += click_value
    score_label.config(text=f"Score: {score}")

#define upgrade function before you use it
def upgrade():
    global score, click_value, upgrade_cost
    if score >= upgrade_cost:
        score -= click_value
        click_value += 1
        upgrade_cost *= 2 #double the cost for next upgrade
        score_label.config(text=f"Score: {score}")
        upgrade_cost.config(text=f"upgrade click (+1) - cost: {upgrade_cost}")

# GUI setup
root = tk.Tk()
root.title("Python Clicker Game")
root.geometry("300x300")

# Score Label
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 18))
score_label.pack(pady=20)

# Click Button
click_button = tk.Button(root, text="Click Me!", command=click, font=("Arial", 16), bg="lightgreen")
click_button.pack(pady=10)

# Upgrade Button
upgrade_button = tk.Button(root, text=f"Upgrade Click (+1) - Cost: {upgrade_cost}", command=upgrade, font=("Arial", 12), bg="lightblue")
upgrade_button.pack(pady=10)

# Run the app
root.mainloop()