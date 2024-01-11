@echo off
setlocal enabledelayedexpansion

set "directoriesToDelete="
set "confirmation="

REM Add the directories to the list
set "directoriesToDelete=C:\test\mockArchive\RiggingSkinFixAndPointCache" 
set "directoriesToDelete=!directoriesToDelete! C:\test\mockArchive\Nuke-HeiroConform_Rubiks"
set "directoriesToDelete=!directoriesToDelete! C:\test\mockArchive\RepoRetimeRoughKey"

echo ---- Studio Stash Delete Script ----
echo.

echo Directories to delete:
REM Print each directory name and prompt for confirmation
for %%d in (%directoriesToDelete%) do (
    echo %%d
)

echo.
REM Prompt the user for confirmation
set /p "confirmation=Type 'delete' to confirm deletion: "

REM Check user input
if /i "%confirmation%"=="delete" (
    for %%d in (%directoriesToDelete%) do (
        if exist "%%d" (
            echo Deleting: %%d
            rmdir /s /q "%%d"
        ) else (
            echo Directory not found: %%d
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
