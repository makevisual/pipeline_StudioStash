import tkinter as tk
from tkinter import ttk 

sdstVer = [0,0,1]
data = [
    (R"W:\Projects\Hot Wheels - Racerverse - Segment"       , "unknown" ),
    (R"W:\Projects\FMW - Campaign"                          , "unknown" ),
    (R"W:\Projects\Hot Wheels - MT - Crushzilla Playset"    , "unknown" ),
    (R"W:\Projects\BraveHurts"                              , "unknown" ),
    (R"W:\Projects\Hot Wheels - City - Ultimate Garage"     , "unknown" ),
    (R"W:\Projects\Hot Wheels - City - TRCD"                , "unknown" ),
]

class SDST_UI_Main:

    # Function for creating the UI, and laying out its 
    def __init__(self, root, sdstData):

        # Create the main window
        self.root = root
        self.root.title("StudioStash v"+ str(sdstVer[0]) + "." + str(sdstVer[1]) + "." + str(sdstVer[2]) )

        # Set the window size (width x height)
        print("UI INIT")
        self.root.geometry("600x420")  # Width: 400, Height: 300
        self.root.iconbitmap("makeIcon.ico")
        self.root.configure(bg="#303841") 

        # Set the style
        style = ttk.Style()
        style.configure("TLabel", background="#303841", foreground="white")  # Set label colors
        style.configure("TButton", background="#4f565e", foreground="black")  # Set button colors
        style.configure("TEntry", fieldbackground="#444444", foreground="black") 
        style.configure("TText", background="#303841", foreground="white") 

        # PathsSrc ui items
        self.lab_pathsSrc = ttk.Label(self.root, text="Add path(s) to archive:")
        self.lab_pathsSrc.place(x=10, y=10)

        self.txt_pathsSrc = tk.Text(self.root,width=70,height=2)
        self.txt_pathsSrc.place(x=10, y=30)
        self.txt_pathsSrc.configure(bg="#4f565e") 
        self.txt_pathsSrc.configure(fg="white") 

        self.btn_pathsSrcAdd = ttk.Button(self.root, text="Add", command=self.testFunction)
        self.btn_pathsSrcAdd.place(x=10, y=70)

        self.btn_pathsSrcClear = ttk.Button(self.root, text="Clear", command=self.testFunction)
        self.btn_pathsSrcClear.place(x=88, y=70)

        # PathsDst ui items
        self.lab_pathsDst = ttk.Label(self.root, text="Destination Path:")
        self.lab_pathsDst.place(x=10, y=110)

        self.txt_pathsDst = tk.Entry(self.root,width=93)
        self.txt_pathsDst.place(x=10, y=130)
        self.txt_pathsDst.configure(bg="#4f565e") 
        self.txt_pathsDst.configure(fg="white") 

        self.lab_pathsDstDisplay = ttk.Label(self.root, text="no destination set")
        self.lab_pathsDstDisplay.place(x=10, y=150)

        self.btn_pathsDstAdd = ttk.Button(self.root, text="Set", command=self.testFunction)
        self.btn_pathsDstAdd.place(x=10, y=172)

        self.btn_pathsDstClear = ttk.Button(self.root, text="Clear", command=self.testFunction)
        self.btn_pathsDstClear.place(x=88, y=172)

        # PathsActive
        self.lab_pathsActive = ttk.Label(self.root, text="Valid path(s):")
        self.lab_pathsActive.place(x=10, y=220)

        self.trv_pathsActive = ttk.Treeview(self.root, columns=("path", "size"), show="headings", height=4)
        self.trv_pathsActive.place(x=10, y=242)

        self.trv_pathsActive_init()
        self.trv_pathsActive_populate(sdstData)

        self.btn_pathsActiveClear = ttk.Button(self.root, text="Clear All", command=self.testFunction)
        self.btn_pathsActiveClear.place(x=10, y=352)
        
        self.btn_pathsActiveCheckSize = ttk.Button(self.root, text="Check Size(s)", command=self.testFunction)
        self.btn_pathsActiveCheckSize.place(x=360, y=352)

        self.btn_pathsActiveGenScript = ttk.Button(self.root, text="Generate Archive Script", command=self.testFunction)
        self.btn_pathsActiveGenScript.place(x=439, y=352)

        # status bar
        self.lab_status = ttk.Label(self.root, text=":")
        self.lab_status.place(x=10, y=395)
        self.statusUpdate("ready")

    def testFunction(self):
        
        print("Test Function Ran")


    def statusUpdate(self, arg_text):

        print("---- test ---- ")
        #lab_status.set =("status: "+arg_text)
        self.lab_status.config(text=("status: "+ arg_text))

    def trv_pathsActive_init(self):

        # Set column headings
        self.trv_pathsActive.heading("path", text="Path")
        self.trv_pathsActive.heading("size", text="Size")

        # Set column widths
        self.trv_pathsActive.column("path", width=480)
        self.trv_pathsActive.column("size", width=80)

    def trv_pathsActive_populate(self,sdstData):

        print("---- trv_pathsActive_populate ----")

        sdstData.display_info()

        for op in sdstData.copyOperations:
            op.display_info()

        for item in data:
            self.trv_pathsActive.insert("", "end", values=item)
        

        pass


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    from sdst_classes import *
    sdstData = SDSTData()

    # Create an instance of the SDST_UI_Main class
    my_gui = SDST_UI_Main(root, sdstData)

    # Start the Tkinter main loop
    root.mainloop()