@echo off
setlocal enabledelayedexpansion

:: Define the target and shortcut names
set "targetPath=C:\Windows\System32\"
set "shortcutName=NotepadShortcut1"

:: Define the working directory if needed
set "workingDirectory=C:\Path\To\Working\Directory"

:: Specify the desktop directory
set "desktopDir=%userprofile%\Desktop"

:: Create the shortcut file content
(
    echo [InternetShortcut]
    echo URL=file://!targetPath!
    if defined workingDirectory (
        echo WorkingDirectory=!workingDirectory!
    )
) > "%desktopDir%\!shortcutName!.url"

:: Launch Explorer to refresh the desktop
start /B explorer.exe


pause
:: Exit the batch script
exit