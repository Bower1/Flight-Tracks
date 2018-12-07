#Title: Flights and Gliders Oct 2018
#Author: Brian Bower
#With assistance from Pat Upson and Diego Ibarra 

#This is the third version of the flight tracks and glider track scripts. This one combines both. 
#The script take all csv files for flights and gliders in one folder, fixes all errors so they can be used in arcgis, 
#calculates the filename and ID fields (this was done manually before), determines if they are a plane or a glider track based once
#names and creates a point feature. These points are then processed with ArcGIS and updates the weekly glider and flight track files. 

#A few more bits of automation will be added to the script. As of now, this version of the script works. 


#import libraries
import arcpy, os, re, glob, pandas as pd, numpy as np 
from pandas import DataFrame

output_ws_plane = r'Q:\IN\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\Scratch.gdb'
    
csv_root = r'Q:\IN\NARightWhale\Monitoring\CSV_Processing'

output_ws_glider = r'Q:\IN\NARightWhale\Monitoring\Glider\Gliders2018\Scratch.gdb'

#clear scratch geodatabases of last weeks intermediate files  
#
#Plane
arcpy.env.workspace = output_ws_plane

FCList = arcpy.ListFeatureClasses('*')

for fc in FCList:
    arcpy.Delete_management(fc)

#Gliders
arcpy.env.workspace = output_ws_glider

FCList = arcpy.ListFeatureClasses('*')

for fc in FCList:
    arcpy.Delete_management(fc)

###CSV correction 
#list all csv's in a folder
csvlist = glob.glob(str(csv_root) + "\*.csv")
#look for dashes
for csv in csvlist: 
    if csv.find("-"):
        newfilename = csv.replace("-", "_")
        os.rename(csv, newfilename) 
#list csv's again to find spaces
csvlist = glob.glob(str(csv_root) + "\*.csv")
#look for spaces         
for csv in csvlist:
    if csv.find(" "):
        newfilename = csv.replace(" ", "_")
        os.rename(csv, newfilename) 

#Finding latest week and adding one to it.         
FlightTrackFC = r'Q:\IN\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb\FlightTracks'
inputField = "Week"
with arcpy.da.SearchCursor(FlightTrackFC, [inputField]) as cursor:
    values = sorted({row[0] for row in cursor})   
    max1 = (max(values) + 1)
    max2 = str(max1)
    

#relist csv files for updated names 
csv_list = glob.glob(str(csv_root) + "\*.csv")

#search for names within csv to descipher if the csv is a flight 
#or glider. If there are more names, they will need to be added to the script.        
for csv in csv_list: 
    if "twin" in csv or "tc_dash" in csv:
        newcsv = os.path.join(csv_root, "Plane_{}".format(os.path.basename(csv)))
        os.rename(csv, newcsv)        
    elif "DAL" in csv or "Fundy" in csv or "otn" in csv or "scotia":
        newcsv = os.path.join(csv_root, "Glider_{}".format(os.path.basename(csv)))
        os.rename(csv, newcsv)   

#search for all plane csv's
csv_plane = glob.glob(str(csv_root) + "\*Plane*.csv")    

#iterate through all plane csv's   
for csv in csv_plane:
    df = pd.read_csv(csv, index_col = 'time') #read csv
    df.rename(columns={'id':'Plane'}, inplace = True) #rename column id to plane
    df.index = np.arange(1, len(df) + 1) #creates numbered index
    df['ID'] = df.index #creates index field
    #Concatenating year, month, day and week 
    Filename = "F" + df.call_sign.str[0:4] + df.call_sign.str[5:7] + df.call_sign.str[8:10] + max2 + "_" 
    #adds plane name to the end of the string
    if "twin" in csv:
        df['Filename'] = Filename + "TwinOtter"
        print df
    elif "tc_dash8" in csv:
        df['Filename'] = Filename + "TC_Dash8"
        print df
    elif "tc_dash7" in csv:
        df['Filename'] = Filename + "TC_Dash7"
        print df
    #write to csv    
    df.to_csv('{}'.format(csv))   

#set work environment for planes 
arcpy.env.workspace = output_ws_plane

#list all plane csv's with new names
csv_plane = glob.glob(str(csv_root) + "\*Plane*.csv")

