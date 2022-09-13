import bpy
from bpy.types import (Operator,
                       Panel,
                       PropertyGroup
                       )
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       CollectionProperty,
                       PointerProperty,
                       )
from .operators import *
from .functions import *


class SVF_PT_Armature_Tools_Panel(Panel):
    bl_label = "Armature Tools"
    bl_idname = "SVF_PT_Armature_Tools_Panel"
    bl_category = "Armature"
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'


    @classmethod
    def poll(self, context):
        return context.object and context.object.type == "ARMATURE" and context.object.animation_data and context.object.animation_data.action
    
    def draw(self, context):
        
        ob = context.object
        data = ob.data
        scene = context.scene
        layout = self.layout
        col = layout.column(align=True)
        
        row = col.row(align=True)
        row.label(text = "Graph Editor", icon = "GRAPH")
        row = col.row(align=True)
        row.label(text = "Stacked View:")
        row.prop(scene, 'svf_use_expand', text = 'Expand', icon = "TRIA_RIGHT")
        row.prop(scene, 'svf_use_pin', text = 'Pin', icon = "PINNED")
        row = col.row(align=True)
        stack = row.operator(SVF_OT_Stack_Visible_Fcurves.bl_idname, text = "Stack Curves", icon = "COLLAPSEMENU")
        stack.use_pin = scene.svf_use_pin
        stack.use_expand = scene.svf_use_expand
        
        row = col.row(align=True)
        row.separator()
        
        row = col.row(align=True)
        row.label(text = "Armature", icon = "ARMATURE_DATA")
        row = col.row(align=True)
        row.label(text = "Override:")
        row.prop(scene, 'svf_override_drivers', text = 'Drivers', icon = "DRIVER")
        row.prop(scene, 'svf_override_layers', text = 'Layers', icon = "LAYER_USED")
    
        row = col.row(align=True)
        sync = row.operator(SVF_OT_Sync_Armature_Visibility.bl_idname, text = "Sync Visibility", icon = "UV_SYNC_SELECT")
        sync.override_drivers = scene.svf_override_drivers
        sync.override_layers = scene.svf_override_layers
        row = col.row(align=True)
        sel = row.operator(SVF_OT_Sync_Armature_Visibility_to_Selected.bl_idname, text = "Sync with Selected Curves", icon = "RESTRICT_SELECT_OFF")
        sel.override_drivers = scene.svf_override_drivers
        sel.override_layers = scene.svf_override_layers
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.operator(SVF_OT_Restore_Armature_Visibility.bl_idname, text = "Restore Visibility", icon = "FILE_REFRESH")



class SVF_PT_Freeze_Layers_Panel(Panel):
    """Freeze Armature Layers Panel"""
    bl_label = "Freeze Layers"
    bl_idname = "SVF_PT_Freeze_Layers_Panel"
    bl_category = "Armature"
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = "SVF_PT_Armature_Tools_Panel"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(self, context):
        return context.object and context.object.type == "ARMATURE" and context.object.animation_data and context.object.animation_data.action
    
    def draw(self, context):
        
        ob = context.object
        data = ob.data
        layout = self.layout
        col = layout.column(align=True)

        split_major = col.split(factor = 0.93)
        
        col = split_major.column(align=True)
        split = col.split()
        col_layers = split.column(align=True)
        row = col_layers.row(align=True)
        for i in range(8):
            lock_icon = "LAYER_USED"
            if context.active_pose_bone and i in [layer for layer in range(32) if context.active_pose_bone.bone.layers[layer]]:
                lock_icon = "LAYER_ACTIVE"
            if data.svf_freezed_layers.get("layer"+str(i)):
                lock_icon = "LOCKED"
            freeze = row.operator(SVF_OT_Freeze_Armature_Layer.bl_idname, text = "", icon = lock_icon)
            freeze.layer = i
        row = col_layers.row(align=True)
        for i in range(16,24):
            lock_icon = "LAYER_USED"
            if context.active_pose_bone and i in [layer for layer in range(32) if context.active_pose_bone.bone.layers[layer]]:
                lock_icon = "LAYER_ACTIVE"
            if data.svf_freezed_layers.get("layer"+str(i)):
                lock_icon = "LOCKED"
            freeze = row.operator(SVF_OT_Freeze_Armature_Layer.bl_idname, text = "", icon = lock_icon)
            freeze.layer = i
        col_layers = split.column(align=True)
        row = col_layers.row(align=True)
        for i in range(8, 16):
            lock_icon = "LAYER_USED"
            if context.active_pose_bone and i in [layer for layer in range(32) if context.active_pose_bone.bone.layers[layer]]:
                lock_icon = "LAYER_ACTIVE"
            if data.svf_freezed_layers.get("layer"+str(i)):
                lock_icon = "LOCKED"
            freeze = row.operator(SVF_OT_Freeze_Armature_Layer.bl_idname, text = "", icon = lock_icon)
            freeze.layer = i
        row = col_layers.row(align=True)
        for i in range(24,32):
            lock_icon = "LAYER_USED"
            if context.active_pose_bone and i in [layer for layer in range(32) if context.active_pose_bone.bone.layers[layer]]:
                lock_icon = "LAYER_ACTIVE"
            if data.svf_freezed_layers.get("layer"+str(i)):
                lock_icon = "LOCKED"
            freeze = row.operator(SVF_OT_Freeze_Armature_Layer.bl_idname, text = "", icon = lock_icon)
            freeze.layer = i
        
        col = split_major.column(align=True)
        row = col.row(align=True)
        row.operator(SVF_OT_Freeze_Armature_Layer_All.bl_idname, text = "", icon = "LOCKED")
        row = col.row(align=True)
        row.operator(SVF_OT_Freeze_Armature_Layer_None.bl_idname, text = "", icon = "UNLOCKED")



