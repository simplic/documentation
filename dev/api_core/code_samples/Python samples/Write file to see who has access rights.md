# Working with writing a file to see who has access rights

In this code sample a file with all the usernames that have access rights is written.
## Required Modules

- [Simplic.Localization](xref:Simplic.Localization) 
  - [ILocalizationService](xref:Simplic.Localization.ILocalizationService)
- [Simplic.Authorization](xref:Simplic.Authorization) 
  - [IAuthorizationService](xref:Simplic.Authorization.IAuthorizationService)
- simplic
  - [Sql](xref:PythonAPI.Sql)
  - [DependencyInjection](xref:PythonAPI.DependencyInjection)
  - [UserManager](xref:PythonAPI.UserManager)
- [System](xref:System)
  - [Console](xref:System.Console)
- [System.IO](xref:System.IO)
  - [File](xref:System.IO.File)

## Samples
# Python

```python
from Simplic.Localization import ILocalizationService
from Simplic.Authorization import IAuthorizationService
from simplic import Sql, DependencyInjection, UserManager
from System import Console
from System.IO import File

# Get the LocalizationService and the AuthorizationService 
l_service = DependencyInjection.resolve(ILocalizationService)
a_service = DependencyInjection.resolve(IAuthorizationService)
 
txt = '# Berechtigungen Simplic Anwendungen\r\n'

# List with all the selected columns and rows
for r in Sql.execute('SELECT * FROM ESS_MS_Intern_Page order by MenuText'):
    # Translates the MenuText key to a language.
    name = l_service.Translate(r.MenuText)
     
    txt = txt + '## Anwendung: ' + name + '\r\n'
    # The value of the access rights is set to false.
    has_access_rights = False
    # Gets the RowAccess of given row id
    access = a_service.GetAccessRights('ESS_MS_Intern_Page', 'Guid', r.Guid)
 
    groups = []
    users = []
 
    # List with all groups that have full access
    for group in access.GroupFullAccess:
        
        # Append group with full access to the groups list
        groups.append(group)
        # has_access_rights for the current group is set to true
        has_access_rights = True
        for g_r in Sql.execute('SELECT * FROM ESS_MS_Intern_Groups WHERE Ident = ?', 'Simplic', [group]):
            txt = txt + '* ' + g_r.Name + '\r\n'

            # If the name is SimpleUser every user has all the rights
            if g_r.Name == 'SimpleUser':
                txt = txt + '  * Alle Benutzer\r\n'
            else:
                for ua in Sql.execute('SELECT * FROM ESS_MS_Intern_UserAssignment WHERE GroupId = ? order by UserId', 'simplic', [g_r.GroupId]):
                    
                    # To avoid double Users
                    if ua.UserId in users:
                        continue
                    # Append the UserId to the users list
                    users.append(ua.UserId)
                    # The Usernames who have access are added to the String
                    txt = txt + '  * ' + UserManager.get_friendlyusername(ua.UserId) + '\r\n'
 
    # All groups who have read access
    for group in access.GroupReadAccess:
        # To avoid double groups
        if group in groups:
            continue
        # Append group to the groups list
        groups.append(group)
 
        has_access_rights = True
        for g_r in Sql.execute('SELECT * FROM ESS_MS_Intern_Groups WHERE Ident = ?', 'Simplic', [group]):
            txt = txt + '* ' + g_r.Name + '\r\n'
 
            if g_r.Name == 'SimpleUser':
                txt = txt + '  * Alle Benutzer\r\n'
            else:
                for ua in Sql.execute('SELECT * FROM ESS_MS_Intern_UserAssignment WHERE GroupId = ?', 'simplic', [g_r.GroupId]):
 
                    if ua.UserId in users:
                        continue
 
                    users.append(ua.UserId)
 
                    txt = txt + '  * ' + UserManager.get_friendlyusername(ua.UserId) + '\r\n'

    # All groups who have write access 
    for group in access.GroupWriteAccess:
 
        if group in groups:
            continue
        groups.append(group)
 
        has_access_rights = True
        for g_r in Sql.execute('SELECT * FROM ESS_MS_Intern_Groups WHERE Ident = ?', 'Simplic', [group]):
            txt = txt + '* ' + g_r.Name + '\r\n'
 
            if g_r.Name == 'SimpleUser':
                txt = txt + '  * Alle Benutzer\r\n'
            else:
                for ua in Sql.execute('SELECT * FROM ESS_MS_Intern_UserAssignment WHERE GroupId = ?', 'simplic', [g_r.GroupId]):
 
                    if ua.UserId in users:
                        continue
 
                    users.append(ua.UserId)
 
                    txt = txt + '  * ' + UserManager.get_friendlyusername(ua.UserId) + '\r\n'

    # All users who have full access are added to the String
    for user in access.UserFullAccess:
        has_access_rights = True
        txt = txt + '* ' + UserManager.get_friendlyusername(user)
    # All users who have read access are added to the String 
    for user in access.UserReadAccess:
        has_access_rights = True
        txt = txt + '* ' + UserManager.get_friendlyusername(user)
    # All users who have write access are added to the String 
    for user in access.UserWriteAccess:
        has_access_rights = True
        txt = txt + '* ' + UserManager.get_friendlyusername(user)
    # If no one has specifically got access rights, every user has the same access rights.
    if not has_access_rights:
        txt = txt + '* Alle Anwender\r\n'
 
Console.WriteLine(txt)
# Write File with all the usernames that have access rights
File.WriteAllText('C:\\simplic\\r.md', txt)

```
***

## Expected Output
```
e.g. (a list with all the usernames that have access rights)
## Anwendung: Auftragsstatus
* Alle Anwender
## Anwendung: Ausrüstung
* SuperUser
  * Super User
  * Benedikt Eggers
```