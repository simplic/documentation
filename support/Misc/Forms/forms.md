# Simplic.Forms
## Why we need Simplic.Forms
The Form-Designer serves as a construction kit for the customer to create his own forms completely according to his ideas.
This way the customer will be able to modify his own forms without the help of SIMPLIC development and both parties will save time and the customer will be even more flexible. For example, QM forms can be created to record quality characteristics. 
## Generate a new Form
The "Form Designer" is located in the ribbon tab "Konfiguration".

![Taskbar](~/images/Forms/taskbar.png)  

Otherwise the user can search and then selecting "Form Designer" to start it.  

![Search](~/images/Forms/searchbar.png)  

With a "right click" in the grid or press the Key "F8" a new form will open.  

![NewFormButton](~/images/Forms/newFormButton.png)  

When a form exists, the user can edit it with a "right click" or press the Key "F5" and the form will open.  

 ![EditFormButton](~/images/Forms/editFormButton.png)  

 The guid will be created automatically when the form is opened, we will need the Guid later.  
 The new form need a "Name", "Beschreibung" and a "Tabellen Name".  
 After that we need a "Datenstruktur" with a "right click" in the discolored area, the user can create a new data.  

![NewTreeviewItem](~/images/Forms/newTreeviewItem.png)  

A new Form is open with "Feldname" and "Datentyp".  
The "Feldname" is the name of the attribute.  
The "Datentyp" is the datatype of the attribute.  
With clicking "Speichern und schließen" the form will be closed and saved.   

![NewTreeviewItemForm](~/images/Forms/newTreeviewItemForm.png)  

The user can always switch to the designer and create his form.
![SwitchDesign](~/images/Forms/switchDesign.png)  

Now the user sees a new form with three columns.  
Left is the tool box.  
In the middle is the designer surface.  
Right is the attribute list.  

![DesignTab](~/images/Forms/designTab.png)  

First, the user selects an item from the tool box and drags it to the designer surface in the center.  

![SelectDesignerItem](~/images/Forms/selectDesignerItem.png)  
![ItemDesignSurface](~/images/Forms/itemDesignSurface.png)  

The user selects an item from the design surface and gets the attribute list by right clicking on it.  
For example: The item is a TextBox and the user right-clicks in "Text" and selects "Binding".  

![SelectBindingText](~/images/Forms/selectBindingText.png)  

In the attribute list the attribut "Text" will be expanded.  
Three attributes are very important.  
**Mode** it must be TwoWay  
**Path** the name of the data from the "Datenstruktur"  
**UpdateSourceTrigger** the default value is "PropertyChanged" or for text it is "LostFocus"  
*PropertyChanged:* Updates the binding source immediately whenever the binding target property changes.  
*LostFocus:* Updates the binding source whenever the binding target element loses focus.  

![ImportantBinding](~/images/Forms/importantBinding.png)  

Below the designer surface there are two tabs Xaml and Designer. By default you are in the Designer tab, but if you want to see the added tools and settings as Xaml,
you can easily navigate there by clicking on Xaml.  

![ClickXaml](~/images/Forms/clickXaml.png)  

The user can test the form at any time by clicking "Ausführen" and will see the form in a seperate window.  

![TestingForm](~/images/Forms/testingForm.png)  

When the user clicks "Speichern und schließen" in the main window, the form is saved.  

## Create Database Table
The user must create the dataBase table.  
The name of the table must be the same as the designer name.  
The columns "Guid", "TenantId", "IsDeleted", "CreateDateTime", "UpdateDateTime", "CreateUserId", "UpdateUserId" and "ConfigurationGuid" are always important.  
The other columns must have the same name and data type as in the form designer.  

![DataBase](~/images/Forms/dataBaseTable.png)  

## Create Grid
Once the database table is created, the user must create a grid.  
Important in grid "Menü" are **Klasse**, **Namespace**, **Statische Methode**.  
The three attributes are in the following picture.  
**Name-Parameter Name** and **Wert-Parameter Name** are important too.  
The parameter "Name" is always "ConfigurationId" and the "Wert" is the guid from the Form.  

![GridProperty](~/images/Forms/gridProperty.png)  
![GridPropertyEdit](~/images/Forms/gridPropertyEdit.png)  

## Create Application
![AddApplication](~/images/Forms/addApplication.png)  
