# Adding repositories to the release notes

First add a `infrastructure.json` to the repository like specified here: [Adding repositories to the version number update](adding_version_numbers.md).
Then create a empty release-notes.xml in the master & dev branch if not existant already. If the repository is a main repository, include a empty user-release-notes.xml aswell.

```xml
<ReleaseNotes>
</ReleaseNotes>
```

At last add the repositories HTTPS clone link to the `repositories.json` file located in release_notes/build.

The release notes written in the xml will then appear on the releaese notes page.
