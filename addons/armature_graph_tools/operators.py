import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       CollectionProperty,
                       PointerProperty,
                       )
from bpy.types import (Operator,
                       Panel,
                       PropertyGroup,
                       UIList
                       )
from .functions import *



class SVF_Freeze_Bones_Names(PropertyGroup):
    """Bones names to exclude from any Add-On's Affection"""
    name: StringProperty(name="Bone Name", description="Bone name to exclude from any Add-On's Affection", default="Bone", update = freezed_bone_name_check)

class SVF_Freeze_Armature_Layers(PropertyGroup):
    """Armature Layers to exclude from any Add-On's Affection"""
    """Yes I know this looks outstandingly stupid but CollectionProperty.add() won't work for the Linked Data-Block,
    neither I have the ability to change the bpy.types.Armature.BoolProperty for the Linked stuff...
    so I use the Operator that changes the Property instead of just doing this from UI"""
    layer0: BoolProperty(default = False)
    layer1: BoolProperty(default = False)
    layer2: BoolProperty(default = False)
    layer3: BoolProperty(default = False)
    layer4: BoolProperty(default = False)
    layer5: BoolProperty(default = False)
    layer6: BoolProperty(default = False)
    layer7: BoolProperty(default = False)
    layer8: BoolProperty(default = False)
    layer9: BoolProperty(default = False)
    layer10: BoolProperty(default = False)
    layer11: BoolProperty(default = False)
    layer12: BoolProperty(default = False)
    layer13: BoolProperty(default = False)
    layer14: BoolProperty(default = False)
    layer15: BoolProperty(default = False)
    layer16: BoolProperty(default = False)
    layer17: BoolProperty(default = False)
    layer18: BoolProperty(default = False)
    layer19: BoolProperty(default = False)
    layer20: BoolProperty(default = False)
    layer21: BoolProperty(default = False)
    layer22: BoolProperty(default = False)
    layer23: BoolProperty(default = False)
    layer24: BoolProperty(default = False)
    layer25: BoolProperty(default = False)
    layer26: BoolProperty(default = False)
    layer27: BoolProperty(default = False)
    layer28: BoolProperty(default = False)
    layer29: BoolProperty(default = False)
    layer30: BoolProperty(default = False)
    layer31: BoolProperty(default = False)



class SVF_UL_Freeze_Bones_Names_List(UIList):
    """Freeze Bones Names List."""

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(item, "name", text =  "", emboss = False, icon = "BONE_DATA")

        elif self.layout_type in {'GRID'}:
            #layout.alignment = 'CENTER'
            layout.prop(item, "name", text =  "", emboss = False, icon = "BONE_DATA")

    

class SVF_OT_Stack_Visible_Fcurves(Operator):
    """Move Visible FCurves to the Top"""
    bl_idname = "graph.stack_visible_fcurves"
    bl_label = "Moves Visible FCurves to the Top"
    bl_options = {'REGISTER', 'UNDO'}
    
    use_expand: bpy.props.BoolProperty(
        name = "Expand",
        default = False,
        description = "Expand"
        )
    
    use_pin: bpy.props.BoolProperty(
        name = "Pin",
        default = False,
        description = "Pin"
        )
    
    
    def execute(self, context):
        
        ob = context.active_object
        action = ob.animation_data.action
        fcurves = action.fcurves
        
        vis_curves = []
        
        for curve in fcurves:
            if not curve.hide:
                vis_curves.append(curve)
            else:
                if curve.group:
                    curve.group.select = False
                    curve.group.show_expanded = False
                    curve.group.show_expanded_graph = False
                    curve.group.use_pin = False
        
        if len(vis_curves) > 0:
            vis_groups = []
            for curve in vis_curves:
                if curve.group:
                    if not curve.group in vis_groups:
                        vis_groups.append(curve.group)
                
                else:
                    if action.groups.get("UNGROUPPED"):
                        curve.group = action.groups.get("UNGROUPPED")
                        curve.group.select = True
                    else:
                        group_new = action.groups.new("UNGROUPPED")
                        curve.group = group_new
                        curve.group.select = True
                    vis_groups.append(curve.group)
            
            for group in vis_groups:
                group.select = True
                group.show_expanded = self.use_expand
                group.show_expanded_graph = self.use_expand
                if self.use_pin:
                    group.use_pin = True
                else:
                    group.use_pin = False
        
            
            bpy.ops.anim.channels_move(direction='TOP')
            
        
        return {'FINISHED'}


