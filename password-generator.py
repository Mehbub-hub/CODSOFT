import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """Generate password based on user input"""
    try:
        # Get the length from user input
        length = int(entry_length.get())
        
        if length < 1:
            messagebox.showerror("Error", "Length must be at least 1!")
            return
        
        if length > 128:
            messagebox.showwarning("Warning", "Length too long! Maximum is 128.")
            return
        
        # Get selected complexity options
        include_upper = var_upper.get()
        include_lower = var_lower.get()
        include_digit = var_digit.get()
        include_special = var_special.get()
        
        # Build character pool based on selections
        chars = ""
        if include_upper:
            chars += string.ascii_uppercase
        if include_lower:
            chars += string.ascii_lowercase
        if include_digit:
            chars += string.digits
        if include_special:
            chars += string.punctuation
        
        # Validate at least one type is selected
        if not chars:
            messagebox.showwarning("Warning", "Select at least one character type!")
            return
        
        # Generate the password using random characters
        password = ""
        for i in range(length):
            password += random.choice(chars)
        
        # Display the generated password
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, password)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def copy_to_clipboard():
    """Copy password to clipboard"""
    password = text_result.get(1.0, tk.END).strip()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Success", "Password copied!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

def clear_fields():
    """Clear all fields"""
    entry_length.delete(0, tk.END)
    text_result.delete(1.0, tk.END)
    var_upper.set(1)
    var_lower.set(1)
    var_digit.set(1)
    var_special.set(1)

# Create main window
root = tk.Tk()
root.title("Password Generator - Task 3")
root.state('zoomed')  # Maximize window
root.configure(bg="#e8f5e9")

# Bind ESC to quit fullscreen
def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

# Title bar
title_bar = tk.Frame(root, bg="#1b5e20", height=100)
title_bar.pack(fill=tk.X, side=tk.TOP)

tk.Label(title_bar, text="PASSWORD GENERATOR", 
         font=("Arial", 32, "bold"), bg="#1b5e20", 
         fg="white").pack(pady=30)

# Main content frame (centered)
center_frame = tk.Frame(root, bg="#e8f5e9")
center_frame.pack(expand=True)

content = tk.Frame(center_frame, bg="white", relief=tk.RIDGE, bd=5)
content.pack(padx=50, pady=30)

# Inner padding frame
inner = tk.Frame(content, bg="white")
inner.pack(padx=50, pady=40)

# SECTION 1: Password Length
section1 = tk.Frame(inner, bg="white")
section1.pack(fill=tk.X, pady=(0, 30))

tk.Label(section1, text="Enter Password Length:", 
         font=("Arial", 20, "bold"), bg="white", 
         fg="#1b5e20").pack(anchor=tk.W, pady=(0, 10))

entry_length = tk.Entry(section1, font=("Arial", 18), 
                        width=40, bd=3, relief=tk.SOLID)
entry_length.pack(ipady=8)
entry_length.insert(0, "16")

# SECTION 2: Complexity Options
section2 = tk.Frame(inner, bg="white")
section2.pack(fill=tk.X, pady=(0, 30))

tk.Label(section2, text="Select Password Complexity:", 
         font=("Arial", 20, "bold"), bg="white", 
         fg="#1b5e20").pack(anchor=tk.W, pady=(0, 15))

# Checkboxes frame
checks = tk.Frame(section2, bg="white")
checks.pack(anchor=tk.W)

var_upper = tk.IntVar(value=1)
var_lower = tk.IntVar(value=1)
var_digit = tk.IntVar(value=1)
var_special = tk.IntVar(value=1)

cb1 = tk.Checkbutton(checks, text="Include Uppercase (A-Z)", 
                     variable=var_upper, font=("Arial", 16),
                     bg="white", fg="black", selectcolor="lightgreen",
                     activebackground="white", activeforeground="black")
cb1.pack(anchor=tk.W, pady=5)

cb2 = tk.Checkbutton(checks, text="Include Lowercase (a-z)", 
                     variable=var_lower, font=("Arial", 16),
                     bg="white", fg="black", selectcolor="lightgreen",
                     activebackground="white", activeforeground="black")
cb2.pack(anchor=tk.W, pady=5)

cb3 = tk.Checkbutton(checks, text="Include Numbers (0-9)", 
                     variable=var_digit, font=("Arial", 16),
                     bg="white", fg="black", selectcolor="lightgreen",
                     activebackground="white", activeforeground="black")
cb3.pack(anchor=tk.W, pady=5)

cb4 = tk.Checkbutton(checks, text="Include Special Characters (!@#$)", 
                     variable=var_special, font=("Arial", 16),
                     bg="white", fg="black", selectcolor="lightgreen",
                     activebackground="white", activeforeground="black")
cb4.pack(anchor=tk.W, pady=5)

# SECTION 3: Generate Button
section3 = tk.Frame(inner, bg="white")
section3.pack(fill=tk.X, pady=(20, 30))

btn_generate = tk.Button(section3, text="GENERATE PASSWORD", 
                        font=("Arial", 18, "bold"), bg="#2d6a4f", 
                        fg="white", command=generate_password,
                        width=30, height=2, cursor="hand2",
                        relief=tk.RAISED, bd=4)
btn_generate.pack()

# SECTION 4: Display Password
section4 = tk.Frame(inner, bg="white")
section4.pack(fill=tk.X, pady=(0, 20))

tk.Label(section4, text="Generated Password:", 
         font=("Arial", 20, "bold"), bg="white", 
         fg="#1b5e20").pack(anchor=tk.W, pady=(0, 10))

result_frame = tk.Frame(section4, bg="#d8f3dc", relief=tk.SOLID, bd=3)
result_frame.pack(fill=tk.X)

text_result = tk.Text(result_frame, font=("Courier", 16, "bold"), 
                     height=2, bg="#d8f3dc", fg="#1b5e20",
                     wrap=tk.WORD, relief=tk.FLAT, padx=10, pady=10)
text_result.pack(fill=tk.BOTH, expand=True)

# SECTION 5: Action Buttons
section5 = tk.Frame(inner, bg="white")
section5.pack(fill=tk.X, pady=(20, 0))

btn_copy = tk.Button(section5, text="Copy to Clipboard", 
                    font=("Arial", 14, "bold"), bg="#40916c", 
                    fg="white", command=copy_to_clipboard,
                    width=18, height=2, cursor="hand2",
                    relief=tk.RAISED, bd=3)
btn_copy.pack(side=tk.LEFT, padx=10)

btn_clear = tk.Button(section5, text="Clear", 
                     font=("Arial", 14, "bold"), bg="#6c757d", 
                     fg="white", command=clear_fields,
                     width=18, height=2, cursor="hand2",
                     relief=tk.RAISED, bd=3)
btn_clear.pack(side=tk.LEFT, padx=10)

# Footer
footer = tk.Frame(root, bg="#1b5e20", height=50)
footer.pack(fill=tk.X, side=tk.BOTTOM)

tk.Label(footer, text="Press F11 for fullscreen | Press ESC to exit fullscreen", 
         font=("Arial", 11), bg="#1b5e20", fg="white").pack(pady=12)

# Start the application
root.mainloop()
