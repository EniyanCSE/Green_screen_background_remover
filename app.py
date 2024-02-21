import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk
import os

class ImageBackgroundRemovalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Background Removal")

        # This will maximize the window
        self.root.state('zoomed')
        
        self.file_path = None
        self.processed_image = None

        # Create widgets
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10, padx=10, anchor='center')

        self.process_button = tk.Button(root, text="Process Image", command=self.process_image, state=tk.DISABLED)
        self.process_button.pack(pady=10, padx=10, anchor='center')

        self.download_button = tk.Button(root, text="Download Processed Image", command=self.download_image, state=tk.DISABLED)
        self.download_button.pack(pady=10, padx=10, anchor='center')

        self.image_label = tk.Label(root)
        self.image_label.pack()
        
        # Center the buttons in the window
        root.update()  # Update the root layout to calculate sizes
        width = root.winfo_width()
        self.upload_button.pack_configure(padx=width//2 - self.upload_button.winfo_reqwidth()//2)
        self.process_button.pack_configure(padx=width//2 - self.process_button.winfo_reqwidth()//2)
        self.download_button.pack_configure(padx=width//2 - self.download_button.winfo_reqwidth()//2)

    def upload_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg;.jpeg;*.png")])
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
            # Resize for display
            max_size = (self.root.winfo_width(), self.root.winfo_height())
            image.thumbnail(max_size, Image.ANTIALIAS)
            
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)
        else:
            # If no image to display, clear the label
            self.image_label.config(image=None)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageBackgroundRemovalApp(root)
    root.mainloop()
