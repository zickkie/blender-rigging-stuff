import bpy

drivers = bpy.context.active_object.animation_data.drivers

for bone in bpy.context.selected_pose_bones:
    for drv in drivers:
        if bone.name in drv.data_path and "bbone" in drv.data_path:
            for var in drv.driver.variables:
                for tgt in var.targets:
                    if "rotation" in tgt.data_path:
                        if int(tgt.data_path[-2]) == 0:
                            type = "ROT_X"
                            space = "LOCAL_SPACE"
                            bone_tgt = tgt.data_path.split('["')[1].split('"]')[0]
                            var.type = "TRANSFORMS"
                            var.targets[0].bone_target = bone_tgt
                            var.targets[0].transform_type = type
                            var.targets[0].transform_space = space