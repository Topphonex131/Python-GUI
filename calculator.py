import tkinter as tk

# Custom evaluate function
def safe_evaluate(expression):
    try:
        # Tokenize and calculate safely
        tokens = []
        num = ""
        for char in expression:
            if char in "0123456789.":
                num += char
            elif char in "+-*/":
                if num:
                    tokens.append(float(num))
                    num = ""
                tokens.append(char)
        if num:
            tokens.append(float(num))

        # Simple two-pass evaluation (first *, / then +, -)
        i = 0
        while i < len(tokens):
            if tokens[i] == "*":
                tokens[i-1] *= tokens[i+1]
                del tokens[i:i+2]
                i -= 1
            elif tokens[i] == "/":
                tokens[i-1] /= tokens[i+1]
                del tokens[i:i+2]
                i -= 1
            else:
                i += 1

        result = tokens[0]
        i = 1
        while i < len(tokens):
            op = tokens[i]
            if op == "+":
                result += tokens[i+1]
            elif op == "-":
                result -= tokens[i+1]
            i += 2

        return str(result)

    except Exception:
        return "Error"

# UI setup
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        expression = entry.get()
        result = safe_evaluate(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Safe Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for button in buttons:
    b = tk.Button(root, text=button, font="Arial 18", width=4, height=2)
    b.grid(row=row, column=col)
    b.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
