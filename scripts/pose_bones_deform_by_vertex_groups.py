import bpy

vert_groups = []

for ob in bpy.context.view_layer.layer_collection.children['cat'].collection.objects:
    if len(ob.vertex_groups) > 0:
        for vg in ob.vertex_groups:
            vert_groups.append(vg.name)

for data_bone in bpy.context.object.data.bones:
    if data_bone.name in vert_groups:
        data_bone.use_deform = True
    else:
        data_bone.use_deform = False