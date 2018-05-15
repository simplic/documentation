# LookUpTextBox

The `LookUpTextBox` control is the default control for a pick list

### Assembly: `Simplic.Framework.DBUI`
### Namespace: `http://schemas.simplic-systems.com/2016/xaml/presentation`
### Class: `LookupTextBox`
### Derives from: `LookupTextBoxBase, IDisposable`


## Importent member:
1. `Identity` [object] Selected item 
2. `SelectionProvider` [ItemBoxSelectionProvider] 
Assigns the itembox
3. `Parameter` [IDictionary<string,object>]
List of sql parameter which can be found in the grid of the itembox.
The keys have to insert like \[ParameterKey] in the sql script.
4. `ShowIdentityTextBox` [bool] shows a second textbox with the indentity value
5. `VerticalAlignIdentityTextBox` [bool] the indentity textbox is shown in a second row when 
the parameter is true.

## Example
### XAML
```ruby 
 <simplic:LookupTextBox x:Name="LookUpLevel" Width="200" Height="24" 
   Identity="{Binding LevelId, Mode=TwoWay,UpdateSourceTrigger=PropertyChanged,ValidatesOnDataErrors=True}" 
   Parameter="{Binding LookUpParameters,UpdateSourceTrigger=PropertyChanged}" 
   ShowIdentityTextBox="False" Uid="P1">
                                               
 <dbui:LookupTextBox.SelectionProvider>
   <dbui:ItemBoxSelectionProvider ItemBoxName="IB_DunningLevel" DisplayColumn="Friendlyname"    IdentityColumn="Guid" DisplayFriendlyColumn="Friendlyname" 
	LoadByIdentityStatement="SELECT cast(dc.LevelNumber as varchar) +' / '+dt.Name as Friendlyname ,dc.LevelNumber, dc.Guid FROM IT_Financial_DunningLevel dc join IT_Financial_DunningType dt on dt.Guid = dc.TypeId  where dc.Guid = '[SearchString]'">

</dbui:ItemBoxSelectionProvider>
</dbui:LookupTextBox.SelectionProvider>
</simplic:LookupTextBox>
```
### C# Viewmodel
```ruby
 private Dictionary<string, object> lookUpParameters;
 
        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="proposal"></param>
        public DunningProposalViewModel(DunningProposal proposal)
        {
            lookUpParameters = new Dictionary<string, object>();
            LookUpParameters.Add("_param1", PersonalAccountDunningGroup.Guid);
        }

        /// <summary>
        /// Gets the parameters for the level lookup 
        /// </summary>
        public Dictionary<string, object> LookUpParameters
        {
            get
            {
                return lookUpParameters;
            }
        }
```
### SQL
```ruby
SELECT dc.*,dt.Name as TypeName,cast(dc.LevelNumber as varchar) +' / '+dt.Name as Friendlyname  FROM IT_Financial_DunningLevel dc
join IT_Financial_DunningType dt on dt.Guid = dc.TypeId 
where 1 = 1 and dc.Guid != '00000000-0000-0000-0000-000000000000'
and (cast(dc.LevelNumber as varchar) LIKE '%[SearchString]%' or dt.Name  LIKE '%[SearchString]%' ) 
and dc.GroupId = '[_param1]'
order by dc.LevelNumber
```