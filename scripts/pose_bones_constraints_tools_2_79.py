bl_info = {
    "name": "Bone Constraints Tools",
    "author": "Arthur Shapiro",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Properties > Bone Constraints",
    "description": "Bone Constraints Specials Enable/Disable/Expand/Move to the Top/Bottom",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"
    }


import bpy
from bpy.types import Operator


class POSE_PT_toggle_expand(Operator):
    """Toggle expanded view of bone constraints in UI"""
    bl_label = "Toggle expand constraints"
    bl_idname = "bone.toggle_expand_constraints"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints:
                c.show_expanded = not c.show_expanded
        
        return {'FINISHED'}
    
    
class POSE_PT_toggle_mute(Operator):
    """Toggle mute bone constraints"""
    bl_label = "Toggle mute constraints"
    bl_idname = "bone.toggle_mute_constraints"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints:
                c.mute = not c.mute
        
        return {'FINISHED'}


class POSE_PT_move_top(Operator):
    """Move selected constraint to the top of the stack"""
    bl_label = "Move selected constraint to the top of the stack"
    bl_idname = "bone.move_constraint_to_the_top"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        bpy.context.area.type = 'PROPERTIES'
        for b in bpy.context.selected_pose_bones:
            for i in range(len(b.constraints)):
                bpy.context.active_object.data.bones.active = bpy.context.active_object.data.bones[b.name]
                my_context = bpy.context.copy()
                my_context["constraint"] = b.constraints[bpy.context.scene.constraint_name]
                bpy.ops.constraint.move_up(my_context, constraint=bpy.context.scene.constraint_name, owner="BONE")
        
        return {'FINISHED'}
    

class POSE_PT_move_bottom(Operator):
    """Move selected constraint to the bottom of the stack"""
    bl_label = "Move selected constraint to the bottom of the stack"
    bl_idname = "bone.move_constraint_to_the_bottom"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        bpy.context.area.type = 'PROPERTIES'
        for b in bpy.context.selected_pose_bones:
            for i in range(len(b.constraints)):
                bpy.context.active_object.data.bones.active = bpy.context.active_object.data.bones[b.name]
                my_context = bpy.context.copy()
                my_context["constraint"] = b.constraints[bpy.context.scene.constraint_name]
                bpy.ops.constraint.move_down(my_context, constraint=bpy.context.scene.constraint_name, owner="BONE")
        
        return {'FINISHED'}
    

def menu(self, context):
    if (bpy.context.active_object):
        if (len(bpy.context.active_pose_bone.constraints)):
            col = self.layout.column(align=True)

            row = col.row(align=True)
            row.operator(POSE_PT_toggle_expand.bl_idname,
                         icon='TRIA_DOWN', text="Expand/Collapse All")
            row.operator(POSE_PT_toggle_mute.bl_idname,
                         icon='RESTRICT_VIEW_OFF', text="Mute/Unmute All")
        
            row = col.row(align = False)
            row.prop(context.scene, "constraint_name", text = "")
            row.operator(POSE_PT_move_top.bl_idname,
                         icon='TRIA_UP_BAR', text="")
            row.operator(POSE_PT_move_bottom.bl_idname,
                         icon='TRIA_DOWN_BAR', text="")



def register():
    
    bpy.types.Scene.constraint_name = bpy.props.StringProperty(
        name = "Constraint Name to move to the Top / Bottom",
        default = "Constraint Name",
        description = "Constraint Name to move to the Top / Bottom"
        )
    
    bpy.utils.register_class(POSE_PT_toggle_expand)
    bpy.utils.register_class(POSE_PT_toggle_mute)
    bpy.utils.register_class(POSE_PT_move_top)
    bpy.utils.register_class(POSE_PT_move_bottom)
    
    bpy.types.BONE_PT_constraints.prepend(menu)


def unregister():
    bpy.types.BONE_PT_constraints.remove(menu)

    bpy.utils.unregister_class(POSE_PT_toggle_expand)
    bpy.utils.unregister_class(POSE_PT_toggle_mute)
    bpy.utils.unregister_class(POSE_PT_move_top)
    bpy.utils.unregister_class(POSE_PT_move_bottom)

    del bpy.types.Scene.constraint_name

if __name__ == "__main__":
    register()
    
    
    

#bpy.context.area.type = 'PROPERTIES'
#for i in range (3):
#    for b in bpy.context.selected_pose_bones:
#        bpy.context.active_object.data.bones.active = bpy.context.active_object.data.bones[b.name]
#        my_context = bpy.context.copy()
#        my_context["constraint"] = b.constraints["Head Scale"]
#        bpy.ops.constraint.move_up(my_context, constraint="Head Scale", owner="BONE")
#bpy.context.area.type = 'TEXT_EDITOR'