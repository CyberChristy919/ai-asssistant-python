import json
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk


def run_pip_command(args):
    return subprocess.run(
        [sys.executable, "-m", "pip", *args],
        capture_output=True,
        text=True,
        check=True
    )


def install_package():
    package_name = package_entry.get().strip()
    if not package_name:
        status_label.config(text="Please enter a package name.", fg="red")
        return

    status_label.config(text=f"Installing {package_name}...", fg="blue")
    root.update_idletasks()

    try:
        result = run_pip_command(["install", package_name])
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.stdout if result.stdout else f"{package_name} installed successfully.\n")
        output_text.config(state=tk.DISABLED)
        status_label.config(text=f"Success! Installed {package_name}.", fg="green")
        show_installed_packages()
    except subprocess.CalledProcessError as e:
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, e.stderr if e.stderr else str(e))
        output_text.config(state=tk.DISABLED)
        status_label.config(text=f"Failed to install {package_name}.", fg="red")
        messagebox.showerror("Installation Error", f"Could not install {package_name}.")


def show_installed_packages():
    try:
        result = run_pip_command(["list", "--format=json"])
        packages = json.loads(result.stdout)

        for item in packages_tree.get_children():
            packages_tree.delete(item)

        for package in packages:
            packages_tree.insert("", tk.END, values=(package["name"], package["version"]))

        packages_label.config(text=f"Installed packages ({len(packages)})")
    except Exception as e:
        packages_label.config(text="Installed packages (unavailable)")
        messagebox.showerror("Package List Error", str(e))


root = tk.Tk()
root.title("Pip Package Installer")
root.geometry("900x720")
root.minsize(760, 560)

header = tk.Label(root, text="Pip Package Installer", font=("Arial", 16, "bold"))
header.pack(pady=12)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=8)

label = tk.Label(entry_frame, text="Package name:")
label.grid(row=0, column=0, padx=8, pady=8, sticky="w")

package_entry = tk.Entry(entry_frame, width=30)
package_entry.grid(row=0, column=1, padx=8, pady=8)
package_entry.insert(0, "folium")

button_frame = tk.Frame(root)
button_frame.pack(pady=6)

install_button = tk.Button(button_frame, text="Install Package", command=install_package, width=20)
install_button.grid(row=0, column=0, padx=6)

refresh_button = tk.Button(button_frame, text="Refresh Installed Packages", command=show_installed_packages, width=24)
refresh_button.grid(row=0, column=1, padx=6)

status_label = tk.Label(root, text="Enter a package name and click Install Package.", fg="blue")
status_label.pack(pady=8)

output_title = tk.Label(root, text="Installation output")
output_title.pack()

output_text = scrolledtext.ScrolledText(
    root,
    height=8,
    width=100,
    wrap=tk.WORD,
    bg="white",
    fg="black",
    insertbackground="black",
    font=("Courier New", 10)
)
output_text.pack(fill=tk.BOTH, expand=False, padx=12, pady=8)
output_text.config(state=tk.DISABLED)

packages_label = tk.Label(root, text="Installed packages")
packages_label.pack()

packages_frame = tk.Frame(root)
packages_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

columns = ("Package", "Version")
packages_tree = ttk.Treeview(packages_frame, columns=columns, show="headings", height=18)
packages_tree.heading("Package", text="Package")
packages_tree.heading("Version", text="Version")
packages_tree.column("Package", width=420, anchor="w")
packages_tree.column("Version", width=140, anchor="w")
packages_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(packages_frame, orient=tk.VERTICAL, command=packages_tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
packages_tree.configure(yscrollcommand=scrollbar.set)

show_installed_packages()

root.mainloop()
