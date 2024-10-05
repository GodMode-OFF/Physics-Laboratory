import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# Constants
distance_slit_source = 125 / 1000  # converting mm to meters
d = 2.13e-10  # Angstrom to meters

# Function to calculate theoretical wavelength
def theoretical_wavelength(voltage):
    h = 6.626e-34  # Planck's constant
    m = 9.109e-31  # mass of electron
    e = 1.602e-19  # elementary charge
    kinetic_energy = e * voltage * 1000  # converting kilovolts to volts
    lambda_theoretical = h / np.sqrt(2 * m * kinetic_energy)
    return lambda_theoretical * 1e10  # converting meters to Angstrom

# Function to calculate experimental wavelength
def experimental_wavelength(diameter):
    return (d * diameter) / (2 * distance_slit_source) * 1e7  # converting meters to Angstrom

# Function to calculate error
def calculate_error(experimental, theoretical):
    return ((experimental - theoretical) / theoretical) * 100

# Function to plot graph
def plot_graph(accelerating_voltages, wavelengths):
    inv_sqrt_voltage = 1 / np.sqrt(accelerating_voltages)
    plt.plot(wavelengths, inv_sqrt_voltage, marker='o', linestyle='-')
    plt.xlabel('Wavelength (Angstrom)')
    plt.ylabel('1 / sqrt(Accelerating Voltage)')
    plt.title('de Broglie Wavelength vs 1/sqrt(Voltage)')
    plt.grid(True)
    plt.show()

# Function to handle button click
def calculate_wavelength():
    for i in range(3):
        voltage = float(entries[i][0].get())
        diameter = float(entries[i][1].get())

        theoretical = theoretical_wavelength(voltage)
        experimental = experimental_wavelength(diameter)
        error = calculate_error(experimental, theoretical)

        tree.insert("", "end", values=(voltage, experimental, theoretical, error))

    accelerating_voltages = [float(entry[0].get()) for entry in entries[:3]]
    wavelengths = [float(entry[1].get()) for entry in entries[:3]]
    plot_graph(accelerating_voltages, wavelengths)

# GUI
root = tk.Tk()
root.title("de Broglie Experiment")

# Create treeview
tree = ttk.Treeview(root)
tree["columns"] = ("1", "2", "3", "4")
tree.heading("1", text="Accelerating Voltage (kV)")
tree.heading("2", text="Experimental Wavelength (Angstrom)")
tree.heading("3", text="Theoretical Wavelength (Angstrom)")
tree.heading("4", text="Error (%)")
tree.pack()

# Create labels and entry fields
entries = []
for i in range(3):
    frame = ttk.Frame(root)
    frame.pack(pady=5)
    ttk.Label(frame, text="Voltage (kV): ").grid(row=0, column=0)
    ttk.Label(frame, text="Diameter (mm): ").grid(row=0, column=2)
    voltage_entry = ttk.Entry(frame)
    diameter_entry = ttk.Entry(frame)
    voltage_entry.grid(row=0, column=1)
    diameter_entry.grid(row=0, column=3)
    entries.append((voltage_entry, diameter_entry))

# Button to calculate wavelengths
calculate_button = ttk.Button(root, text="Calculate Wavelength", command=calculate_wavelength)
calculate_button.pack(pady=10)

root.mainloop()
