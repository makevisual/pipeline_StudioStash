@echo off
setlocal enabledelayedexpansion
set "directoriesToDelete[0]=C:\test\mockProjects\RepoRetimeRoughKey - Copy"
set "directoriesToDelete[1]=C:\test\mockProjects\Nuke-HeiroConform Rubiks - Copy"
set "directoriesToDelete[2]=C:\test\mockArchive\RepoRetimeRoughKey"
set "confirmation="
echo ---- Studio Stash Delete Script ----
echo.
echo Directories to delete:
REM Print each directory name and prompt for confirmation
for %%d in (0 1 2) do (
    echo !directoriesToDelete[%%d]!
)
echo.
REM Prompt the user for confirmation
set /p "confirmation=Type 'delete' to confirm deletion: "

REM Check user input
if /i "%confirmation%"=="delete" (
    for %%d in (0 1 2) do (
        set "currentDir=!directoriesToDelete[%%d]!"
        if exist "!currentDir!" (
            echo Deleting: !currentDir!
            rmdir /s /q "!currentDir!"
        ) else (
            echo Directory not found: !currentDir!
        )
    )
) else (
    echo Deletion canceled. No directories were deleted.
)
REM Display final confirmation message
echo.
echo All specified directories processed.
REM Pause to keep the window open
pause
endlocal
