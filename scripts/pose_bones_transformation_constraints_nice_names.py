import bpy

# Main variables
b = ''
map_s = ''
ch_s = ''
map_t = ''
ch_t = ''

# Iterating through all the Armature pose bones finding all the Transformation Constraints that were not renamed in any way
for bone in bpy.context.active_object.pose.bones:
    for con in bone.constraints:
        if "Transformation" in con.name:
            
            # 1st block: Source Bone
            b = con.subtarget.replace("crocodile_father.", "")
            
            # 2nd block: Source Mapping
            if con.map_from == "LOCATION":
                map_s = "Loc"
                if (con.from_min_x != 0 or con.from_max_x != 0):
                    ch_s = "X"
                elif (con.from_min_y != 0 or con.from_max_y != 0):
                    ch_s = "Y"
                elif (con.from_min_z != 0 or con.from_max_z != 0):
                    ch_s = "Z"
            elif con.map_from == "ROTATION":
                map_s = "Rot"
                if (con.from_min_x_rot != 0 or con.from_max_x_rot != 0):
                    ch_s = "X"
                elif (con.from_min_y_rot != 0 or con.from_max_y_rot != 0):
                    ch_s = "Y"
                elif (con.from_min_z_rot != 0 or con.from_max_z_rot != 0):
                    ch_s = "Z"        
            else:
                map_s = "Sc"
                if (con.from_min_x_scale != 0 or con.from_max_x_scale != 0):
                    ch_s = "X"
                elif (con.from_min_y_scale != 0 or con.from_max_y_scale != 0):
                    ch_s = "Y"
                elif (con.from_min_z_scale != 0 or con.from_max_z_scale != 0):
                    ch_s = "Z"
                    
            # 3rd block: Target Mapping
            if con.map_to == "LOCATION":
                map_t = "Loc"
                if (con.to_min_x != 0 or con.to_max_x != 0):
                    ch_t = "X"
                elif (con.to_min_y != 0 or con.to_max_y != 0):
                    ch_t = "Y"
                elif (con.to_min_z != 0 or con.to_max_z != 0):
                    ch_t = "Z"
            elif con.map_to == "ROTATION":
                map_t = "Rot"
                if (con.to_min_x_rot != 0 or con.to_max_x_rot != 0):
                    ch_t = "X"
                elif (con.to_min_y_rot != 0 or con.to_max_y_rot != 0):
                    ch_t = "Y"
                elif (con.to_min_z_rot != 0 or con.to_max_z_rot != 0):
                    ch_t = "Z"        
            else:
                map_t = "Sc"
                if (con.to_min_x_scale != 0 or con.to_max_x_scale != 0):
                    ch_t = "X"
                elif (con.to_min_y_scale != 0 or con.to_max_y_scale != 0):
                    ch_t = "Y"
                elif (con.to_min_z_scale != 0 or con.to_max_z_scale != 0):
                    ch_t = "Z"
            
            
            # Final Transformation Constraint name
            con.name = b + " " + map_s + " " + ch_s + " to " + map_t + " " + ch_t