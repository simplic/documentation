# Git

Simplic uses git and GitHub for version control purpose. The following rules must be followed when contributing to a simplic project:

## Branches

A branch should start with the following prefix:

1. `f_` for a feature
2. `b_` for a bug fix

E.g. `f_new_contact_window`, `b_message_box_title`.

A branch should only contain changes that belong together. Initial branches might contain some more changes. If a branch contains changes,
it should start with `f_`.

### Default branches

All simplic repositories contain two default branches: `master` and `dev`.

* `master`: Contains the current release
* `dev`: Contains a working but untested version of the product

## Commit messages

Commit messages should be as descriptive as possible. Adding a prefix for the action is recommended:

> Add: new message box when closing a contact
>
> Remove: Title bar in contact window
>
> Change: Viewmodels are always dirty

A commit should always contains changes that belongs togehter.

---

If the project is connected to ZenHub, a pull request must be connected with the ZenHub issue.