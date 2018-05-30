###This script will move all files from the workspace 
###to the Table of Contents in order and in the correct 
###groups. The fcs will have all symbology added from layer files
###The fcs will be ordered, grouped, groups saved as layer files,
###all files removed and groups readded in order
###Author: Brian Bower with help from Phillip Greyson
###Date: July 14th, 2017

#import arcpy os time and glob
import arcpy, os, glob, time 

#set workspace 
ws = r'D:\ADAPT\ADAPT_Canada_Atlantic_2016\Data\rPED.gdb'

arcpy.env.workspace  = ws 

#define mxd and dataframe 
mxd = arcpy.mapping.MapDocument("Current")
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

#define time 
start = time.time()

#define empty layer 
emp_grp_lyr = r'D:\ADAPT\Processing\EmptyGroupLayers' 

#add empty group layers to map with glob 
lyr_list = glob.glob(str(emp_grp_lyr) + "\*.lyr")
arcpy.AddMessage("Lyr List: ")

for lyr in lyr_list:
    addLayer = arcpy.mapping.Layer(lyr)
    arcpy.mapping.AddLayer(df, addLayer, "Bottom")
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'  
####################SP0010###############################################################   
#add SP0010 and symbology 

sym = arcpy.mapping.Layer(r'D:\ADAPT\Processing\LayerFiles\SP0010.lyr')

fclist = arcpy.ListFeatureClasses("*010")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
###add SP0011 to toc    
sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0011.lyr")

fclist = arcpy.ListFeatureClasses("*011")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
##add SP0012 to toc
sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0012.lyr")

fclist = arcpy.ListFeatureClasses("*012")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0013 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0013.lyr")

fclist = arcpy.ListFeatureClasses("*013")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0014 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0014.lyr")

fclist = arcpy.ListFeatureClasses("*014")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0015 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0015.lyr")

fclist = arcpy.ListFeatureClasses("*015")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0016 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0016.lyr")

fclist = arcpy.ListFeatureClasses("*016")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0023 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0023.lyr")

fclist = arcpy.ListFeatureClasses("*023")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0030 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0030.lyr")

fclist = arcpy.ListFeatureClasses("*030")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0031 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0031.lyr")

fclist = arcpy.ListFeatureClasses("*031")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0040 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0040.lyr")

fclist = arcpy.ListFeatureClasses("*040")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0041 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0041.lyr")

fclist = arcpy.ListFeatureClasses("*041")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0042 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0042.lyr")

fclist = arcpy.ListFeatureClasses("*042")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP043 to toc   
sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0043.lyr")

fclist = arcpy.ListFeatureClasses("*043")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0044 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0044.lyr")

fclist = arcpy.ListFeatureClasses("*044")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0050 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0050.lyr")

fclist = arcpy.ListFeatureClasses("*050")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0051 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0051.lyr")

fclist = arcpy.ListFeatureClasses("*051")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0052 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0052.lyr")

fclist = arcpy.ListFeatureClasses("*052")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0060 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0060.lyr")

fclist = arcpy.ListFeatureClasses("*060")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0061 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0061.lyr")

fclist = arcpy.ListFeatureClasses("*061")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0062 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0062.lyr")

fclist = arcpy.ListFeatureClasses("*062")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0064 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0064.lyr")

fclist = arcpy.ListFeatureClasses("*064")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0070 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0070.lyr")

fclist = arcpy.ListFeatureClasses("*070")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0112 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0112.lyr")

fclist = arcpy.ListFeatureClasses("*0112")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0114 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0114.lyr")

fclist = arcpy.ListFeatureClasses("*0114")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0118 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0118.lyr")

fclist = arcpy.ListFeatureClasses("*0118")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0122 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0122.lyr")

fclist = arcpy.ListFeatureClasses("*0122")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0123 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0123.lyr")

fclist = arcpy.ListFeatureClasses("*0123")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0141 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0141.lyr")

fclist = arcpy.ListFeatureClasses("*0141")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0142 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0142.lyr")

fclist = arcpy.ListFeatureClasses("*0142")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0143 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0143.lyr")

fclist = arcpy.ListFeatureClasses("*0143")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0160 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0160.lyr")

fclist = arcpy.ListFeatureClasses("*0160")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0200 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0200.lyr")

fclist = arcpy.ListFeatureClasses("*0200")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0201 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0201.lyr")

fclist = arcpy.ListFeatureClasses("*0201")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0202 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0202.lyr")

