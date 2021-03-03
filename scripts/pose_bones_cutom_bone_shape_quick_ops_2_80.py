bl_info = {
    "name": "Bones Custom Shape Quick Actions",
    "description": "Addon for quick actions with custom bone shapes: copy shape to selected / clear shape",
    "author": "Arthur Shapiro",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > (Armature) Pose Mode > Alt + V",
    "category": "Rigging"}

import bpy
from bpy.types import AddonPreferences
from bpy.types import Menu

#################################
### Mirror Selection Function ###
#################################

def copy_shape():

    arm = bpy.context.active_object
    active = bpy.context.active_pose_bone
    
    for bone in bpy.context.selected_pose_bones:
        if bone.name != active.name:
            bone.custom_shape = active.custom_shape
            bone.custom_shape_scale = active.custom_shape_scale
            bone.custom_shape_transform = active.custom_shape_transform
            bone.use_custom_shape_bone_size = active.use_custom_shape_bone_size
            arm.data.bones[bone.name].show_wire = arm.data.bones[active.name].show_wire
            
def clear_shape():
    
    for bone in bpy.context.selected_pose_bones:
        bone.custom_shape = None
    
########################
### Copy Shape Class ###
########################

class POSE_PT_copy_custom_shape(bpy.types.Operator):
    """Copy custom shape from active bones to selected"""
    bl_label = "Copy Custom Shape"
    bl_idname = "pose.copy_custom_shape"
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
            
        copy_shape()
            
        return {'FINISHED'}
    

#########################
### Clear Shape Class ###
#########################

class POSE_PT_clear_custom_shape(bpy.types.Operator):
    """Clear custom shapes of all the selected pose bones"""
    bl_label = "Clear Custom Shape"
    bl_idname = "pose.clear_custom_shape"
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
            
        clear_shape()
            
        return {'FINISHED'}


###################################
### Shape-Based Selection Class ###
###################################

class POSE_PT_shape_based_selection(bpy.types.Operator):
    """Select all the visible pose bones with the custom shapes identical to active pose bone"""
    bl_label = "Shape-based selection"
    bl_idname = "pose.shape_based_selection"
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
            
        ob = bpy.context.active_pose_bone.custom_shape
        for bone in bpy.context.visible_pose_bones:
            if bone.custom_shape == ob:
                bpy.context.active_object.data.bones[bone.name].select = True
            
        return {'FINISHED'}
    
    
######################
### Pie Menu Class ###
###################### 

class Bone_Custom_Shape_Menu(Menu):
    bl_idname = "Bone_Custom_Shape_Menu"
    bl_label = "Bone Custom Shape Menu"
   
    def draw(self, context):

        ob = bpy.context.active_object
        
        layout = self.layout
        pie = layout.menu_pie()

        if ob: 
            mode = ob.mode
            if mode == "POSE":
                pie.operator("pose.copy_custom_shape",  icon="LINKED")
                pie.operator("pose.clear_custom_shape", icon="UNLINKED")
                pie.operator("pose.shape_based_selection", icon="OBJECT_DATA")


###############
### Classes ###
###############

addon_keymaps = []

classes = (
    POSE_PT_copy_custom_shape,
    POSE_PT_clear_custom_shape,
    POSE_PT_shape_based_selection,
    Bone_Custom_Shape_Menu
)
     
    
####################
### Registration ###
####################
    
def register():
    for c in classes:
        bpy.utils.register_class(c)
   
    # add keymap entry
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    kmi_mnu = km.keymap_items.new("wm.call_menu_pie", "V", "PRESS", alt=True)
    kmi_mnu.properties.name = Bone_Custom_Shape_Menu.bl_idname

    addon_keymaps.append((km, kmi_mnu))
    
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    # remove keymap entry
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()


if __name__ == "__main__":
    register()