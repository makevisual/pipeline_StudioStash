import tkinter as tk
from tkinter import ttk
import os
import configparser

# Main data class for holding all the data, and data objects
class SDSTData:
    def __init__(self, sdstVer=[0,0,1], input_pathsSrc=None, input_pathsDst=None, input_pathDstLink=None, pathDstLink=None, pathsSrc=[], pathsSrcSpaceReport=[], pathsSrcSpaceReportRun=True, pathsDst=[], pathsDstSpaceReport=[], copyOperations=[], archiveScriptString="", ui_main=None, configFile=None, config=None):
        self.input_pathsSrc         = input_pathsSrc
        self.input_pathsDst         = input_pathsDst
        self.input_pathDstLink      = input_pathDstLink
        self.pathsSrc               = pathsSrc
        self.pathsSrcSpaceReport    = pathsSrcSpaceReport
        self.pathsSrcSpaceReportRun = pathsSrcSpaceReportRun
        self.pathsDst               = pathsDst
        self.pathDstLink            = pathDstLink
        self.copyOperations         = copyOperations
        self.archiveScriptString    = archiveScriptString
        self.ui_main                = ui_main
        self.configFile             = configFile 
        self.config                 = config

        self.getConfigFile()
        self.loadPropsFromConfig()

    # Prints the available information
    def display_info(self):
        print(f"input_pathsSrc:         {self.input_pathsSrc}")
        print(f"input_pathsDst:         {self.input_pathsDst}")
        print(f"input_pathDstLink:      {self.input_pathDstLink}")
        print(f"pathsSrc:               {self.pathsSrc}")
        print(f"pathsSrcSpaceReport:    {self.pathsSrcSpaceReport}")
        print(f"pathsSrcSpaceReportRun: {self.pathsSrcSpaceReportRun}")
        print(f"pathsDst:               {self.pathsDst}")
        print(f"pathDstLink:            {self.pathDstLink}")
        print(f"copyOperations:         {self.copyOperations}")
        print(f"archiveScriptString:    {self.archiveScriptString}")
        print(f"ui_main:                {self.ui_main}")
        print(f"configFile:             {self.configFile}")
        print(f"config:             {self.config}")

    # Create a new config file
    def createConfigFile(self):

        # Create a new configparser object
        config = configparser.ConfigParser()

        # Add sections and options
        config.add_section('Settings')
        config.set('Settings', 'ShortcutPath', 'None')

        # Get the path to the user's AppData\Roaming folder
        appdata_folder = os.getenv('APPDATA')

        # Specify the path to the configuration file
        config_file_path = os.path.join(appdata_folder, 'StudioStash', 'config.ini')

        # Ensure the directory exists
        os.makedirs(os.path.dirname(config_file_path), exist_ok=True)

        # Write the configuration to the file
        with open(config_file_path, 'w') as configfile:
            config.write(configfile)
     
    # Retrieve and apply the stored data to the data object
    def loadPropsFromConfig(self):

        # Create a ConfigParser object
        config = configparser.ConfigParser()

        # Read the INI file
        config.read(self.configFile)

        # Access properties in the INI file
        self.pathDstLink = config.get('Settings', 'shortcutpath')

        # Print the values
        # print(f"shortcutpath: {self.pathDstLink}")

    # Get the path of the config file, call createConfigFile() if no config file is found
    def getConfigFile(self):

        # Get the path to the user's AppData\Roaming folder
        appdata_folder = os.getenv('APPDATA')

        # Specify the path to the configuration file
        config_file_path = os.path.join(appdata_folder, 'StudioStash', 'config.ini')

        # Assign the correct config file path to the data object
        self.configFile = config_file_path

        # If there is no cofig file, create an empty one
        if os.path.exists(self.configFile):
            pass
        else:
            self.createConfigFile()

        # instantiate the config to the data object
        config = configparser.ConfigParser()
        config.read(self.configFile)

        self.config = config

# class for one copy operation
class CopyOperationInfo:
    def __init__(self, handle=None, projectName=None, pathSrc=None, pathSrcSize=None, pathDstRoot=None, pathDstProject=None, pathDstFull=None, copyOperation=None):
        self.handle         = handle
        self.pathSrc        = pathSrc
        self.pathSrcSize    = pathSrcSize
        self.pathDstRoot    = pathDstRoot
        self.pathDstFull    = pathDstFull
        self.copyOperation  = copyOperation

    # Prints the available information
    def display_info(self):
        print(f"handle:             {self.handle}")
        print(f"projectName:        {self.projectName}")
        print(f"pathSrc:            {self.pathSrc}")
        print(f"pathSrcSize:        {self.pathSrcSize}")
        print(f"pathDstRoot:        {self.pathDstRoot}")
        print(f"pathDstProject:     {self.pathDstProject}")
        print(f"pathDstFull:        {self.pathDstFull}")
        print(f"copyOperation:      {self.copyOperation}")

    # populates self with the copy operation details
    def populate(self, arg_pathSrc="", arg_pathDst="",arg_handle=None):

        # Sanitize and assign the source and destination paths
        self.pathSrc       = arg_pathSrc
        self.pathDstRoot   = arg_pathDst
        self.arg_handle    = arg_handle

        # Get the source drive letter
        parts1      = self.pathSrc.split(":\\")
        driveletter = parts1[0]

        # Get the source folder Name
        parts2      = self.pathSrc.split("\\")
        projectName = parts2[(len(parts2) - 1)]

        # Store the parts for later usage
        self.projectName = projectName
        self.pathDstProject = ( self.pathDstRoot +"\\" +self.projectName)

        # Concatenate the destination path, and the robocopy operation
        self.pathDstFull = ( self.pathDstRoot + "\\" + projectName + "\\" + driveletter)
        self.copyOperation = ( "robocopy \""+ self.pathSrc + "\" \"" + self.pathDstFull + "\" /MIR /MT:8 /w:1 /r:2" + "\n" + "attrib -h -s -r " + "\"" + self.pathDstFull + "\"")

        # returns the populated object
        return self

# Debug / temp data
if __name__ == "__main__":
    
    # opInfo = CopyOperationInfo()
    # opInfo.populate("C:\\\\test\\\\mockProjects\\Nuke-HeiroConform_Rubiks","C:\\test\\mockArchive")
    # opInfo.display_info()

    sdstData = SDSTData()
    sdstData.display_info()