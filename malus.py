import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

class PolarizationExperiment:
    def __init__(self, root):
        self.root = root
        self.root.title("Polarization Experiment")
        
        self.degrees = list(range(90, -10, -10)) + list(range(-10, -100, -10))
        
        self.current_values = {}
        self.create_table()
        self.create_graph_button()
    
    def create_table(self):
        table_frame = ttk.Frame(self.root)
        table_frame.pack(pady=10)
        
        ttk.Label(table_frame, text="Angle (degrees)").grid(row=0, column=0)
        ttk.Label(table_frame, text="Current (µA)").grid(row=0, column=1)
        
        for i, degree in enumerate(self.degrees, start=1):
            ttk.Label(table_frame, text=str(degree)).grid(row=i, column=0)
            self.current_values[degree] = tk.StringVar()
            ttk.Entry(table_frame, textvariable=self.current_values[degree]).grid(row=i, column=1)
    
    def create_graph_button(self):
        ttk.Button(self.root, text="Plot Graph", command=self.plot_graph).pack(pady=10)
    
    def plot_graph(self):
        angles = np.radians(self.degrees)
        currents = [float(self.current_values[degree].get() or 0) for degree in self.degrees]
        
        plt.figure(figsize=(8, 6))
        plt.plot(angles, currents, marker='o', linestyle='-')
        plt.title("Polarization Experiment")
        plt.xlabel("Angle (radians)")
        plt.ylabel("Current (µA)")
        plt.grid(True)
        plt.show()

def main():
    root = tk.Tk()
    app = PolarizationExperiment(root)
    root.mainloop()

if __name__ == "__main__":
    main()
