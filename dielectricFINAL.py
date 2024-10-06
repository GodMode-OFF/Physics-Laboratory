import tkinter as tk
from tkinter import messagebox

def calculate_dielectric_constant():
    try:
        # Get user inputs
        thickness_mm = float(thickness_entry.get())  # This is currently unused
        C1 = float(C1_entry.get())
        C2 = float(C2_entry.get())
        C3 = float(C3_entry.get())

        # Corrected formula to calculate the dielectric constant (K)
        K = (C2 - C1) / (C3 - C1)

        # Display the result
        result_label.config(text=f"Dielectric Constant (K): {K:.4f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create a GUI window
root = tk.Tk()
root.title("Dielectric Constant Calculator")

# Create input fields
thickness_label = tk.Label(root, text="Thickness (mm):")
thickness_entry = tk.Entry(root)
C1_label = tk.Label(root, text="Capacitance (C1, pF):")
C1_entry = tk.Entry(root)
C2_label = tk.Label(root, text="Capacitance (C2, pF):")
C2_entry = tk.Entry(root)
C3_label = tk.Label(root, text="Capacitance (C3, pF):")
C3_entry = tk.Entry(root)

# Create a button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate_dielectric_constant)

# Create a label to display the result
result_label = tk.Label(root, text="")

# Arrange widgets in the grid
thickness_label.grid(row=0, column=0)
thickness_entry.grid(row=0, column=1)
C1_label.grid(row=1, column=0)
C1_entry.grid(row=1, column=1)
C2_label.grid(row=2, column=0)
C2_entry.grid(row=2, column=1)
C3_label.grid(row=3, column=0)
C3_entry.grid(row=3, column=1)
calculate_button.grid(row=4, columnspan=2)
result_label.grid(row=5, columnspan=2)

root.mainloop()
