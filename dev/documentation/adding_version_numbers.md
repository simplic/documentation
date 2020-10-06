# Addings Repositories to the Version number update

The version number update script automatically sets new release/assembly versions for you in your code aswell as the database.
To add a repository to the auto version update, include the template as a step, add a `infrastructure.json` file to the repository and (if not done already) add the simplic-bot logins and the sc-dev02 connection string to the pipelines variables. This should be done before the MSBuild task.

Commits in which version numbers should be updated, have to specify the "size" of the update in their Commit message like this `Type: major|minor|patch`. If no Type is specified, it will default to patch.

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
  "productname": "SimplicApplicationCollection",
  "is_main_repo": false,
  "main_repo_name": "simplic-logistics",
  "main_repo_init_path": "src/Simplic.PlugIn.Logistics/Init.cs"
}
```

### Infrastructure variables explanation

Required

- **product_name**: A String value, indicating the productname of the repository or the repositories main repository.
- **is_main_repo**: A boolean value, indicating whether the repository is the main repository of a module or not.

Optional:

- **main_repo_name**: Set this if the repository isnt the main repository.
- **main_repo_init_path**: Set this to the relative path to the Init.cs file, if the main repository contains more than one Init.cs file.
