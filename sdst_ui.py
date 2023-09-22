import tkinter as tk
from tkinter import ttk 
from sdst_functions import *
import os
import datetime
import threading

sdstVer = [0,0,1]

class SDST_UI_Main:

    # Function for creating the UI, and laying out its 
    def __init__(self, root, sdstData):

        self.sdstData = sdstData

        # Create the main window
        self.root = root
        self.root.title("StudioStash v"+ str(sdstVer[0]) + "." + str(sdstVer[1]) + "." + str(sdstVer[2]) )

        # Set the window size (width x height)
        self.root.geometry("600x560")  # Width: 400, Height: 300
        self.root.iconbitmap("makeIcon.ico")
        self.root.configure(bg="#303841") 

        # Set the style
        style = ttk.Style()
        style.configure("TLabel", background="#303841", foreground="white")  # Set label colors
        style.configure("TButton", background="#4f565e", foreground="black")  # Set button colors
        style.configure("TEntry", fieldbackground="#444444", foreground="black") 
        style.configure("TText", background="#303841", foreground="white") 

        # PathsSrc Entry
        self.lab_pathsSrc = ttk.Label(self.root, text="Source path(s) to copy:")
        self.lab_pathsSrc.place(x=10, y=10)
        self.txt_pathsSrc = tk.Text(self.root,width=70,height=2)
        self.txt_pathsSrc.place(x=10, y=30)
        self.txt_pathsSrc.configure(bg="#4f565e") 
        self.txt_pathsSrc.configure(fg="white") 
        self.btn_pathsSrcAdd = ttk.Button(self.root, text="Add", command=self.testFunction)
        self.btn_pathsSrcAdd.place(x=10, y=70)

        # PathsSrcActive Treeview
        self.lab_pathsSrcActive = ttk.Label(self.root, text="Valid source path(s):")
        self.lab_pathsSrcActive.place(x=10, y=100)
        self.trv_pathsSrcActive = ttk.Treeview(self.root, columns=("path", "size"), show="headings", height=4)
        self.trv_pathsSrcActive.place(x=10, y=120)
        self.btn_pathsSrcActiveClear = ttk.Button(self.root, text="Clear All", command=self.btn_pathsSrcActiveClear_pressed)
        self.btn_pathsSrcActiveClear.place(x=10, y=230)
        #self.btn_pathsSrcActiveCheckSize = ttk.Button(self.root, text="Check Size(s)", command=self.btn_pathsSrcActiveCheckSize_pressed)
        self.btn_pathsSrcActiveCheckSize = ttk.Button(self.root, text="Check Size(s)", command=lambda: threading.Thread(target=self.btn_pathsSrcActiveCheckSize_pressed).start())
        self.btn_pathsSrcActiveCheckSize.place(x=88, y=230)
        # And initialize it
        self.trv_pathsSrcActive_init()

        # PathsDst Entry
        self.lab_pathsDst = ttk.Label(self.root, text="Destination path(s):")
        self.lab_pathsDst.place(x=10, y=280)

        self.txt_pathsDst = tk.Entry(self.root,width=93)
        self.txt_pathsDst.place(x=10, y=300)
        self.txt_pathsDst.configure(bg="#4f565e") 
        self.txt_pathsDst.configure(fg="white") 

        self.btn_pathsDstAdd = ttk.Button(self.root, text="Add", command=self.btn_pathsDstAdd_pressed)
        self.btn_pathsDstAdd.place(x=10, y=322)
        
        # PathsSrcActive Treeview
        self.lab_pathsDstActive = ttk.Label(self.root, text="Valid destination path(s):")
        self.lab_pathsDstActive.place(x=10, y=355)
        self.trv_pathsDstActive = ttk.Treeview(self.root, columns=("path", "size"), show="headings", height=2)
        self.trv_pathsDstActive.place(x=10, y=375)
        self.btn_pathsDstActiveClear = ttk.Button(self.root, text="Clear All", command=self.btn_pathsDstActiveClear_pressed)
        self.btn_pathsDstActiveClear.place(x=10, y=445)
        self.btn_pathsDstActiveCheckSize = ttk.Button(self.root, text="Check Free Space ", command=self.btn_pathsDstActiveCheckSize_pressed)
        self.btn_pathsDstActiveCheckSize.place(x=88, y=445)
        # And initialize it
        self.trv_pathsDstActive_init()

        # Generate button
        self.btn_pathsSrcActiveGenScript = ttk.Button(self.root, text="  Generate Batch Archive Script  ", command=self.btn_pathsSrcActiveGenScript_pressed)
        self.btn_pathsSrcActiveGenScript.place(x=395, y=500)

        self.btn_injectData = ttk.Button(self.root, text="  inject temp data  ", command=self.injectData)
        self.btn_injectData.place(x=10, y=500)

        self.btn_displayData = ttk.Button(self.root, text="  print data  ", command=self.sdstDataDisplay)
        self.btn_displayData.place(x=120, y=500)

        # status bar
        self.lab_status = ttk.Label(self.root, text=":")
        self.lab_status.place(x=10, y=530)
        self.statusUpdate("Ready")

    def generateCopyOperations(self):

        # print("---- trv_pathsSrcActive_populate ----")
        # sdstData.display_info()

        # for op in self.sdstData.copyOperations:
        #     op.display_info()

        pass

    # Prints data object to the console
    def sdstDataDisplay(self):

        self.sdstData.display_info()

        self.statusUpdate("Displaying sdstData")

    # Injects testing data into sdstData
    def injectData(self):

        # Temp Data
        # self.sdstData.pathsSrc=["C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks", "C:\\\\test\\\\mockProjects\\\\RepoRetimeRoughKey","W:\\\\Projects\\\\AOT - Teaser"]
        # self.sdstData.pathsSrc=["C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks", "C:\\\\test\\\\mockProjects\\\\RepoRetimeRoughKey","W:\\\\Projects\\\\AOT - Teaser","X:\\\\Projects\\\\Days","X:\\\\Projects\\\\CHS - CorpRefresh Video","X:\\\\Projects\\\\F22 HW City - Action Spiral Playset"]
        self.sdstData.pathsSrc=["C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks", "C:\\\\test\\\\mockProjects\\\\RepoRetimeRoughKey","W:\\\\Projects\\\\AOT - Teaser","X:\\\\Projects\\\\Callaway - Precision Technology","X:\\\\Projects\\\\Bridgestone - B-Seal","X:\\\\Projects\\\\CMDA"]
        self.sdstData.pathsDst=["C:\\test\\mockArchive"]

        # populate
        self.trv_pathsSrcActive_populate()
        self.trv_pathsDstActive_populate()

        self.statusUpdate("Test Data Injected")

    # thread for calculating the size of source paths, and returning them to the UI
    def btn_pathsSrcActiveCheckSize_pressed(self):

        # Clear out reports, and fill them with "calculating..."
        spaceReports = []
        entryText = "Calculating..."

        for i in range(len(sdstData.pathsSrc)):
            spaceReports.append(entryText)

        # Update the list with the 'calculating' list
        self.btn_pathsSrcActiveCheckSize_pressed_updateSize(spaceReports)

        # For each of the paths find the size
        i=0
        for curPath in self.sdstData.pathsSrc:

            # Update the UI with the path being operated on
            self.btn_pathsSrcActiveCheckSize_pressed_statusUpdate( curPath )

            # Start Calculating the size
            curPathSpaceReport = get_folder_size(curPath)

            # Turn it into Gigabytes
            size_kb = curPathSpaceReport / 1024
            size_mb = size_kb / 1024
            size_gb = size_mb / 1024

            # Replace the "Calculating" text, with the actual size
            spaceReports[i]=size_gb

            # Return the space reports to the main thread, and update the UI
            self.btn_pathsSrcActiveCheckSize_pressed_updateSize(spaceReports)            

            i+=1

    # called by btn_pathsSrcActiveCheckSize_pressed to update the status bar
    def btn_pathsSrcActiveCheckSize_pressed_statusUpdate(self,curPath):

        self.statusUpdate("Calculating Directory Size - "+ str(curPath) + "...")

    # called by btn_pathsSrcActiveCheckSize_pressed to update the folder sizes
    def btn_pathsSrcActiveCheckSize_pressed_updateSize(self,spaceReportsStream):

        # Assign the returned data from the thread, and then update the UI
        self.sdstData.pathsSrcSpaceReport = spaceReportsStream
        self.trv_pathsSrcActive_populate()

    # refreshes the free space calculation by re-populating the destination treeview
    def btn_pathsDstActiveCheckSize_pressed(self):
        self.trv_pathsDstActive_populate()
        self.statusUpdate("Free Space Calculated")

    # Function for pressing the Clear Destination
    def btn_pathsDstActiveClear_pressed(self):
        self.sdstData.pathsDst = []
        self.trv_pathsDstActive_clear()
        self.statusUpdate("Destination Path Cleared")

    # Function for pressing the Set Destination button
    def btn_pathsDstAdd_pressed(self):

        # Get the text string from the UI
        self.sdstData.input_pathsSrc = self.txt_pathsDst.get()

        # Sanatize the string
        cleaned_path = self.sdstData.input_pathsSrc.replace("\"", "")   # Takes away Quotes
        cleaned_path = cleaned_path.replace("/", "\\")                  # Sets slash directions
        cleaned_path = cleaned_path.replace(",", "")                    # takes away commas

        # Test if path exists 
        if os.path.exists(cleaned_path):
            
            # Only commits the destination if it is a valid path
            # TODO - add support for multiple destinations
            self.sdstData.pathsDst = [cleaned_path]

        # If invalid, clear any existing paths out
        else: 
            self.sdstData.pathsDst = None

        #update the dataObject with the the string, and update the UI
        self.sdstData.display_info()
        self.lab_pathsDstDisplay_Update()                           

    # Function for pressing the "Clear All" valid paths button
    def btn_pathsSrcActiveClear_pressed(self):
