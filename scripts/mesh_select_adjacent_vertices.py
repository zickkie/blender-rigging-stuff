import bpy
import bmesh

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.mode_set(mode='EDIT')

obj = bpy.context.edit_object
me = obj.data
bm = bmesh.from_edit_mesh(me)

adj = []

for vert in bpy.context.active_object.data.vertices:
    if vert.select == True:
        ind = vert.index

bm.verts.ensure_lookup_table()

for i in range(len(bm.verts[ind].link_faces)):
    for vert in bm.verts[ind].link_faces[i].verts:
        if vert.index != ind:
            adj.append(vert.index)

bmesh.update_edit_mesh(me)
            
bpy.ops.object.mode_set(mode='OBJECT')

for vert in bpy.context.active_object.data.vertices:
    if vert.index in adj or vert.index == ind:
        vert.select = True

bpy.ops.object.mode_set(mode='EDIT')