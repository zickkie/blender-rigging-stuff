import bpy

# Setting main variables
ob = bpy.context.active_object
active = bpy.context.active_pose_bone

for bone in bpy.context.selected_pose_bones:
    #Checking that there is any custom shape of the pose bone
    if bone.custom_shape is not None:
        # Extract bone shape mesh data
        source_data = bone.custom_shape.data
        
        # Adding the cube - container of mesh data for futher mirroring
        bpy.ops.mesh.primitive_cube_add()
        ob_target = bpy.context.active_object
        ob_target.name = "shape_" + bone.name
        
        # Copying mesh data for preserving the original bone custom shape
        new_data = source_data.copy()
        
        # Assigning new data to the new object
        ob_target.data = new_data
       
        # Aligning the object to the pose bone via Copy Transforms constraint
        for i in range(2):
            ob_target.location[i] = 0.0
            ob_target.rotation_euler[i] = 0.0
            ob_target.scale[i] = 1.0
        constraint = ob_target.constraints.new("COPY_TRANSFORMS")
        constraint.target = ob
        constraint.subtarget = bone.name
        
        # Applying the constraint
        bpy.ops.object.visual_transform_apply()
        ob_target.constraints.remove(constraint)
        
        # Scaling object negatively along local X axis
        source_scale = ob_target.scale[0]
        ob_target.scale[0] = -ob_target.scale[0]
        
        # Applying scale for mesh mirroring (and then restoring it)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True, properties=False)
        for i in range(3):
            ob_target.scale[i] = ob_target.scale[i] / source_scale
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True, properties=False)
        
        # Setting the new custom bone shape
        ob.pose.bones[bone.name].custom_shape = ob_target
        
        # Removing the no longer usable object
        bpy.ops.object.delete()
        
        # Turning back to selection
        ob.select_set(True)
        bpy.context.view_layer.objects.active = ob
        bpy.ops.object.mode_set(mode='POSE')
    