class SVF_PT_Freeze_Bones_Names_Panel(Panel):
    """Freeze Bones Names Panel"""
    bl_label = "Freeze Bones Names"
    bl_idname = "SVF_PT_Freeze_Bones_Names_Panel"
    bl_category = "Armature"
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = "SVF_PT_Armature_Tools_Panel"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(self, context):
        return context.object and context.object.type == "ARMATURE" and context.object.animation_data and context.object.animation_data.action
    
    def draw(self, context):
        
        scene = context.scene
        layout = self.layout
        col = layout.column(align=True)
        
        row = col.row()
        row.template_list("SVF_UL_Freeze_Bones_Names_List", "Freeze_Bones_Names_List", scene, "svf_freezed_names", scene, "svf_freezed_names_index")

        col = row.column(align = True)
        col.operator(SVF_OT_Freeze_Bones_Names_List_Add.bl_idname, text = "", icon = "ADD")
        col.operator(SVF_OT_Freeze_Bones_Names_List_Remove.bl_idname, text = "", icon = "REMOVE")
        row = col.row()
        row.prop(scene, "svf_freezed_bones_names_case_sensitive", text = "", icon = "SORTALPHA")

        
    
    
        
##################################   
########## REGISTRATION ##########
##################################            
classes = (
        SVF_PT_Armature_Tools_Panel,
        SVF_PT_Freeze_Layers_Panel,
        SVF_PT_Freeze_Bones_Names_Panel
        )
        
def register():
    
    bpy.types.Scene.svf_use_expand = BoolProperty(
        name = "Expand Stacked Channels",
        default = True,
        description = "Expand Stacked Channels"
        )
    bpy.types.Scene.svf_use_pin = BoolProperty(
        name = "Pin Stacked Channels",
        default = False,
        description = "Pin Stacked Channels"
        )
    bpy.types.Scene.svf_override_drivers = BoolProperty(
        name = "Override Drivers",
        default = True,
        description = "Allow to reveal the Pose Bones hidden by the Drivers"
        )
    bpy.types.Scene.svf_override_layers = BoolProperty(
        name = "Override Layers",
        default = True,
        description = "Allow to reveal the the Pose Bones by revealing the hidden Armature Layers"
        )
    bpy.types.Armature.svf_is_synced = BoolProperty(
        name = "Is Armature Synced",
        default = False,
        description = "Is the FCurves visibility synced with the Pose Bones visibility"
        )
    bpy.types.Scene.svf_freezed_bones_names_case_sensitive = BoolProperty(
        name = "Case Sensitive",
        default = False,
        description = "Equating the Item to a part of the Bone Name will be Case Sensitive"
        )
        
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Armature.svf_freezed_layers = PointerProperty(type = SVF_Freeze_Armature_Layers)
    bpy.types.Scene.svf_freezed_names = CollectionProperty(type = SVF_Freeze_Bones_Names)
    bpy.types.Scene.svf_freezed_names_index = IntProperty(name = "Freezed Name; Supports Wildcards using *", default = 0)

def unregister():
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.svf_use_expand
    del bpy.types.Scene.svf_use_pin
    del bpy.types.Scene.svf_override_drivers
    del bpy.types.Scene.svf_override_layers
    del bpy.types.Armature.svf_is_synced
    del bpy.types.Armature.svf_freezed_layers
    del bpy.types.Scene.svf_freezed_names
    del bpy.types.Scene.svf_freezed_names_index
    del bpy.types.Scene.svf_freezed_bones_names_case_sensitive