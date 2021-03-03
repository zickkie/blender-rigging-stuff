bl_info = {
    "name": "Mirror Vertex Groups",
    "author": "Arthur Shapiro",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Properties > Mesh Data > Vertex Groups Context Menu",
    "description": "Mirror Vertex Groups",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"
    }

import bpy

# Mirror Function
def mirror_vertex_groups(src, tgt, mirror):
    
    #left = [".L", ".LEFT", ".LT", "-L", "-LEFT", "-LT", "_L", "_LEFT", "_LT", "L.", "LEFT.", "LT.", "L-", "LEFT-", "LT-", "L_", "LEFT_", "LT_"]

    #right = [".R", ".RIGHT", ".RT", "-R", "-RIGHT", "-RT", "_R", "_RIGHT", "_RT", "R.", "RIGHT.", "RT.", "R-", "RIGHT-", "RT-", "R_", "RIGHT_", "RT_"]
    
    ob = bpy.context.active_object

    ob.vertex_groups.active_index = 0

    for i in range(len(bpy.context.active_object.vertex_groups)):

        ind = ob.vertex_groups.active.index
        
        if src in ob.vertex_groups.active.name and ob.vertex_groups.get(ob.vertex_groups.active.name.replace(src, tgt)) is None:
            
            if mirror == True:
            
                bpy.ops.object.vertex_group_copy()
                bpy.ops.object.vertex_group_mirror(use_topology=False)
                ob.vertex_groups.active.name = ob.vertex_groups.active.name.replace(src, tgt).replace("_copy", "")
            
            else:
                
                ob.vertex_groups.active.name = ob.vertex_groups.active.name.replace(src, tgt)
            
        bpy.context.object.vertex_groups.active_index = (ind + 1)

    bpy.ops.object.vertex_group_sort(sort_type = "NAME")


# Mirror Class    
class mirror_vertex_groups_class(bpy.types.Operator):
    """Mirror Vertex Groups"""
    bl_idname = "mesh.mirror_vertex_groups_class"
    bl_label = "Mirror Vertex Groups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        mirror_vertex_groups(bpy.context.scene.mirror_vertex_groups_source, bpy.context.scene.mirror_vertex_groups_target, True)
            
        return {'FINISHED'}

    
# Rename Class    
class rename_vertex_groups_class(bpy.types.Operator):
    """Rename Vertex Groups"""
    bl_idname = "mesh.rename_vertex_groups_class"
    bl_label = "Rename Vertex Groups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        mirror_vertex_groups(bpy.context.scene.mirror_vertex_groups_source, bpy.context.scene.mirror_vertex_groups_target, False)
            
        return {'FINISHED'}
    
# Symmetrize Class    
class symmetrize_vertex_group_class(bpy.types.Operator):
    """Symmetrize Active Vertex Group by Global X Axis"""
    bl_idname = "mesh.symmetrize_vertex_group_class"
    bl_label = "Symmetrize Active Vertex Group"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        ob = bpy.context.active_object
        mode = bpy.context.object.mode
        vg_active_name = ob.vertex_groups.active.name
        vg_active_ind = ob.vertex_groups[vg_active_name].index

        R_verts = [vert.index for vert in ob.data.vertices if vert.co[0] < 0]
        L_C_verts = [vert.index for vert in ob.data.vertices if vert.co[0] >= 0]

        bpy.ops.object.vertex_group_copy()
        bpy.ops.object.vertex_group_mirror(use_topology=False)
        vg_mirror_name = ob.vertex_groups.active.name
        vg_mirror_ind = ob.vertex_groups[vg_mirror_name].index

        for vert in ob.data.vertices:
            
            if vert.index in R_verts:
                for gr in vert.groups:
                    if gr.group == vg_active_ind:
                        gr.weight = 0.0
            
            elif vert.index in L_C_verts:
                for gr in vert.groups:
                    if gr.group == vg_mirror_ind:
                        gr.weight = 0.0

        bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
        symm_mod = ob.modifiers["VertexWeightMix"]

        symm_mod.vertex_group_a = vg_active_name
        symm_mod.vertex_group_b = vg_mirror_name
        symm_mod.mix_mode = 'ADD'
        symm_mod.mix_set = 'OR'

        bpy.ops.object.modifier_apply(modifier="VertexWeightMix")

        ob.vertex_groups.remove(ob.vertex_groups[vg_mirror_name])
        bpy.context.object.vertex_groups.active_index = vg_active_ind

        bpy.ops.object.mode_set(mode=mode)
        
        return {'FINISHED'}
    

# Draw Function
def mirror_vertex_groups_menu(self, context):
    
    self.layout.separator()
    
    self.layout.row(align=True)
    self.layout.operator("mesh.symmetrize_vertex_group_class", text="Symmetrize", icon = "ARROW_LEFTRIGHT")
    self.layout.operator("mesh.rename_vertex_groups_class", text="Rename", icon = "FILE_TEXT")
    self.layout.operator("mesh.mirror_vertex_groups_class", text="Mirror by Name", icon = "MOD_MIRROR")
    self.layout.prop(context.scene, 'mirror_vertex_groups_target', text = '')
    self.layout.prop(context.scene, 'mirror_vertex_groups_source', text = '')
    self.layout.label(text = "Mirror Vertex Groups by Name")
    self.layout.separator()

 
 
# Register    
def register():
    
    bpy.types.Scene.mirror_vertex_groups_source = bpy.props.StringProperty(
        name = "Source string",
        default = ".L",
        description = "Source string to find vertex groups for mirroring"
        )
    
    bpy.types.Scene.mirror_vertex_groups_target = bpy.props.StringProperty(
        name = "Target string",
        default = ".R",
        description = "Target string to name the mirrored vertex groups"
        )
    
    bpy.utils.register_class(symmetrize_vertex_group_class)
    bpy.utils.register_class(mirror_vertex_groups_class)
    bpy.utils.register_class(rename_vertex_groups_class)
    bpy.types.MESH_MT_vertex_group_context_menu.prepend(mirror_vertex_groups_menu)


def unregister():
    
    bpy.types.MESH_MT_vertex_group_context_menu.remove(mirror_vertex_groups_menu)
    bpy.utils.unregister_class(rename_vertex_groups_class)
    bpy.utils.unregister_class(mirror_vertex_groups_class)
    bpy.utils.unregister_class(symmetrize_vertex_group_class)

    del bpy.types.Scene.mirror_vertex_groups_source
    del bpy.types.Scene.mirror_vertex_groups_target

if __name__ == "__main__":
    register()
