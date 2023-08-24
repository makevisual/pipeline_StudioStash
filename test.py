import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Text Widget Example")

# Create a custom style
style = ttk.Style()
style.configure("Custom.TText", background="lightgray")  # Change "lightgray" to your desired color

# Create a Text widget using the custom style
text_widget = tk.Text(root, height=10, width=40, style="Custom.TText")

# Pack the Text widget
text_widget.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
