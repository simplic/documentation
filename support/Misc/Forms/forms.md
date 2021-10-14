# Simplic.Forms
## Why we need Simplic.Forms
The Form-Designer serves as a construction kit for the customer to create his own forms completely according to his ideas.
This way the customer will be able to modify his own forms without the help of SIMPLIC development and both parties will save time and the customer will be even more flexible. For example, QM forms can be created to record quality characteristics. 
## Generate new Form
First the User click "Konfiguration" and then Form Designer to start the Form Designer.
![Taskbar](~/images/Forms/taskbar.jpg)
Otherwise the User can search and then clicking Form Designer to start it.
![Search](searchbar.jpg)
The Grid is open and with a "right Click" or press the Key "F8" a new Form is open.
![NewFormButton](~/images/Forms/newFormButton.jpg)
When a Form exists the User can edit it with a "right click" or press the Key "F5" and the Form will open.
 ![EditFormButton](~/images/Forms/editFormButton.jpg)
 The Guid will be created automatic when the Form is open, We will need the Guid later.
 The new Form need a "Name", "Beschreibung" and a "Tabellen Name".
 After that we need a "Datenstruktur" with a "right click" in the discolored area, the User can create a new data.
![NewTreeviewItem](~/images/Forms/newTreeviewItem.jpg)
A new Form is open with "Feldname" and "Datentyp".
The "Feldname" is the name of the attribut.
The "Datentyp" is the datatype of the attribut.
With clicking "Speichern und schließen" the Form will be closed and saved. 
![NewTreeviewItemForm](~/images/Forms/newTreeviewItemForm.jpg)
When the "Datenstruktur" complete is, the User can switch to Design and create the actual Form.
![SwitchDesign](~/images/Forms/switchDesign.jpg)
Now the User see a new Form with three columns.
Left is the ToolBox.
In the middle is the Designer Surface.
Right is the Attribute List.
![DesignTab](~/images/Forms/designTab.jpg)
First the User choose a item from the ToolBox make a "left click"  and drag into the Designer Surface in the middle.
![SelectDesignerItem](~/images/Forms/selectDesignerItem.jpg)
![ItemDesignSurface](~/images/Forms/itemDesignSurface.jpg)
The User choose a item in the Design Surface then in the right the Attribute List will be open. 
For example the item is a TextBox so the User do a "right click" in "Text" and choose "Binding".
![SelectBindingText](~/images/Forms/selectBindingText.jpg)
In the Attribute List the attribut "Text" will be expanded.
Three attributes are very Important.
**Mode** it must be TwoWay
**Path** the name of the data from the "Datenstruktur"
**UpdateSourceTrigger** it must be PropertyChanged
![ImportantBinding](~/images/Forms/importantBinding.jpg)
Under the Designer Surface are the 2 tabs Xaml and Designer. By default you are in the Designer, but if you want to see the added tools and settings as Xaml, 
you can easily navigate there by clicking on Xaml.
![ClickXaml](~/images/Forms/clickXaml.jpg)
Everytime the User can testing the Form with clicking "Ausführen" and see the Form in a Window where it will be also later.
![TestingForm](~/images/Forms/testingForm.jpg)
When the User click "Speichern und schließen" in the Main Window then the Form will be saved.
## Create Database Table
The User must create the DataBase Table.
The name of the Table must be the same from the Designer name.
The Columns "Guid", "TenantId", "IsDeleted", "CreateDateTime", "UpdateDateTime", "CreateUserId", "UpdateUserId" and "ConfigurationGuid" are always important.
The other Columns must have the same name and datatyp from the Form Designer.
![DataBase](~/images/Forms/dataBase.jpg)
## Create Grid
When the Database is created then the User must create a Grid.
Important in Grid "Menü" are **Klasse**, **Namespace**, **Statische Methode**.
The three attributes are in the following picture.
**Name-Parameter Name** and **Wert-Parameter Name** are important too.
The Parameter "Name" is always "ConfigurationId" and the "Wert" is the Guid from the Form.
![GridProperty](~/images/Forms/gridProperty.jpg)
![GridPropertyEdit](~/images/Forms/gridPropertyEdit.jpg)
## Create Application
![AddApplication](~/images/Forms/addApplication.jpg)
