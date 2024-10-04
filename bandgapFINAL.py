import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from math import log10

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to calculate 10^3/T
def calc_inverse_temp_kelvin(kelvin):
    return 10**3 / kelvin

# Function to calculate log of current
def calc_log_current(current):
    return log10(current)

# Function to plot the graph
def plot_graph(inverse_temp, log_currents):
    plt.figure(figsize=(10, 5))
    for i, log_current in enumerate(log_currents):
        plt.plot(inverse_temp, log_current, label=f'logI{i+1} for V{i+1}')
    plt.xlabel('10^3/T (K^-1)')
    plt.ylabel('log(I) (A)')
    plt.title('Graph of 10^3/T vs. log(I)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to handle the 'Calculate and Plot' button click
def on_calculate():
    try:
        # Get user inputs
        temperatures = [float(entry.get()) for entry in temp_entries]
        currents_v1 = [float(entry.get()) for entry in current_v1_entries]
        currents_v2 = [float(entry.get()) for entry in current_v2_entries]
        currents_v3 = [float(entry.get()) for entry in current_v3_entries]

        # Convert temperatures to Kelvin and calculate 10^3/T
        kelvin_temps = [celsius_to_kelvin(temp) for temp in temperatures]
        inverse_temps = [calc_inverse_temp_kelvin(k_temp) for k_temp in kelvin_temps]

        # Calculate log of currents
        log_currents_v1 = [calc_log_current(i) for i in currents_v1]
        log_currents_v2 = [calc_log_current(i) for i in currents_v2]
        log_currents_v3 = [calc_log_current(i) for i in currents_v3]

        # Plot the graph
        plot_graph(inverse_temps, [log_currents_v1, log_currents_v2, log_currents_v3])
    except ValueError:
        error_label.config(text='Please enter valid numbers.')

# Set up the main application window
root = tk.Tk()
root.title('Energy Band Gap Experiment')

# Create a frame for the table
table_frame = ttk.Frame(root)
table_frame.grid(column=0, row=0, columnspan=4)

# Create lists to hold the entry widgets
temp_entries = []
current_v1_entries = []
current_v2_entries = []
current_v3_entries = []

# Function to add a new row to the table
def add_row():
    row = len(temp_entries)
    temp_entry = ttk.Entry(table_frame, width=10)
    temp_entry.grid(column=0, row=row+1, padx=5, pady=5)
    temp_entries.append(temp_entry)

    current_v1_entry = ttk.Entry(table_frame, width=10)
    current_v1_entry.grid(column=1, row=row+1, padx=5, pady=5)
    current_v1_entries.append(current_v1_entry)

    current_v2_entry = ttk.Entry(table_frame, width=10)
    current_v2_entry.grid(column=2, row=row+1, padx=5, pady=5)
    current_v2_entries.append(current_v2_entry)

    current_v3_entry = ttk.Entry(table_frame, width=10)
    current_v3_entry.grid(column=3, row=row+1, padx=5, pady=5)
    current_v3_entries.append(current_v3_entry)

# Add the initial row to the table
add_row()

# Create labels for the table columns
ttk.Label(table_frame, text='Temperature (°C)').grid(column=0, row=0, padx=5, pady=5)
ttk.Label(table_frame, text='Current for 1V (µA)').grid(column=1, row=0, padx=5, pady=5)
ttk.Label(table_frame, text='Current for 2V (µA)').grid(column=2, row=0, padx=5, pady=5)
ttk.Label(table_frame, text='Current for 3V (µA)').grid(column=3, row=0, padx=5, pady=5)

# Create a button to add a new row to the table
add_row_button = ttk.Button(root, text='Add Row', command=add_row)
add_row_button.grid(column=0, row=1, pady=10)

# Create a button to calculate and plot the graph
calculate_button = ttk.Button(root, text='Calculate and Plot', command=on_calculate)
calculate_button.grid(column=1, row=1, pady=10)

# Label for displaying errors
error_label = ttk.Label(root, text='', foreground='red')
error_label.grid(column=2, row=1, columnspan=2)

# Run the application
root.mainloop()