fclist = arcpy.ListFeatureClasses("*0202")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0203 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0203.lyr")

fclist = arcpy.ListFeatureClasses("*0203")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'

#add SP0204 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0204.lyr")

fclist = arcpy.ListFeatureClasses("*0204")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0216 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0216.lyr")

fclist = arcpy.ListFeatureClasses("*0216")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0220 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0220.lyr")

fclist = arcpy.ListFeatureClasses("*0220")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0221 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0221.lyr")

fclist = arcpy.ListFeatureClasses("*0221")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0241 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0241.lyr")

fclist = arcpy.ListFeatureClasses("*0241")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0300 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0300.lyr")

fclist = arcpy.ListFeatureClasses("*0300")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0304 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0304.lyr")

fclist = arcpy.ListFeatureClasses("*0304")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0320 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0320.lyr")

fclist = arcpy.ListFeatureClasses("*0320")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0350 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0350.lyr")

fclist = arcpy.ListFeatureClasses("*0350")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0400 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0400.lyr")

fclist = arcpy.ListFeatureClasses("*0400")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0409 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0409.lyr")

fclist = arcpy.ListFeatureClasses("*0409")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0410 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0410.lyr")

fclist = arcpy.ListFeatureClasses("*0410")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0411 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0411.lyr")

fclist = arcpy.ListFeatureClasses("*0411")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0412 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0412.lyr")

fclist = arcpy.ListFeatureClasses("*0412")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0413 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0413.lyr")

fclist = arcpy.ListFeatureClasses("*0413")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
mxd.save();
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0414 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0414.lyr")

fclist = arcpy.ListFeatureClasses("*0414")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0501 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0501.lyr")

fclist = arcpy.ListFeatureClasses("*0501")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer   
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
#add SP0502 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0502.lyr")

fclist = arcpy.ListFeatureClasses("*0502")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0610 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0610.lyr")

fclist = arcpy.ListFeatureClasses("*0610")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0622 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0622.lyr")

fclist = arcpy.ListFeatureClasses("*0622")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0623 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0623.lyr")

fclist = arcpy.ListFeatureClasses("*0623")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0630 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0630.lyr")

fclist = arcpy.ListFeatureClasses("*0630")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
    
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0640 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0640.lyr")

fclist = arcpy.ListFeatureClasses("*0640")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0647 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0647.lyr")

fclist = arcpy.ListFeatureClasses("*0647")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0701 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0701.lyr")

fclist = arcpy.ListFeatureClasses("*0701")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP0704 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP0704.lyr")

fclist = arcpy.ListFeatureClasses("*0704")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
#add SP2550 and symbology 

sym = arcpy.mapping.Layer(r"D:\ADAPT\Processing\LayerFiles\SP2550.lyr")

fclist = arcpy.ListFeatureClasses("*2550")
 
for fc in fclist:
    FC = os.path.join(ws, "", fc)
    layer = arcpy.mapping.Layer(fc)
    layer.visible = False
    arcpy.mapping.AddLayer(df, layer, "TOP")
    arcpy.ApplySymbologyFromLayer_management(fc, sym)
    del layer
mxd.save(); 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
##############################################
###########################################

####Order all layers in the table of contents
group_layer = [lyr for lyr in arcpy.mapping.ListLayers(mxd) if lyr.isGroupLayer][0]
lyr_names = sorted(lyr.name for lyr in arcpy.mapping.ListLayers(mxd) if lyr.isFeatureLayer) 
for name in lyr_names:
    arcpy.mapping.MoveLayer(df, group_layer, arcpy.mapping.ListLayers(mxd, name)[0], "BEFORE")
mxd.save(); 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs'
####################SP0010####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*010", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Cod_Atlantic", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*010", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Cod_Atlantic", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*010", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Cod_Atlantic", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
####################SP0011####################################################################
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*011", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Haddock", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*011", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Haddock", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*011", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Haddock", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")
####################SP0012####################################################################
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*012", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_White_Hake", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*012", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_White_Hake", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*012", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_White_Hake", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")
    
####################SP0013####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*013", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Squirrel_Or_Red_Hake", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*013", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Squirrel_Or_Red_Hake", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*013", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Squirrel_Or_Red_Hake", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0014####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*014", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Silver_Hake", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*014", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Silver_Hake", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*014", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Silver_Hake", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0015####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*015", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Cusk", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*015", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Cusk", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*015", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Cusk", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  