#write all csv's to point feature classes  
for plane in csv_plane:
    x = "lon"
    y = "lat"
    outlyr = os.path.join(output_ws_plane, "{}_layer".format(plane)) #retains name of input csv for in memory layer
    sr = arcpy.SpatialReference(4326) #Spatial reference for layer will be set to WGS84
    arcpy.MakeXYEventLayer_management(plane, x, y, outlyr, sr, "") #writes in memory layer 
    outfc1 = os.path.join(output_ws_plane, "{}".format(os.path.basename(outlyr))) #make the output name same as layer 
    outfc = outfc1[:-9] #removes .csv_layer 
    arcpy.CopyFeatures_management(outlyr, outfc) #writes point fc  


arcpy.env.workspace = r'Q:\IN\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb' 

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
arcpy.env.workspace = output_ws_plane

FCList = arcpy.ListFeatureClasses('*')

#Once everything has been checked the point to line tool is ran!        
#point to line
lineField = "Filename"
sortField = "ID"
for fc in FCList:
    outfc = os.path.join(output_ws_plane, "{}_line".format(os.path.basename(fc))) 
    arcpy.PointsToLine_management(fc, outfc, lineField, sortField)
    print("All points turned to line features")
#Smooth lines  REQUIRES ADVANCED LICENSE
FCList = arcpy.ListFeatureClasses("*_line")

for fc in FCList:
    outfc = os.path.join(output_ws_plane, "{}_smooth".format(os.path.basename(fc)))
    arcpy.SmoothLine_cartography(fc, outfc, "PAEK", "1000 Meters", "FIXED_CLOSED_ENDPOINT", "NO_CHECK")	
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
for dirpath, dirnames, filenames in arcpy.da.Walk(output_ws_plane, datatype = "FeatureClass", type = "Polyline"):
    for filename in filenames:
	    if p.match (filename) is not None:
		    print filename
		    fcs.append(os.path.join(dirpath, filename))

outfile = r'Q:\IN\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb\FlightTracksNew'

arcpy.Merge_management(fcs, outfile)

#OUTPUT THIS FILE WITH THE GEODATABASE CONNECTED TO THE MAP  NAME IT FlightTracks: NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb 

arcpy.env.workspace = r'Q:\IN\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb'

Final_Out = r'Q:\IN\NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb\FlightTracks'

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

#Process Glider Tracks 


#Find Max Month.     
inputField = "Month"
with arcpy.da.SearchCursor(FlightTrackFC, [inputField]) as cursor:
    values = sorted({row[0] for row in cursor})   
    maxmon = (max(values)) 
    maxmon1 = str(maxmon)

#List all glider track csv files        
csv_glider = glob.glob(str(csv_root) + "\*Glider*.csv")

#iterate through glider csv's
for csv in csv_glider:
    df = pd.read_csv(csv, index_col = 'date') #read csv file
    df.rename(columns={'id':'Glider'}, inplace = True) #rename id to glider
    df.index = np.arange(1, len(df) + 1) #create numbered index 
    df['ID'] = df.index
    df['year'] = df.year.astype(str)
    #concatenates yeah, month and week together
    Filename = "F" + df.year.str[0:4] + maxmon1 + max2 + "_"
    if "DAL" in csv:
        df['Filename'] = Filename + "Dal_Glider"
    elif "dal" in csv:
        df['Filename'] = Filename + "Dal_Glider"    
    elif "Fundy" in csv:
        df['Filename'] = Filename + "Fundy_Glider"
    elif "fundy" in csv:
        df['Filename'] = Filename + "Fundy_Glider"
    elif "OTN" in csv:
        df['Filename'] = Filename + "OTN_Glider"
    elif "Scotia" in csv:
        df['Filename'] = Filename + "Scotia_Glider"    
    print df
    #write to csv
    df.to_csv('{}'.format(csv))    

#convert glider csvs to points
for glider in csv_glider:
    x = "lon"
    y = "lat"
    outlyr = os.path.join(output_ws_glider, "{}_layer".format(glider)) #retains name of input csv for in memory layer
    sr = arcpy.SpatialReference(4326) #Spatial reference for layer will be set to WGS84
    arcpy.MakeXYEventLayer_management(glider, x, y, outlyr, sr, "") #writes in memory layer 
    outfc1 = os.path.join(output_ws_glider, "{}".format(os.path.basename(outlyr))) #make the output name same as layer 
    outfc = outfc1[:-9] #removes .csv_layer 
    arcpy.CopyFeatures_management(outlyr, outfc) #write to point fc 
    
arcpy.env.workspace = r'Q:\IN\NARightWhale\Monitoring\Glider\Gliders2018\GliderTracks_2018.gdb'

