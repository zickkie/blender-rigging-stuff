bl_info = {
    "name": "Parent Bones in Pose Mode",
    "author": "Arthur Shapiro",
    "version": (0, 1),
    "blender": (2, 83, 0),
    "location": "View 3D -> Ctrl-Shift-P whit Pose Bones selected",
    "description": "Parent Bones in Pose Mode",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"
    }


import bpy
from bpy.types import Operator


class Parent_Bones_in_Pose_Mode(Operator):
    """Parent Bones in Pose Mode"""
    bl_label = "Parent Bones in Pose Mode"
    bl_idname = "pose.parent_bones_in_pose_mode"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        if context.object and context.object.type == "ARMATURE" and context.object.mode == "POSE":
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.armature.parent_set(type='OFFSET')
            bpy.ops.object.mode_set(mode='POSE')
   
        return {'FINISHED'}

addon_keymaps = []

def register():
    
    bpy.utils.register_class(Parent_Bones_in_Pose_Mode)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name ='3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new("pose.parent_bones_in_pose_mode", type= 'Q', value = 'PRESS', ctrl = True, shift = True)
        addon_keymaps.append((km, kmi))

def unregister():
    
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    bpy.utils.unregister_class(Parent_Bones_in_Pose_Mode)

if __name__ == "__main__":
    register()