import bpy

keys = []
for item in bpy.context.active_pose_bone.keys():
    if not item.startswith("_"):
        keys.append(item)
for item in keys:
    bpy.context.active_pose_bone.property_overridable_library_set('["' + item + '"]', True)