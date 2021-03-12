import bpy

reparent_list =[]
for ob in bpy.context.selected_objects:
    reparent_list.append(ob.name)
    
bpy.ops.object.select_all(action='DESELECT')
    
for object in reparent_list:
    ob = bpy.data.objects[object]
    rig = ob.parent
    rig_bone = rig.pose.bones[ob.parent_bone]
    
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob

    ob.parent = None

    rig.select_set(True)
    bpy.context.view_layer.objects.active = rig
    rig.data.bones.active = rig.data.bones[rig_bone.name]

    bpy.ops.object.parent_set(type='BONE')
