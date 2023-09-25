import tkinter as tk
from tkinter import ttk
from sdst_classes import *
from sdst_functions import *
from sdst_ui import *
import os

# Update the sizes on each of the copyOperations
def weighCopyOps():
	for op in sdstData.copyOperations:
		print("Calculating size: ", op.pathSrc )
		op.pathSrcSize = get_folder_size(op.pathSrc)


# function for creating all of the CopyOperationInfo objects from a list of input paths and the destination path
# the created objecs are added to the "sdstData.copyOperations" list for later access
def collectCopyOps():

	# Create a new variable for handleID
	handleID = 1 

	# create a CopyOperationInfo for each of the paths provided
	for path in sdstData.pathsSrc:

		# Create a new CopyOp, and give it a handle
		curOp = newCopyOp(path)
		curOp.handle = handleID
		handleID+=1

		# Add the newly created 
		sdstData.copyOperations.append(curOp)


# returns a new CopyOperationInfo object from the provided path
def newCopyOp(arg_path):

	# Make a new operator
	newOp 				= CopyOperationInfo()

	# Sanitize and assign the source and destination paths
	newOp.pathSrc 		= (os.path.normpath(arg_path))
	newOp.pathDstRoot 	= (os.path.normpath(sdstData.pathsDst[0]))

	# Get the source drive letter
	parts1 		= arg_path.split(":\\")
	driveletter	= parts1[0]

	# Get the source folder Name
	parts2 		= arg_path.split("\\")
	projectName = parts2[(len(parts2) - 1)]

	# Concatenate the destination path, and the robocopy operation
	newOp.pathDstFull = ( newOp.pathDstRoot + "\\" + projectName + "\\" + driveletter)
	newOp.copyOperation = ( "robocopy \""+ newOp.pathSrc + "\" \"" + newOp.pathDstFull + "\" /MIR /MT:8 /w:1 /r:2" + "\n" + "attrib -h -s -r " + "\"" + pathDstFull + "\"")

	# returns the populated object
	return newOp


# Generates the string based off of the sdstData for the copy operation, and stores it on sdstData
def generateArchiveScript(sdstData):

	# declare Vars
	newStr = ""

	# generate the string for the file
	for curOp in sdstData.copyOperations:
		#print(curOp.copyOperation)
		newStr += str(curOp.copyOperation)
		newStr += "\n"
	
	newStr += "@echo off\n"
	newStr += "echo ------------------------ Studio Stash ------------------------\n"
	newStr += "echo Studio Stash operation completed, read robocopy reports above.\n"
	newStr += "echo --------------------------------------------------------------\n"
	newStr += "pause"

	sdstData.archiveScriptString = newStr

def uiStart(sdstData):
	# Create the main window
	root = tk.Tk()

	# Create an instance of the SDST_UI_Main class
	sdst_UI_Main = SDST_UI_Main(root, sdstData)

	# Start the Tkinter main loop
	root.mainloop()

	return sdst_UI_Main

# Instantiate the data object
sdstData = SDSTData()
sdstData.display_info()


# Collect all the copyOperations
collectCopyOps()

# Measure the size of each of the copyOperations
#weighCopyOps()

##### Generate and save the .bat file for robocopy to execute ####
# generateArchiveScript(sdstData)
# bat_saveAs(sdstData.archiveScriptString)


#### Display all of the copy operations data
# for op in sdstData.copyOperations:
# 	op.display_info()

# print("------asfdasfd---------")
# print(sdstData.archiveScriptString)



# Instantiate the ui
sdstData.ui_main = uiStart(sdstData)