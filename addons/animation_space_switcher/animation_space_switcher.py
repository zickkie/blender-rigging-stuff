bl_info = {
    "name": "Space Switcher",
    "author": "Arthur Shapiro, Stanislav Ovcharov",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > N-panel",
    "description": "Switch Loc/Rot/Scale Space of the Selected Pose Bones seamlessly" ,
    "warning": "",
    "doc_url": "https://github.com/zickkie/blender-rigging-stuff/tree/main/addons/anmation_space_switcher",
    "category": "Animation",
}


import bpy
from random import randint
from bpy.types import Operator, Panel


class SS_OT_bake_to_empties(Operator):
    """Bake Pose Bones Animation to Empties"""
    bl_idname = "pose.space_switcher_bake_to_empties"
    bl_label = "Bake to Empties"
    bl_options = {'REGISTER', 'UNDO'}
    
    bake_loc: bpy.props.BoolProperty(default=True)
    bake_rot: bpy.props.BoolProperty(default=False)
    bake_scale: bpy.props.BoolProperty(default=False)
    
    @classmethod
    def poll(self, context):
        if (context.scene.space_switcher_bake_loc or context.scene.space_switcher_bake_rot or context.scene.space_switcher_bake_scale):
            if context.active_object and context.active_object.type == "ARMATURE" and context.active_object.mode == "POSE" and len(context.selected_pose_bones) > 0:
                return True
            else:
                return False
        else:
            return False
    
    def execute(self, context):
        
        # I try to connect constraints and Empties not just with naming but with Empties' Custom Properties also
        # Such Custom Properties contain info about correspondive Pose Bone and some random Int
        # This random is needed for situations when you click "Bake to Empties" multiple times

        ob = context.active_object
        rand = randint(0, 100000)
        
        # Random is added to the Scene Custom Properties
        if not "random_order" in context.scene or not context.scene["random_order"]:
            context.scene["random_order"] = [rand]
        else:
            list = context.scene["random_order"]
            list_new = []
            for item in list:
                list_new.append(item)
            list_new.append(rand)
            context.scene["random_order"] = list_new
        
        # Create Collection for Empties
        if not context.scene.collection.children.get("SpaceSwitchers"):
            coll = context.blend_data.collections.new("SpaceSwitchers")
            context.scene.collection.children.link(coll)
        else:
            coll = context.scene.collection.children.get("SpaceSwitchers")
            
        
        sel_list = [bone.name for bone in context.selected_pose_bones]
        
        i = context.scene.space_switcher_global_count

        channels = []
        
        # Empties creating
        for bone in context.selected_pose_bones:
        
            name = str(i) + "_SpaceSwitch_" + ob.name + "_" + bone.name
            
            empty = bpy.data.objects.new(name, None)
            empty.empty_display_type = 'CUBE'
            empty.show_in_front = True
            coll.objects.link(empty)
            empty["bone"] = (bone.name + "_" + str(rand))
            
            if self.bake_loc:
                emp_con = empty.constraints.new("COPY_LOCATION")
                emp_con.name = "CL_SpaceSwitch"
                emp_con.target = ob
                emp_con.subtarget = bone.name
                if not "location" in channels:
                    channels.append("location")
            
            if self.bake_rot:
                emp_con = empty.constraints.new("COPY_ROTATION")
                emp_con.name = "CR_SpaceSwitch"
                emp_con.target = ob
                emp_con.subtarget = bone.name
                if not "rotation" in channels:
                    channels.append("rotation")
        
            if self.bake_scale:
                emp_con = empty.constraints.new("COPY_SCALE")
                emp_con.name = "CS_SpaceSwitch"
                emp_con.target = ob
                emp_con.subtarget = bone.name
                if not "scale" in channels:
                    channels.append("scale")
        
        

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')

        # Baking Empties transforms        
        for emp in context.scene.objects:
            if "bone" in emp and str(rand) in emp["bone"]:
                emp.select_set(True)
                context.view_layer.objects.active = emp
        
        bpy.ops.nla.bake(frame_start=context.scene.space_switcher_frame_start,
                        frame_end=context.scene.space_switcher_frame_end,
                        step=1,
                        only_selected=True,
                        visual_keying=True,
                        clear_constraints=True,
                        clear_parents=False,
                        use_current_action=True,
                        clean_curves=False,
                        bake_types={'OBJECT'})
        
        # Removing FCurves of the Empties that are surplus due to Baking settings
        for emp in context.scene.objects:
            if "bone" in emp and str(rand) in emp["bone"]:
                emp.animation_data.action.name = emp.name
                for curve in emp.animation_data.action.fcurves:
                    exist = False
                    for channel in channels:
                        if channel in curve.data_path:
                            exist = True
                    if not exist:
                        emp.animation_data.action.fcurves.remove(curve)

                        
        bpy.ops.object.select_all(action='DESELECT')
        ob.select_set(True)
        context.view_layer.objects.active = ob
        bpy.ops.object.mode_set(mode='POSE')
        
        bpy.ops.pose.select_all(action='DESELECT')

        # Connecting Pose Bones back to Empties via constraints of corresponding type
        for name in sel_list:
            ob.pose.bones[name].bone.select = True
            ob.data.bones.active = ob.pose.bones[name].bone

            if self.bake_loc:
                bone_con = ob.pose.bones[name].constraints.new("COPY_LOCATION")
                bone_con.name = str(i) + "_CL_SpaceSwitch"
                for emp in bpy.data.objects:
                    if "bone" in emp and emp["bone"] == name + "_" + str(rand):
                        bone_con.target = emp
            
            if self.bake_rot:
                bone_con = ob.pose.bones[name].constraints.new("COPY_ROTATION")
                bone_con.name = str(i) + "_CR_SpaceSwitch"
                for emp in bpy.data.objects:
                    if "bone" in emp and emp["bone"] == name + "_" + str(rand):
                        bone_con.target = emp

            if self.bake_scale:
                bone_con = ob.pose.bones[name].constraints.new("COPY_SCALE")
                bone_con.name = str(i) + "_CS_SpaceSwitch"
                for emp in bpy.data.objects:
                    if "bone" in emp and emp["bone"] == name + "_" + str(rand):
                        bone_con.target = emp

        # Switching count to create the global amount of this operator use   
        context.scene.space_switcher_global_count += 1
        
        return {'FINISHED'}


