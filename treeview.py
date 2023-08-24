import tkinter as tk
from tkinter import ttk

def populate_treeview(tree):
    # Sample data for the Treeview
    data = [
        ("Item 1", "Small", "Red"),
        ("Item 2", "Medium", "Green"),
        ("Item 3", "Large", "Blue"),
        ("Item 4", "Small", "Yellow"),
        ("Item 5", "Medium", "Orange"),
    ]

    for item in data:
        tree.insert("", "end", values=item)

# Create the main window
root = tk.Tk()
root.title("Treeview Example")

# Create a Treeview with columns: Name, Size, Color
tree = ttk.Treeview(root, columns=("Name", "Size", "Color"), show="headings")

# Set column headings
tree.heading("Name", text="Name")
tree.heading("Size", text="Size")
tree.heading("Color", text="Color")

# Set column widths
tree.column("Name", width=100)
tree.column("Size", width=100)
tree.column("Color", width=100)

# Insert sample data into the Treeview
populate_treeview(tree)

# Pack the Treeview
tree.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()