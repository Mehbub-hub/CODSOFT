import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get values
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        op = var.get()
        
        # Calculate
        if op == 1:
            result = n1 + n2
        elif op == 2:
            result = n1 - n2
        elif op == 3:
            result = n1 * n2
        elif op == 4:
            if n2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = n1 / n2
        
        # Show result
        result_label.config(text=str(result))
        
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="0")
    var.set(1)

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="CALCULATOR", font=("Arial", 24, "bold"), 
         bg="#2d6a4f", fg="white", pady=20).pack(fill=tk.X)

# Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=30, padx=40)

# First number
tk.Label(frame, text="First Number:", font=("Arial", 12), 
         bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
entry1 = tk.Entry(frame, font=("Arial", 14), width=25)
entry1.grid(row=1, column=0, pady=10)

# Operations
tk.Label(frame, text="Operation:", font=("Arial", 12), 
         bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)

var = tk.IntVar(value=1)

tk.Radiobutton(frame, text="Addition (+)", variable=var, value=1, 
               font=("Arial", 11), bg="#f0f0f0").grid(row=3, column=0, sticky="w")
tk.Radiobutton(frame, text="Subtraction (-)", variable=var, value=2, 
               font=("Arial", 11), bg="#f0f0f0").grid(row=4, column=0, sticky="w")
tk.Radiobutton(frame, text="Multiplication (×)", variable=var, value=3, 
               font=("Arial", 11), bg="#f0f0f0").grid(row=5, column=0, sticky="w")
tk.Radiobutton(frame, text="Division (÷)", variable=var, value=4, 
               font=("Arial", 11), bg="#f0f0f0").grid(row=6, column=0, sticky="w")

# Second number
tk.Label(frame, text="Second Number:", font=("Arial", 12), 
         bg="#f0f0f0").grid(row=7, column=0, sticky="w", pady=(15,5))
entry2 = tk.Entry(frame, font=("Arial", 14), width=25)
entry2.grid(row=8, column=0, pady=10)

# Buttons
btn_frame = tk.Frame(frame, bg="#f0f0f0")
btn_frame.grid(row=9, column=0, pady=20)

tk.Button(btn_frame, text="Calculate", font=("Arial", 12, "bold"), 
         bg="#2d6a4f", fg="white", width=12, command=calculate).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear", font=("Arial", 12, "bold"), 
         bg="#666", fg="white", width=12, command=clear).pack(side=tk.LEFT, padx=5)

# Result
result_frame = tk.Frame(frame, bg="#d8f3dc", bd=2, relief=tk.SOLID)
result_frame.grid(row=10, column=0, pady=20, sticky="ew")

tk.Label(result_frame, text="Result:", font=("Arial", 12), 
         bg="#d8f3dc").pack(pady=(10,5))
result_label = tk.Label(result_frame, text="0", font=("Arial", 20, "bold"), 
                        bg="#d8f3dc", fg="#2d6a4f")
result_label.pack(pady=(0,10))

root.mainloop()
