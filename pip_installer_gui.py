import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

def install_package():
    package_name = package_entry.get().strip()
    if not package_name:
        status_label.config(text="Please enter a package name.", fg="red")
        return

    status_label.config(text=f"Installing {package_name}...", fg="blue")
    root.update_idletasks()

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name],
            capture_output=True,
            text=True,
            check=True
        )
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.stdout if result.stdout else f"{package_name} installed successfully.")
        status_label.config(text=f"Success! Installed {package_name}.", fg="green")
    except subprocess.CalledProcessError as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, e.stderr if e.stderr else str(e))
        status_label.config(text=f"Failed to install {package_name}.", fg="red")
        messagebox.showerror("Installation Error", f"Could not install {package_name}.")

root = tk.Tk()
root.title("Pip Package Installer")
root.geometry("520x420")

header = tk.Label(root, text="Pip Package Installer", font=("Arial", 16, "bold"))
header.pack(pady=12)

frame = tk.Frame(root)
frame.pack(pady=8)

label = tk.Label(frame, text="Package name:")
label.grid(row=0, column=0, padx=8, pady=8, sticky="w")

package_entry = tk.Entry(frame, width=30)
package_entry.grid(row=0, column=1, padx=8, pady=8)
package_entry.insert(0, "folium")

install_button = tk.Button(root, text="Install Package", command=install_package, width=20)
install_button.pack(pady=6)

status_label = tk.Label(root, text="Enter a package name and click Install Package.", fg="blue")
status_label.pack(pady=8)

output_text = tk.Text(root, height=16, width=60)
output_text.pack(padx=12, pady=10)

root.mainloop()
