import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def browse_input():
    folder = filedialog.askdirectory(title="Select Input Directory")
    if folder:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, folder)

def browse_output():
    folder = filedialog.askdirectory(title="Select Output Directory")
    if folder:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder)

def create_thumbnails():
    input_directory = input_entry.get().strip()
    output_directory = output_entry.get().strip()

    if not input_directory or not output_directory:
        status_label.config(text="Please select both input and output directories.", fg="red")
        return

    if not os.path.isdir(input_directory):
        status_label.config(text="Input directory does not exist.", fg="red")
        return

    os.makedirs(output_directory, exist_ok=True)

    count = 0

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                with Image.open(os.path.join(input_directory, filename)) as img:
                    img.thumbnail((50, 50))
                    img.save(os.path.join(output_directory, filename))
                    count += 1
            except Exception as e:
                status_label.config(text=f"Error processing {filename}: {str(e)}", fg="red")
                return

    status_label.config(text=f"Success! Created {count} thumbnail(s).", fg="green")

root = tk.Tk()
root.title("Thumbnail Generator")
root.geometry("700x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Thumbnail Generator", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=15)

tk.Label(root, text="Input Directory:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
input_entry = tk.Entry(root, width=55)
input_entry.grid(row=1, column=1, padx=10, pady=10)
input_entry.insert(0, "input_images/")

tk.Button(root, text="Browse", width=12, command=browse_input).grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Output Directory:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
output_entry = tk.Entry(root, width=55)
output_entry.grid(row=2, column=1, padx=10, pady=10)
output_entry.insert(0, "output/thumbnails/")

tk.Button(root, text="Browse", width=12, command=browse_output).grid(row=2, column=2, padx=10, pady=10)

create_button = tk.Button(root, text="Create Thumbnails", width=20, command=create_thumbnails)
create_button.grid(row=3, column=1, pady=20)

status_label = tk.Label(root, text="Choose folders and click Create Thumbnails.", fg="blue")
status_label.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
