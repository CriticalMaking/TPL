# Slightly modified from here: https://github.com/peteowlett/b3dBarChart

# import csv reader and blenderpython libraries
import csv
import bpy
import colorsys

# read the CSV data into a csv.reader object
with open('/home/gbby/Documents/Research/Infovis/Toronto/TPL/data/pvol_queen.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    # define looping variables
    i = 0
    j = 0
    
    # create a cube for each bar in the chart and scale to the data point value
    for row in data:
        for cell in row:

            # create a new cube
            bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(i*0.25, j*0.25, 0), rotation=(0, -20.4, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            
            # scale to fit in camera view
            # change the resize values if necessary
            bpy.ops.transform.resize(value=(0.1, 0.1, 0.1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
            
            #### select the uppermost face then transform it in edit mode
            # go into edit mode, deselect all nodes, then go back to object mode
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.editmode_toggle()
            
            # Now in object mode use the data block to select the vertices
            bpy.context.active_object.data.vertices[4].select = True
            bpy.context.active_object.data.vertices[5].select = True
            bpy.context.active_object.data.vertices[6].select = True
            bpy.context.active_object.data.vertices[7].select = True
            
            # Enter edit mode
            bpy.ops.object.editmode_toggle()
                      
            # Move the top face upwards to the desired height for the bar
            bpy.ops.transform.translate(value=(0, 0, float(cell)*.0005), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
            
            # back to object mode
            bpy.ops.object.editmode_toggle()

            # Create a new material
            myMatName = str(i) + '-' + str(j)
            myMat = bpy.data.materials.new(myMatName)
            
            # Set the new material's colour
            # luminence ranges from 90 (dark) to 180 (light)
            # Hue rolls from 0 to 255 in increments of 255/len(row)
            myHSLColors = (j*(1/len(row)),0.5,(90/255)+((90/255)*(i/len(row))))
            myRGBColors = colorsys.hls_to_rgb(myHSLColors[0], myHSLColors[1], myHSLColors[2])
            myMat.diffuse_color = myRGBColors
            
            # should update the material for each individual cross street
            
            # Append the material to the object
            bpy.context.object.data.materials.append(myMat)
            
            # Iterate data point in the loop
            i = i+1
        
        # Iterate to the next y-row and reset x counter    
        j = j+1
        i=0
