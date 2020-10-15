# Adding repositories to the release notes

First add a `infrastructure.json` to the repository like specified here: [Adding repositories to the version number update](adding_version_numbers.md).
Then create a empty release-notes.xml in the master & dev branch if not existant already. If the repository is a main repository, include a empty user-release-notes.xml aswell.

```xml
<ReleaseNotes>
</ReleaseNotes>
```

At last add the repositories HTTPS clone link to the `repositories.json` file located in release_notes/build.

The release notes written in the xml will then appear on the releaese notes page.



# Adding release notes

First, search for the file release-notes.xml in your current solution. Then add your performed changes as follows:

e. g.

```xml
<ReleaseNotes>
	<ChangeSet>
		<Change type="enhancement">Write the change you made here. Always end a change with a period.</Change>
	</ChangeSet>
  <ChangeSet>
    ...
  </ChangeSet>
  ...
</ReleaseNotes>
```
**Note:** Utilize for every change its own element and save all elements according to one overall change-task in a ChangeSet. Furthermore, add for every change a changetype as shown above.

Possible changetypes:
  enhancement
  feature
  bug
  
Don't add a guid to the ChangeType, as that will be added later automatically
  
