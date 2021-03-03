import bpy

set = bpy.context.active_object.pose.bones

for bone in set:
    keys = []
    for item in bone.keys():
        if not item.startswith("_RNA"):
            keys.append(item)      
    for item in keys:
        bone.property_overridable_library_set('["' + item + '"]', True)