class SS_OT_attach_switch(Operator):
    """Switch the Attach of Pose Bones to Empties"""
    bl_idname = "pose.space_switcher_attach_switch"
    bl_label = "Attach Switch"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    @classmethod
    def poll(self, context):
        state = False
        if context.active_object and context.active_object.type == "ARMATURE" and context.active_object.mode == "POSE" and len(context.selected_pose_bones) > 0:
            for bone in context.selected_pose_bones:
                for con in bone.constraints:
                    if "COPY" in con.type and "bone" in con.target:
                        state = True
        return state         
    
    
    def execute(self, context):
        
        # Simply turn On/Off the visibilty of the Attach Constraints for the Selected Pose Bones
        ob = context.active_object

        for bone in context.selected_pose_bones:
                for con in bone.constraints:
                    if "COPY" in con.type and con.target and "bone" in con.target:
                        con.mute = context.scene.space_switcher_constraints_switch

        context.scene.space_switcher_constraints_switch = not context.scene.space_switcher_constraints_switch
        
        return {'FINISHED'}


class SS_OT_attach_clear(Operator):
    """Delete the the latest Empties & Pose Bones Attach Constraints"""
    bl_idname = "pose.space_switcher_attach_clear"
    bl_label = "Attach Clear"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    @classmethod
    def poll(self, context):
        return "random_order" in context.scene and len(context.scene["random_order"]) > 0       
    
    def execute(self, context):
        
        # Delete Empties, Empties' Actions and Pose BonesConstraints,
        # that have been created by the last use of "Bake to Empties" operator
        ob = context.active_object

        curr_rand = context.scene["random_order"][-1]

        for bone in context.selected_pose_bones:
            for con in bone.constraints:
                if not con.target:
                    if "SpaceSwitch" in con.name:
                        bone.constraints.remove(con)
                elif "COPY" in con.type and "bone" in con.target:
                        if con.target["bone"] == (bone.name + "_" + str(curr_rand)):
                            bone.constraints.remove(con)
            
            for emp in bpy.data.objects:
                if "bone" in emp and emp["bone"] == (bone.name + "_" + str(curr_rand)):
                    bpy.data.actions.remove(emp.animation_data.action)
                    bpy.data.objects.remove(emp, do_unlink = True)

        
        # If there are no Empties in Scene that contain Property with last random,
        # then this random integer is replaced from Scene Custom Property
        # thus the "queue" is now one element shorter
        remains = False
        for obj in bpy.data.objects:
            if "bone" in obj and str(curr_rand) in obj["bone"]:
                remains = True

        if not remains:
            rand_new = [item for item in context.scene["random_order"]]
            rand_new.pop(-1)
            context.scene["random_order"] = rand_new

        
        return {'FINISHED'}