####################SP0016####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*016", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Pollock", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*016", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Pollock", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*016", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Pollock", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0023####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*023", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Redfish_Unseparated", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*023", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Redfish_Unseparated", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*023", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Redfish_Unseparated", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0030####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*030", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Halibut_Atlantic", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*030", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Halibut_Atlantic", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*030", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Halibut_Atlantic", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0031####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*031", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Turbot_GreenlandHalibut", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*031", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Turbot_GreenlandHalibut", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*031", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Turbot_GreenlandHalibut", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")
mxd.save();     
####################SP0040####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*040", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_American_Plaice", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*040", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_American_Plaice", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*040", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_American_Plaice", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0041####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*041", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Witch_Flounder", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*041", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Witch_Flounder", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*041", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Witch_Flounder", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0042####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*042", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Yellowtail_Flounder", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*042", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Yellowtail_Flounder", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*042", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Yellowtail_Flounder", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0043####################################################################  
#add SP0043 and symbology 
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*043", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Winter_Flounder", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*043", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Winter_Flounder", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*043", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Winter_Flounder", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0044####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*044", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Gulf_Stream_Flounder", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*044", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Gulf_Stream_Flounder", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*044", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Gulf_Stream_Flounder", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0050####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*050", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Striped_Atlantic_Wolffish", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*050", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Striped_Atlantic_Wolffish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*050", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Striped_Atlantic_Wolffish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0051####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*051", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Spotted_Wolffish", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*051", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Spotted_Wolffish", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*051", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Spotted_Wolffish", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0052####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*052", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Northern_Wolffish", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*052", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Northern_Wolffish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*052", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Northern_Wolffish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0060####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*060", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Herring_Atlantic", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*060", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Herring_Atlantic", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*060", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Herring_Atlantic", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0061####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*061", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Shad_American", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*061", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Shad_American", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*061", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Shad_American", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0062####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*062", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Alewife", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*062", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Alewife", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*062", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Alewife", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")
    
####################SP0064####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*064", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Capelin", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*064", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Capelin", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*064", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Capelin", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0070####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*070", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Mackerel_Atlantic", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*070", df)    
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Mackerel_Atlantic", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*070", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Mackerel_Atlantic", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0112####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0112", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Longfin_Hake", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0112", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Longfin_Hake", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0112", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Longfin_Hake", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0114####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0114", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Fourbeard_Rockling", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0114", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Fourbeard_Rockling", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0114", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Fourbeard_Rockling", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0118####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0118", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Greenland_Cod", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0118", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Greenland_Cod", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0118", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Greenland_Cod", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
    
####################SP0122####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0122", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Cunner", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0122", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Cunner", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0122", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Cunner", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0123####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0123", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Rosefish_BlackBelly", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0123", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Rosefish_BlackBelly", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0123", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Rosefish_BlackBelly", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0141####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0141", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Summer_Flounder", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0141", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Summer_Flounder", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0141", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Summer_Flounder", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0142####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0142", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Fourspot_Flounder", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0142", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Fourspot_Flounder", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0142", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Fourspot_Flounder", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0143####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0143", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Brill_Windowpane", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0143", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Brill_Windowpane", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0143", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Brill_Windowpane", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0160####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0160", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Argentine_Atlantic", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0160", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Argentine_Atlantic", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0160", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Argentine_Atlantic", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0200####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0200", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Barndoor_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0200", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Barndoor_Skate", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0200", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Barndoor_Skate", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0201####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0201", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Thorny_Skate", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0201", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Thorny_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0201", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Thorny_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0202####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0202", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Smooth_Skate", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0202", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Smooth_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0202", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Smooth_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0203####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0203", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Little_Skate", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0203", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Little_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0203", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Little_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0204####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0204", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Winter_Skate", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0204", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Winter_Skate ", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0204", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Winter_Skate", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")      
    
####################SP0216####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0216", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Atlantic_Torpedo", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0216", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Atlantic_Torpedo", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0216", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Atlantic_Torpedo", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")      
    
####################SP0220####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0220", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Spiny_Dogfish", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0220", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Spiny_Dogfish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0220", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Spiny_Dogfish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  

####################SP0221####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0221", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Black_Dogfish", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0221", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Black_Dogfish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0221", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Black_Dogfish", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  

####################SP0241####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0241", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Northern_Hagfish", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0241", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Northern_Hagfish", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0241", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Northern_Hagfish", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
mxd.save();
####################SP0300####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0300", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Longhorn_Sculpin", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0300", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Longhorn_Sculpin", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0300", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Longhorn_Sculpin", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  

