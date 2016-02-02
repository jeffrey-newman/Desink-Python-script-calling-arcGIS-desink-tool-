


# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *


# Set environment settings
# env.workspace = "C:/sapyexamples/data"



# Name: FlowDirection_Example.py
# Description: Creates a raster of flow direction from each cell to its
#    steepest downslope neighbor.
# Requirements: Spatial Analyst Extension
# Author: ESRI
#
#Name: Sink_Ex_02.py
# Description: Creates a raster identifying all sinks or areas of internal drainage.
# Requirements: Spatial Analyst Extension
# Author: ESRI


# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

def sink_and_flow_direction(results_directory, base_dem):

    # Execute FlowDirection
    outFlowDirection = FlowDirection(base_dem, "NORMAL")
    
    # Save the output 
    flow_dir_name = results_directory + "\\dem-incised-flowdirection.tif"
    outFlowDirection.save(flow_dir_name)
    
    # Execute Sinks
    outSink = Sink(outFlowDirection)
    
    # Save the output 
    sinks_name = results_directory + "\\dem-incised-sinks.tif"
    outSink.save(sinks_name)
    
    # Execute Fill
    outFill = Fill(base_dem)
    
    # Save the output 
    fill_name = results_directory + "\\dem-incised-fill.tif"
    outFill.save(fill_name)
    
    # Execute FlowDirection
    outFlowDirection_fill = FlowDirection(outFill, "NORMAL")
    
    # Save the output 
    flow_dir_fill_name = results_directory + "\\dem-incised-fill-flowdirection.tif"
    outFlowDirection_fill.save(flow_dir_fill_name)
    
    # Execute Sinks
    outSink = Sink(outFlowDirection_fill)
    
    # Save the output 
    sinks_fill_name = results_directory + "\\dem-incised-fill-sinks.tif"
    outSink.save(sinks_fill_name)
    
    return None
    
## 1 m DEM
#base_dem_1m = "C:\\Users\\a1091793\\Modelling\\Patawalonga flood\\1m resolution\\Incised DEM and graph\\incised-dem.tif"
#results_directory_1m = "C:\\Users\\a1091793\\Modelling\\Patawalonga flood\\1m resolution\\Flow Direction and Filled DEM"
#sink_and_flow_direction(results_directory_1m, base_dem_1m)
#
## 3 m - min DEM
#base_dem_3m_min = "C:\\Users\\a1091793\\Modelling\\Patawalonga flood\\3m resolution\\3m - min - DEM\\Incised DEM and graph\\incised-dem.tif"
#results_directory_3m_min = "C:\\Users\\a1091793\\Modelling\\Patawalonga flood\\3m resolution\\3m - min - DEM\\Flow Direction and Filled DEM 2"
#sink_and_flow_direction(results_directory_3m_min, base_dem_3m_min)

# 3 m - mean DEM
base_dem_3m_mean = "C:\\Users\\a1091793\\Modelling\\Patawalonga flood\\3m resolution\\3m - mean - DEM\\Incised DEM and graph\\incised-dem.tif"
results_directory_3m_mean = "C:\\Users\\a1091793\\Modelling\\Patawalonga flood\\3m resolution\\3m - mean - DEM\\Flow Direction and Filled DEM 2"
sink_and_flow_direction(results_directory_3m_mean, base_dem_3m_mean)
