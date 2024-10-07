import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk

# Initialize an empty list to store entered data
data_entries = []

# Function to calculate Hall coefficient
def calculate_hall_coefficient():
    try:
        I = float(current_entry.get())  # Current in micro-amperes
        VH_forward = float(forward_entry.get()) / 1000.0  # Reading in mV (convert to V)
        VH_reverse = float(reverse_entry.get()) / 1000.0  # Reading in mV (convert to V)

        # Calculate mean voltage
        VH_mean = (VH_forward - VH_reverse) / 2

        # Calculate Hall coefficient (RH)
        B = 1.0  # Assume a magnetic field strength (you can input the actual value)
        RH = VH_mean * 1000 / (I * B)

        # Append entered data to the list
        data_entries.append((I, VH_forward, VH_reverse, VH_mean, RH))

        # Display results
        result_label.config(text=f"RH (Hall Coefficient): {RH:.4f}")

        # Clear input fields
        current_entry.delete(0, tk.END)
        forward_entry.delete(0, tk.END)
        reverse_entry.delete(0, tk.END)

        # Update the table
        update_table()

    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Function to update the table with new data
def update_table():
    # Clear existing rows
    for row in data_tree.get_children():
        data_tree.delete(row)

    # Insert new rows
    for entry in data_entries:
        data_tree.insert("", "end", values=entry)

# Create the GUI
root = tk.Tk()
root.title("Hall Effect Experiment")

# Create labels and entry fields
current_label = tk.Label(root, text="Current (μA):")
current_entry = tk.Entry(root)
forward_label = tk.Label(root, text="Reading (Forward, VH in mV):")
forward_entry = tk.Entry(root)
reverse_label = tk.Label(root, text="Reading (Reverse, VH in mV):")
reverse_entry = tk.Entry(root)

# Button to calculate the Hall coefficient
calculate_button = tk.Button(root, text="Calculate", command=calculate_hall_coefficient)

# Label to display the result
result_label = tk.Label(root, text="Results will appear here.")

# Create a table to display the data
data_tree = ttk.Treeview(root, columns=("Current", "VH Forward", "VH Reverse", "VH Mean", "RH"))
data_tree.heading("#1", text="Current (μA)")
data_tree.heading("#2", text="VH Forward (V)")
data_tree.heading("#3", text="VH Reverse (V)")
data_tree.heading("#4", text="VH Mean (V)")
data_tree.heading("#5", text="RH")

# Arrange widgets in the GUI using grid layout
current_label.grid(row=0, column=0, padx=10, pady=5)
current_entry.grid(row=0, column=1, padx=10, pady=5)
forward_label.grid(row=1, column=0, padx=10, pady=5)
forward_entry.grid(row=1, column=1, padx=10, pady=5)
reverse_label.grid(row=2, column=0, padx=10, pady=5)
reverse_entry.grid(row=2, column=1, padx=10, pady=5)
calculate_button.grid(row=3, columnspan=2, pady=10)
result_label.grid(row=4, columnspan=2, pady=10)

# Place the data table below the input fields
data_tree.grid(row=5, columnspan=2, padx=10, pady=10)

# Run the GUI
root.mainloop()