class WM_OT_scene_clear(Operator):
    """Delete All the the Empties & Pose Bones Attach Constraints"""
    bl_idname = "wm.space_switcher_scene_clear"
    bl_label = "Delete ALL Constraints & Empties in Scene?"
    bl_options = {'REGISTER', 'UNDO'}    
    
    def execute(self, context):
        
        # Just delete everything connected in any way with all these Empties
        # (and delete Empties themselves too)
        ob = context.active_object

        for bone in ob.pose.bones:
                for con in bone.constraints:
                    if "COPY" in con.type and not con.target:
                        if "SpaceSwitch" in con.name:
                            bone.constraints.remove(con)
                    elif "COPY" in con.type and "bone" in con.target:
                        if "bone" in con.target:
                            bone.constraints.remove(con)

        
        for emp in bpy.data.objects:
            if "bone" in emp:
                bpy.data.actions.remove(emp.animation_data.action)
                bpy.data.objects.remove(emp, do_unlink = True)
        
        context.scene["random_order"] = []
        for coll in bpy.data.collections:
            if "SpaceSwitch" in coll.name:
                bpy.data.collections.remove(coll)

        
        return {'FINISHED'}
    
    # Popup "Are you sure" window
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class SS_OT_bake_to_bones(Operator):
    """Bake the final Transforms back to Seleceted Pose Bones"""
    bl_idname = "pose.space_switcher_bake_to_bones"
    bl_label = "Bake to Bones"
    bl_options = {'REGISTER', 'UNDO'}
    
    clear: bpy.props.BoolProperty(default = True)
    new: bpy.props.BoolProperty(default = True)
    
    @classmethod
    def poll(self, context):
        return context.active_object and context.active_object.type == "ARMATURE" and context.active_object.mode == "POSE" and len(context.selected_pose_bones) > 0
    
    def execute(self, context):
        
        # Bake final Transforms of the Empties back to the Selected Pose Bones
        bpy.ops.nla.bake(frame_start=context.scene.space_switcher_frame_start,
                        frame_end=context.scene.space_switcher_frame_end,
                        step=1,
                        only_selected=True,
                        visual_keying=True,
                        clear_constraints=False,
                        clear_parents=False,
                        use_current_action = not self.new,
                        clean_curves=False,
                        bake_types={'POSE'})
        
        # Execute SS_OT_attach_clear after baking
        if self.clear:
            bpy.ops.pose.space_switcher_attach_clear()

        return {'FINISHED'}


class SS_OT_bake_frames_from_scene(Operator):
    """Copy Start and End Baking Frames from Scene"""
    bl_idname = "pose.space_switcher_frames_from_scene"
    bl_label = "Attach Clear"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        context.scene.space_switcher_frame_start = context.scene.frame_start
        context.scene.space_switcher_frame_end = context.scene.frame_end

        return {'FINISHED'}


