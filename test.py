import tkinter as tk
from tkinter import filedialog

def save_as():
    default_file_name = "my_file.txt"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_file_name, filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write("Hello, this is a test content!")

# Create the main window
root = tk.Tk()
root.title("Save As Dialog Example")

# Create a button to trigger the save-as dialog
save_button = tk.Button(root, text="Save As", command=save_as)
save_button.pack(pady=20)

# Run the main loop
root.mainloop()
