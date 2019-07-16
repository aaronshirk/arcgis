import sys, arcpy, os, tempfile, json, logging, shutil


def updatePointSymbology(layer, sym):
    # Always change to the GraduatedSymbolsRenderer from the SimpleRenderer
    if sym.renderer.type != 'SimpleRenderer':
        sym.updateRenderer('SimpleRenderer')
    sym.updateRenderer('GraduatedSymbolsRenderer')
    sym.renderer.classificationField = 'alert_level'
    sym.renderer.breakCount = 4

    points_labels = ['0 - 1', '> 1 - 2', '> 2 - 3', '> 3 - 4']
    points_upperBounds = [1, 2, 3, 4]
    points_sizes = [6, 16.50, 27, 37.50] 
    layers_colors = [{'RGB': [5, 113, 176, 40]}, {'RGB': [146, 197, 222, 50]},
                       {'RGB': [244, 165, 130, 50]}, {'RGB': [202, 0, 32, 30]}]


    for i in range(4):
        item = sym.renderer.classBreaks[i]
        item.symbol.applySymbolFromGallery('Circle', 1)
        item.label = points_labels[i]
        item.upperBound = points_upperBounds[i]
        item.symbol.size = points_sizes[i]
        item.symbol.color = layers_colors[i]

    # Update point symbology
    layer.symbology = sym
    print("Point symbology complete...")
    
def updatePolySymbology(layer, sym):
    # Always change to the GraduatedSymbolsRenderer from the SimpleRenderer
    if sym.renderer.type != 'SimpleRenderer':
        sym.updateRenderer('SimpleRenderer') 
    sym.updateRenderer('GraduatedColorsRenderer')
    sym.renderer.classificationField = 'alert_level'
    sym.renderer.breakCount = 4

    polygons_labels = ['0 - 1', '> 1 - 2', '> 2 - 3', '> 3 - 4']
    polygons_upperBounds = [1, 2, 3, 4]
    layers_colors = [{'RGB': [5, 113, 176, 40]}, {'RGB': [146, 197, 222, 50]},
                       {'RGB': [244, 165, 130, 50]}, {'RGB': [202, 0, 32, 30]}]

    for i in range(4):
        item = sym.renderer.classBreaks[i]
        item.label = polygons_labels[i]
        item.upperBound = polygons_upperBounds[i]
        item.symbol.color = layers_colors[i]

    # Update polygon symbology
    layer.symbology = sym
    print("Polygon symbology complete...")
    

# Set the default gdb to Live.gdb
print("Setting Live.gdb as default...")
arcpy.env.workspace = os.path.join(r'C:\Users\Aaron\Documents\ArcGIS\Projects\CoralReefWatch', 'Live.gdb')

# Staring symbology update
print("Staring symbology update...")
p = arcpy.mp.ArcGISProject("CURRENT")
m = p.listMaps('Map')[0]



for k in range(2):    
    lyr = m.listLayers('alert_*')[k]
    sym = lyr.symbology

    if lyr.name == 'alert_stations':
        print("Processing alert_station point symbology...")
        updatePointSymbology(lyr, sym)
    else:
        print("Processing alert_area polygon symbology...")
        updatePolySymbology(lyr, sym)

