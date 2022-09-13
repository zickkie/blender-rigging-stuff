import fnmatch

def set_bone_visibility(context, bone, mute_driver, mute_layers, goal):
    """Hides or inhides the Pose Bone depending on its presence in the FCurves list and Layers/Drivers properties of the Operator"""
    pbone = context.object.pose.bones[bone]
    if mute_layers and goal == "show":
        visible_layers = False
        for i in range(32):
            if pbone.bone.layers[i]:
                layer = i
                if context.object.data.layers[i]:
                    visible_layers = True
        if not visible_layers:
            context.object.data.layers[layer] = True

            
    if mute_driver:
        if context.object.data and context.object.data.animation_data and context.object.data.animation_data.drivers:
            for driver in context.object.data.animation_data.drivers:
                if "hide" in driver.data_path and bone in driver.data_path:
                    if not driver.mute:
                        driver.mute = True
                        driver.driver.expression += ""
    
    if not pbone.bone.hide:
        if goal == "show":
            pass
        else:
            pbone.bone.hide = True
    else:
        if goal == "show":
            pbone.bone.hide = False
        else:
            pass            


def armature_state(context):
    """Creates the dictionary of the Armature Pose Bones / Layers Visibility at the moment before Sync"""
    ob = context.active_object
    data = ob.data
    data["svf_armature_state"] = {}
    armature_state_dict = {}
    armature_drivers = [driver.data_path.split('bones["')[1].split('"]')[0] for driver in data.animation_data.drivers if ('bones["' in driver.data_path and "hide" in driver.data_path)]
    layers = [armature_layer for armature_layer in data.layers]
    for bone in ob.pose.bones:
        bone_hide = bone.bone.hide
        bone_driver = (bone.name in armature_drivers)
        bone_mute = False
        if bone_driver:
            for driver in data.animation_data.drivers:
                if bone.name in driver.data_path and "hide" in driver.data_path:
                    bone_mute = driver.mute

        armature_state_dict[bone.name] = {
                                    "bone_hide": bone_hide,
                                    "bone_driver": bone_driver,
                                    "bone_mute": bone_mute,
                                    "layers": layers}
    data["svf_armature_state"] = armature_state_dict
    data["svf_armature_state"]["layers"] = layers


def freezed_bone_name_check(self, context):
    """Checks the Freeze Bones Names item naming"""
    scene = context.scene
    name = scene.svf_freezed_names[scene.svf_freezed_names_index].name
    if (name.count("*") == len(name)) or (name.count(" ") == len(name)) or name == "":
        scene.svf_freezed_names[scene.svf_freezed_names_index].name = "Untitled"


def freeze_bones_list_search(context, bone_name):
    """Checks if the Bone Name is in the Freezed Bones List"""
    scene = context.scene
    freeze_list = [key for key in scene.svf_freezed_names.keys()]
    if context.scene.svf_freezed_bones_names_case_sensitive:
        return any(fnmatch.fnmatchcase(bone_name, item) for item in freeze_list)
    else:
        return any(fnmatch.fnmatch(bone_name, item) for item in freeze_list)
