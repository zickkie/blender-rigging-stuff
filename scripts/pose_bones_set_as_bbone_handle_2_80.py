bl_info = {
    "name": "Quick Bendy Bones Handle",
    "description": "Addon for quick setting the selected pose bone as ",
    "author": "Arthur Shapiro",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > (Armature) Pose Mode > Ctrl + Shift + T",
    "category": "Rigging"}

import bpy
from bpy.types import AddonPreferences
from bpy.types import Menu

#####################################
### BBone Handle Setting Function ###
#####################################

def bbone_handle(option):

    ob = bpy.context.active_object
    active = ob.data.bones[bpy.context.active_pose_bone.name]

    for b in bpy.context.selected_pose_bones:
        if b.name != active.name:
            selected = ob.data.bones[b.name]
    
    if option == "start":
        
        ob.data.bones[active.name].bbone_handle_type_start = 'ABSOLUTE'
        ob.data.bones[active.name].bbone_custom_handle_start = selected
    
    elif option == "end":
        
        ob.data.bones[active.name].bbone_handle_type_end = 'ABSOLUTE'
        ob.data.bones[active.name].bbone_custom_handle_end = selected

##########################################
### BBone Handle Setting Class (start) ###
##########################################

class POSE_PT_bbone_custom_handle_start(bpy.types.Operator):
    """Set active bone as tanget bbone start handle of active bone"""
    bl_label = "Set as Start Handle"
    bl_idname = "pose.bbone_custom_handle_start"
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
            
        bbone_handle("start")
            
        return {'FINISHED'}
    

########################################
### BBone Handle Setting Class (end) ###
########################################

class POSE_PT_bbone_custom_handle_end(bpy.types.Operator):
    """Set active bone as tanget bbone end handle of active bone"""
    bl_label = "Set as End Handle"
    bl_idname = "pose.bbone_custom_handle_end"
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
            
        bbone_handle("end")
            
        return {'FINISHED'}
    
    
######################
### Pie Menu Class ###
###################### 

class BBone_Custom_Handle_Menu(Menu):
    bl_idname = "BBone_Custom_Handle_Menu"
    bl_label = "BBone Custom Handle Menu"
   
    def draw(self, context):

        ob = bpy.context.active_object
        
        layout = self.layout
        pie = layout.menu_pie()

        if ob: 
            mode = ob.mode
            if mode == "POSE":
                pie.operator("pose.bbone_custom_handle_start",  icon="TRACKING_FORWARDS_SINGLE")
                pie.operator("pose.bbone_custom_handle_end", icon="TRACKING_BACKWARDS_SINGLE")


###############
### Classes ###
###############

addon_keymaps = []

classes = (
    POSE_PT_bbone_custom_handle_start,
    POSE_PT_bbone_custom_handle_end,
    BBone_Custom_Handle_Menu
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

    kmi_mnu = km.keymap_items.new("wm.call_menu_pie", "T", "PRESS", ctrl=True, shift=True)
    kmi_mnu.properties.name = BBone_Custom_Handle_Menu.bl_idname

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