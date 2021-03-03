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
        
        expanded = False
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints:
                if c.show_expanded == True:
                    expanded = True
                    break
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints:
                if expanded == True:
                    c.show_expanded = False
                else:
                    c.show_expanded = True
            
        
        return {'FINISHED'}
    
    
class POSE_PT_toggle_mute(Operator):
    """Toggle mute bone constraints"""
    bl_label = "Toggle mute constraints"
    bl_idname = "bone.toggle_mute_constraints"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        muted = False
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints:
                if c.mute == True:
                    muted = True
                    break
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints:
                if muted == True:
                    c.mute = False
                else:
                    c.mute = True
        
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
    
    
class POSE_PT_reset_stretch_length(Operator):
    """Reset all the Stretch To constraints Rest Length"""
    bl_label = "Reset all the Stretch To constraints Rest Length"
    bl_idname = "bone.reset_stretch_length"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.active_object.pose.bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.rest_length = 0
        
        return {'FINISHED'}
# Selected
class POSE_PT_reset_stretch_length_sel(Operator):
    """Reset all the Stretch To constraints Rest Length"""
    bl_label = "Reset all the Stretch To constraints Rest Length"
    bl_idname = "bone.reset_stretch_length_sel"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.rest_length = 0
        
        return {'FINISHED'}


class POSE_PT_rotation_swing(Operator):
    """Set the Stretch To constraints Rotation Mode to SWING"""
    bl_label = "Set the Stretch To constraints Rotation Mode to SWING"
    bl_idname = "bone.rotation_swing"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.active_object.pose.bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.keep_axis = "SWING_Y"
        
        return {'FINISHED'} 
# Selected    
class POSE_PT_rotation_swing_sel(Operator):
    """Set the Stretch To constraints Rotation Mode to SWING"""
    bl_label = "Set the Stretch To constraints Rotation Mode to SWING"
    bl_idname = "bone.rotation_swing_sel"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.keep_axis = "SWING_Y"
        
        return {'FINISHED'}


class POSE_PT_volume_xz(Operator):
    """Set the Stretch To constraints Volume Preservation to XZ"""
    bl_label = "Set the Stretch To constraints Volume Preservation to XZ"
    bl_idname = "bone.volume_xz"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.active_object.pose.bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.volume = 'VOLUME_XZX'
        
        return {'FINISHED'}
# Selected
class POSE_PT_volume_xz_sel(Operator):
    """Set the Stretch To constraints Volume Preservation to XZ"""
    bl_label = "Set the Stretch To constraints Volume Preservation to XZ"
    bl_idname = "bone.volume_xz_sel"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.volume = 'VOLUME_XZX'
        
        return {'FINISHED'}
                    
                    
class POSE_PT_volume_none(Operator):
    """Set the Stretch To constraints Volume Preservation to NONE"""
    bl_label = "Set the Stretch To constraints Volume Preservation to NONE"
    bl_idname = "bone.volume_none"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.active_object.pose.bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.volume = 'NO_VOLUME'

        
        return {'FINISHED'} 
# Selected
class POSE_PT_volume_none_sel(Operator):
    """Set the Stretch To constraints Volume Preservation to NONE"""
    bl_label = "Set the Stretch To constraints Volume Preservation to NONE"
    bl_idname = "bone.volume_none_sel"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        for b in bpy.context.selected_pose_bones:
            for c in b.constraints: 
                if c.type == "STRETCH_TO":
                    c.volume = 'NO_VOLUME'

        
        return {'FINISHED'}   

    

