import tkinter as tk
from tkinter import ttk

sdstVer = [0,0,1]
data = [
    (R"W:\Projects\Hot Wheels - Racerverse - Segment"		, "unknown"	),
    (R"W:\Projects\FMW - Campaign"							, "unknown"	),
    (R"W:\Projects\Hot Wheels - MT - Crushzilla Playset"	, "unknown"	),
    (R"W:\Projects\BraveHurts"								, "unknown"	),
    (R"W:\Projects\Hot Wheels - City - Ultimate Garage"		, "unknown"	),
    (R"W:\Projects\Hot Wheels - City - TRCD"				, "unknown" ),
]

def ui_init():
	# Set the window size (width x height)
	print("UI INIT")
	window.geometry("600x300")  # Width: 400, Height: 300
	window.iconbitmap("makeIcon.ico")
	window.configure(bg="#303841")  

def get_folder_size(folder_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

    size_bytes = total_size

    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    size_gb = size_mb / 1024


    print(f"Total size: {size_bytes} bytes, {size_kb:.2f} KB, {size_mb:.2f} MB, {size_gb:.2f} GB")

    return total_size

def change_button_color():
    new_color = color_entry.get()
    style.configure("TButton", background=new_color)

def trv_pathsSrc_init():
	# Set column headings
	trv_pathsSrc.heading("path", text="Path")
	trv_pathsSrc.heading("size", text="Size")

	# Set column widths
	trv_pathsSrc.column("path", width=450)
	trv_pathsSrc.column("size", width=100)

def trv_pathsSrc_populate():
    for item in data:
        trv_pathsSrc.insert("", "end", values=item)

def statusUpdate(arg_text):
	print("---- test ---- ")
	#lab_status.set =("status: "+arg_text)
	lab_status.set =("status: "+ arg_text)

# Create the main window
window = tk.Tk()
window.title("StudioStash v"+ str(sdstVer[0]) + "." + str(sdstVer[1]) + "." + str(sdstVer[2]) )

ui_init()

# Create a style for the widgets
style = ttk.Style()
style.configure("TLabel", background="#303841", foreground="white")  # Set label colors
style.configure("TButton", background="#4f565e", foreground="black")  # Set button colors
style.configure("TEntry", fieldbackground="#444444", foreground="black") 
style.configure("TText", background="#303841", foreground="white") 


#### UI Items ####
lab_pathsSrc = ttk.Label(window, text="Path(s) to archive:")
lab_pathsSrc.place(x=10, y=10)

txt_pathsSrc = tk.Text(window,width=70,height=2)
txt_pathsSrc.place(x=10, y=30)
txt_pathsSrc.configure(bg="#4f565e") 
txt_pathsSrc.configure(fg="white") 

btn_pathsSrcAdd = ttk.Button(window, text="Add", command=change_button_color)
btn_pathsSrcAdd.place(x=10, y=70)

btn_pathsSrcClear = ttk.Button(window, text="Clear", command=change_button_color)
btn_pathsSrcClear.place(x=88, y=70)



lab_pathsDst = ttk.Label(window, text="Destination Path:")
lab_pathsDst.place(x=10, y=110)

txt_pathsDst = tk.Entry(window,width=93)
txt_pathsDst.place(x=10, y=130)
txt_pathsDst.configure(bg="#4f565e") 
txt_pathsDst.configure(fg="white") 

btn_pathsDstAdd = ttk.Button(window, text="Check", command=change_button_color)
btn_pathsDstAdd.place(x=10, y=152)

btn_pathsDstClear = ttk.Button(window, text="Clear", command=change_button_color)
btn_pathsDstClear.place(x=88, y=152)

lab_status = ttk.Label(window, text=":")
lab_status.place(x=10, y=275)
statusUpdate("ready")
# todo: finish setting the text


# trv_pathsSrc = ttk.Treeview(window, columns=("path", "size"), show="headings", height=4)
# trv_pathsSrc.place(x=10, y=110)
# trv_pathsSrc_init()
# trv_pathsSrc_populate()






# Create a button to change the color
# btn_generateBat = ttk.Button(window, text="Generate .Bat tool", command=change_button_color)
#btn_generateBat.pack()



# Start the main event loop
window.mainloop()
ui_init()


