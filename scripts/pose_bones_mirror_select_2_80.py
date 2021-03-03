bl_info = {
    "name": "Mirror Bone Select",
    "description": "Addon for quick selection (pie menu) of bones with mirrored naming (L to R and vice versa)",
    "author": "Arthur Shapiro",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > (Armature) Pose Mode > Shift + X",
    "category": "Animation"}

import bpy
from bpy.types import AddonPreferences
from bpy.types import Menu

#################################
### Mirror Selection Function ###
#################################

def mirror_select(option):

    left = [".L", ".LEFT", ".LT", "-L", "-LEFT", "-LT", "_L", "_LEFT", "_LT", "L.", "LEFT.", "LT.", "L-", "LEFT-", "LT-", "L_", "LEFT_", "LT_"]

    right = [".R", ".RIGHT", ".RT", "-R", "-RIGHT", "-RT", "_R", "_RIGHT", "_RT", "R.", "RIGHT.", "RT.", "R-", "RIGHT-", "RT-", "R_", "RIGHT_", "RT_"]

    for item in left:
        if item != item.lower():
            item_lower = item.lower()
            left.append(item_lower)
        
    for item in right:
        if item != item.lower():
            item_lower = item.lower()
            right.append(item_lower)
        
    list = []
    list_source = []
    list_inverted = []
    data_bones = bpy.context.active_object.data.bones
    active_L = False
    active_R = False
    
    for b in bpy.context.selected_pose_bones:
        list.append(b.name)
        
        for item_l in left:
            if item_l in b.name:
                list_inverted.append(b.name.replace(item_l, right[left.index(item_l)]))
                list_source.append(b.name)
        
        for item_r in right:
            if item_r in b.name:
                list_inverted.append(b.name.replace(item_r, left[right.index(item_r)]))
                list_source.append(b.name)

    for b in data_bones:
        
        if option == "append":   
            if b.name in list_inverted:
                b.select = True
        
        elif option == "invert":

            L = False
            R = False

            if b.name in list_inverted:
                b.select = True
                
            elif b.name in list_source:
                b.select = False
    
            
    if option == "invert":

        for item_l in left:
            if item_l in data_bones.active.name:
                item_L = item_l 
                L = True
                break

        for item_r in right:
            if item_r in data_bones.active.name:
                item_R = item_r
                R = True
                break

        print(L, R) 

        if L == True:
            data_bones.active = data_bones[data_bones.active.name.replace(item_L, right[left.index(item_L)])]
        elif R == True:
            data_bones.active = data_bones[data_bones.active.name.replace(item_R, left[right.index(item_R)])]

                    


#######################################
### Mirror Selection Class (Append) ###
#######################################

class POSE_PT_bones_mirror_select_append(bpy.types.Operator):
    """Append to selection bones with mirrored naming"""
    bl_label = "Append Mirror"
    bl_idname = "pose.bones_mirror_select_append"
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
            
        mirror_select("append")
            
        return {'FINISHED'}
    

#######################################
### Mirror Selection Class (Invert) ###
#######################################

class POSE_PT_bones_mirror_select_invert(bpy.types.Operator):
    """Remove selected bones with those with mirrored naming"""
    bl_label = "Invert Mirror"
    bl_idname = "pose.bones_mirror_select_invert"
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
            
        mirror_select("invert")
            
        return {'FINISHED'}
    
    
######################
### Pie Menu Class ###
###################### 

class BONE_MT_Bone_Mirror_Select_Menu(Menu):
    bl_idname = "Bone_Mirror_Select_Menu"
    bl_label = "Bone Mirror Select Menu"
   
    def draw(self, context):

        ob = bpy.context.active_object
        
        layout = self.layout
        pie = layout.menu_pie()

        if ob: 
            mode = ob.mode
            if mode == "POSE":
                pie.operator("pose.bones_mirror_select_append",  icon="ADD")
                pie.operator("pose.bones_mirror_select_invert", icon="MOD_MIRROR")


###############
### Classes ###
###############

addon_keymaps = []

classes = (
    POSE_PT_bones_mirror_select_append,
    POSE_PT_bones_mirror_select_invert,
    BONE_MT_Bone_Mirror_Select_Menu
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

    kmi_mnu = km.keymap_items.new("wm.call_menu_pie", "X", "PRESS", shift=True)
    kmi_mnu.properties.name = BONE_MT_Bone_Mirror_Select_Menu.bl_idname

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