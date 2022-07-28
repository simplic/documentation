# Setting up BaGet (local NuGet server)

## Prerequisits:
**.NET Core SDK**: `https://dotnet.microsoft.com/en-us/download`
**Node.js**: `https://nodejs.org/en/`

## Setup:
Download and extract the latest BaGet release: `https://github.com/loic-sharma/BaGet/releases`

Create a new .cmd file using any editor containing the following commands:

> cd \<your BaGet folder directory (e.g. %userprofile%\Downloads\BaGet)\>
> dotnet baget.dll

Save the file to the following directory: `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`

## How to use BaGet:
After completing these steps and either restarting your Windows machine or executing the .cmd file manually a BaGet server will be running locally on your system (localhost:5000).

When creating local NuGet packages for .NET standard projects using the Local NuGet Manager included in the simplic-sdk repository, 
the created packages will be uploaded to the BaGet server making them accessible for use in Docker Compose.

A list of hosted packages can be viewed in a browser: `http://localhost:5000/`

To clear the BaGet server deleting all uploaded packages, just delete the BaGet folder and extract the .zip file again.