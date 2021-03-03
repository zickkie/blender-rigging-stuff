bl_info = {
    "name": "Pose Bones Selection Tool",
    "author": "Arthur Shapiro",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Bone Properties -> Relations",
    "description": "Select Parent/Children of the Selected Pose Bones",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"
    }


import bpy
from bpy.types import Operator

class POSE_PT_append_parents_to_selection(Operator):
    """Append to selection all the Parent Bones of the Selected Pose Bones"""
    bl_label = "Select Parent Bones (append)"
    bl_idname = "bone.append_parents_to_selection"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        ob = bpy.context.active_object
        list = [bone.name for bone in bpy.context.selected_pose_bones]
        for name in list:
            bone = ob.pose.bones[name]
            if bone.parent is not None:
                parent = bone.parent
                ob.data.bones[parent.name].select = True
            
        return {'FINISHED'}

class POSE_PT_invert_selection_to_parents(Operator):
    """Invert Selection from Pose Bones to their Parents"""
    bl_label = "Select Parent Bones (invert)"
    bl_idname = "bone.invert_selection_to_parents"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        ob = bpy.context.active_object
        list = [bone.name for bone in bpy.context.selected_pose_bones]
        source = [item for item in list]
        for name in list:
            bone = ob.pose.bones[name]
            if bone.parent is not None:
                parent = bone.parent
                ob.data.bones[parent.name].select = True
                ob.data.bones.active = ob.data.bones[parent.name]
                for item in list:
                    ob.data.bones[item].select = False
        
        return {'FINISHED'}
                    
class POSE_PT_append_children_to_selection(Operator):
    """Append to selection all the Child Bones of the Selected Pose Bones"""
    bl_label = "Select Child Bones (append)"
    bl_idname = "bone.append_children_to_selection"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        ob = bpy.context.active_object
        list = [bone.name for bone in bpy.context.selected_pose_bones]
        for name in list:
            bone = ob.pose.bones[name]
            if len(bone.children) > 0:
                for child in bone.children:
                    ob.data.bones[child.name].select = True
        
        return {'FINISHED'}
                    
class POSE_PT_invert_selection_to_children(Operator):
    """Invert Selection from Pose Bones to their Children"""
    bl_label = "Select Child Bones (invert)"
    bl_idname = "bone.invert_selection_to_children"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        ob = bpy.context.active_object
        list = [bone.name for bone in bpy.context.selected_pose_bones]
        for name in list:
            bone = ob.pose.bones[name]
            if len(bone.children) > 0:
                for child in bone.children:
                    ob.data.bones[child.name].select = True
                    ob.data.bones.active = ob.data.bones[child.name]
                    for item in list:
                        ob.data.bones[item].select = False
            
        return {'FINISHED'}

def menu(self, context):
    if bpy.context.object.type == 'ARMATURE' and bpy.context.object.mode == "POSE":
        if len(bpy.context.selected_pose_bones) > 0:
            col = self.layout.column(align=True)

            row = col.row(align=True)
            row.operator(POSE_PT_append_parents_to_selection.bl_idname,
                         icon='EXPORT', text="Select Parent Bones (append)")
            row.operator(POSE_PT_invert_selection_to_parents.bl_idname,
                         icon='SORT_DESC', text="Select Parent Bones (invert)")
        
            row = col.row(align=True)
            row.operator(POSE_PT_append_children_to_selection.bl_idname,
                         icon='IMPORT', text="Select Child Bones (append)")
            row.operator(POSE_PT_invert_selection_to_children.bl_idname,
                         icon='SORT_ASC', text="Select Child Bones (invert)")


def register():
    
    bpy.utils.register_class(POSE_PT_append_parents_to_selection)
    bpy.utils.register_class(POSE_PT_invert_selection_to_parents)
    bpy.utils.register_class(POSE_PT_append_children_to_selection)
    bpy.utils.register_class(POSE_PT_invert_selection_to_children)
    
    bpy.types.BONE_PT_relations.prepend(menu)


def unregister():
    
    bpy.types.BONE_PT_relations.remove(menu)

    bpy.utils.unregister_class(POSE_PT_append_parents_to_selection)
    bpy.utils.unregister_class(POSE_PT_invert_selection_to_parents)
    bpy.utils.unregister_class(POSE_PT_append_children_to_selection)
    bpy.utils.unregister_class(POSE_PT_invert_selection_to_children)

if __name__ == "__main__":
    register()