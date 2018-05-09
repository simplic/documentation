# LookUpTextBox

The `LookUpTextBox` control is the default control for a pick list

Assembly: `Simplic.UI`
Namespace: `Simplic.Framework.DBUI`
Class: `LookupTextBox`
Derives from: `LookupTextBoxBase, IDisposable`


Importent member:
1. `Identity` type object
Selected item 
2.`SelectionProvider` type ItemBoxSelectionProvider 
Assigns the itembox
3.`Parameter` type IDictionary<string,object>
List of sql parameter which can be found in the grid of the itembox.
The keys have to insert like \[ParameterKey] in the sql script.

`Example

 <simplic:LookupTextBox x:Name="LookUpLevel" Width="200" Height="24" 
   Identity="{Binding LevelId, Mode=TwoWay,UpdateSourceTrigger=PropertyChanged,ValidatesOnDataErrors=True}" 
   Parameter="{Binding LookUpParameters,UpdateSourceTrigger=PropertyChanged}" 
   ShowIdentityTextBox="False" Uid="P1">
                                                
 <dbui:LookupTextBox.SelectionProvider>
   <dbui:ItemBoxSelectionProvider ItemBoxName="IB_DunningLevel" DisplayColumn="Friendlyname" IdentityColumn="Guid" DisplayFriendlyColumn="Friendlyname" 
LoadByIdentityStatement="SELECT cast(dc.LevelNumber as varchar) +' / '+dt.Name as Friendlyname ,dc.LevelNumber, dc.Guid FROM IT_Financial_DunningLevel dc join IT_Financial_DunningType dt on dt.Guid = dc.TypeId  where dc.Guid = '[SearchString]'">

 </dbui:ItemBoxSelectionProvider>
</dbui:LookupTextBox.SelectionProvider>
</simplic:LookupTextBox>
