# List of directories to analyze
$directories_dst = @(
    "C:\test\mockProjects\Nuke-HeiroConform_Rubiks",
    "C:\test\mockProjects\RepoRetimeRoughKey",
    "C:\test\mockProjects\RiggingSkinFixAndPointCache",
    "X:\Projects\CrunchyRoll - Frieren"
)

# List of directories to analyze
$directories_src = @(
    "C:\test\mockProjects\Nuke-HeiroConform_Rubiks",
    "C:\test\mockProjects\RepoRetimeRoughKey",
    "C:\test\mockProjects\RiggingSkinFixAndPointCache",
    "X:\Projects\CrunchyRoll - Frieren"
)



#### DST

# Initialize counters
$totalFiles_dst = 0
$totalSize_dst = 0

# Iterate through each directory
foreach ($directory in $directories_dst) {
    # Get all files in the current directory
    $files = Get-ChildItem -Path $directory -File -Recurse

    # Update counters
    $totalFiles_dst += $files.Count
    $totalSize_dst += $files | Measure-Object -Property Length -Sum | Select-Object -ExpandProperty Sum
}

# Convert total size to human-readable format
$totalSize_dstInKB = $totalSize_dst / 1KB
$totalSize_dstInMB = $totalSize_dst / 1MB
$totalSize_dstInGB = $totalSize_dst / 1GB
$totalSize_dstInTB = $totalSize_dst / 1TB

# Display results
Write-Host "- DESTINATION:"
Write-Host "  - calculating..."
Write-Host "  - Total Number of Files: $totalFiles_dst"
Write-Host "  - Total File Size: $($totalSize_dst) bytes ( $totalSize_dstInGB GB, $totalSize_dstInTB TB )"


##### SRC

# Initialize counters
$totalFiles_src = 0
$totalSize_src = 0

# Iterate through each directory
foreach ($directory in $directories_src) {
    # Get all files in the current directory
    $files = Get-ChildItem -Path $directory -File -Recurse

    # Update counters
    $totalFiles_src += $files.Count
    $totalSize_src += $files | Measure-Object -Property Length -Sum | Select-Object -ExpandProperty Sum
}

# Convert total size to human-readable format
$totalSize_srcInKB = $totalSize_src / 1KB
$totalSize_srcInMB = $totalSize_src / 1MB
$totalSize_srcInGB = $totalSize_src / 1GB
$totalSize_srcInTB = $totalSize_src / 1TB

# Display results
Write-Host "- SOURCE:"
Write-Host "  - calculating..."
Write-Host "  - Total Number of Files: $totalFiles_src"
Write-Host "  - Total File Size: $($totalSize_src) bytes ( $totalSize_srcInGB GB, $totalSize_srcInTB TB )"
