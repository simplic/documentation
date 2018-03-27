# Simplic Nuget Packages
Having a nuget package repository is a huge benefit for projects depending on each other. As we have a couple of (~66) projects, it is a big help
to use Nuget packages. In order to do that we have create a private nuget package. 

## Using Simplic Nuget Packages

In order to be able to use our nuget package feed, you need to add it to your source list as follows:

- in visual studio go to Tools -> NuGet Package Manager -> Package Manager Settings -> Package Sources. Click on green plus icon and enter the following: Name: Simplic, Source: http://simplic.biz:10380/nuget . if you encounter any problems try running this command in cmd : ```nuget setapikey 65398cf6H4 -source "http://simplic.biz:10380/nuget"```

## Adding a package (project) to simplic nuget package feed
Nuget accepts only .nupkg files. So we need to create a .nuspec file for each project we want to upload to the nuget feed. 

Example .nuspec file:
```xml
<?xml version="1.0"?>
<package xmlns="http://schemas.microsoft.com/packaging/2011/08/nuspec.xsd">
	<metadata>
		<id>$id$</id>
		<version>$version$</version>
		<authors>SIMPLIC GmbH</authors>
		<owners>SIMPLIC GmbH</owners>    
		<projectUrl>git hub project link comes here</projectUrl>
		<iconUrl><![CDATA[https://avatars1.githubusercontent.com/u/14359329?v=3&s=460]]> </iconUrl>
		<description>here comes the description of the package</description>
		<requireLicenseAcceptance>false</requireLicenseAcceptance>            		
	</metadata>
</package>
```
