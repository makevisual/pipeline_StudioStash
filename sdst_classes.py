# Main data class for holding all the data, and data objects
class SDSTData:
    def __init__(self, sdstVer=[0,0,1], input_pathsSrc=None, input_pathsDst=None, pathsSrc=[], pathsDst=[], copyOperations=[], archiveScriptString="", ui_main=None):
        self.input_pathsSrc         = input_pathsSrc
        self.input_pathsDst         = input_pathsDst
        self.pathsSrc               = pathsSrc
        self.pathsDst               = pathsDst
        self.copyOperations         = copyOperations
        self.archiveScriptString    = archiveScriptString
        self.ui_main                = ui_main

    def display_info(self):
        print(f"input_pathsSrc:         {self.input_pathsSrc}")
        print(f"input_pathsDst:         {self.input_pathsDst}")
        print(f"pathsSrc:               {self.pathsSrc}")
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

    def display_info(self):
        print(f"handle:         {self.handle}")
        print(f"pathSrc:        {self.pathSrc}")
        print(f"pathSrcSize:    {self.pathSrcSize}")
        print(f"pathDstRoot:    {self.pathDstRoot}")
        print(f"pathDstFull:    {self.pathDstFull}")
        print(f"copyOperation:  {self.copyOperation}")


# opInfo = CopyOperationInfo()
# opInfo.display_info()
# sdstData = SDSTData()
# sdstData.display_info()