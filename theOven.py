'''
Pythin 3.
Sammuel A. W.
07-19-2023
This program will be used to take user input to customize a pizza that they want, then to have the user enter where they want it delivered.
'''

import tkinter as tk

# Main window
root = tk.Tk()
root.title("Pizza Palace")

# Size of window
root.geometry("400x400")

# Function: price calculation
def calculate_price():
    pass

# Create pizza size options
pizzaSizeLabel = tk.Label(root, text="Please select Pizza Size:")
pizzaSizeLabel.pack()

# Pizza toppings
pizza_toppings_label = tk.Label(root, text="Please select Toppings:")
pizza_toppings_label.pack()


# Crust type 
pizza_crust_label = tk.Label(root, text="Pleas select Crust Type:")
pizza_crust_label.pack()

# Calculation button
calculate_button = tk.Button(root, text="Calculate Price", command=calculate_price)
calculate_button.pack()

# Display label
pizza_price_label = tk.Label(root, text="Price: $0.00")
pizza_price_label.pack()

# Loops
root.mainloop()
