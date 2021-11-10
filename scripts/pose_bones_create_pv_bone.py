import bpy

def create_pv_bone():
    
    ob = bpy.context.active_object
    mode = ob.mode
    
    select_list = [bone.name for bone in bpy.context.selected_pose_bones]
    active_bone = ob.data.bones.active
    
    if not ob.animation_data:
        ob.animation_data.create()
    
    for bone in bpy.context.selected_pose_bones:
        
        rot_mode = bone.rotation_mode
        bone.rotation_mode = 'XYZ'

        for i in range(4):
            
            # Bone duplicating
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.armature.select_all(action='DESELECT')
            ob.data.edit_bones[bone.name].select = True
            ob.data.edit_bones[bone.name].select_head  = True
            ob.data.edit_bones[bone.name].select_tail  = True
            ob.data.edit_bones.active = ob.data.edit_bones[bone.name]
            
            connect = ob.data.edit_bones[bone.name].use_connect
            if connect:
                ob.data.edit_bones[bone.name].use_connect = False
            
            bpy.ops.armature.duplicate(do_flip_names=False)
            
            if connect:
                ob.data.edit_bones[bone.name].use_connect = True
            
            
            
            # Bone naming
            suffix = ("PV_0" + str(i) + "_")
            bpy.context.active_bone.name = suffix + bone.name
            name_new = bpy.context.active_bone.name
            
            bpy.context.active_bone.length = ob.data.edit_bones[bone.name].length * 0.75
            bpy.context.active_bone.bbone_x = ob.data.edit_bones[bone.name].bbone_x * 0.5
            bpy.context.active_bone.bbone_z = ob.data.edit_bones[bone.name].bbone_z * 0.5
            bpy.context.active_bone.parent = ob.data.edit_bones[bone.name]
            bpy.context.active_bone.use_connect = False
            
            # Pose aligning
            bpy.ops.object.mode_set(mode='POSE')
            ob.pose.bones[name_new].rotation_mode = bone.rotation_mode
            
            if i == 0:
                ob.pose.bones[name_new].rotation_euler[0] = 1.5708
            elif i == 1:
                ob.pose.bones[name_new].rotation_euler[2] = 1.5708
            elif i == 2:
                ob.pose.bones[name_new].rotation_euler[0] = -1.5708
            else:
                ob.pose.bones[name_new].rotation_euler[2] = -1.5708
            
            bpy.ops.pose.select_all(action='DESELECT')
            ob.data.bones[name_new].select = True
            ob.data.bones.active = ob.data.bones[name_new]
            bpy.ops.pose.armature_apply(selected=True)
            
            ob.pose.bones[name_new].rotation_mode = rot_mode 
            
            # Transformation constraint
            con_pv_rot = ob.pose.bones[name_new].constraints.new("TRANSFORM")
            con_pv_rot.name = "PV_Rot"
            con_pv_rot.target = ob
            con_pv_rot.subtarget = bone.name
            
            con_pv_rot.target_space = 'LOCAL'
            con_pv_rot.owner_space = 'LOCAL'
            
            con_pv_rot.map_from = 'ROTATION'
            if i % 2 == 0:
                con_pv_rot.from_min_x_rot = -3.14159
                con_pv_rot.from_max_x_rot = 3.14159
                con_pv_rot.from_rotation_mode = 'SWING_TWIST_X'
            else:
                con_pv_rot.from_min_z_rot = -3.14159
                con_pv_rot.from_max_z_rot = 3.14159
                con_pv_rot.from_rotation_mode = 'SWING_TWIST_Z'

            con_pv_rot.map_to = 'ROTATION'
            if i % 2 == 0:
                con_pv_rot.to_min_x_rot = 1.5708
                con_pv_rot.to_max_x_rot = -1.5708
            else:
                con_pv_rot.to_min_z_rot = 1.5708
                con_pv_rot.to_max_z_rot = -1.5708
            
            # Driver
            points = (([-1.5708, 1.0], [-2.0, 1.0], [-1.0, 1.0]), ([0.0, 1.0], [-0.5, 1.0], [-0.5, 1.0]), ([1.5708, 3.0], [1.0, 3.0], [2.0, 3.0]), ([2.0, 3.0], [1.5, 3.0], [2.5, 3.0]))
            
            for driver in ob.animation_data.drivers:
                if driver.data_path == ('pose.bones["' + name_new + '"].scale') and driver.array_index == 1:
                    ob.animation_data.drivers.remove(driver)
                
            
            drv = ob.animation_data.drivers.new(data_path = ('pose.bones["' + name_new + '"].scale'), index = 1)
            drv.keyframe_points.add(count = 2)
            drv.driver.type = "SCRIPTED"
            drv.driver.expression = "var"
            
            var = drv.driver.variables.new()
            var.type = "TRANSFORMS"
            tgt = var.targets[0]
            tgt.id = ob
            tgt.bone_target = bone.name
            
            if i % 2 == 0:
                tgt.transform_type = 'ROT_X'
                tgt.rotation_mode = 'SWING_TWIST_X'
                tgt.transform_space = 'LOCAL_SPACE'
                
                if i == 2:
                    drv.driver.expression = "-var"
            
            else:
                tgt.transform_type = 'ROT_Z'
                tgt.rotation_mode = 'SWING_TWIST_Z'
                tgt.transform_space = 'LOCAL_SPACE'
                
                if i == 3:
                    drv.driver.expression = "-var"
                
            
            for k in range (4):
                drv.keyframe_points[k].interpolation = "LINEAR"
                drv.keyframe_points[k].co[0] = points[k][0][0]
                drv.keyframe_points[k].co[1] = points[k][0][1]
                drv.keyframe_points[k].handle_left[0] = points[k][1][0]
                drv.keyframe_points[k].handle_left[1] = points[k][1][1]
                drv.keyframe_points[k].handle_right[0] = points[k][2][0]
                drv.keyframe_points[k].handle_right[1] = points[k][2][1]
            
            drv.driver.expression += ''
        
        bone.rotation_mode = rot_mode
        
        for bone in ob.data.bones:
            if bone.name in select_list:
                bone.select = True
            else:
                bone.select = False
        
        ob.data.bones.active = active_bone

    
    bpy.ops.object.mode_set(mode=mode)


create_pv_bone()                