def menu(self, context):
    if (context.active_object and context.active_object.type == "ARMATURE" and context.active_object.mode == "POSE"):
        if (len(bpy.context.active_pose_bone.constraints)):
            col = self.layout.column(align=True)

            row = col.row(align=True)
            row.operator(POSE_PT_toggle_expand.bl_idname,
                         icon='TRIA_DOWN', text="Expand/Collapse All")
            row.operator(POSE_PT_toggle_mute.bl_idname,
                         icon='HIDE_OFF', text="Mute/Unmute All")
        
            row = col.row(align = True)
            row.prop(context.scene, "constraint_name", text = "")
            row.operator(POSE_PT_move_top.bl_idname,
                         icon='TRIA_UP_BAR', text="")
            row.operator(POSE_PT_move_bottom.bl_idname,
                         icon='TRIA_DOWN_BAR', text="")
            
            
            row = col.row()
            row.prop(context.scene, "show_stretchto_operators", text = "Stretch To Operators", toggle = True)
            row = col.row()
            
            if bpy.context.scene.show_stretchto_operators == True:
                strto = col.split()
                
                str_labels  = strto.column()
                
                row = str_labels.row()
                row.label(text = 'Set')
                row = str_labels.row()
                row.label(text = 'Length')
                row = str_labels.row()
                row.label(text = 'Rotation Mode')
                row = str_labels.row()
                row.label(text = 'Volume')
                
                str_operators  = strto.column()
                row = str_operators.row()
                row.prop(context.scene, "constraints_for_selected_only", text = "Selected Only", toggle = True)
                row = str_operators.row()
                if bpy.context.scene.constraints_for_selected_only == True:
                    row.operator(POSE_PT_reset_stretch_length_sel.bl_idname,
                                 icon='FILE_REFRESH', text="Reset")
                else:
                    row.operator(POSE_PT_reset_stretch_length.bl_idname,
                                 icon='FILE_REFRESH', text="Reset")              
                row = str_operators.row()
                if bpy.context.scene.constraints_for_selected_only == True:
                    row.operator(POSE_PT_rotation_swing_sel.bl_idname,
                                 icon='CON_TRACKTO', text="Swing Rotation")
                else:
                    row.operator(POSE_PT_rotation_swing.bl_idname,
                                 icon='CON_TRACKTO', text="Swing Rotation")
                row = str_operators.row(align = True)
                if bpy.context.scene.constraints_for_selected_only == True:
                    row.operator(POSE_PT_volume_xz_sel.bl_idname,
                                 icon='CON_SAMEVOL', text="Volume: XZ")
                    row.operator(POSE_PT_volume_none_sel.bl_idname,
                                 icon='CON_SIZELIMIT', text="Volume: NONE")
                else:
                    row.operator(POSE_PT_volume_xz.bl_idname,
                                 icon='CON_SAMEVOL', text="Volume: XZ")
                    row.operator(POSE_PT_volume_none.bl_idname,
                                 icon='CON_SIZELIMIT', text="Volume: NONE")


def register():
    
    bpy.types.Scene.constraint_name = bpy.props.StringProperty(
        name = "Constraint Name to move to the Top / Bottom",
        default = "Constraint Name",
        description = "Constraint Name to move to the Top / Bottom"
        )
    
    bpy.types.Scene.constraints_for_selected_only = bpy.props.BoolProperty(
        name = "Apply Stretch To constraints operators for selected pose bones only",
        default = False,
        description = "Apply Stretch To constraints operators for selected pose bones only"
        )
    
    bpy.types.Scene.show_stretchto_operators = bpy.props.BoolProperty(
        name = "Show Stretch To operators",
        default = False,
        description = "Show Stretch To operators"
        )
    
    bpy.utils.register_class(POSE_PT_toggle_expand)
    bpy.utils.register_class(POSE_PT_toggle_mute)
    bpy.utils.register_class(POSE_PT_move_top)
    bpy.utils.register_class(POSE_PT_move_bottom)
    bpy.utils.register_class(POSE_PT_reset_stretch_length)
    bpy.utils.register_class(POSE_PT_reset_stretch_length_sel)
    bpy.utils.register_class(POSE_PT_rotation_swing)
    bpy.utils.register_class(POSE_PT_rotation_swing_sel)
    bpy.utils.register_class(POSE_PT_volume_xz)
    bpy.utils.register_class(POSE_PT_volume_xz_sel)
    bpy.utils.register_class(POSE_PT_volume_none)
    bpy.utils.register_class(POSE_PT_volume_none_sel)
    
    bpy.types.BONE_PT_constraints.prepend(menu)


def unregister():
    bpy.types.BONE_PT_constraints.remove(menu)

    bpy.utils.unregister_class(POSE_PT_toggle_expand)
    bpy.utils.unregister_class(POSE_PT_toggle_mute)
    bpy.utils.unregister_class(POSE_PT_move_top)
    bpy.utils.unregister_class(POSE_PT_move_bottom)
    bpy.utils.unregister_class(POSE_PT_reset_stretch_length)
    bpy.utils.unregister_class(POSE_PT_reset_stretch_length_sel)
    bpy.utils.unregister_class(POSE_PT_rotation_swing)
    bpy.utils.unregister_class(POSE_PT_rotation_swing_sel)
    bpy.utils.unregister_class(POSE_PT_volume_xz)
    bpy.utils.unregister_class(POSE_PT_volume_xz_sel)
    bpy.utils.unregister_class(POSE_PT_volume_none)
    bpy.utils.unregister_class(POSE_PT_volume_none_sel)

    del bpy.types.Scene.constraint_name
    del bpy.types.Scene.constraints_for_selected_only
    del bpy.types.Scene.show_stretchto_operators

if __name__ == "__main__":
    register()