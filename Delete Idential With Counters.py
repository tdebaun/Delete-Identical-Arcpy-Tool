#-------------------------------------------------------------------------------
# Name:        Delete Identical Script
# Purpose: This script searches an attribute table based on a single field
# identifying all unique values and deleting all duplicte entries after the first.
#-------------------------------------------------------------------------------

import arcpy

#Define parameters, a shapefile to search as input and the field to search by as the searchfield


feature = input("enter the filepath for the feature to be updated: ")

searchField = input("enter the names of the fields to be searched (please use a comma and a space to sperate): ")

searchField = tuple(searchField.split(', '))

#create a set (values) to hold the unique values from the attribute table to trim based on
values = {}
values = set()

#create counters to log how many unique rows were saved and how many rows were deleted
unique = 0
deleted = 0

#create the cursor
cursor = arcpy.da.UpdateCursor(feature, searchField)

#start a loop that searches through the attribute table
for row in cursor:

    #create a temporary variable to hold the value to be checked
    check = str(row)

    #Use an if statement to evaluate the current attribute value
    #if the value is already in the set of unique values -> delete the entry and go to the next entry
    #otherwise add the value to the value to the set and go to the next entry
    if check in values:
        cursor.deleteRow()
        deleted += 1
    else:
        values.add(check)
        unique += 1

del cursor

#display the number of unique rows and deleted rows
print("Unique Row values encountered: %d" %(unique))
print("Rows Deleted: %d" %(deleted))
