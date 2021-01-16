# Client deployment using powersehll

This article describes how to automate the deployment of a Simplic Studio installation for clients. 
The script below must be added to `Group policies` -> `Startup scripts` (Powershell tab) for `Computer policies`.

```powershell
# Simplic Deploy UB 2021.01.06

# Local directory
$simplicPrg = "C:\Program Files (x86)\Simplic\Simplic Studio\Simplic Studio.exe"

# Directory with the simplic studio setup. Must be available from the client computer
$simplicSetupFolder = "C:\Temp\Setup"

if (Test-Path $simplicPrg -PathType leaf) {
    $simplicVersion = (get-item $simplicPrg).VersionInfo.fileversion  -replace "[^0-9]"
}
else {
    $simplicVersion = 0
}

$folderContent = (Get-ChildItem $simplicSetupFolder).Name
$setupVersion = $FolderContent -replace "[^0-9]"

if($setupVersion -gt $simplicVersion) {
    $setupString = $simplicSetupFolder + "\" + $folderContent
    Invoke-Command –ComputerName localhost –ScriptBlock {msiexec /I $setupString /qn}      
}

```