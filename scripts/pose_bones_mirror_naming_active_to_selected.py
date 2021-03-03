import bpy

ob = bpy.context.active_object
dbones = ob.data.bones

for bone in bpy.context.selected_pose_bones:
    if dbones.active.name == bone.name:
        active = bone
    else:
        selected = bone
    
selected.name = active.name.replace(".L", ".R")