####################SP0304####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0304", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Mailed_Scuplin", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0304", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Mailed_Scuplin", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0304", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Mailed_Scuplin", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0320####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0320", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Sea_Raven", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0320", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Sea_Raven", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0320", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Sea_Raven", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0350####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0350", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Atlantic_Sea_Poacher", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0350", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Atlantic_Sea_Poacher", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0350", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Atlantic_Sea_Poacher", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0400####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0400", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Monkfish_Goosefish_Angler", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0400", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Monkfish_Goosefish_Angler", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0400", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Monkfish_Goosefish_Angler", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0409####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0409", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_American_Straptail_Grenadier", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0409", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_American_Straptail_Grenadier", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0409", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_American_Straptail_Grenadier", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0410####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0410", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Marlin-Spike_Grenadier", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0410", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Marlin-Spike_Grenadier", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0410", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Marlin-Spike_Grenadier", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0411####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0411", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Roughhead_Grenadier", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0411", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Roughhead_Grenadier", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0411", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Roughhead_Grenadier", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")
    
####################SP0412####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0412", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Roughnose_Grenadier", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0412", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Roughnose_Grenadier", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0412", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Roughnose_Grenadier", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0413####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0413", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Longnose_Grenadier", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0413", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Longnose_Grenadier", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0413", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Longnose_Grenadier", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0414####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0414", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Roundnose_Grenadier", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0414", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Roundnose_Grenadier", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0414", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Roundnose_Grenadier", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

####################SP0501####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0501", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Lumpfish", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0501", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Lumpfish", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0501", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Lumpfish", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0502####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0502", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Atlantic_Spiny_Lumpsucker", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0502", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Atlantic_Spiny_Lumpsucker", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0502", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Atlantic_Spiny_Lumpsucker", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0610####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0610", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Northern_Sand_Lance", df)[0]     
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0610", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Northern_Sand_Lance", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0610", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Northern_Sand_Lance", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0622####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0622", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Snake_Blenny", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0622", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Snake_Blenny", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0622", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Snake_Blenny", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0623####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0623", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Daubed_Shanny", df)[0]   
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0623", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Daubed_Shanny", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0623", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Daubed_Shanny", df)[0] 
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0630####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0630", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Wrymouth", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0630", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Wrymouth", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0630", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Wrymouth", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0640####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0640", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Ocean_Pout", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0640", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Ocean_Pout", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0640", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Ocean_Pout", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0647####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0647", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Shorttailed_Eelpout_Vahl", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0647", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Shorttailed_Eelpout_Vahl", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0647", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Shorttailed_Eelpout_Vahl", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0701####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0701", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Butterfish", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0701", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Butterfish", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0701", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Butterfish", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP0704####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*0704", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_American_John_Dory", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*0704", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_American_John_Dory", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*0704", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_American_John_Dory", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
    
####################SP2550####################################################################  
#Move layers to groups 
ls = arcpy.mapping.ListLayers(mxd, "FALL*2550", df)
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Fall_Atlantic_Lobster", df)[0]    
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SPRING*2550", df)   
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Spring_Atlantic_Lobster", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")

ls = arcpy.mapping.ListLayers(mxd, "SUMMER*2550", df) 
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Summer_Atlantic_Lobster", df)[0]  
for lyr in ls:
    arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, lyr, "BOTTOM")  
mxd.save();
############GroupLayers##############
#output for new group layers    
grp_layer_path = r'D:\ADAPT\Processing\GroupLayers'

#list and write group layers to folder

for grp_lyr in arcpy.mapping.ListLayers(mxd):
    if grp_lyr.isGroupLayer:
    outlyr = os.path.join(grp_layer_path, grp_lyr.name)
    outlyr = outlyr + ".lyr"
        arcpy.SaveToLayerFile_management(grp_lyr, outlyr, "RELATIVE")
        
######Remove all layers from TOC. This will remove the duplicates for later
for lyr in arcpy.mapping.ListLayers(mxd):
    arcpy.mapping.RemoveLayer(df, lyr)
    
#list all layers written to layer path  
lyr_list = glob.glob(str(grp_layer_path) + "\*.lyr")
arcpy.AddMessage("Lyr List: ") 

#add all groups to TOC
for layer in lyr_list:
    addLayer = arcpy.mapping.Layer(layer)
    arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")  
        

#refrech active view, TOC and del MXD   
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
mxd.save()
del mxd 
print 'Processing time:', int((time.time()-start)/60), 'mins, ',
int((time.time()-start)%60), 'secs' 