class SVF_OT_Sync_Armature_Visibility(Operator):
    """Synchronize the Visibility of the FCurves and the Pose Bones"""
    bl_idname = "graph.sync_armature_visibility"
    bl_label = "Synchronize the Visibility of the FCurves and the Pose Bones"
    bl_options = {'REGISTER', 'UNDO'}
    
    override_drivers: bpy.props.BoolProperty(
        name = "Override Drivers",
        default = True,
        description = "Override Drivers"
        )
    
    override_layers: bpy.props.BoolProperty(
        name = "Override Layers",
        default = True,
        description = "Override Layers"
        )
    
    def execute(self, context):
        
        ob = context.active_object
        data = ob.data
        action = ob.animation_data.action
        fcurves = action.fcurves
        
        if not ob.data.svf_is_synced:
            armature_state(context)
        
        vis_curves_bones = [curve.data_path.split('pose.bones["')[1].split('"]')[0] for curve in fcurves if ('pose.bones["' in curve.data_path and not curve.hide)]
        print(vis_curves_bones)
        if vis_curves_bones:
            if context.area.spaces[0].dopesheet.show_only_selected:
                for bone in ob.pose.bones:
                    if not (any(x in [i for i in range(32) if bone.bone.layers[i]] for x in [j for j in range(32) if getattr(data.svf_freezed_layers, "layer"+str(j))]) or freeze_bones_list_search(context, bone.name)):
                        if bone in context.selected_pose_bones and bone.name in vis_curves_bones:
                            set_bone_visibility(context, bone.name, self.override_drivers, self.override_layers, "show")
                        else:
                            set_bone_visibility(context, bone.name, self.override_drivers, self.override_layers, "hide")
            else:
                for bone in ob.pose.bones:
                    if not (any(x in [i for i in range(32) if bone.bone.layers[i]] for x in [j for j in range(32) if getattr(data.svf_freezed_layers, "layer"+str(j))]) or freeze_bones_list_search(context, bone.name)):
                        if bone.name in vis_curves_bones:
                            set_bone_visibility(context, bone.name, self.override_drivers, self.override_layers, "show")
                        else:
                            set_bone_visibility(context, bone.name, self.override_drivers, self.override_layers, "hide")
            data.svf_is_synced = True
        else:
            self.report({"WARNING"}, "No Bones-related Selected FCurves")
        
        return {'FINISHED'}
        


class SVF_OT_Sync_Armature_Visibility_to_Selected(Operator):
    """Synchronize the Visibility of the Pose Bones with the FCurves Selection"""
    bl_idname = "graph.sync_armature_visibility_to_selected"
    bl_label = "Synchronize the Visibility the Pose Bones with the FCurves Selection"
    bl_options = {'REGISTER', 'UNDO'}
    
    override_drivers: bpy.props.BoolProperty(
        name = "Override Drivers",
        default = True,
        description = "Override Drivers"
        )
    
    override_layers: bpy.props.BoolProperty(
        name = "Override Layers",
        default = True,
        description = "Override Layers"
        )
    
    def execute(self, context):
        
        ob = context.active_object
        data = ob.data
    
        
        if not ob.data.svf_is_synced:
            armature_state(context)
        
        sel_curves_bones = [curve.data_path.split('pose.bones["')[1].split('"]')[0] for curve in context.selected_visible_fcurves if 'pose.bones["' in curve.data_path]

        if sel_curves_bones:
            for bone in ob.pose.bones:
                if not (any(x in [i for i in range(32) if bone.bone.layers[i]] for x in [j for j in range(32) if getattr(data.svf_freezed_layers, "layer"+str(j))]) or freeze_bones_list_search(context, bone.name)):
                    if bone.name in sel_curves_bones:
                        set_bone_visibility(context, bone.name, self.override_drivers, self.override_layers, "show")
                        bone.bone.select = True
                    else:
                        bone.bone.select = False
                        set_bone_visibility(context, bone.name, self.override_drivers, self.override_layers, "hide")
            data.bones.active = data.bones[sel_curves_bones[-1]]
        else:
            self.report({"WARNING"}, "No Bones-related Selected FCurves")
                    
        
        data.svf_is_synced = True
        
        return {'FINISHED'}
    
    

