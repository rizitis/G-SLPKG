# MIT License
# Copyright (c) [25/08/2023] [Anagnostakis Ioannis] [rizitis@gmail.com]
# G-SLPKG is a gui interface for slpkg [slackware package manager]

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import subprocess
import sys 
import webbrowser

def run_command(command):
    if command == "Search":
        package_name = package_entry.get()
        repo_name = repo_entry.get()
        full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -s {package_name} -o {repo_name}\"'"
        subprocess.run(full_command, shell=True)
    elif command == "Reinstall":
        package_name = package_entry.get()
        repo_name = repo_entry.get()
        full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -ir {package_name} -o {repo_name}\"'"
        subprocess.run(full_command, shell=True)
    elif command == "Install":
        package_name = package_entry.get()
        repo_name = repo_entry.get()
        full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -i {package_name} -o {repo_name}\"'"
        subprocess.run(full_command, shell=True)
    elif command == "Requires":
        package_name = package_entry.get()
        full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -t {package_name}\"'"
        subprocess.run(full_command, shell=True)
    elif command == "Depends On":
        package_name = package_entry.get()
        full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -e {package_name}\"'"
        subprocess.run(full_command, shell=True)
    elif command == "UPDATE REPOS":
        full_command = "xfce4-terminal --hold -e 'su -c \"slpkg -u\"'"
        subprocess.run(full_command, shell=True)
    elif command == "UPGRADE PACKAGES":
        full_command = "xfce4-terminal --hold -e 'su -c \"slpkg -U\"'"
        subprocess.run(full_command, shell=True)
    else:
        command_function = command_functions.get(command)
        if command_function:
            command_function()

def run_install_command(command):
    if command == "Check Installed":
        check_installed()  # Call the check_installed function directly
    else:
        run_command(command)

def install():
    package_name = package_entry.get()
    messagebox.showinfo("Install Package", f"Installing package: {package_name}")

def search():
    package_name = package_entry.get()
    messagebox.showinfo("Package Search", f"Searching for package: {package_name}")

def reinstall():
    package_name = package_entry.get()
    messagebox.showinfo("Reinstall Package", f"Reinstalling package: {package_name}")

def requires():
    package_name = package_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -t {package_name}\"'"
    subprocess.run(full_command, shell=True)

def depends_on():
    package_name = package_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -e {package_name}\"'"
    subprocess.run(full_command, shell=True)

def check_installed():
    package_name = package_entry.get()  
    full_command = f"ls /var/log/packages | grep {package_name}"
    try:
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
        output = result.stdout.strip()
        if output:
            messagebox.showinfo("Package Check", f"Package {package_name} is installed.")
        else:
            messagebox.showinfo("Package Check", f"Package {package_name} is not installed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def open_repositories():
    full_command = f"xfce4-terminal  -e 'su -c \"nano /etc/slpkg/repositories.toml\"'"
    subprocess.run(full_command, shell=True)

def open_slpkg_toml():
    full_command = f"xfce4-terminal  -e 'su -c \"nano /etc/slpkg/slpkg.toml\"'"
    subprocess.run(full_command, shell=True)

def open_blacklist_toml():
    full_command = f"xfce4-terminal  -e 'su -c \"nano /etc/slpkg/blacklist.toml\"'"
    subprocess.run(full_command, shell=True)

def check_updates():
    repo_name = repo_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -c -o {repo_name}\"'"
    subprocess.run(full_command, shell=True)

def repo_info():
    repo_name = repo_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -I -o {repo_name}\"'"
    subprocess.run(full_command, shell=True)

def clean_logs():
    full_command = "xfce4-terminal --hold -e 'su -c \"slpkg -L\"'"
    subprocess.run(full_command, shell=True)

def clean_data():
    full_command = "xfce4-terminal --hold -e 'su -c \"slpkg -T\"'"
    subprocess.run(full_command, shell=True)

def clean_tmp():
    full_command = "xfce4-terminal --hold -e 'su -c \"slpkg -D\"'"
    subprocess.run(full_command, shell=True)

def edit_configs():
    full_command = "xfce4-terminal --hold -e 'su -c \"slpkg -g\"'"
    subprocess.run(full_command, shell=True)

def build_packages():
    repo_name = repo_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -b -o {repo_name}\"'"
    subprocess.run(full_command, shell=True)

def download_packages():
    package_name = package_entry.get()
    repo_name = repo_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -d {package_name} -o {repo_name}\"'"
    subprocess.run(full_command, shell=True)

def find_packages():
    package_name = package_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -f {package_name}\"'"
    subprocess.run(full_command, shell=True)

def view_packages():
    package_name = package_entry.get()
    repo_name = repo_entry.get()
    full_command = f"xfce4-terminal --hold -e 'su -c \"slpkg -w {package_name} -o {repo_name}\"'"
    subprocess.run(full_command, shell=True)

def open_github():
    webbrowser.open("https://github.com/rizitis/G-SLPKG")


command_functions = {
    "Search": search,
    "Install": install,
    "Reinstall": reinstall,
    "Requires": requires,
    "Depends On": depends_on,
    "Check Installed": check_installed,
    "Check Updates": check_updates,
    "Repository Info": repo_info,
    "Clean Logs": clean_logs,
    "Clean Data": clean_data,
    "Clean TMP": clean_tmp,
    "Edit Configs": edit_configs,
    "Build Packages": build_packages,
    "Download Packages": download_packages,
    "Find Packages": find_packages,
    "View Packages": view_packages
}



# Create the main window
root = tk.Tk()
root.title("G-SLPKG")
root.configure(bg="#333333")  

# Set up icons
update_manager_icon = PhotoImage(file="/usr/share/g-slpkg/updated.png")
upgrade_icon = PhotoImage(file="/usr/share/g-slpkg/upgrade.png")
install_icon = PhotoImage(file="/usr/share/g-slpkg/install.png")
reinstall_pkg_icon = PhotoImage(file="/usr/share/g-slpkg/reinstall.png")
search_pkg_icon = PhotoImage(file="/usr/share/g-slpkg/search.png")

# Create a style for the menu
menu_style = ttk.Style()
menu_style.theme_use("clam")
menu_style.configure("Modern.TMenu", background="#333333", foreground="#f5f5f5")

# Customize the style for the menu
menu_style.configure("Modern.TMenu", background="#444444", foreground="white")  # Set menu background and text color

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Configure a dark theme for the menu (Linux-specific)
if sys.platform.startswith('linux'):
    menu_bar.configure(bg="#333333", fg="white", activebackground="#444444", activeforeground="white")

def create_menus(menu_bar):
    # Create menus and submenus
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open Repositories", command=open_repositories)
    file_menu.add_command(label="Open slpkg.toml", command=open_slpkg_toml)
    file_menu.add_command(label="Open blacklist.toml", command=open_blacklist_toml)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)


    menu_bar.add_separator()

    # Create the "Commands" menu and use the command_functions dictionary
    commands_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Commands", menu=commands_menu)

    # Use the command_functions dictionary to populate the "Commands" menu
    for label, cmd in command_functions.items():
        if label not in {"Search", "Reinstall", "Install", "UPDATE REPOS", "UPGRADE PACKAGES"}:
            commands_menu.add_command(label=label, command=cmd)

    menu_bar.add_separator()
    
    menu_bar.add_command(label="About", command=open_github)
