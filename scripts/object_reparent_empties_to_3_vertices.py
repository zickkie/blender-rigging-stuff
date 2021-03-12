import bpy

for parent in bpy.context.selected_objects:
    # Create list of children (Empties)
    children_list = []

    for child in parent.children:
        if child.type == "EMPTY" and child.parent_type == "VERTEX_3":
            children_list.append(child.name)

    # Apply Rotation & Scale to the Mesh Object
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    for item in children_list:
        # Create list of 3 Parent Vertices
        empty = bpy.data.objects[item]
        verts = []

        for i in range(3):
            verts.append(empty.parent_vertices[i])
        
        # Unparent Empty (no transforms keeping)
        bpy.ops.object.select_all(action='DESELECT')
        empty.select_set(True)
        bpy.context.view_layer.objects.active = empty
        bpy.ops.object.parent_clear(type='CLEAR')

        # Reparent again to the same vertices
        parent.select_set(True)
        bpy.context.view_layer.objects.active = parent
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')

        for i in range(3):
            parent.data.vertices[verts[i]].select = True
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_parent_set()
        bpy.ops.object.mode_set(mode='OBJECT')