#check last weeks data and remove unnecessary files 
fc1 = "GliderTracksOld" 
fc2 = "GliderTracksNew"
if arcpy.Exists(fc1):
    arcpy.Delete_management(fc1)
    print("GliderTracksOld was deleted")
if arcpy.Exists(fc2):
    arcpy.Delete_management(fc2)
    print("GliderTracksNew was deleted")
else:
    pass
    print("GliderTracksNew and GliderTracksOld were not present") 

    
#rename GliderTracks to GliderTracks Old 
in_data = "GliderTracks"

out_data = "GliderTracksOld"

if arcpy.Exists(in_data):
    arcpy.Rename_management(in_data, out_data)
    print("GliderTracks has been renamed to GliderTracksOld")
else:
    pass 
    print ("GliderTracks has already been renamed/GliderTracksOld already exists")     
    
#change workspace    
arcpy.env.workspace = output_ws_glider
FCList = arcpy.ListFeatureClasses(feature_type = 'point')  

lineField = "Filename"
sortField = "ID"
for fc in FCList:
    outfc = os.path.join(output_ws_glider, "{}_line".format(os.path.basename(fc))) 
    arcpy.PointsToLine_management(fc, outfc, lineField, sortField)
    print("All points turned to line features")
#Smooth lines  REQUIRES ADVANCED LICENSE
FCList = arcpy.ListFeatureClasses("*_line")

for fc in FCList:
    outfc = os.path.join(output_ws_glider, "{}_smooth".format(os.path.basename(fc)))
    arcpy.SmoothLine_cartography(fc, outfc, "PAEK", "10000 Meters", "FIXED_CLOSED_ENDPOINT", "NO_CHECK")	
    print("You're a Smooth Criminal!")        
        
#Add and calculate fields
FCList = arcpy.ListFeatureClasses('*_smooth')

AFields = [
    ("Year", "LONG"),
	("StartMonth", "LONG"),
    ("EndMonth", "LONG"),
	("Week", "LONG"),
	("StartDay", "LONG"),
    ("EndDay", "LONG"),
	("Current", "TEXT")
] 

#Add Fields
for fc in FCList:
    for afc in AFields:
        arcpy.AddField_management(fc, afc[0], afc[1], "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
#Calculate Field Values		
CFields = [
    ("Year", "!Filename![1:5]"),
	("StartMonth", "!Filename![5:7]"),
	("Week", "!Filename![7:9]"),
	("Current", "'C'")
]			

#Calculate fields	
for fc in FCList: 
    for cfc in CFields:
        arcpy.CalculateField_management(fc, cfc[0], cfc[1], "PYTHON_9.3", "")      
    
######################################################
#Creates GliderTracksNewFile
fcs = []   #empty array is filled in with for loop to find all the smooth line features
p = re.compile(".*?_smooth") #wild card to list all smooth line features in scratch
for dirpath, dirnames, filenames in arcpy.da.Walk(output_ws_glider, datatype = "FeatureClass", type = "Polyline"):
    for filename in filenames:
        if p.match (filename) is not None:
            print filename
            fcs.append(os.path.join(dirpath, filename))

outfile = r'Q:\IN\NARightWhale\Monitoring\Glider\Gliders2018\GliderTracks_2018.gdb\GliderTracksNew'

arcpy.Merge_management(fcs, outfile)           
        
#OUTPUT THIS FILE WITH THE GEODATABASE CONNECTED TO THE MAP  NAME IT FlightTracks: NARightWhale\Monitoring\WhaleSurveys\AerialTracks2018\AerialTracks_2018.gdb 

arcpy.env.workspace = r'Q:\IN\NARightWhale\Monitoring\Glider\Gliders2018\GliderTracks_2018.gdb'

Final_Out = r'Q:\IN\NARightWhale\Monitoring\Glider\Gliders2018\GliderTracks_2018.gdb\GliderTracks'

arcpy.Merge_management(["GliderTracksOld", "GliderTracksNew"], Final_Out)        
        
#X is Old N is previous week / not current C is current - Query out X in definition query once complete(done within ArcMap ToC)
fc = "GliderTracks"
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
#CHECK YOUR WORK AND MAKE SURE ALL EDITS WERE CORRECT. FIX THE LITTLE THINGS WITHIN AN EDITING SESSION WITHIN
#ARCMAP IF NECESSARY. DO NOT DELETE THE INTERMEDIATE FILES UNTIL YOU ENSURE THAT EVERYTHING IS CORRECT.           
            
    

    