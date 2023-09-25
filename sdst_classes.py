import tkinter as tk
from tkinter import ttk
import os

# Main data class for holding all the data, and data objects
class SDSTData:
    def __init__(self, sdstVer=[0,0,1], input_pathsSrc=None, input_pathsDst=None, pathsSrc=[], pathsSrcSpaceReport=[], pathsSrcSpaceReportRun=True, pathsDst=[], pathsDstSpaceReport=[], copyOperations=[], archiveScriptString="", ui_main=None):
        self.input_pathsSrc         = input_pathsSrc
        self.input_pathsDst         = input_pathsDst
        self.pathsSrc               = pathsSrc
        self.pathsSrcSpaceReport    = pathsSrcSpaceReport
        self.pathsSrcSpaceReportRun = pathsSrcSpaceReportRun
        self.pathsDst               = pathsDst
        self.copyOperations         = copyOperations
        self.archiveScriptString    = archiveScriptString
        self.ui_main                = ui_main


    def display_info(self):
        print(f"input_pathsSrc:         {self.input_pathsSrc}")
        print(f"input_pathsDst:         {self.input_pathsDst}")
        print(f"pathsSrc:               {self.pathsSrc}")
        print(f"pathsSrcSpaceReport:    {self.pathsSrcSpaceReport}")
        print(f"pathsSrcSpaceReportRun: {self.pathsSrcSpaceReportRun}")
        print(f"pathsDst:               {self.pathsDst}")
        print(f"copyOperations:         {self.copyOperations}")
        print(f"archiveScriptString:    {self.archiveScriptString}")
        print(f"ui_main:                {self.ui_main}")

# class for one copy operation
class CopyOperationInfo:
    def __init__(self, handle=None, pathSrc=None, pathSrcSize=None, pathDstRoot=None, pathDstFull=None, copyOperation=None):
        self.handle         = handle
        self.pathSrc        = pathSrc
        self.pathSrcSize    = pathSrcSize
        self.pathDstRoot    = pathDstRoot
        self.pathDstFull    = pathDstFull
        self.copyOperation  = copyOperation

    # Prints the available information
    def display_info(self):
        print(f"handle:         {self.handle}")
        print(f"pathSrc:        {self.pathSrc}")
        print(f"pathSrcSize:    {self.pathSrcSize}")
        print(f"pathDstRoot:    {self.pathDstRoot}")
        print(f"pathDstFull:    {self.pathDstFull}")
        print(f"copyOperation:  {self.copyOperation}")

    def populate(self, arg_pathSrc="", arg_pathDst="",arg_handle=None):

        # Sanitize and assign the source and destination paths
        self.pathSrc       = arg_pathSrc
        self.pathDstRoot   = arg_pathDst

        # self.pathSrc       = (os.path.normpath(arg_pathSrc))
        # self.pathDstRoot   = (os.path.normpath(arg_pathDst))

        # Get the source drive letter
        parts1      = self.pathSrc.split(":\\")
        driveletter = parts1[0]

        # Get the source folder Name
        parts2      = self.pathSrc.split("\\")
        projectName = parts2[(len(parts2) - 1)]

        # Concatenate the destination path, and the robocopy operation
        self.pathDstFull = ( self.pathDstRoot + "\\" + projectName + "\\" + driveletter)
        self.copyOperation = ( "robocopy \""+ self.pathSrc + "\" \"" + self.pathDstFull + "\" /MIR /MT:8 /w:1 /r:2" + "\n" + "attrib -h -s -r " + "\"" + self.pathDstFull + "\"")

        # returns the populated object
        return self

#        pass


if __name__ == "__main__":
    
    opInfo = CopyOperationInfo()
    opInfo.populate("C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks","C:\\test\\mockArchive")
    opInfo.display_info()
    # sdstData = SDSTData()
    # sdstData.display_info()