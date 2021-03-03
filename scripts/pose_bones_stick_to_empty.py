import bpy

# Setting main variables
armature = bpy.context.active_object

for bone in bpy.context.selected_pose_bones:
    # Switching to Object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Creating Empty and aligning in to the active Pose Bone
    bpy.ops.object.empty_add(type='PLAIN_AXES')
    empty = bpy.context.active_object
    empty.name = "TRANSFORMS_" + bone.name
    empty.empty_display_size = 0.1
    constraint = empty.constraints.new("COPY_TRANSFORMS")
    constraint.target = armature
    constraint.subtarget = bone.name

    # Applying the constraint
    bpy.ops.object.visual_transform_apply()
    empty.constraints.remove(constraint)

    # Constraint the active Pose Bone to the Empty
    bpy.ops.object.select_all(action='DESELECT')
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    bone_constraint = bone.constraints.new("COPY_TRANSFORMS")
    bone_constraint.name = "_FREEZE_TRANSFORMS"
    bone_constraint.target = empty
