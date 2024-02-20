import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk
import os

class ImageBackgroundRemovalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Background Removal")

        self.file_path = None
        self.processed_image = None

        # Create widgets
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.process_button = tk.Button(root, text="Process Image", command=self.process_image, state=tk.DISABLED)
        self.process_button.pack()

        self.download_button = tk.Button(root, text="Download Processed Image", command=self.download_image, state=tk.DISABLED)
        self.download_button.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

    def upload_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            self.display_image()
            self.process_button.config(state=tk.NORMAL)

    def process_image(self):
        if self.file_path:
            img = Image.open(self.file_path)
            self.processed_image = remove(img)
            self.display_image(self.processed_image)
            self.download_button.config(state=tk.NORMAL)

    def download_image(self):
        if self.processed_image:
            output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if output_path:
                self.processed_image.save(output_path)

    def display_image(self, image=None):
        if image:
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)
        else:
            self.image_label.config(image=None)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageBackgroundRemovalApp(root)
    root.mainloop()
