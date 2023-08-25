import tkinter as tk
from tkinter import ttk
from sdst_classes import *
from sdst_functions import *
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
	newOp.copyOperation = ( "robocopy "+ newOp.pathSrc + " " + newOp.pathDstFull + " /E /COPYALL /R:3 /W:1 /MT:32" )

	# returns the populated object
	return newOp

sdstData = SDSTData()

# generate some fake input data
#sdstData.pathsSrc=[R"C:\test\mockProjects\Nuke-HeiroConform_Rubiks", R"C:\test\mockProjects\RepoRetimeRoughKey", R"W:\Projects\BraveHurts"]
sdstData.pathsSrc=[R"C:\test\mockProjects\Nuke-HeiroConform_Rubiks", R"C:\test\mockProjects\RepoRetimeRoughKey"]
sdstData.pathsDst=[R"C:\test\mockArchive"]



collectCopyOps()
weighCopyOps()

# create and display the info of the copy operation
# curOp = newCopyOp(sdstData.pathsSrc[1])
# curOp.pathSrcSize = get_folder_size(sdstData.pathsSrc[1])

for op in sdstData.copyOperations:
	op.display_info()