# Apply modern styles to buttons
modern_button_style = ttk.Style()
modern_button_style.configure("Modern.TButton", background="#333333", foreground="#f5f5f5", font=("Roboto", 10))
modern_button_style.map("Modern.TButton", background=[("active", "#555555")])
  
  
# Create the main content area
content_frame = tk.Frame(root, bg="#333333")
content_frame.pack(padx=20, pady=20)

# Create a frame for the package and repository widgets
input_frame = tk.Frame(content_frame, bg="#333333")
input_frame.pack(fill=tk.X, padx=5, pady=5)

# Entry widget for package name
package_label = tk.Label(input_frame, text="Enter Package Name:", foreground="white", background="#333333")
package_label.grid(row=0, column=0, padx=(5, 0), sticky="w")

package_entry = ttk.Entry(input_frame, style="Modern.TEntry")
package_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")  # Remove columnspan
package_entry.config(width=60)  # Adjust width as needed

# Entry widget for repository name
repo_label = tk.Label(input_frame, text="Enter Repository Name:", foreground="white", background="#333333")
repo_label.grid(row=1, column=0, padx=(5, 0), sticky="w")

repo_entry = ttk.Entry(input_frame, style="Modern.TEntry")
repo_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")  # Remove columnspan
repo_entry.config(width=60)  # Adjust width as needed


# Load the logo image
logo_image = tk.PhotoImage(file="/usr/share/g-slpkg/slackware_logo_med.png")

# Load the icon image
icon_image = tk.PhotoImage(file="/usr/share/g-slpkg/hacker_128.png")  

# Create a label for the logo and icon
logo_icon_frame = tk.Frame(input_frame, background="#333333")
logo_icon_frame.grid(row=0, column=2, rowspan=2, padx=(10, 0), sticky="n")  # Adjust padding and sticky

# Create a label for the logo
logo_label = tk.Label(logo_icon_frame, image=logo_image, background="#333333")
logo_label.pack(side="left")  # Display logo on the left side

# Create a label for the icon
icon_label = tk.Label(logo_icon_frame, image=icon_image, background="#333333")
icon_label.pack(side="right")  # Display icon on the right side, not exactly but...i tried

# Set the icon and logo images
logo_label.image = logo_image  # Keep references to the images to prevent them from being garbage collected
icon_label.image = icon_image


# Display recent activity or notifications
activity_label = tk.Label(input_frame, text="Recent Activity:", foreground="white", background="#333333")
activity_label.grid(row=2, column=0, columnspan=2, padx=5, pady=(10, 0), sticky="w")

activity_text = tk.Text(input_frame, height=4, width=20, wrap="word")
activity_text.grid(row=3, column=0, columnspan=3, padx=5, pady=(0, 10), sticky="ew")


def refresh_activity():
    # Run the command to get recent activity
    command = "/bin/ls -tr /var/log/pkgtools/removed_scripts/ | tail -4"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    activity_output = result.stdout.strip()

    # Clear existing content and insert new activity
    activity_text.config(state="normal")
    activity_text.delete("1.0", "end")
    activity_text.insert("1.0", activity_output)
    activity_text.config(state="disabled")

    # Refresh again after 5 seconds
    root.after(5000, refresh_activity)

# Start the initial refresh
refresh_activity()


# Create a frame for the buttons
button_frame = tk.Frame(content_frame, bg="#333333")
button_frame.pack(fill=tk.X, padx=5, pady=10)

# Create buttons with icons
button_data = [
    ("Search", search_pkg_icon, "Search"),
    ("Install", install_icon, "Install"),
    ("Reinstall", reinstall_pkg_icon, "Reinstall"),
    ("UPDATE ALL REPOS", update_manager_icon, "UPDATE REPOS"),
    ("UPGRADE PACKAGES", upgrade_icon, "UPGRADE PACKAGES")
]

for text, icon, cmd in button_data:
    button = ttk.Button(
    button_frame,
    text=text,
    image=icon,
    compound="left",
    command=lambda c=cmd: run_install_command(c),
    style="Modern.TButton"
)

    button.pack(side=tk.LEFT, padx=5)
    
create_menus(menu_bar)
root.mainloop()
