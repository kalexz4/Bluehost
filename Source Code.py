from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path + '.encrypted', 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = file_path.rsplit('.encrypted', 1)[0]
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

def encrypt_selected_files():
    key = generate_key()
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)
            status_label.config(text=f"{file_path} encrypted successfully!")
        else:
            status_label.config(text=f"File '{file_path}' not found.")

def decrypt_selected_files():
    key = generate_key()
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        if os.path.isfile(file_path):
            decrypt_file(file_path, key)
            status_label.config(text=f"{file_path} decrypted successfully!")
        else:
            status_label.config(text=f"File '{file_path}' not found.")

# Create GUI window
root = tk.Tk()
root.title("File Encryption Tool")
root.geometry("600x400")  # Set window size
root.configure(bg="black")  # Set background color

# Create frame for buttons
button_frame = tk.Frame(root, bg="black")
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create Encrypt button
encrypt_button = tk.Button(button_frame, text="Encrypt Files", command=encrypt_selected_files, bg="green", fg="white", width=20)
encrypt_button.grid(row=0, column=0, padx=10, pady=10)

# Create Decrypt button
decrypt_button = tk.Button(button_frame, text="Decrypt Files", command=decrypt_selected_files, bg="green", fg="white", width=20)
decrypt_button.grid(row=0, column=1, padx=10, pady=10)

# Status label
status_label = tk.Label(root, text="", width=50, bg="black", fg="white")
status_label.pack()

root.mainloop()
