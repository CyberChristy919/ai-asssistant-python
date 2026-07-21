import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext


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
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.stdout if result.stdout else f"{package_name} installed successfully.\n")
        status_label.config(text=f"Success! Installed {package_name}.", fg="green")
        show_installed_packages()
    except subprocess.CalledProcessError as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, e.stderr if e.stderr else str(e))
        status_label.config(text=f"Failed to install {package_name}.", fg="red")
        messagebox.showerror("Installation Error", f"Could not install {package_name}.")


def show_installed_packages():
    try:
        result = run_pip_command(["list", "--format=columns"])
        packages_text.delete("1.0", tk.END)
        packages_text.insert(tk.END, result.stdout)
        package_count = max(len(result.stdout.strip().splitlines()) - 2, 0)
        packages_label.config(text=f"Installed packages ({package_count})")
    except subprocess.CalledProcessError as e:
        packages_text.delete("1.0", tk.END)
        packages_text.insert(tk.END, e.stderr if e.stderr else str(e))
        packages_label.config(text="Installed packages (unavailable)")


root = tk.Tk()
root.title("Pip Package Installer")
root.geometry("820x720")
root.minsize(700, 560)

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

output_text = scrolledtext.ScrolledText(root, height=10, width=95, wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=False, padx=12, pady=8)

packages_label = tk.Label(root, text="Installed packages")
packages_label.pack()

packages_text = scrolledtext.ScrolledText(
    root,
    height=18,
    width=95,
    wrap=tk.NONE,
    bg="white",
    fg="black",
    insertbackground="black",
    font=("Courier New", 10)
)
packages_text.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
packages_text.config(state=tk.DISABLED)

show_installed_packages()

root.mainloop()
