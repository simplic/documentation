# WebGrid

 The Plugin Simplic.WebGrid offers the possiblity to display grids in a browser
Follow these steps

## 1.Create URL to display a grid in a browser

The structure of such a url looks like this 
```
<ip-adress-web-api>:<port>/api/v1-0/webgrid/show?grid=<grid-name>&<conditions[optional]>&api_key=<api-key>&user_name=<user-name>
```
For example we look at the **Document Grid**
```
http://192.168.99.181:48080/api/v1-0/webgrid/show?grid=IB_WebGrid_Sample&api_key=~ssk-b3c905c6716d4d28b6751645642acdc5&user_name=SuperUser
```
### Conditions
We can place simple sql conditions 
These operations are supported
|url-code| sql-operator |
|--|--|
| like | like  |
|eq|=|
| neq | !=  |
| gt | >  |
| gte | >= |
| sm | <  |
| sme | <=  |

**Example**
In this Example we looking for all documents where the update user name is 'superuser'
```
&param_updateusername_eq=superuser
```

```
http://192.168.99.181:48080/api/v1-0/webgrid/show?grid=IB_WebGrid_Sample&param_updateusername_eq=superuser&api_key=~ssk-b3c905c6716d4d28b6751645642acdc5&user_name=SuperUser
```

You can add more conditions afterwards

## 2.Enable grid for the web grid
Only Grids that contain this statement in the sql statement will be shown
```
-- enable-web-grid
 ```



