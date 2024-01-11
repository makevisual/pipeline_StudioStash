import tkinter as tk
from tkinter import ttk 
from sdst_functions import *
import os
import sys
import datetime
import threading
import win32com.client
import shutil 

sdstVer = [0,1,2]

class SDST_UI_Main:

    # Function for creating the UI, and laying out its 
    def __init__(self, root, sdstData):

        self.sdstData = sdstData

        # Create the main window
        self.root = root
        self.root.title("StudioStash v"+ str(sdstVer[0]) + "." + str(sdstVer[1]) + "." + str(sdstVer[2]) )

        # Set the window size (width x height)
        self.root.geometry("600x580")  # Width: 400, Height: 300
        self.root.configure(bg="#303841") 

        # Sort out the icon file for compiling
        if getattr(sys, 'frozen', False):
            # Running as a PyInstaller executable
            icon_path = os.path.join(sys._MEIPASS, 'makeIcon.ico')
        else:
            # Running as a regular Python script
            icon_path = 'makeIcon.ico'

        #icon_path = R"C:\Users\MAKE\Documents\GitHub\pipeline_StudioStash\Codebase\makeIcon.ico"
        self.root.iconbitmap(icon_path)

        # Set the style
        style = ttk.Style()
        style.configure("TLabel", background="#303841", foreground="white")  # Set label colors
        style.configure("TButton", background="#4f565e", foreground="black", height="2")  # Set button colors
        style.configure("TEntry", fieldbackground="#444444", foreground="black") 
        style.configure("TText", background="#303841", foreground="white") 

        # PathsSrc Entry
        self.lab_pathsSrc = ttk.Label(self.root, text="Source path(s) to copy:")
        self.lab_pathsSrc.place(x=10, y=10)
        self.txt_pathsSrc = tk.Text(self.root,width=50,height=2)
        self.txt_pathsSrc.place(x=10, y=30)
        self.txt_pathsSrc.configure(bg="#4f565e") 
        self.txt_pathsSrc.configure(fg="white") 
        self.btn_pathsSrcAdd = ttk.Button(self.root, text="Add", command=self.btn_pathsSrcAdd_pressed)
        self.btn_pathsSrcAdd.place(x=10, y=70)

        # PathsSrcActive Treeview
        self.lab_pathsSrcActive = ttk.Label(self.root, text="Valid source path(s):")
        self.lab_pathsSrcActive.place(x=10, y=100)
        self.trv_pathsSrcActive = ttk.Treeview(self.root, columns=("path", "size"), show="headings", height=4)
        self.trv_pathsSrcActive.place(x=10, y=120)
        self.btn_pathsSrcActiveClear = ttk.Button(self.root, text="Clear All", command=self.btn_pathsSrcActiveClear_pressed)
        self.btn_pathsSrcActiveClear.place(x=10, y=230)
        self.btn_pathsSrcActiveCheckSize = ttk.Button(self.root, text="Check Size(s)", command=lambda: threading.Thread(target=self.btn_pathsSrcActiveCheckSize_pressed).start())
        self.btn_pathsSrcActiveCheckSize.place(x=88, y=230)
        self.lab_pathsSrcActiveTotalSize = ttk.Label(self.root, text="Total Size: 0 GB")
        self.lab_pathsSrcActiveTotalSize.place(x=440, y=232)

        # And initialize it
        self.trv_pathsSrcActive_init()

        # PathsDst Entry
        self.lab_pathsDst = ttk.Label(self.root, text="Destination path(s):")
        self.lab_pathsDst.place(x=10, y=260)
        self.txt_pathsDst = tk.Entry(self.root,width=93)
        self.txt_pathsDst.place(x=10, y=280)
        self.txt_pathsDst.configure(bg="#4f565e") 
        self.txt_pathsDst.configure(fg="white") 
        self.btn_pathsDstAdd = ttk.Button(self.root, text="Add", command=self.btn_pathsDstAdd_pressed)
        self.btn_pathsDstAdd.place(x=10, y=302)
        
        # PathsDstActive Treeview
        self.lab_pathsDstActive = ttk.Label(self.root, text="Valid destination path(s):")
        self.lab_pathsDstActive.place(x=10, y=335)
        self.trv_pathsDstActive = ttk.Treeview(self.root, columns=("path", "size"), show="headings", height=2)
        self.trv_pathsDstActive.place(x=10, y=355)
        self.btn_pathsDstActiveClear = ttk.Button(self.root, text="Clear All", command=self.btn_pathsDstActiveClear_pressed)
        self.btn_pathsDstActiveClear.place(x=10, y=425)
        self.btn_pathsDstActiveCheckSize = ttk.Button(self.root, text="Check Free Space ", command=self.btn_pathsDstActiveCheckSize_pressed)
        self.btn_pathsDstActiveCheckSize.place(x=88, y=425)
        # And initialize it
        self.trv_pathsDstActive_init()

        # PathDstLinkActive
        self.lab_pathDstLink = ttk.Label(self.root, text="Shortcut path:")
        self.lab_pathDstLink.place(x=10, y=460) #280
        self.btn_pathDstLinkSet = ttk.Button(self.root, text="Set", command=self.btn_pathDstLinkSet_pressed)
        self.btn_pathDstLinkSet.place(x=10, y=480)
        self.txt_pathDstLink = tk.Entry(self.root,width=80)
        self.txt_pathDstLink.place(x=90, y=482)
        self.txt_pathDstLink.configure(bg="#4f565e") 
        self.txt_pathDstLink.configure(fg="white") 

        # PathDstLinkActive / Clear
        self.btn_pathDstLinkActiveClear = ttk.Button(self.root, text="Clear", command=self.btn_pathDstLinkActiveClear_pressed)
        self.btn_pathDstLinkActiveClear.place(x=10, y=505)
        self.lab_pathDstLinkActive = ttk.Label(self.root, text="No Shortcut Path Set")
        self.lab_pathDstLinkActive.place(x=90, y=508) #280

        # CopyOperationType
        options = ["select copy method","additive copy", "mirror copy"]
        self.sdstData.copyMethod = tk.StringVar(root)
        self.sdstData.copyMethod.set(options[0])
        self.ddl_copyMethod = ttk.OptionMenu(self.root, self.sdstData.copyMethod, *options, command=self.ddl_copyMethod_pressed)
        self.ddl_copyMethod.place(x=238, y=531)
        self.ddl_copyMethod.config(width=20)

        # Generate button
        self.btn_GenScript_pressed = ttk.Button(self.root, text="  Generate Batch Archive Script  ", command=self.btn_GenScript_pressed)
        self.btn_GenScript_pressed.place(x=395, y=530) #500
        self.btn_GenScript_pressed.config(state="disabled")

        # status bar
        self.lab_status = ttk.Label(self.root, text=":")
        self.lab_status.place(x=10, y=555) #530
        self.statusUpdate("Ready")

        # buttons for debug and testing
        self.btn_injectData = ttk.Button(self.root, text="  inject temp data  ", command=self.injectData)
        self.btn_injectData.place(x=200, y=10)
        self.btn_displayData = ttk.Button(self.root, text="  print data  ", command=self.sdstDataDisplay)
        self.btn_displayData.place(x=300, y=10)

        self.pathDstLink_update()

    # Function to set the copy method, when selected from the dropdown
    def ddl_copyMethod_pressed(self, *args):

        self.sdstData.copyMethodStr = self.sdstData.copyMethod.get()

        if self.sdstData.copyMethodStr == "mirror copy":
            self.statusUpdate("'Mirror Copy' Selected, WARNING! This will remove destination files and directories absent in source.")

        if self.sdstData.copyMethodStr == "additive copy":
            self.statusUpdate("'Additive Copy' Selected, this will append to all destination files and directories.")

        self.btn_GenScript_pressed.config(state="enabled")

    # Function to update the UI items, if the destination path is valid or not
    def pathDstLink_update(self):

        # Test if the path has been set
        if self.sdstData.pathDstLink != None:

        # Test if the path exists
            if os.path.exists(self.sdstData.pathDstLink):

                # Update the shortcut path display
                self.lab_pathDstLinkActive.config(text=(self.sdstData.pathDstLink))

                # Update the status
                self.statusUpdate("Shortcut Path Set")

            # If the path does not exist
            else:

                # Nullify the data
                self.sdstData.pathDstLink = None

        # If the destination path is null
        if self.sdstData.pathDstLink == None:

            # Update the config file
            self.sdstData.config.set('Settings', 'shortcutpath', "None")

            # Save the changes back to the file
            with open(self.sdstData.configFile, 'w') as configfile:
                self.sdstData.config.write(configfile)

            # Update UI with invailid path warning
            self.statusUpdate("No Vailid Shortcut Path Set") 
            self.lab_pathDstLinkActive.config(text=("No Shortcut Path Set"))

    # Function for when the clear shortcut path is pressed
    def btn_pathDstLinkActiveClear_pressed(self):

        # Nullify the data
        self.sdstData.pathDstLink = None

        # Update all relevant UI items
        self.pathDstLink_update()

    # Function for when the set shortcut path button is pressed
    def btn_pathDstLinkSet_pressed(self):
        self.sdstData.input_pathDstLink = self.txt_pathDstLink.get()
        # print ("--- Raw SRC Input --- ", self.sdstData.input_pathDstLink)

        # Sanatize the string
        cleaned_path = self.sdstData.input_pathDstLink.replace("\"", "")   # Takes away Quotes
        cleaned_path = cleaned_path.replace("/", "\\")                  # Sets slash directions
        cleaned_path = cleaned_path.replace(",", "")                    # takes away commas

        # Run the filepath through a normalizer for the operating system
        cleaned_path = os.path.normpath(cleaned_path)

        # Test if path exists 
        if os.path.exists(cleaned_path):
            
            # Update the data object
            self.sdstData.pathDstLink = cleaned_path

            # Update the config file
            self.sdstData.config.set('Settings', 'shortcutpath', self.sdstData.pathDstLink)

            # Save the changes back to the file
            with open(self.sdstData.configFile, 'w') as configfile:
                self.sdstData.config.write(configfile)

        # If the path is invalid, nullify the data
        else:
            self.sdstData.pathDstLink = None

        # Update the UI items related to the shortcut link
        self.pathDstLink_update()

        sdstData.display_info()

    # Function for button press that sanitizes the input text and adds it to the sdstData.pathsSrc if they exist
    def btn_pathsSrcAdd_pressed(self):

        # Get the text string from the UI
        self.sdstData.input_pathsSrc = self.txt_pathsSrc.get("1.0","end-1c")
        # print ("--- Raw SRC Input --- ", self.sdstData.input_pathsSrc)

        # Get the input data to begin working with it
        filepathsraw = self.sdstData.input_pathsSrc

        # clean the string up
        filepathsclean = self.sdstData.input_pathsSrc.replace("\"", "")     # Takes away Quotes
        filepathsclean = filepathsclean.replace("/", "\\")                  # Sets slash directions
        filepathsclean = filepathsclean.replace(",", "\n")                  # turns commas into a new line

        # Split it into a list for each line in the string
        filepathscleansplit = filepathsclean.split('\n')
        
        # Remove any leading or trailing whitespaces from each file path, and removes empty lines
        filepaths = [path.strip() for path in filepathscleansplit if path.strip()]

        # Run all of the filepaths through a normalizer for the operating system
        for filepath in filepaths:
            filepath = os.path.normpath(filepath)

        # Create a new empty list for storing valid filepaths
        validFilepaths = []

        # Check the path if they are valid
        for curPath in filepaths:

            # Checks if the filepath is a valid path
            if os.path.exists(curPath):

                # Adds the valid path to the list
                validFilepaths.append(curPath)

        # Adds the valid filepaths to the paths Src list
        self.sdstData.pathsSrc += validFilepaths

        # Remove any duplicates from the list
        self.sdstData.pathsSrc = list(set(self.sdstData.pathsSrc))

        # Update the UI with the new items
        self.trv_pathsSrcActive_populate()

    # Function for updating the label for the total source path size from the calculated space reports
    def lab_pathsSrcActiveTotalSize_update(self):

        # pathsSrcSpaceReport
        sizeFloat = 0

        # Loop through the space reports
        for num in self.sdstData.pathsSrcSpaceReport:

            # If it is a float
            if isinstance(num, float):

                # Add it to the tally
                sizeFloat += num

        # Round the number off
        sizeFloat = round(sizeFloat, 2)

        # Upeate the label with the total size
        self.lab_pathsSrcActiveTotalSize.config(text=("Total Size: "+ (str(sizeFloat)) + " GB"))

    # Prints data object to the console
    def sdstDataDisplay(self):

        self.sdstData.display_info()

        self.statusUpdate("Displaying sdstData")

    # Injects testing data into sdstData
    def injectData(self):

        # Temp Data
        self.sdstData.pathsSrc=["C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks", "C:\\\\test\\\\mockProjects\\\\RepoRetimeRoughKey"]
        # self.sdstData.pathsSrc=["C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks", "C:\\\\test\\\\mockProjects\\\\RepoRetimeRoughKey","W:\\\\Projects\\\\AOT - Teaser"]
        # self.sdstData.pathsSrc=["C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks", "C:\\\\test\\\\mockProjects\\\\RepoRetimeRoughKey","W:\\\\Projects\\\\AOT - Teaser","X:\\\\Projects\\\\Days","X:\\\\Projects\\\\CHS - CorpRefresh Video","X:\\\\Projects\\\\F22 HW City - Action Spiral Playset"]
        # self.sdstData.pathsSrc=["C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks", "C:\\\\test\\\\mockProjects\\\\RepoRetimeRoughKey","W:\\\\Projects\\\\AOT - Teaser","X:\\\\Projects\\\\Callaway - Precision Technology","X:\\\\Projects\\\\Bridgestone - B-Seal","X:\\\\Projects\\\\CMDA"]
        self.sdstData.pathsDst=["C:\\test\\mockArchive"]
        self.sdstData.pathDstLink= "C:\\test\\shortcutPaths"

        # populate the tree views
        self.trv_pathsSrcActive_populate()
        self.trv_pathsDstActive_populate()

        # Run the copy operation collection
        self.collectCopyOps()

        # Update the status
        self.statusUpdate("Test Data Injected")

    # !!! --- thread for calculating the size of source paths, and returning them to the UI
    def btn_pathsSrcActiveCheckSize_pressed(self):

        # Clear out reports, and fill them with "calculating..."
        spaceReports = []                   # New list, that is clean
        self.pathsSrcSpaceReport = []       # Clean out the stored list as well
        entryText = "Calculating..."        # Dummy text to be in place until overwritten
        self.pathsSrcSpaceReportRun = True  # PoisonPill for terminating early

        # Fill the space reports with placeholder entry text, until it can be overwritten
        for j in range(len(sdstData.pathsSrc)):
            spaceReports.append(entryText)

        # Update the list view with the 'calculating' list
        self.btn_pathsSrcActiveCheckSize_pressed_updateSize(spaceReports)

        # For each of the paths find the size
        i=0 # Loop counter
        for curPath in self.sdstData.pathsSrc:

            # Before beginning any new checks, exit the operation if the killswitch has been flipped
            if self.pathsSrcSpaceReportRun == False:

                break

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
            self.lab_pathsSrcActiveTotalSize_update()

            # Increment
            i+=1

        self.btn_pathsSrcActiveCheckSize_pressed_statusComplete()

    # called by btn_pathsSrcActiveCheckSize_pressed to update the status bar
    def btn_pathsSrcActiveCheckSize_pressed_statusUpdate(self,curPath):

        self.statusUpdate("Calculating Directory Size - "+ str(curPath) + "...")

    # called by btn_pathsSrcActiveCheckSize_pressed to update the status bar
    def btn_pathsSrcActiveCheckSize_pressed_statusComplete(self):

        self.statusUpdate("Calculating Directory Size complete")

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
        self.sdstData.input_pathsDst = self.txt_pathsDst.get()
        # print ("--- Raw DST Input --- ", self.sdstData.input_pathsDst)

        # Sanatize the string
        cleaned_path = self.sdstData.input_pathsDst.replace("\"", "")   # Takes away Quotes
        cleaned_path = cleaned_path.replace("/", "\\")                  # Sets slash directions
        cleaned_path = cleaned_path.replace(",", "")                    # takes away commas

        # Run the filepath through a normalizer for the operating system
        cleaned_path = os.path.normpath(cleaned_path)

        # Test if path exists 
        if os.path.exists(cleaned_path):
            
            # Only commits the destination if it is a valid path
            self.sdstData.pathsDst.append(cleaned_path)

            # remove duplicate items from the list, if any were added
            self.sdstData.pathsDst = list(set(self.sdstData.pathsDst))

            # update the dataObject with the the string, and update the UI
            self.sdstData.display_info()
            self.trv_pathsDstActive_populate()

            # Update the log
            self.statusUpdate("Path Added")

        # If invalid, clear any existing paths out
        else: 
            # Update the log
            self.statusUpdate("Invalid Destination Path")
               
    # Function for pressing the "Clear All" valid paths button
    def btn_pathsSrcActiveClear_pressed(self):

        # Set the killswitch to stop the size calculation thread
        self.pathsSrcSpaceReportRun = False
        # Clear out the data object
        self.sdstData.pathsSrc = []
        # Clear out the treeview
        self.trv_pathsSrcActive_clear()
        # Update the log
        self.statusUpdate("Source Path(s) Cleared")
        
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

    # Sets the columns headding and size of the Paths Src Treeview
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

    # function for creating all of the CopyOperationInfo objects and storing it in "sdstData.copyOperations"
    def collectCopyOps(self):

        # Create a new variable for handleID
        self.sdstData.copyOperations = []
        handleID = 1 

        # Loop for each of the destinations
        for pathDst in self.sdstData.pathsDst:

            # create a CopyOperationInfo for each of the src paths provided
            for pathSrc in self.sdstData.pathsSrc:

                # Verify paths are sanatized for the OS
                pathSrc = os.path.normpath(pathSrc)
                pathDst = os.path.normpath(pathDst)

                # Create a new CopyOp, and populate it
                curOp = CopyOperationInfo()
                curOp.populate(pathSrc, pathDst, handleID)

                # Increment the handle
                handleID+=1

                # Add the newly created 
                self.sdstData.copyOperations.append(curOp)

    # Create a .lnk file from passed arguments
    def generateShortcut(self, arg_target, arg_shortcut):

        # Create a shortcut object
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(arg_shortcut)

        # Set the target path for the shortcut
        shortcut.TargetPath = arg_target

        # Save the shortcut  
        shortcut.Save()

    # Generate the interrogate script .ps1 command
    def generateInterrogateScript(self):

        # declare Vars
        newStr = ""
        newStr += "@echo off\n"
        newStr += "\n"
        newStr += "#### INPUTS\n"
        newStr += "\n"


        # TODO: Change this to be a dynamic list

        newStr += "# List of directories to analyze"
        newStr += "$directories_dst = @(\n"
        newStr += "   \"C:\\test\\mockProjects\\Nuke-HeiroConform_Rubiks\",\n"
        newStr += "   \"C:\\test\\mockProjects\\RepoRetimeRoughKey\",\n"
        newStr += "   \"C:\\test\\mockProjects\\RiggingSkinFixAndPointCache\",\n"
        newStr += "   \"X:\\Projects\\CrunchyRoll - Frieren\"\n"
        newStr += ")"
        newStr += "\n"


        # TODO: Change this to be a dynamic list

        newStr += "# List of directories to analyze\n"
        newStr += "$directories_src = @(\n"
        newStr += "   \"C:\\test\\mockProjects\\Nuke-HeiroConform_Rubiks\",\n"
        newStr += "   \"C:\\test\\mockProjects\\RepoRetimeRoughKey\",\n"
        newStr += "   \"C:\\test\\mockProjects\\RiggingSkinFixAndPointCache\",\n"
        newStr += "   \"X:\\Projects\\CrunchyRoll - Frieren\"\n"
        newStr += ")"


        newStr += "\n"
        newStr += "\n"
        newStr += "#### DST"
        newStr += "\n"
        newStr += "# Initialize counters\n"
        newStr += "$totalFiles_dst = 0\n"
        newStr += "$totalSize_dst = 0\n"
        newStr += "\n"
        newStr += "# Display prompt\n"
        newStr += "Write-Host \"- DESTINATION:\n"
        newStr += "Write-Host \"   - calculating...\n"
        newStr += "\n"
        newStr += "# Iterate through each directory\n"
        newStr += "foreach ($directory in $directories_dst) {\n"
        newStr += "    # Get all files in the current directory\n"
        newStr += "    $files = Get-ChildItem -Path $directory -File -Recurse\n"
        newStr += "\n"
        newStr += "    # Update counters\n"
        newStr += "    $totalFiles_dst += $files.Count\n"
        newStr += "    $totalSize_dst += $files | Measure-Object -Property Length -Sum | Select-Object -ExpandProperty Sum\n"
        newStr += "}\n"
        newStr += "\n"
        newStr += "# Convert total size to human-readable format\n"
        newStr += "$totalSize_dstInKB = $totalSize_dst / 1KB\n"
        newStr += "$totalSize_dstInMB = $totalSize_dst / 1MB\n"
        newStr += "$totalSize_dstInGB = $totalSize_dst / 1GB\n"
        newStr += "$totalSize_dstInTB = $totalSize_dst / 1TB\n"
        newStr += "\n"
        newStr += "# Display results\n"
        newStr += "Write-Host \"   - Total Number of Files: $totalFiles_dst\"\n"
        newStr += "Write-Host \"   - Total File Size: $($totalSize_dst) bytes ( $totalSize_dstInGB GB, $totalSize_dstInTB TB )\"\n"
        newStr += "\n"
        newStr += "\n"
        newStr += "##### SRC\n"
        newStr += "\n"
        newStr += "# Initialize counters\n"
        newStr += "$totalFiles_src = 0\n"
        newStr += "$totalSize_src = 0\n"
        newStr += "\n"
        newStr += "# Display prompt\n"
        newStr += "Write-Host \"- SOURCE:\"\n"
        newStr += "Write-Host \"   - calculating...\"\n"
        newStr += "\n"
        newStr += "# Iterate through each directory\n"
        newStr += "foreach ($directory in $directories_src) {\n"
        newStr += "    # Get all files in the current directory\n"
        newStr += "    $files = Get-ChildItem -Path $directory -File -Recurse\n"
        newStr += "\n"
        newStr += "    # Update counters\n"
        newStr += "    $totalFiles_src += $files.Count\n"
        newStr += "    $totalSize_src += $files | Measure-Object -Property Length -Sum | Select-Object -ExpandProperty Sum\n"
        newStr += "}\n"
        newStr += "\n"
        newStr += "# Convert total size to human-readable format\n"
        newStr += "$totalSize_srcInKB = $totalSize_src / 1KB\n"
        newStr += "$totalSize_srcInMB = $totalSize_src / 1MB\n"
        newStr += "$totalSize_srcInGB = $totalSize_src / 1GB\n"
        newStr += "$totalSize_srcInTB = $totalSize_src / 1TB\n"
        newStr += "\n"
        newStr += "# Display results\n"
        newStr += "Write-Host \"   - Total Number of Files: $totalFiles_src\"\n"
        newStr += "Write-Host \"   - Total File Size: $($totalSize_src) bytes ( $totalSize_srcInGB GB, $totalSize_srcInTB TB )\"\n"
        newStr += "\n"
        newStr += "\n"
        newStr += "##### RESULTS\n"
        newStr += "# Display prompt\n"
        newStr += "Write-Host \"- RESULTS:\"\n"
        newStr += "\n"
        newStr += "# Compare total file sizes\n"
        newStr += "if ($totalSize_src -eq $totalSize_dst) {\n"
        newStr += "    Write-Host \"   - Source and Destination file size match.\"\n"
        newStr += "} else {\n"
        newStr += "    Write-Host \"   - WARNING! - Source and Destination file size DO NOT match.\"\n"
        newStr += "}\n"
        newStr += "\n"
        newStr += "# Compare total file counts\n"
        newStr += "if ($totalFiles_src -eq $totalFiles_dst) {\n"
        newStr += "    Write-Host \"   - Source and Destination file count match.\"\n"
        newStr += "} else {\n"
        newStr += "    Write-Host \"   - WARNING! - Source and Destination file count DO NOT match.\"\n"
        newStr += "}\n"
        newStr += "\n"

        # Store the newly generated script string
        self.sdstData.interrogateScriptString = newStr

    # Generate the archive script .bat command
    def generateArchiveScript(self):

        # declare Vars
        newStr = ""

        newStr += "@echo off\n"
        newStr += "echo Starting the operation...\n"
        newStr += "setlocal enabledelayedexpansion\n"
        newStr += "for /f \"tokens=1-4 delims=:.,\" %%a in (\"%time%\") do (\n"
        newStr += "    set /a \"start_time=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100\"\n"
        newStr += ")\n"
        newStr += "\n"
        newStr += "\n"

        # generate the string for the file
        for curOp in self.sdstData.copyOperations:
            #print(curOp.copyOperation)
            newStr += str(curOp.copyOperation)

            if self.sdstData.copyMethodStr == 'additive copy':
                newStr += str(curOp.copyOperationAdd)

            if self.sdstData.copyMethodStr == 'mirror copy':
                newStr += str(curOp.copyOperationOver)

            newStr += "\n"
            newStr += "\n"
        
        # Add footer
        newStr += "\n"
        newStr += "\n"
        newStr += "for /f \"tokens=1-4 delims=:.,\" %%a in (\"%time%\") do (\n"
        newStr += "    set /a \"end_time=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100\"\n"
        newStr += ")\n"
        newStr += "\n"
        newStr += "set /a \"duration=end_time - start_time\"\n"
        newStr += "set /a \"seconds=duration / 100\"\n"
        newStr += "set /a \"milliseconds=duration %% 100\"\n"
        newStr += "set /a \"minutes=seconds / 60\"\n"
        newStr += "set /a \"seconds=seconds %% 60\"\n"
        newStr += "set /a \"hours=duration / 3600000\""
        newStr += "\n"
        newStr += "echo ------------------------ Studio Stash ------------------------\n"
        newStr += "echo Studio Stash operation completed, read robocopy reports above.\n"
        newStr += ("echo " + str(len(self.sdstData.copyOperations)) + " folders were processed. \n")
        newStr += "echo The operation took !hours! hours, !minutes! minutes and !seconds! seconds and !milliseconds! milliseconds.\n"
        newStr += "echo --------------------------------------------------------------\n"

        self.sdstData.archiveScriptString = newStr

    # Generate the archive script .bat command
    def generateDeleteScript(self):

        # declare Vars
        newStr = ""

        newStr += "@echo off\n"




        self.sdstData.deleteScriptString = newStr

    # Function for creating all the shortcut links, from the data object
    # NOTE - The destination of the shortcut must exist for windows to create a link
    # A directory will be made if one does not exist, to link to.
    def generateShortcutLinks(self):

        # Test if the shortcut directory path exists
            if os.path.exists(self.sdstData.pathDstLink):
                
                # for each of the operations, create a shortcut
                for curOp in sdstData.copyOperations:

                    # Make the folder for the shortcut target, if one is not there already.
                    if os.path.exists(curOp.pathDstFull):
                        pass 
                    else:
                        os.makedirs(curOp.pathDstFull)

                    # Create a new timestamp, for folder naming
                    now = datetime.datetime.now()
                    curTimeStamp = ( str(now.year) + "_" + str(now.month) + "_" + str(now.day) )

                    # Generate the full shortcut path
                    shortcutLinkPath = (self.sdstData.pathDstLink + "\\" + curOp.projectName +"__" + curTimeStamp + ".lnk" )

                    # Create the shortcuts
                    self.generateShortcut(curOp.pathDstFull, shortcutLinkPath)

    def generateShortcutLinksCleanup(self):
        # Test if the shortcut directory path exists
            if os.path.exists(self.sdstData.pathDstLink):
                
                # for each of the operations, create a shortcut
                for curOp in sdstData.copyOperations:

                    # Test if the folder is less than 10 kb, and delete if true
                    if get_folder_size(curOp.pathDstProject) <= 10:
                        shutil.rmtree(curOp.pathDstProject)

    # Main export button pressed
    def btn_GenScript_pressed(self):
        
        # Collect the copy operations
        self.collectCopyOps()
        
        # Display the copy operations info
        for op in self.sdstData.copyOperations:
            op.display_info()

        # generate archive script
        self.generateArchiveScript()

        # generate interrogate script
        self.generateInterrogateScript()

        # generate interrogate script
        self.generateDeleteScript()

        # generate shortcut links
        self.generateShortcutLinks()

        # remove any temporary directories made for the shortcut generation
        self.generateShortcutLinksCleanup()

        # update status        
        self.statusUpdate(str(len(self.sdstData.copyOperations)) + " Copy operations generated " )




        # TODO - Change this to multiple files to be exported simutaneusly 
        # Generate the .bat file
        #bat_saveAs(self.sdstData.archiveScriptString)
        exportScripts( self.sdstData.archiveScriptString, self.sdstData.interrogateScriptString, self.sdstData.deleteScriptString )





    # For testing buttons
    def testFunction(self):
        
        print("Test Function Ran")
        self.statusUpdate(" Test Function Ran " )

#if __name__ == "__main__":
#   pass
    
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