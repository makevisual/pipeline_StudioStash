import tkinter as tk
from tkinter import ttk
from sdst_classes import *


def ui_init():
	# Set the window size (width x height)
	print("UI INIT")
	window.geometry("600x400")  # Width: 400, Height: 300
	window.iconbitmap("makeIcon.ico")
	window.configure(bg="#303841")  

def change_button_color():
    new_color = color_entry.get()
    style.configure("TButton", background=new_color)

def trv_pathsActive_init():
	# Set column headings
	trv_pathsActive.heading("path", text="Path")
	trv_pathsActive.heading("size", text="Size")

	# Set column widths
	trv_pathsActive.column("path", width=480)
	trv_pathsActive.column("size", width=80)

def trv_pathsActive_populate():
    for item in data:
        trv_pathsActive.insert("", "end", values=item)

def statusUpdate(arg_text):
	print("---- test ---- ")
	#lab_status.set =("status: "+arg_text)
	lab_status.config(text=("status: "+ arg_text))

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

# PathsSrc
lab_pathsSrc = ttk.Label(window, text="Add path(s) to archive:")
lab_pathsSrc.place(x=10, y=10)

txt_pathsSrc = tk.Text(window,width=70,height=2)
txt_pathsSrc.place(x=10, y=30)
txt_pathsSrc.configure(bg="#4f565e") 
txt_pathsSrc.configure(fg="white") 

btn_pathsSrcAdd = ttk.Button(window, text="Add", command=change_button_color)
btn_pathsSrcAdd.place(x=10, y=70)

btn_pathsSrcClear = ttk.Button(window, text="Clear", command=change_button_color)
btn_pathsSrcClear.place(x=88, y=70)

# PathsDst
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

# PathsActive
lab_pathsActive = ttk.Label(window, text="Valid path(s):")
lab_pathsActive.place(x=10, y=200)

trv_pathsActive = ttk.Treeview(window, columns=("path", "size"), show="headings", height=4)
trv_pathsActive.place(x=10, y=222)
trv_pathsActive_init()
trv_pathsActive_populate()

btn_pathsActiveCheckSize = ttk.Button(window, text="Check Size(s)", command=change_button_color)
btn_pathsActiveCheckSize.place(x=10, y=332)

btn_pathsActiveGenScript = ttk.Button(window, text="Generate Archive Script", command=change_button_color)
# btn_pathsActiveGenScript.place(x=88, y=332)
btn_pathsActiveGenScript.place(x=439, y=332)



# status 
lab_status = ttk.Label(window, text=":")
lab_status.place(x=10, y=375)
statusUpdate("ready")







# Create a button to change the color
# btn_generateBat = ttk.Button(window, text="Generate .Bat tool", command=change_button_color)
#btn_generateBat.pack()





opInfo = CopyOperationInfo()
opInfo.display_info()

sdstData = SDSTData()
sdstData.display_info()


print("end")





# Start the main event loop
window.mainloop()
ui_init()