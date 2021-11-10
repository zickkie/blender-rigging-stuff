import bpy

rot_mode_dict = {
    'QUATERNION': 0,
    'XYZ': 1,
    'XZY': 2,
    'YXZ': 3,
    'YZX': 4,
    'ZXY': 5,
    'ZYX': 6,
    'AXIS_ANGLE': -1
    }

def pose_bone_rot_order_keys(bone_name):
    ob = bpy.context.active_object
    bone = ob.pose.bones[bone_name]
    frame_c = bpy.context.scene.frame_current
    l = []
    rot_mode_path = 'pose.bones["' + bone_name + '"].rotation_mode'
    rot_mode_value = rot_mode_dict[bone.rotation_mode]
    
    if not ob.animation_data:
        ob.animation_data_create()
            
            
    if ob.animation_data.action == None: # no active action, create one
        action = bpy.data.actions.new(name = ob.name + "_Action")
        ob.animation_data.action = action
        fcurve_rot_mode = action.fcurves.new(data_path = rot_mode_path, index = 0, action_group = bone_name)
        kf_rot_mode = fcurve_rot_mode.keyframe_points.insert(frame = frame_c, value=rot_mode_value)
        kf_rot_mode.interpolation = "LINEAR"
         
    else: # action exists; search for relevant fcurves, create it if none found
        for curve in ob.animation_data.action.fcurves:
            l.append(curve.data_path)
        if rot_mode_path not in l:
            fcurve_rot_mode = ob.animation_data.action.fcurves.new(data_path = rot_mode_path, index = 0, action_group = bone_name)
            kf_rot_mode = fcurve_rot_mode.keyframe_points.insert(frame = frame_c, value=rot_mode_value)
            kf_rot_mode.interpolation = "LINEAR"
        else:
            for curve in ob.animation_data.action.fcurves:
                if rot_mode_path in curve.data_path:
                    kf_rot_mode = curve.keyframe_points.insert(frame = frame_c, value=rot_mode_value)
                    kf_rot_mode.interpolation = "LINEAR"
                    
for bone in bpy.context.selected_pose_bones:
    pose_bone_rot_order_keys(bone.name)
