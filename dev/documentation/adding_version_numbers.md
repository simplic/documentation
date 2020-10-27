# Addings Repositories to the Version number update

The version number update script automatically sets new release/assembly versions for you in your code aswell as the database.
To add a repository to the auto version update and include the template as a step within the pipeline.
You will also have to add the credentials of the simplic-bot aswell as the database-connection-string to the pipelines variables.

If you're adding a new main repository (we define a main repository as one, that is an individual product), make sure to add a `infrastructure.json` file to the repository.

Commits in which version numbers should be updated, have to specify the "size" of the update in their Commit message like this `Type: major|minor|patch|ignore`. If you're working with Pullrequests, you can also use labels.
If no Type is specified, it will default to patch.

Include example:

```yml
resources:
  repositories:
    - repository: infrastructure
      type: github
      name: simplic/build-infrastructure
      endpoint: simplic-bot

steps:
  - ${{ if not(eq(variables['Build.Reason'], 'PullRequest')) }}:
      - template: version-number-update-template.yml@infrastructure
        parameters:
          connection_string: $(connection_string)
          git_user: $(git_user)
          git_pass: $(git_pass)
          branch_name: ${{ replace(variables['Build.SourceBranch'], 'refs/heads/', '') }}
```

infrastructure.json example:

```json
{
  "productname": "ProductNameInDatabase",
  "init_path": "src/Init.cs",
  "subrepositories": [
    "https://github.com/simplic/simplic-change-tracking.git",
    "https://github.com/simplic/simplic-commandshell.git"
  ]
}
```

### Infrastructure variables explanation

Required

- **product_name**: A String value, indicating the productname of the repository or the repositories main repository.
- **init_path**: The path to the Init.cs file of the repository.
- **subrepositories**: A list of https clone links of all the subrepositories of the repository.
