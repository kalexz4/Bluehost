import tkinter as tk
from tkinter import filedialog, colorchooser
from cryptography.fernet import Fernet
import os

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

def open_color_picker(attribute):
    color = colorchooser.askcolor()[1]
    if color:
        if attribute == 'background':
            root.configure(bg=color)
            custom_button.configure(bg=color)  # Change Customize button background color
        elif attribute == 'foreground':
            root.configure(fg=color)
            custom_button.configure(fg=color)
        elif attribute == 'button':
            encrypt_button.configure(bg=color)
            decrypt_button.configure(bg=color)

            # Update Customize button background color
            custom_button.configure(bg=color)

# Create GUI window
root = tk.Tk()
root.title("File Encryption Tool")
root.geometry("600x400")  # Set window size

# Set default colors
root.configure(bg="black")

# Create frame for buttons
button_frame = tk.Frame(root, bg="black")

# Create Encrypt button
encrypt_button = tk.Button(button_frame, text="Encrypt Files (Ctrl+E)", command=encrypt_selected_files, bg="green", fg="white")
encrypt_button.pack(side=tk.LEFT, padx=10)

# Create Decrypt button
decrypt_button = tk.Button(button_frame, text="Decrypt Files (Ctrl+D)", command=decrypt_selected_files, bg="green", fg="white")
decrypt_button.pack(side=tk.LEFT, padx=10)

# Pack the buttons frame at the center, slightly higher
button_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create Customization button
custom_button = tk.Button(root, text="Customize", command=lambda: open_color_picker('button'), width=25, bg="green", fg="white")
custom_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Function to bind tooltip to button
def bind_tooltip(widget, text):
    widget.bind("<Enter>", lambda event: status_label.config(text=text))
    widget.bind("<Leave>", lambda event: status_label.config(text=""))

# Status label
status_label = tk.Label(root, text="", width=50)
status_label.pack()

root.mainloop()
