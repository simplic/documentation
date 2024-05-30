# ArchiveAndEnqueue grid menu function

The ArchiveAndEnqueue method (namespace = Simplic.OutputManagement.UI, class = ArchiveAndEnqueueHelper) allows to create a report from any data set and enqueue it in the output management. 
The necessary parameters are defined in the grid menu function configuration. 
The ArchiveAndEnqueue grid menu function "name parameter name" field content in the "script/CLR" section must be of the format <report name>,<output queue configuration ID>,<stack ID>. Additional whitespaces are not allowed. 
The ArchiveAndEnqueue grid menu function "value parameter name" field content in the "script/CLR" section must be of the format <reference number column name>,<instance data ID column name>,<contact ID number column name>,<personal account ID column name>,<tenant ID column name>. Additional whitespaces are not allowed.