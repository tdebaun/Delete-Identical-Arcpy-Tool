# Delete-Identical-Arcpy-Tool
A simple script to trim down ArcGIS data based on rows with identical field values. This script can be used as a simplified replacement for the Delete Identical Tool, which is locked to higher ArcGIS license levels. The script searches the chosen shapefile based on the specified fields. Each time a new unique value is encountered in the chosen fields that row is added to a set. Subsequent rows are checked against this set, and when a subsequent row matches a row already in the set it is deleted. When multiple fields are entered the tool only removes rows that match a previously checked row in all search fields.

You will need to enter the filepath of the shapefile to run the tool on when prompted. 
You will need to enter the name(s) of at least one field for the tool to use in it's calculation, seperated by a comma and a space. Be sure to use the field name and not the alias.

Example 1 - One search field is chosen in the second prompt (Field A), 
in Row 1 Field A = 5,
in Row 2 Field A = 4,
in Row 3 Field A = 5.  
In this example Row 3 will be removed as the Field A value of "5" was already encountered in Row 1.

Example 2 - Two search fields are chosen (Field A & Field B). 
in Row 1 A = 5 and B = 6, 
in Row 2 A = 5 and B = 7, 
in Row 3 A = 5 and B = 6,
in Row 4 A = 4 and B = 6.
In this example only Row 3 will be deleted. While Field A is equal in rows 1, 2 and 3, Row 2 has a different value for Field B, and thus since the rows don't match in every selected field Row 2 is not deleted. Likewise while Row 4 matches Rows 1 and 3 in Field B, it has a different value in Field A and is thus considered a unique entry.