class VIEW3D_PT_space_switcher_panel(Panel):
    """Space Switching Addon UI"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animation"
    bl_label = "Space Switcher"

    def draw(self, context):

        scene = context.scene

        layout = self.layout
        col = layout.column()

        box_bake = col.box()
        box_bake.label(text = "Bake Channels", icon = "GRAPH")
        col_bake = box_bake.column(align = True)
        row = col_bake.row(align = True)
        row.prop(scene, "space_switcher_bake_loc", text = "Location", toggle = True)
        row = col_bake.row(align = True)
        row.prop(scene, "space_switcher_bake_rot", text = "Rotation", toggle = True)
        row = col_bake.row(align = True)
        row.prop(scene, "space_switcher_bake_scale", text = "Scale", toggle = True)

        box_bake_frames = col.box()
        col_bake_frames = box_bake_frames.column(align = True)
        row = col_bake_frames.row(align = True)
        row.label(text = "Bake Frames", icon = "FRAME_NEXT")
        row.operator(SS_OT_bake_frames_from_scene.bl_idname, text = 'From Scene', icon = "SCENE_DATA")

        split_frames = col_bake_frames.split()

        col_fr_start = split_frames.column()
        row = col_fr_start.row()
        row.label(text="Frame Start")
        row = col_fr_start.row()
        row.prop(scene, "space_switcher_frame_start", text = "")

        col_fr_end = split_frames.column()
        row = col_fr_end.row()
        row.label(text="Frame End")
        row = col_fr_end.row()
        row.prop(scene, "space_switcher_frame_end", text = "")
        

        row = col.row()
        bte = row.operator(SS_OT_bake_to_empties.bl_idname, text = 'Bake to Empties', icon = "OUTLINER_OB_EMPTY")
        bte.bake_loc = context.scene.space_switcher_bake_loc
        bte.bake_rot = context.scene.space_switcher_bake_rot
        bte.bake_scale = context.scene.space_switcher_bake_scale
        if (context.scene.space_switcher_bake_loc or context.scene.space_switcher_bake_rot or context.scene.space_switcher_bake_scale):
            if context.active_object and context.active_object.type == "ARMATURE" and context.active_object.mode == "POSE" and len(context.selected_pose_bones) > 0:
                row.enabled = True
            else:
                row.enabled = False
        else:
            row.enabled = False

        row = col.row()

        if context.scene.space_switcher_constraints_switch:
            ic = "RESTRICT_VIEW_OFF"
            lab = "Disable Constraints"
        else:
            ic = "RESTRICT_VIEW_ON"
            lab = "Enable Constraints"
        row.operator(SS_OT_attach_switch.bl_idname, text = lab, icon = ic)
        
        row.operator(SS_OT_attach_clear.bl_idname, text = 'Attach Clear', icon = "CANCEL")
        state = False
        if context.active_object and context.active_object.type == "ARMATURE" and context.active_object.mode == "POSE" and len(context.selected_pose_bones) > 0:
            for bone in context.selected_pose_bones:
                for con in bone.constraints:
                    if "COPY" in con.type and "bone" in con.target:
                        state = True
        row.enabled = state

        row = col.row()
        row.operator(WM_OT_scene_clear.bl_idname, text = 'Clear Scene', icon = "SHADERFX")
        state = False
        row.enabled = (context.active_object and context.active_object.type == "ARMATURE")



        row = col.row()
        row.separator(factor = 1)

        row = col.row()
        btb = row.operator(SS_OT_bake_to_bones.bl_idname, text = 'Bake to Bones', icon = "BONE_DATA")
        if context.active_object and context.active_object.type == "ARMATURE" and context.active_object.mode == "POSE" and len(context.selected_pose_bones) > 0:
            row.enabled = True
        else:
            row.enabled = False
        btb.clear = context.scene.space_switcher_clear_after_bake
        btb.new = context.scene.space_switcher_bake_to_new_action
        
        row = col.row(align=True)
        row.prop(scene, "space_switcher_clear_after_bake", text = "Clear after Bake", icon = "TRASH")
        row.prop(scene, "space_switcher_bake_to_new_action", text = "To New Action", icon = "PLUS")
        




        
        
classes = (
    SS_OT_bake_to_empties,
    SS_OT_attach_switch,
    SS_OT_attach_clear,
    WM_OT_scene_clear,
    SS_OT_bake_to_bones,
    SS_OT_bake_frames_from_scene,
    VIEW3D_PT_space_switcher_panel,
)

# Thank you Dr.Siebren for this great "register_classes_factory" function, I haven't known about that!
_register, _unregister = bpy.utils.register_classes_factory(classes)
    
def register():
    
    bpy.types.Scene.space_switcher_global_count = bpy.props.IntProperty(
        name = "Global Count",
        default = 0,
        min = 0,
        max = 100000,
        description = "Global Count"
        )
    
    bpy.types.Scene.space_switcher_constraints_switch = bpy.props.BoolProperty(
        name = "Constraints Switch",
        default = False,
        description = "Turn Off/On the visibility of Bones Attach to Empties"
        )
    
    bpy.types.Scene.space_switcher_clear_after_bake = bpy.props.BoolProperty(
        name = "Clear after Bake",
        default = True,
        description = "For Selected Bones - Delete Constraints and Empties after Bake "
        )

    bpy.types.Scene.space_switcher_bake_to_new_action = bpy.props.BoolProperty(
        name = "Bake to New Action",
        default = False,
        description = "Bake to New Action"
        )

    bpy.types.Scene.space_switcher_bake_loc = bpy.props.BoolProperty(
        name = "Bake Location",
        default = True,
        description = "Bake Location"
        )
    
    bpy.types.Scene.space_switcher_bake_rot = bpy.props.BoolProperty(
        name = "Bake Rotation",
        default = True,
        description = "Bake Rotation"
        )
    
    bpy.types.Scene.space_switcher_bake_scale = bpy.props.BoolProperty(
        name = "Bake Scale",
        default = True,
        description = "Bake Scale"
        )

    bpy.types.Scene.space_switcher_frame_start = bpy.props.IntProperty(
        name = "Frame Start",
        default = 0,
        min = -100000,
        max = 100000,
        description = "Frame Start"
    )

    bpy.types.Scene.space_switcher_frame_end = bpy.props.IntProperty(
        name = "Frame End",
        default = 0,
        min = -100000,
        max = 100000,
        description = "Frame End"
    )

    _register()
    
def unregister():
    
    _unregister()

    del bpy.types.Scene.space_switcher_global_count
    del bpy.types.Scene.space_switcher_constraints_switch
    del bpy.types.Scene.space_switcher_clear_after_bake
    del bpy.types.Scene.space_switcher_bake_to_new_action
    del bpy.types.Scene.space_switcher_bake_loc
    del bpy.types.Scene.space_switcher_bake_rot
    del bpy.types.Scene.space_switcher_bake_scale
    del bpy.types.Scene.space_switcher_frame_start
    del bpy.types.Scene.space_switcher_frame_end


if __name__ == "__main__":
    register()
