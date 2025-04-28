
import secrets
import string
import sys
import tkinter as tk
from tkinter import messagebox

UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation
ALL = UPPER + LOWER + DIGITS + SYMBOLS

def generate_password(length: int) -> str:
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    
    password_chars = [
        secrets.choice(UPPER),
        secrets.choice(LOWER),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]
    
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(ALL) for _ in range(remaining)]
    
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

def main():
    root = tk.Tk()
    root.title("Strong Password Generator")
    root.geometry("500x180")
    root.resizable(False, False)

    tk.Label(root, text="Enter password length (>=8):", font=("Arial", 14)).pack(pady=10)
    length_var = tk.StringVar(value="12")
    length_entry = tk.Entry(root, textvariable=length_var, font=("Consolas", 14), width=10, justify="center")
    length_entry.pack()

    pwd_var = tk.StringVar()
    pwd_entry = tk.Entry(root, textvariable=pwd_var, font=("Consolas", 14), width=32, justify="center")
    pwd_entry.pack(pady=10)

    def on_generate():
        try:
            length = int(length_var.get())
            pwd = generate_password(length)
            pwd_var.set(pwd)
        except ValueError as e:
            messagebox.showerror("Invalid length", str(e))

    def on_copy():
        pwd = pwd_var.get()
        if not pwd:
            messagebox.showwarning("Nothing to copy", "Generate a password first.")
            return
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard. It will clear in 30 seconds.")
        # Clear clipboard after 30 s
        root.after(30_000, root.clipboard_clear)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="Generate", font=("Arial", 12), command=on_generate).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Copy", font=("Arial", 12), command=on_copy).grid(row=0, column=1, padx=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        try:
            length = int(sys.argv[2]) if len(sys.argv) > 2 else 12
            print(generate_password(length))
        except Exception as exc:
            print(f"Error: {exc}")
            sys.exit(1)
    else:
        main()
