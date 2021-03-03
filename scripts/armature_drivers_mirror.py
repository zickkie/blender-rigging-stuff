import bpy

# Naming of "Root" custom properties
src_drv = "_L"
dst_drv = "_R"

# Naming of Bones
src_path = ".L"
dst_path = ".R"

# Main variables
ob = bpy.context.active_object
active = bpy.context.active_pose_bone

# Creating list of unique L-properties of the "Root"        
k = []
for item in active.keys():
    if item != "_RNA_UI" and src_drv in item and item.replace(src_drv, dst_drv) not in active.keys():
        k.append(item)

# Creating corresponding R-properties of the "Root"
for i in range(len(k)): 
    prop = k[i]
    prop_new = prop.replace(src_drv, dst_drv)
    active[prop_new] = active[prop]
    
    active["_RNA_UI"].update({prop_new: {"min": active["_RNA_UI"][prop]["min"], "max": active["_RNA_UI"][prop]["max"], "soft_min": active["_RNA_UI"][prop]["soft_min"], "soft_max": active["_RNA_UI"][prop]["soft_max"]}})
    

### DRIVERS MIRRORING (OBJECT) ###

# Listing all the OBJECT drivers
all = [dr.data_path for dr in ob.animation_data.drivers]

# Iterating through the existing drivers
for dr in ob.animation_data.drivers:
    
    # Searching for the L-drivers
    if src_path in dr.data_path:
        
        ind = dr.array_index
        extrapolation = dr.extrapolation
        
        ## CREATING DICTIONARY OF THE L-DRIVER
        
        # Type and expression
        src_dict = {
            "type": dr.driver.type,
            "expression": dr.driver.expression
            }
        
        variables = len(dr.driver.variables)
        
        # Iterating through the driver's variables
        for i in range(variables):
            src_dict[("var" + str(i) + "_name")] = dr.driver.variables[i].name
            src_dict[("var" + str(i) + "_type")] = dr.driver.variables[i].type
            src_dict[("var" + str(i) + "_targets")] = len(dr.driver.variables[i].targets)
            # Iterating through the variable's targets
            for t in range(src_dict[("var" + str(i) + "_targets")]):
                
                src_dict[("var" + str(i) + str(t) + "_id")] = dr.driver.variables[i].targets[t].id
                src_dict[("var" + str(i) + str(t) + "_data_path")] = dr.driver.variables[i].targets[t].data_path
                src_dict[("var" + str(i) + str(t) + "_id_type")] = dr.driver.variables[i].targets[t].id_type
                src_dict[("var" + str(i) + str(t) + "_bone_target")] = dr.driver.variables[i].targets[t].bone_target
                src_dict[("var" + str(i) + str(t) + "_transform_type")] = dr.driver.variables[i].targets[t].transform_type
                src_dict[("var" + str(i) + str(t) + "_rotation_mode")] = dr.driver.variables[i].targets[t].rotation_mode
                src_dict[("var" + str(i) + str(t) + "_transform_space")] = dr.driver.variables[i].targets[t].transform_space
        
        # Checking for modifiers if necessary (NOTE: only one "Limits" modifier without additional propertis is supported for now)
        mods = len(dr.modifiers)
        if mods > 0:
            
            src_dict["mod_type"] = dr.modifiers[0].type
            src_dict["mute"] = dr.modifiers[0].mute
            src_dict["use_min_x"] = dr.modifiers[0].use_min_x
            src_dict["min_x"] = dr.modifiers[0].min_x
            src_dict["use_min_y"] = dr.modifiers[0].use_min_y
            src_dict["min_y"] = dr.modifiers[0].min_y
            src_dict["use_max_x"] = dr.modifiers[0].use_max_x
            src_dict["max_x"] = dr.modifiers[0].max_x
            src_dict["use_max_y"] = dr.modifiers[0].use_max_y
            src_dict["max_y"] = dr.modifiers[0].max_y
            
        # Writing down driver's F-Curve keyframe points (KPs)
        points = len(dr.keyframe_points)
        for c in range(points):
            # KP Interpolation type
            src_dict[("point" + str(c) + "_interpolation")] = dr.keyframe_points[c].interpolation
            # KP main value
            src_dict[("point" + str(c) + "_co1")] = dr.keyframe_points[c].co[1]
            src_dict[("point" + str(c) + "_co0")] = dr.keyframe_points[c].co[0]
            # KP left handle
            src_dict[("point" + str(c) + "_lh_x")] = dr.keyframe_points[c].handle_left[0]
            src_dict[("point" + str(c) + "_lh_y")] = dr.keyframe_points[c].handle_left[1]
            src_dict[("point" + str(c) + "_lh_type")] = dr.keyframe_points[c].handle_left_type
            # KP right handle
            src_dict[("point" + str(c) + "_rh_x")] = dr.keyframe_points[c].handle_right[0]
            src_dict[("point" + str(c) + "_rh_y")] = dr.keyframe_points[c].handle_right[1]
            src_dict[("point" + str(c) + "_rh_type")] = dr.keyframe_points[c].handle_right_type
            
         
        ## CREATING MIRRORED DRIVER ##
        
        # Checking that this mirrored driver doesn't already exist
        mir_path = dr.data_path.replace(src_path, dst_path)
         
        if mir_path not in all:
            
            # Adding driver
            if mir_path.endswith("location") or mir_path.endswith("rotation") or mir_path.endswith("rotation_euler") or mir_path.endswith("scale"):
                create_driver = ob.driver_add(mir_path, ind)
                drv = create_driver.driver
            else:
                create_driver = ob.driver_add(mir_path, -1)
                drv = create_driver.driver
            # Removig automatically created driver's modifier (it is created instead of keyframe points which are None)
            if len(create_driver.modifiers) > 0:
                for mod in range(len(create_driver.modifiers)):
                    create_driver.modifiers.remove(create_driver.modifiers[mod])
            
            # Type and expression
            drv.type = src_dict["type"]
            drv.expression = src_dict["expression"]
            # Expression: L to R
            if src_drv in drv.expression:
                drv.expression = drv.expression.replace(src_drv, dst_drv)
            
            # Creating driver's variables
            for i in range(variables):

                var = drv.variables.new()
                var.name = src_dict[("var" + str(i) + "_name")]
                # Variable name: L to R
                if src_drv in var.name:
                    var.name = var.name.replace(src_drv, dst_drv)
                var.type = src_dict[("var" + str(i) + "_type")]
                
                # Variable's targets
                for ta in range(src_dict[("var" + str(i) + "_targets")]):
                    
                    if var.type == "SINGLE_PROP":
                        var.targets[ta].id_type = src_dict[("var" + str(i) + str(ta) + "_id_type")]
                    var.targets[ta].id = src_dict[("var" + str(i) + str(ta) + "_id")]
                    var.targets[ta].data_path = src_dict[("var" + str(i) + str(ta) + "_data_path")]
                    # Target's data path: L to R
                    if src_drv in var.targets[ta].data_path:
                        var.targets[ta].data_path = var.targets[ta].data_path.replace(src_drv, dst_drv)
                    if src_path in var.targets[ta].data_path:
                        var.targets[ta].data_path = var.targets[ta].data_path.replace(src_path, dst_path)
                    var.targets[ta].bone_target = src_dict[("var" + str(i) + str(ta) + "_bone_target")]
                    # Target's bone target: L to R
                    if src_drv in var.targets[ta].bone_target:
                        var.targets[ta].bone_target = var.targets[ta].bone_target.replace(src_drv, dst_drv)
                    if src_path in var.targets[ta].bone_target:
                        var.targets[ta].bone_target = var.targets[ta].bone_target.replace(src_path, dst_path)

                    var.targets[ta].transform_type = src_dict[("var" + str(i) + str(ta) + "_transform_type")]
                    var.targets[ta].rotation_mode = src_dict[("var" + str(i) + str(ta) + "_rotation_mode")]
                    var.targets[ta].transform_space = src_dict[("var" + str(i) + str(ta) + "_transform_space")]
            
            # Creating driver's modifier
            if mods > 0:
                limits = create_driver.modifiers.new("LIMITS")
                limits.mute = src_dict["mute"]
                limits.use_min_x = src_dict["use_min_x"]
                limits.min_x = src_dict["min_x"]
                limits.use_min_y = src_dict["use_min_y"]
                limits.min_y = src_dict["min_y"]
                limits.use_max_x = src_dict["use_max_x"]
                limits.max_x = src_dict["max_x"]
                limits.use_max_y = src_dict["use_max_y"]
                limits.max_y = src_dict["max_y"]
            
            # Creating driver's KPs
            create_driver.keyframe_points.add(count = points)
            for c in range(points):
                # KP Interpolation type
                create_driver.keyframe_points[c].interpolation = src_dict[("point" + str(c) + "_interpolation")]
                # KP main value
                create_driver.keyframe_points[c].co[1] = src_dict[("point" + str(c) + "_co1")]
                create_driver.keyframe_points[c].co[0] = src_dict[("point" + str(c) + "_co0")]
                # KP left handle
                create_driver.keyframe_points[c].handle_left[0] = src_dict[("point" + str(c) + "_lh_x")]
                create_driver.keyframe_points[c].handle_left[1] = src_dict[("point" + str(c) + "_lh_y")]
                create_driver.keyframe_points[c].handle_left_type = src_dict[("point" + str(c) + "_lh_type")]
                # KP right handle
                create_driver.keyframe_points[c].handle_right[0] = src_dict[("point" + str(c) + "_rh_x")]
                create_driver.keyframe_points[c].handle_right[1] = src_dict[("point" + str(c) + "_rh_y")]
                create_driver.keyframe_points[c].handle_right_type = src_dict[("point" + str(c) + "_rh_type")]
            
            # Driver's FCurve extrapolation type
            create_driver.extrapolation = extrapolation

        
