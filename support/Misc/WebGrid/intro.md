# WebGrid

 The plugin Simplic.WebGrid offers the possiblity to display grids from the Simplic Studio in any internet browser

To achieve this you need to follow these steps below

## 1.Create URL to display a grid in a browser

First open the browser of your choice, for example **Google Chrome**

Now we need a URL and the structure looks like this 
```
<ip-adress-web-api>:<port>/api/v1-0/webgrid/show?grid=<grid-name>&<conditions[optional]>&api_key=<api-key>&user_name=<user-name>
```
**Explanation for each placeholder**

|Placeholder| Explanation | Example|
|--|--|--|
| ip-adress-web-api | The ip adress of the host/webapi | 192.168.99.181
|port| The port of the host/webapi| 48080
|grid-name|The name of the grid that should be displayed| IB_WebGrid_Sample
|conditions|Sql-like conditions to aggregate the data|param_barcode_eq=7744
|api-key| The api key that is assigned to the user|demokey
|user-name|The name of the user| DemoUser



So we get the following url


```
http://192.168.99.181:48080/api/v1-0/webgrid/show?grid=IB_WebGrid_Sample&api_key=demokey&user_name=DemoUser
```
### **Conditions**
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
In this example we are looking for all documents where the update user name is 'superuser'
```
&param_updateusername_eq=superuser
```

```
http://192.168.99.181:48080/api/v1-0/webgrid/show?grid=IB_WebGrid_Sample&param_updateusername_eq=superuser&api_key=demokey&user_name=SuperUser
```

You can add more conditions afterwards the first conditions

## 2.Configurate a  grid for the web grid
Only Grids that contain this statement in the sql statement will be shown
```
-- enable-web-grid
 ```
For example
```
-- enable-web-grid

SELECT top 100 * FROM  IT_Document
WHERE 1 = 1
[WhereCondition]
Order By CreateDateTime
```

The [WhereCondition] is important for the **conditions** because that tag gets replaced by the conditions


**Grid Columns**

It is very important to have the **BlobGuid** as a non active column in the grid. This column is responsible to display the document/data




 ## 3.Dependencies

 This plugin has a dependency to SAC
