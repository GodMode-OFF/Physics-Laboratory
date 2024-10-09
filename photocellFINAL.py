import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# Function to calculate 1/d^2 and d^2 * deflection angle
def calculate_values(d, angle):
    d_squared = d ** 2
    inverse_d_squared = 1 / d_squared
    product = d_squared * angle
    return inverse_d_squared, product

# Function to plot the graph
def plot_graph(data):
    x_values = [item['inverse_d_squared'] for item in data]
    y_values = [item['deflection_angle'] for item in data]
    
    plt.plot(x_values, y_values, 'o-', label='Deflection Angle vs 1/d^2')
    plt.xlabel('1/d^2 (m^-2)')
    plt.ylabel('Deflection Angle (degrees)')
    plt.title('Graph of Deflection Angle vs 1/d^2')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to add data to the table
def add_data():
    try:
        position_lamp = float(entry_lamp.get())
        position_cell = float(entry_cell.get())
        deflection_angle = float(entry_angle.get())
        distance = float(entry_distance.get())
        
        inverse_d_squared, product = calculate_values(distance, deflection_angle)
        
        # Append data to the list
        data.append({
            'position_lamp': position_lamp,
            'position_cell': position_cell,
            'deflection_angle': deflection_angle,
            'distance': distance,
            'inverse_d_squared': inverse_d_squared,
            'product': product
        })
        
        # Insert data into the treeview
        tree.insert('', 'end', values=(position_lamp, position_cell, deflection_angle, distance, inverse_d_squared, product))
        
        # Clear entry fields after adding data
        entry_lamp.delete(0, tk.END)
        entry_cell.delete(0, tk.END)
        entry_angle.delete(0, tk.END)
        entry_distance.delete(0, tk.END)

    except ValueError:
        print("Please enter valid numbers.")

# Main window
root = tk.Tk()
root.title("Photoelectric Effect Experiment")

# Data list
data = []

# Entry fields
entry_lamp = tk.Entry(root)
entry_lamp.grid(row=0, column=1)
entry_cell = tk.Entry(root)
entry_cell.grid(row=1, column=1)
entry_angle = tk.Entry(root)
entry_angle.grid(row=2, column=1)
entry_distance = tk.Entry(root)
entry_distance.grid(row=3, column=1)

# Labels
tk.Label(root, text="Position of Lamp").grid(row=0, column=0)
tk.Label(root, text="Position of Photocell").grid(row=1, column=0)
tk.Label(root, text="Deflection Angle").grid(row=2, column=0)
tk.Label(root, text="Distance from Photocell to Lamp").grid(row=3, column=0)

# Button to add data to the table
button_add = tk.Button(root, text="Add Data", command=add_data)
button_add.grid(row=4, columnspan=2)

# Table to display the data
tree = ttk.Treeview(root)
tree['columns'] = ('position_lamp', 'position_cell', 'deflection_angle', 'distance', 'inverse_d_squared', 'product')

# Set up column headings and widths
for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(row=5, columnspan=2)

# Button to plot the graph
button_plot = tk.Button(root, text="Plot Graph", command=lambda: plot_graph(data))
button_plot.grid(row=6, columnspan=2)

# Start the main loop
root.mainloop()
