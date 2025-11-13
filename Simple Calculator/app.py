import tkinter as tk

def add():
    result = float(entry1.get()) + float(entry2.get())
    label_result.config(text="Result: " + str(result))

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    label_result.config(text="Result: " + str(result))

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    label_result.config(text="Result: " + str(result))

def divide():
    try:
        result = float(entry1.get()) / float(entry2.get())
        label_result.config(text="Result: " + str(result))
    except ZeroDivisionError:
        label_result.config(text="Error: Division by zero")

# Create GUI
root = tk.Tk()
root.title("Calculator")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

button_add = tk.Button(root, text="Add", command=add)
button_sub = tk.Button(root, text="Subtract", command=subtract)
button_mul = tk.Button(root, text="Multiply", command=multiply)
button_div = tk.Button(root, text="Divide", command=divide)

label_result = tk.Label(root, text="Result: ")

entry1.pack()
entry2.pack()
button_add.pack()
button_sub.pack()
button_mul.pack()
button_div.pack()
label_result.pack()

root.mainloop()
