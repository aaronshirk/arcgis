## Overview

ArcGIS mapping project using [NOAA Coral Reef Watch spatial data](https://coralreefwatch.noaa.gov/vs/vs_polygons.json) to visualize risk areas for coral bleaching around the world.   

The spatial data is a raw json file that is downloaded from their [project web site](https://coralreefwatch.noaa.gov/satellite/index.php) and contains point and polygon spacial information for **virtual stations** and their corresponding monitoring areas.  Each of these virtual stations and areas are tagged with a risk level from 1 to 4 (1 being less risk, and 4 being greatest risk).  

This raw data is updated frequently, so the map will become outdated fairly quickly.  This project uses a set of python scripts to quickly recreate the feature layers for stations and areas as well as update their symbology.


## ArcGIS online 

A WebMap of this project is currently hosted on ArcGIS online.
 - [Storm Surge Web Map](https://arcg.is/1WCf5W) 


## Project Components
1. ArcGIS Pro Project file
2. Data Feed Python Script
3. Symbology Update Python Script


## Development and Update Process

Since the spacial data updates frequently, it's necessary to update the data from time to time to keep the map current. The basic steps to do this are:

1. Open the ArcGIS project
2. Open up a terminal or Python terminal and *cd* into the project directory
3. Run the data feed Python script
   ```
   python coralreefx_local.py  https://coralreefwatch.noaa.gov/vs/vs_polygons.json C:\<project-directory>\CoralReefWatch\Work.gdb C:\<project-directory>\CoralReefWatch\Live.gdb

   ```
   - *change any path locations in the command to point to your local directory setup*
   - the script will download the latest data, update the feature layers, and then copy the feature layers into the Live.gdb default geospatial database
  
4. Restart ArcGIS Pro and reload the project in order to refresh the map view with new data
5. Run the symbology update python script if the symbology is messed up
   * the default symbology uses a **SimpleRenderer** which does not add much to the visualization.  The script updates to the GraduatedSymbolRenderer based on **alert_level** field
	