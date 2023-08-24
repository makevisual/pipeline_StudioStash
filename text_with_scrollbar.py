import tkinter as tk

def get_text():
    text = text_box.get("1.0", "end-1c")  # Get text from the textbox
    print("Textbox contents:", text)

# Create the main window
root = tk.Tk()
root.title("Text Box Example")

# Create a vertical scrollbar
vertical_scrollbar = tk.Scrollbar(root)
vertical_scrollbar.pack(side="right", fill="y")

# Create a horizontal scrollbar
horizontal_scrollbar = tk.Scrollbar(root, orient="horizontal")
horizontal_scrollbar.pack(side="bottom", fill="x")

# Create a textbox
text_box = tk.Text(root, height=10, width=40, yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)
text_box.pack(padx=10, pady=10)

# Link scrollbars to the textbox
vertical_scrollbar.config(command=text_box.yview)
horizontal_scrollbar.config(command=text_box.xview)

# Create a button to retrieve the text from the textbox
get_text_button = tk.Button(root, text="Get Text", command=get_text)
get_text_button.pack()

# Start the GUI event loop
root.mainloop()