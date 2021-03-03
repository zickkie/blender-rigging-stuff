bl_info = {
    "name": "Show Parent Vertices",
    "author": "Arthur Shapiro",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Objetct Properties > Relations",
    "description": "Select 3 Parent Vertices of the Active Object",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"
    }


import bpy
from bpy.types import Operator

class OBJECT_OT_show_parent_vertices(Operator):
    """Select 3 Parent Vertices of the Active Object"""
    bl_label = "Select 3 Parent Vertices"
    bl_idname = "object.show_parent_vertices"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):

        child = bpy.context.active_object
        parent = bpy.context.active_object.parent
        verts = []

        for i in range(3):
            verts.append(child.parent_vertices[i])


        bpy.data.objects[child.name].select_set(False)
        bpy.data.objects[parent.name].select_set(True)
        bpy.context.view_layer.objects.active = parent

        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.editmode_toggle()

        for i in range(3):
            parent.data.vertices[verts[i]].select = True

        bpy.ops.object.editmode_toggle()
    
        return {'FINISHED'}

def menu(self, context):
    if (bpy.context.active_object) and bpy.context.active_object.parent is not None and bpy.context.active_object.parent_type == "VERTEX_3":
        col = self.layout.column(align=True)

        row = col.row(align=True)
        row.operator(OBJECT_OT_show_parent_vertices.bl_idname,
                     icon='STICKY_UVS_DISABLE', text="Select 3 Parent Vertices")

def register():
    
    bpy.utils.register_class(OBJECT_OT_show_parent_vertices)
    
    bpy.types.OBJECT_PT_relations.append(menu)


def unregister():
    
    bpy.types.OBJECT_PT_relations.remove(menu)

    bpy.utils.unregister_class(OBJECT_OT_show_parent_vertices)

if __name__ == "__main__":
    register()
        