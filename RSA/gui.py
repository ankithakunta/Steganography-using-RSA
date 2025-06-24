import tkinter as tk
from tkinter import filedialog, messagebox
from steg_utils import encode_message, decode_message
from rsa_utils import generate_keys, encrypt_message, decrypt_message
import os

class StegGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 RSA Image Steganography")
        self.root.geometry("500x350")

        self.message_label = tk.Label(root, text="Enter Secret Message:")
        self.message_label.pack()
        self.message_entry = tk.Text(root, height=4, width=50)
        self.message_entry.pack()

        self.select_image_btn = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_image_btn.pack(pady=5)

        self.hide_btn = tk.Button(root, text="🔐 Hide Message", command=self.hide_message)
        self.hide_btn.pack(pady=5)

        self.extract_btn = tk.Button(root, text="🔓 Extract Message", command=self.extract_message)
        self.extract_btn.pack(pady=5)

        self.status = tk.Label(root, text="", fg="blue")
        self.status.pack(pady=10)

        self.image_path = ""

    def select_image(self):
        path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        if path:
            self.image_path = path
            self.status.config(text=f"Selected: {os.path.basename(path)}")

    def hide_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image.")
            return

        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showerror("Error", "Please enter a message.")
            return

        public_key, private_key = generate_keys()
        encrypted = encrypt_message(message, public_key)
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Images", "*.png")])

        if not output_path:
            return

        encode_message(self.image_path, encrypted, output_path)

        with open("private.pem", "wb") as f:
            f.write(private_key)

        messagebox.showinfo("Success", f"Message hidden in:\n{output_path}\n\nPrivate key saved as 'private.pem'.")

    def extract_message(self):
        image_path = filedialog.askopenfilename(title="Select Stego Image", filetypes=[("PNG Images", "*.png")])
        if not image_path:
            return

        key_path = filedialog.askopenfilename(title="Select Private Key", filetypes=[("PEM Files", "*.pem")])
        if not key_path:
            return

        with open(key_path, "rb") as f:
            private_key = f.read()

        try:
            encrypted = decode_message(image_path)
            decrypted = decrypt_message(encrypted, private_key)
            messagebox.showinfo("Hidden Message", decrypted)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract or decrypt:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StegGUI(root)
    root.mainloop()
