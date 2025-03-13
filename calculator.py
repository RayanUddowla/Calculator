import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen_var.get()))
            screen_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=8, relief=tk.SUNKEN)
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["(", ")", "%", "#"],
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="lucida 15 bold", height=2, width=5)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()