class SVF_OT_Restore_Armature_Visibility(Operator):
    """Restore the Visibility of the Pose Bones as at the moment before Syncing"""
    bl_idname = "graph.restore_armature_visibility"
    bl_label = "Restore the Visibility of the Pose Bones as at the moment before Syncing"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        
        ob = context.active_object
        data = ob.data
        if "svf_armature_state" in data.keys():
            for bone in ob.pose.bones:
                if data["svf_armature_state"][bone.name]["bone_driver"]:
                    for driver in data.animation_data.drivers:
                        if bone.name in driver.data_path and "hide" in driver.data_path:
                            driver.mute = data["svf_armature_state"][bone.name]["bone_mute"]
                bone.bone.hide = data["svf_armature_state"][bone.name]["bone_hide"]
            for i in range(32):
                data.layers[i] = data["svf_armature_state"]["layers"][i]
        
        data.svf_is_synced = False
        
        return {'FINISHED'}

   

class SVF_OT_Freeze_Armature_Layer(Operator):
    """Freeze Pose Bones of this Armature Layer for any Add-On's affection"""
    bl_idname = "graph.freeze_armature_layer"
    bl_label = "Freeze Layer"
    bl_options = {'REGISTER', 'UNDO'}
    
    layer: IntProperty()
    
    def execute(self, context):
        
        setattr(context.active_object.data.svf_freezed_layers, ("layer"+str(self.layer)), not(getattr(context.active_object.data.svf_freezed_layers, ("layer"+str(self.layer)))))
        
        return {'FINISHED'}



class SVF_OT_Freeze_Armature_Layer_All(Operator):
    """Freeze Pose Bones of ALL the Armature Layers for any Add-On's affection"""
    bl_idname = "graph.freeze_armature_layer_all"
    bl_label = "Freeze All Layers"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        for i in range(32):
            setattr(context.active_object.data.svf_freezed_layers, ("layer"+str(i)), True)
        
        return {'FINISHED'}



class SVF_OT_Freeze_Armature_Layer_None(Operator):
    """Clear the Armature Layer Freeze"""
    bl_idname = "graph.freeze_armature_layer_none"
    bl_label = "Clear Layers Freeze"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        for i in range(32):
            setattr(context.active_object.data.svf_freezed_layers, ("layer"+str(i)), False)
        
        return {'FINISHED'}



class SVF_OT_Freeze_Bones_Names_List_Add(Operator):
    """Add Name to a Freezed List"""
    bl_idname = "graph.freeze_bones_names_list_add"
    bl_label = "Add Name"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        context.scene.svf_freezed_names.add()
        context.scene.svf_freezed_names_index = len(context.scene.svf_freezed_names) - 1
        
        return {'FINISHED'}



class SVF_OT_Freeze_Bones_Names_List_Remove(Operator):
    """Remove Name from a Freezed List"""
    bl_idname = "graph.freeze_bones_names_list_remove"
    bl_label = "Remove Name"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.scene.svf_freezed_names) > 0
    
    def execute(self, context):
        
        ind = context.scene.svf_freezed_names_index
        context.scene.svf_freezed_names.remove(ind)
        if ind == 0:
            context.scene.svf_freezed_names_index = 0
        else:
            context.scene.svf_freezed_names_index = ind - 1

        return {'FINISHED'}



##################################   
########## REGISTRATION ##########
##################################            
classes = (
        SVF_Freeze_Bones_Names,
        SVF_Freeze_Armature_Layers,
        SVF_UL_Freeze_Bones_Names_List,
        SVF_OT_Stack_Visible_Fcurves,
        SVF_OT_Sync_Armature_Visibility,
        SVF_OT_Sync_Armature_Visibility_to_Selected,
        SVF_OT_Restore_Armature_Visibility,
        SVF_OT_Freeze_Armature_Layer,
        SVF_OT_Freeze_Armature_Layer_All,
        SVF_OT_Freeze_Armature_Layer_None,
        SVF_OT_Freeze_Bones_Names_List_Add,
        SVF_OT_Freeze_Bones_Names_List_Remove
        )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)