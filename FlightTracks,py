###Flight Tracks
#Author: Brian Bower
#With assistance from Diego Ibarra and Pat Upson 
#Updated on: May 17th, 2018

#This script takes point feature classes in a scratch geodatabase and converts them to a line, 
#smooths the line, adds and calculates fields, merges the new files together, merges the previous workspace
#with the new work and updates the current field to filter out data that isn't from the past two weeks. 

#READ THIS BEFORE RUNNING
#DO NOT OPEN THE ARCMAP PROJECT UNTIL COMPLETED. RUN WITH IN CMD PROMPT OR A PYTHON WINDOWN IN ARCCATALOG

#import libraries
import arcpy, os, re 

arcpy.env.workspace = r'S:\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb' 

#check last weeks data and remove unnecessary files 
fc1 = "FlightTracksOld" 
fc2 = "FlightTracksNew"
if arcpy.Exists(fc1):
    arcpy.Delete_management(fc1)
    print("FlightTracksOld was deleted")
if arcpy.Exists(fc2):
    arcpy.Delete_management(fc2)
    print("FlightTracksNew was deleted")
else:
    pass
    print("FlightTracksNew and FlightTracksOld were not present")  

#rename FlightTracks to FlightTracks Old 
in_data = "FlightTracks"

out_data = "FlightTracksOld"

if arcpy.Exists(in_data):
    arcpy.Rename_management(in_data, out_data)
    print("FlightTracks has been renamed to FlightTracksOld")
else:
    pass 
    print ("FlightTracks has already been renamed/FlightTracksOld already exists") 

#change work environment to scratch workspace    
output_ws = r'S:\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\Scratch.gdb'
arcpy.env.workspace = output_ws

#Check for spatial reference in point features
#If there is no spatial reference, it will define the projection
#to WGS84 EPSG - 4326 
#If the excel files can be iterated, this section will be removed
sr = arcpy.SpatialReference(4326)

FCList = arcpy.ListFeatureClasses('*')

for fc in FCList:
    spatial_ref = arcpy.Describe(fc).spatialReference
    if spatial_ref.name == "Unknown":
        arcpy.DefineProjection_management(fc, sr)
        print("{0} Spatial Reference as WGS84 now defined!".format(fc))
    else:
        print("{0} : {1} Point FC has Spatial Reference".format(fc, spatial_ref.name)) 

#Once everything has been checked the point to line tool is ran!        
#point to line
lineField = "Filename"
sortField = "ID"
for fc in FCList:
    outfc = os.path.join(output_ws, "{}_line".format(os.path.basename(fc))) 
    arcpy.PointsToLine_management(fc, outfc, lineField, sortField)
    print("All points turned to line features")
#Smooth lines  REQUIRES ADVANCED LICENSE
FCList = arcpy.ListFeatureClasses("*_line")

for fc in FCList:
    outfc = os.path.join(output_ws, "{}_smooth".format(os.path.basename(fc)))
    arcpy.SmoothLine_cartography(fc, outfc, "PAEK", "10000 Meters", "FIXED_CLOSED_ENDPOINT", "NO_CHECK")    
    print("You're a Smooth Criminal!")
#Add and calculate fields
FCList = arcpy.ListFeatureClasses('*_smooth')

#New field and field type
AFields = [
    ("Year", "LONG"),
    ("Month", "LONG"),
    ("Week", "LONG"),
    ("Day", "LONG"),
    ("Current", "TEXT")
]
#Add Fields
for fc in FCList:
    for afc in AFields:
        arcpy.AddField_management(fc, afc[0], afc[1], "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
#Calculate Field Values     
CFields = [
    ("Year", "!Filename![1:5]"),
    ("Month", "!Filename![5:7]"),
    ("Week", "!Filename![9:11]"),
    ("Day", "!Filename![7:9]"),
    ("Current", "'C'")
]           

#Calculate fields   
for fc in FCList: 
    for cfc in CFields:
        arcpy.CalculateField_management(fc, cfc[0], cfc[1], "PYTHON_9.3", "")
        
######################################################
#Creates FlightTracksNewFile
fcs = []   #empty array is filled in with for loop to find all the smooth line features
p = re.compile(".*?_smooth") #wild card to list all smooth line features in scratch
for dirpath, dirnames, filenames in arcpy.da.Walk(output_ws, datatype = "FeatureClass", type = "Polyline"):
    for filename in filenames:
        if p.match (filename) is not None:
            print filename
            fcs.append(os.path.join(dirpath, filename))

outfile = r'S:\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb\FlightTracksNew'

arcpy.Merge_management(fcs, outfile)

#OUTPUT THIS FILE WITH THE GEODATABASE CONNECTED TO THE MAP  NAME IT FlightTracks: NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb 

arcpy.env.workspace = r'S:\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb'

Final_Out = r'S:\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb\FlightTracks'

arcpy.Merge_management(["FlightTracksOld", "FlightTracksNew"], Final_Out)

#X is Old N is previous week / not current C is current - Query out X in definition query once complete(done within ArcMap ToC)
fc = "FlightTracks"
inputField = "Week"
outputField = "Current"
fieldList = [inputField, outputField]

with arcpy.da.SearchCursor(fc, [inputField]) as cursor:  #This makes a list of all the unique values in the 
    myValues = sorted({row[0] for row in cursor})        #week field. Mathematical operations can be performed 

with arcpy.da.UpdateCursor(fc, fieldList) as cursor:
    for row in cursor:
       if row[0]  < (max(myValues) - 1): #For flight tracks older than two weeks - not mapped
           row[1] = "X"    
           cursor.updateRow(row)
       if row[0]  == (max(myValues)-1):  #For flight tracks for the previous week - mapped and coloured grey
           row[1] = "N"    
           cursor.updateRow(row)               

#END of editing for file tracks
