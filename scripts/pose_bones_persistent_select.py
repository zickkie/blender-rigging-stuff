import bpy
from bpy.app.handlers import persistent


@persistent
def picker_selection_Cat(scene):

    ob = None
    try:
        if bpy.context.active_object and bpy.context.active_object.name == "Cat":
            ob = bpy.context.active_object
    except:
        pass

    pose_bones = ob.pose.bones
    data_bones = ob.data.bones
    prefix = "PROXY_CTRL_"

    if scene.picker_is_operating_Cat:
    
        for bone in data_bones:
            
            if data_bones.get(prefix + bone.name):

                if scene.picker_strict_selection_Cat:
                    bone.select = data_bones[prefix + bone.name].select
                    active = data_bones.active
                    if active.name.startswith(prefix):
                        data_bones.active = data_bones[active.name.replace(prefix, "")]

                else:
                    if data_bones[prefix + bone.name].select:
                        bone.select = True
                        data_bones.active = bone.name

                if not scene.picker_combined_selection_Cat:
                    data_bones[prefix + bone.name].select = False

            if bone.name.startswith(prefix):
                bone.show_wire = not bone.select
        




bpy.app.handlers.depsgraph_update_pre.append(select_bone)
