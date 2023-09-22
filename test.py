    # thread for calculating the size of source paths, and returning them to the UI
    def btn_pathsSrcActiveCheckSize_pressed(self):

        # Clear out reports
        spaceReports = []

        # For each of the paths find the size
        for curPath in self.sdstData.pathsSrc:
            
            sizeCellText = "calculating..."
            spaceReports.append(sizeCellText)

            # Update the UI with the path being operated on
            self.btn_pathsSrcActiveCheckSize_pressed_statusUpdate( curPath )
            self.btn_pathsSrcActiveCheckSize_pressed_updateSize(spaceReports)            

            # Start Calculating the size
            # self.curPathSpaceReport = get_folder_size(curPath)
            curPathSpaceReport = get_folder_size(curPath)

            # Turn it into Gigabytes
            size_kb = curPathSpaceReport / 1024
            size_mb = size_kb / 1024
            size_gb = size_mb / 1024

            # Add the size to the space reports list
            sizeCellText = size_gb

            # Return the space reports to the main thread
            self.btn_pathsSrcActiveCheckSize_pressed_updateSize(spaceReports)       