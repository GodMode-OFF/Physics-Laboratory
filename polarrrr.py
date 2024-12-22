import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to calculate resistivity
def calculate_resistivity(voltage, current_mA, w_cm, s_cm):
    # Convert current from milliamperes to amperes and width and spacing from centimeters to meters
    current_A = current_mA / 1000
    w_m = w_cm / 100
    s_m = s_cm / 100
    a = (voltage / current_A) * 2 * np.pi * s_m
    resistivity = a / (w_m * s_m)
    return resistivity

# Function to plot the graph
def plot_graph(x_values, y_values):
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('1000/T (K⁻¹)')
    plt.ylabel('log10(Resistivity)')
    plt.title('Resistivity vs Temperature Graph')
    plt.grid(True)
    plt.show()

# Function to calculate and update the grid values
def calculate_values(entries, current_mA, w_cm, s_cm):
    try:
        for row in entries:
            # Convert temperature to Kelvin and update the grid
            temp_kelvin = celsius_to_kelvin(float(row[0].get()))
            row[2].delete(0, tk.END)
            row[2].insert(0, str(temp_kelvin))
            
            # Calculate resistivity and update the grid
            resistivity = calculate_resistivity(float(row[1].get()), current_mA, w_cm, s_cm)
            row[3].delete(0, tk.END)
            row[3].insert(0, str(resistivity))
            
            # Calculate 1000/T and update the grid
            inverse_temp = 1000 / temp_kelvin
            row[4].delete(0, tk.END)
            row[4].insert(0, str(inverse_temp))
            
            # Calculate log10(resistivity) and update the grid
            log_resistivity = np.log10(resistivity)
            row[5].delete(0, tk.END)
            row[5].insert(0, str(log_resistivity))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to handle the 'Calculate and Plot Graph' button click
def on_calculate_click(entries, current_mA, w_cm, s_cm):
    calculate_values(entries, current_mA, w_cm, s_cm)
    x_values = [float(row[4].get()) for row in entries]
    y_values = [float(row[5].get()) for row in entries]
    plot_graph(x_values, y_values)

# First GUI to get current, w, s
def first_gui():
    first_window = tk.Tk()
    first_window.title("Input Parameters")

    tk.Label(first_window, text="Current (mA):").grid(row=0, column=0)
    current_entry = tk.Entry(first_window)
    current_entry.grid(row=0, column=1)

    tk.Label(first_window, text="Width (w, cm):").grid(row=1, column=0)
    w_entry = tk.Entry(first_window)
    w_entry.grid(row=1, column=1)

    tk.Label(first_window, text="Spacing (s, cm):").grid(row=2, column=0)
    s_entry = tk.Entry(first_window)
    s_entry.grid(row=2, column=1)

    def on_submit():
        try:
            current_mA = float(current_entry.get())
            w_cm = float(w_entry.get())
            s_cm = float(s_entry.get())
            first_window.destroy()
            second_gui(current_mA, w_cm, s_cm)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    submit_button = tk.Button(first_window, text="Submit", command=on_submit)
    submit_button.grid(row=3, columnspan=2)

    first_window.mainloop()

# Second GUI to take inputs and calculate values
def second_gui(current_mA, w_cm, s_cm):
    second_window = tk.Tk()
    second_window.title("Data Input and Calculation")

    # Column labels
    labels = ["Temperature (°C)", "Voltage (V)", "Temperature (K)", "Resistivity (Ω·m)", "1000/T (K⁻¹)", "log10(Resistivity)"]
    for i, label in enumerate(labels):
        tk.Label(second_window, text=label).grid(row=0, column=i)

    entries = []
    for i in range(1, 14):
        row_entries = []
        for j in range(6):
            entry = tk.Entry(second_window)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        entries.append(row_entries)

    calculate_button = tk.Button(second_window, text="Calculate and Plot Graph",
                                 command=lambda: on_calculate_click(entries, current_mA, w_cm, s_cm))
    calculate_button.grid(row=14, columnspan=6)

    second_window.mainloop()

if __name__ == "__main__":
    first_gui()