#        self.sdstData.

# TODO: Clearthe sdstData when button presse
        self.trv_pathsSrcActive_clear()
        self.statusUpdate("Source Path(s) Cleared")
        
    # Updates the pathsDstDisplay text
    def lab_pathsDstDisplay_Update(self):

        newText = ""    

        if (self.sdstData.pathsDst == None):
            newText = "Destination: invalid path"

        else:

            # If no valid paths are provided, warn the user
            if len(self.sdstData.pathsDst) == 0:
                newText = "Destination: not set"

            # If there is a vailid path, add it to the UI
            if len(self.sdstData.pathsDst) == 1:

                curPath = sdstData.pathsDst[0]
                driveSpaceReport = get_disk_space(curPath)

                curTotal = (f"{driveSpaceReport[0]    / ( 1024 ** 3 ):.2f} GB Total")
                curFree = (f"{driveSpaceReport[2]    / ( 1024 ** 3 ):.2f} GB Free")

                # [total_space, used_space, free_space]
                newText = ( curPath + "   -   " + curFree + "   " + curTotal )

        # Commit the text
        self.lab_pathsDstDisplay.config(text=newText)

    # Clear all the items from the pathsSrcActive Treeview
    def trv_pathsSrcActive_clear(self):

        # Get all item IDs in the Treeview
        item_ids = self.trv_pathsSrcActive.get_children()

        # Delete all items from the Treeview
        for item in item_ids:
            self.trv_pathsSrcActive.delete(item)
    
    # Clear all the items from the pathsDstActive Treeview
    def trv_pathsDstActive_clear(self):

        # Get all item IDs in the Treeview
        item_ids = self.trv_pathsDstActive.get_children()

        # Delete all items from the Treeview
        for item in item_ids:
            self.trv_pathsDstActive.delete(item)

    # Updates the status bar with the passed arg_text
    def statusUpdate(self, arg_text):

        self.lab_status.config(text=("Status: "+ arg_text))

    def trv_pathsSrcActive_init(self):

        # Set column headings
        self.trv_pathsSrcActive.heading("path", text="Path")
        self.trv_pathsSrcActive.heading("size", text="Size")

        # Set column widths
        self.trv_pathsSrcActive.column("path", width=450)
        self.trv_pathsSrcActive.column("size", width=110)

    # Populate the source treeview
    def trv_pathsSrcActive_populate(self):

        # Clear the tree view
        self.trv_pathsSrcActive_clear()

        # Reet list counter
        i = 0

        # Loop through the source paths, and create an entry for each one, and add it to the treeview
        for item in self.sdstData.pathsSrc:

            # start a new entry, with the path name first
            curEntry = [item]

            # Add the size calculation to the entry, if the size has been fetched
            try:
                # Try and add the size data
                try:
                    sizeNumber = round(self.sdstData.pathsSrcSpaceReport[i], 2)
                    sizeString = (str(sizeNumber) + " GB" )

                except:
                    sizeString = self.sdstData.pathsSrcSpaceReport[i]
                    pass

                curEntry.append(sizeString)

            except:
                # If it does not exist, move on
                pass

            # Add the entry to the treeview
            self.trv_pathsSrcActive.insert("", "end", values=curEntry)

            # Increment
            i += 1

    # Sets the size and columns of the destination treeview
    def trv_pathsDstActive_init(self):

        # Set column headings
        self.trv_pathsDstActive.heading("path", text="Path")
        self.trv_pathsDstActive.heading("size", text="Free Space")

        # Set column widths
        self.trv_pathsDstActive.column("path", width=450)
        self.trv_pathsDstActive.column("size", width=110)

    # Populates the destination treeview
    def trv_pathsDstActive_populate(self):

        # First clear it out
        self.trv_pathsDstActive_clear()

        # Cycle through the destination paths, get their free space, and add it to the treeview
        for item in self.sdstData.pathsDst:
            
            sizeReport = get_disk_space(item)
            sizeReportParsed = (f"{sizeReport[2] / ( 1024 ** 3 ):.2f} GB")

            newEntry = [item,sizeReportParsed]
            self.trv_pathsDstActive.insert("", "end", values=newEntry)

    def btn_pathsSrcActiveGenScript_pressed(self):
        print("-- gen script --")
        pass

    # For testing buttons
    def testFunction(self):
        
        print("Test Function Ran")

if __name__ == "__main__":
    
    #Timestamp
    print(datetime.datetime.now())

    # Create the main window
    root = tk.Tk()

    from sdst_classes import *
    sdstData = SDSTData()

    # Create an instance of the SDST_UI_Main class
    my_gui = SDST_UI_Main(root, sdstData)

    # Start the Tkinter main loop
    root.mainloop()