### DRIVERS MIRRORING (OBJECT DATA) ###

# Listing all the OBJECT DATA drivers
all = [dr.data_path for dr in ob.data.animation_data.drivers]

# Iterating through the existing drivers
for dr in ob.data.animation_data.drivers:
    
    # Searching for the L-drivers
    if src_path in dr.data_path:
        
        ind = dr.array_index
        extrapolation = dr.extrapolation
        
        ## CREATING DICTIONARY OF THE L-DRIVER
        
        # Type and expression
        src_dict = {
            "type": dr.driver.type,
            "expression": dr.driver.expression
            }
        
        variables = len(dr.driver.variables)
        
        # Iterating through the driver's variables
        for i in range(variables):
            src_dict[("var" + str(i) + "_name")] = dr.driver.variables[i].name
            src_dict[("var" + str(i) + "_type")] = dr.driver.variables[i].type
            src_dict[("var" + str(i) + "_targets")] = len(dr.driver.variables[i].targets)
            # Iterating through the variable's targets
            for t in range(src_dict[("var" + str(i) + "_targets")]):
                
                src_dict[("var" + str(i) + str(t) + "_id")] = dr.driver.variables[i].targets[t].id
                src_dict[("var" + str(i) + str(t) + "_data_path")] = dr.driver.variables[i].targets[t].data_path
                src_dict[("var" + str(i) + str(t) + "_id_type")] = dr.driver.variables[i].targets[t].id_type
                src_dict[("var" + str(i) + str(t) + "_bone_target")] = dr.driver.variables[i].targets[t].bone_target
                src_dict[("var" + str(i) + str(t) + "_transform_type")] = dr.driver.variables[i].targets[t].transform_type
                src_dict[("var" + str(i) + str(t) + "_rotation_mode")] = dr.driver.variables[i].targets[t].rotation_mode
                src_dict[("var" + str(i) + str(t) + "_transform_space")] = dr.driver.variables[i].targets[t].transform_space
        
        # Checking for modifiers if necessary (NOTE: only one "Limits" modifier without additional propertis is supported for now)
        mods = len(dr.modifiers)
        if mods > 0:
            
            src_dict["mod_type"] = dr.modifiers[0].type
            src_dict["mute"] = dr.modifiers[0].mute
            src_dict["use_min_x"] = dr.modifiers[0].use_min_x
            src_dict["min_x"] = dr.modifiers[0].min_x
            src_dict["use_min_y"] = dr.modifiers[0].use_min_y
            src_dict["min_y"] = dr.modifiers[0].min_y
            src_dict["use_max_x"] = dr.modifiers[0].use_max_x
            src_dict["max_x"] = dr.modifiers[0].max_x
            src_dict["use_max_y"] = dr.modifiers[0].use_max_y
            src_dict["max_y"] = dr.modifiers[0].max_y
            
        # Writing down driver's F-Curve keyframe points (KPs)
        points = len(dr.keyframe_points)
        for c in range(points):
            # KP Interpolation type
            src_dict[("point" + str(c) + "_interpolation")] = dr.keyframe_points[c].interpolation
            # KP main value
            src_dict[("point" + str(c) + "_co1")] = dr.keyframe_points[c].co[1]
            src_dict[("point" + str(c) + "_co0")] = dr.keyframe_points[c].co[0]
            # KP left handle
            src_dict[("point" + str(c) + "_lh_x")] = dr.keyframe_points[c].handle_left[0]
            src_dict[("point" + str(c) + "_lh_y")] = dr.keyframe_points[c].handle_left[1]
            src_dict[("point" + str(c) + "_lh_type")] = dr.keyframe_points[c].handle_left_type
            # KP right handle
            src_dict[("point" + str(c) + "_rh_x")] = dr.keyframe_points[c].handle_right[0]
            src_dict[("point" + str(c) + "_rh_y")] = dr.keyframe_points[c].handle_right[1]
            src_dict[("point" + str(c) + "_rh_type")] = dr.keyframe_points[c].handle_right_type
            
        
        ## CREATING MIRRORED DRIVER ##
        
        # Checking that this mirrored driver doesn't already exist
        mir_path = dr.data_path.replace(src_path, dst_path)
         
        if mir_path not in all:
            
            # Adding driver
            if mir_path.endswith("location") or mir_path.endswith("rotation") or mir_path.endswith("rotation_euler") or mir_path.endswith("scale"):
                create_driver = ob.data.driver_add(mir_path, ind)
                drv = create_driver.driver
            else:
                create_driver = ob.data.driver_add(mir_path, -1)
                drv = create_driver.driver
            # Removig automatically created driver's modifier (it is created instead of keyframe points which are None)
            create_driver.modifiers.remove(create_driver.modifiers[0])
            
            # Type and expression
            drv.type = src_dict["type"]
            drv.expression = src_dict["expression"]
            # Expression: L to R
            if src_drv in drv.expression:
                drv.expression = drv.expression.replace(src_drv, dst_drv)
            
            # Creating driver's variables
            for i in range(variables):

                var = drv.variables.new()
                var.name = src_dict[("var" + str(i) + "_name")]
                # Variable name: L to R
                if src_drv in var.name:
                    var.name = var.name.replace(src_drv, dst_drv)
                var.type = src_dict[("var" + str(i) + "_type")]
                
                # Variable's targets
                for ta in range(src_dict[("var" + str(i) + "_targets")]):
                    
                    if var.type == "SINGLE_PROP":
                        var.targets[ta].id_type = src_dict[("var" + str(i) + str(ta) + "_id_type")]
                    var.targets[ta].id = src_dict[("var" + str(i) + str(ta) + "_id")]
                    var.targets[ta].data_path = src_dict[("var" + str(i) + str(ta) + "_data_path")]
                    # Target's data path: L to R
                    if src_drv in var.targets[ta].data_path:
                        var.targets[ta].data_path = var.targets[ta].data_path.replace(src_drv, dst_drv)
                    if src_path in var.targets[ta].data_path:
                        var.targets[ta].data_path = var.targets[ta].data_path.replace(src_path, dst_path)
                    var.targets[ta].bone_target = src_dict[("var" + str(i) + str(ta) + "_bone_target")]
                    # Target's bone target: L to R
                    if src_drv in var.targets[ta].bone_target:
                        var.targets[ta].bone_target = var.targets[ta].bone_target.replace(src_drv, dst_drv)
                    if src_path in var.targets[ta].bone_target:
                        var.targets[ta].bone_target = var.targets[ta].bone_target.replace(src_path, dst_path)

                    var.targets[ta].transform_type = src_dict[("var" + str(i) + str(ta) + "_transform_type")]
                    var.targets[ta].rotation_mode = src_dict[("var" + str(i) + str(ta) + "_rotation_mode")]
                    var.targets[ta].transform_space = src_dict[("var" + str(i) + str(ta) + "_transform_space")]
            
            # Creating driver's modifier
            if mods > 0:
                limits = create_driver.modifiers.new("LIMITS")
                limits.mute = src_dict["mute"]
                limits.use_min_x = src_dict["use_min_x"]
                limits.min_x = src_dict["min_x"]
                limits.use_min_y = src_dict["use_min_y"]
                limits.min_y = src_dict["min_y"]
                limits.use_max_x = src_dict["use_max_x"]
                limits.max_x = src_dict["max_x"]
                limits.use_max_y = src_dict["use_max_y"]
                limits.max_y = src_dict["max_y"]
            
            # Creating driver's KPs
            create_driver.keyframe_points.add(count = points)
            for c in range(points):
                # KP Interpolation type
                create_driver.keyframe_points[c].interpolation = src_dict[("point" + str(c) + "_interpolation")]
                # KP main value
                create_driver.keyframe_points[c].co[1] = src_dict[("point" + str(c) + "_co1")]
                create_driver.keyframe_points[c].co[0] = src_dict[("point" + str(c) + "_co0")]
                # KP left handle
                create_driver.keyframe_points[c].handle_left[0] = src_dict[("point" + str(c) + "_lh_x")]
                create_driver.keyframe_points[c].handle_left[1] = src_dict[("point" + str(c) + "_lh_y")]
                create_driver.keyframe_points[c].handle_left_type = src_dict[("point" + str(c) + "_lh_type")]
                # KP right handle
                create_driver.keyframe_points[c].handle_right[0] = src_dict[("point" + str(c) + "_rh_x")]
                create_driver.keyframe_points[c].handle_right[1] = src_dict[("point" + str(c) + "_rh_y")]
                create_driver.keyframe_points[c].handle_right_type = src_dict[("point" + str(c) + "_rh_type")]
            
            # Driver's FCurve extrapolation type
            create_driver.extrapolation = extrapolation


### UPDATING ALL THE DRIVERS ###
for driver in ob.animation_data.drivers:
    driver.driver.expression += " "
    driver.driver.expression = driver.driver.expression[:-1]
for driver in ob.data.animation_data.drivers:
    driver.driver.expression += " "
    driver.driver.expression = driver.driver.expression[:-1]