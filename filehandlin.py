import tkinter as tk
from tkinter import filedialog
import os

# Function to import and run the selected file
def run_selected_file(filename):
    if filename.endswith('.py'):
        os.system(f'python {filename}')
    else:
        print("Selected file is not a Python script.")

# Create the main window
root = tk.Tk()
root.title('File Selector')

# Frame for the Listbox
frame = tk.Frame(root)
frame.pack(pady=20)

# Listbox to display files
listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side='left', fill='y')

# Scrollbar for the Listbox
scrollbar = tk.Scrollbar(frame, orient='vertical')
scrollbar.pack(side='right', fill='y')

# Link scrollbar to listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# List of file names (replace with your actual file names)
file_names = ['mallusFINAL.py', 'photcellFINAL.py']

# Add file names to the Listbox
for file in file_names:
    listbox.insert('end', file)

# Function to get the selected file and run it
def select_and_run():
    selected_index = listbox.curselection()
    selected_file = listbox.get(selected_index)
    run_selected_file(selected_file)

# Button to choose the file to run
run_button = tk.Button(root, text='Run Selected File', command=select_and_run)
run_button.pack(pady=20)

# Run the main loop
root.mainloop()
