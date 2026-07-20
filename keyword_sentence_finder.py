import tkinter as tk
from tkinter import filedialog, messagebox
import re

def browse_input_file():
    filename = filedialog.askopenfilename(
        title="Select Input File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filename:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, filename)

def browse_output_file():
    filename = filedialog.asksaveasfilename(
        title="Select Output File",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filename:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, filename)

def find_sentences():
    input_file = input_file_entry.get()
    keyword = keyword_entry.get().strip()
    output_file = output_file_entry.get()

    if not input_file or not keyword or not output_file:
        messagebox.showerror("Error", "Please select an input file, enter a keyword, and choose an output file.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        sentences = re.split(r'(?<=[.!?])\s+', text)
        matching_sentences = []

        for sentence in sentences:
            if keyword.lower() in sentence.lower():
                matching_sentences.append(sentence.strip())

        with open(output_file, "w", encoding="utf-8") as file:
            for sentence in matching_sentences:
                file.write(sentence + "\n")

        messagebox.showinfo("Success", f"Found {len(matching_sentences)} matching sentence(s) and saved them to the output file.")

    except FileNotFoundError:
        messagebox.showerror("Error", "The input file could not be found.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

root = tk.Tk()
root.title("Keyword Sentence Finder")
root.geometry("600x250")

tk.Label(root, text="Input File:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Keyword:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
keyword_entry = tk.Entry(root, width=50)
keyword_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Output File:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_output_file).grid(row=2, column=2, padx=10, pady=10)

tk.Button(root, text="Find Sentences", command=find_sentences).grid(row=3, column=1, pady=20)

root.mainloop()
