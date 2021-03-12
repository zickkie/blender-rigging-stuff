import bpy
import numpy as np
import math
from mathutils import Quaternion


def setup_joints(joint_names, prefix, mode="all"):
    bpy.ops.object.select_all(action="DESELECT")
    if mode == "all":
        for joint_name in joint_names:
            bpy.ops.mesh.primitive_uv_sphere_add(
                radius=0.04, enter_editmode=False, align="WORLD", location=(0, 0, 0)
            )
            for obj in bpy.data.objects:
                if obj.name == "Sphere":
                    obj.name = prefix + joint_name
                    if joint_name != "root":
                        obj.parent = bpy.data.objects[prefix + "root"]
    elif mode == "root":
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=0.04, enter_editmode=False, align="WORLD", location=(0, 0, 0)
        )
        bpy.data.objects["Sphere"].name = prefix + "root"
    else:
        raise ValueError("Only all or root is supported")


def create_bones(bones, coords, prefix):
    bpy.ops.object.armature_add(
        enter_editmode=False, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
    )
    armature = bpy.data.objects["Armature"]
    armature.name = prefix + "Skeleton"
    bpy.ops.object.select_all(action="DESELECT")
    arm_obj = bpy.data.objects[prefix + "Skeleton"]
    arm_obj.select_set(True)
    bpy.context.view_layer.objects.active = arm_obj
    bpy.ops.object.mode_set(mode="EDIT", toggle=False)

    edit_bone = arm_obj.data.edit_bones
    edit_bone.remove(edit_bone[0])
    for j1_name, j2_name in bones:
        b = edit_bone.new(prefix + j1_name + "_" + j2_name)

        b.head = coords[j1_name]
        b.tail = coords[j2_name]
        # b.use_inherit_rotation = False

    # TODO add proper DFS, but we'll have to decide on the tree root first
    edit_bone[prefix + "thumb3_thumb_tip"].parent = edit_bone[prefix + "thumb2_thumb3"]
    edit_bone[prefix + "thumb2_thumb3"].parent = edit_bone[prefix + "thumb1_thumb2"]
    edit_bone[prefix + "thumb1_thumb2"].parent = edit_bone[prefix + "root_thumb1"]
    edit_bone[prefix + "point3_point_tip"].parent = edit_bone[prefix + "point2_point3"]
    edit_bone[prefix + "point2_point3"].parent = edit_bone[prefix + "point1_point2"]
    edit_bone[prefix + "point1_point2"].parent = edit_bone[prefix + "root_point1"]
    edit_bone[prefix + "middle3_middle_tip"].parent = edit_bone[prefix + "middle2_middle3"]
    edit_bone[prefix + "middle2_middle3"].parent = edit_bone[prefix + "middle1_middle2"]
    edit_bone[prefix + "middle1_middle2"].parent = edit_bone[prefix + "root_middle1"]
    edit_bone[prefix + "ring3_ring_tip"].parent = edit_bone[prefix + "ring2_ring3"]
    edit_bone[prefix + "ring2_ring3"].parent = edit_bone[prefix + "ring1_ring2"]
    edit_bone[prefix + "ring1_ring2"].parent = edit_bone[prefix + "root_ring1"]
    edit_bone[prefix + "pinky3_pinky_tip"].parent = edit_bone[prefix + "pinky2_pinky3"]
    edit_bone[prefix + "pinky2_pinky3"].parent = edit_bone[prefix + "pinky1_pinky2"]
    edit_bone[prefix + "pinky1_pinky2"].parent = edit_bone[prefix + "root_pinky1"]
    bpy.ops.object.mode_set(mode="OBJECT")
    armature.parent = bpy.data.objects[prefix + "root"]


def set_constraints(j1_name, j2_name, prefix):
    bpy.ops.object.select_all(action="DESELECT")
    arm_obj = bpy.data.objects[prefix + "Skeleton"]
    arm_obj.select_set(True)
    bpy.context.view_layer.objects.active = arm_obj
    bpy.ops.object.mode_set(mode="POSE", toggle=False)
    arm_obj.pose.bones[prefix + j1_name + "_" + j2_name].constraints.new("COPY_LOCATION")
    arm_obj.pose.bones[prefix + j1_name + "_" + j2_name].constraints.new("DAMPED_TRACK")
    bpy.context.object.pose.bones[prefix + j1_name + "_" + j2_name].constraints[
        "Damped Track"
    ].target = bpy.data.objects[prefix + j2_name]

    bpy.context.object.pose.bones[prefix + j1_name + "_" + j2_name].constraints[
        "Copy Location"
    ].target = bpy.data.objects[prefix + j1_name]
    bpy.ops.object.mode_set(mode="OBJECT")


coords_joints = [
    "root",
    "point1",
    "point2",
    "point3",
    "middle1",
    "middle2",
    "middle3",
    "pinky1",
    "pinky2",
    "pinky3",
    "ring1",
    "ring2",
    "ring3",
    "thumb1",
    "thumb2",
    "thumb3",
    "point_tip",
    "middle_tip",
    "pinky_tip",
    "ring_tip",
    "thumb_tip",
]


def map_coords(coords_raw, mode="coords"):
    if mode == "coords":
        return {name: coords_raw[i] for i, name in enumerate(coords_joints)}
    elif mode == "quats":
        return {
            "root": coords_raw[0],
            "root_thumb1": coords_raw[0].rotation_difference(coords_raw[13]),
            "thumb1_thumb2": coords_raw[13].rotation_difference(coords_raw[14]),
            "thumb2_thumb3": coords_raw[14].rotation_difference(coords_raw[15]),
            "thumb3_thumb_tip": coords_raw[15].rotation_difference(coords_raw[20]),
            "root_point1": coords_raw[0].rotation_difference(coords_raw[1]),
            "point1_point2": coords_raw[1].rotation_difference(coords_raw[2]),
            "point2_point3": coords_raw[2].rotation_difference(coords_raw[3]),
            "point3_point_tip": coords_raw[3].rotation_difference(coords_raw[16]),
            "root_middle1": coords_raw[0].rotation_difference(coords_raw[4]),
            "middle1_middle2": coords_raw[4].rotation_difference(coords_raw[5]),
            "middle2_middle3": coords_raw[5].rotation_difference(coords_raw[6]),
            "middle3_middle_tip": coords_raw[6].rotation_difference(coords_raw[17]),
            "root_ring1": coords_raw[0].rotation_difference(coords_raw[10]),
            "ring1_ring2": coords_raw[10].rotation_difference(coords_raw[11]),
            "ring2_ring3": coords_raw[11].rotation_difference(coords_raw[12]),
            "ring3_ring_tip": coords_raw[12].rotation_difference(coords_raw[19]),
            "root_pinky1": coords_raw[0].rotation_difference(coords_raw[7]),
            "pinky1_pinky2": coords_raw[7].rotation_difference(coords_raw[8]),
            "pinky2_pinky3": coords_raw[8].rotation_difference(coords_raw[9]),
            "pinky3_pinky_tip": coords_raw[9].rotation_difference(coords_raw[18]),
        }


bones = [
    ("root", "thumb1"),
    ("root", "point1"),
    ("root", "middle1"),
    ("root", "ring1"),
    ("root", "pinky1"),
    ("thumb1", "thumb2"),
    ("thumb2", "thumb3"),
    ("thumb3", "thumb_tip"),
    ("point1", "point2"),
    ("point2", "point3"),
    ("point3", "point_tip"),
    ("middle1", "middle2"),
    ("middle2", "middle3"),
    ("middle3", "middle_tip"),
    ("ring1", "ring2"),
    ("ring2", "ring3"),
    ("ring3", "ring_tip"),
    ("pinky1", "pinky2"),
    ("pinky2", "pinky3"),
    ("pinky3", "pinky_tip"),
]


initial_coords_left = '''-0.4783496546203587,0.03191714428730719,0.030931526400675972
-0.03786342141938446,0.005915358945289405,0.13436147158616243
0.1255310961500387,0.025962135992213912,0.14544681214135052
0.23631065758495548,0.019470023126354465,0.14487622834520336
-0.005047447661171345,0.02452232753259131,0.014143822329090873
0.1508659142620152,0.03382897012449566,-0.013828720260797647
0.265389115431465,0.027568448960906544,-0.033551290274477424
-0.13441479432093825,-0.017784499814935864,-0.18511518361574883
-0.049342753632412834,-0.017475376230939584,-0.24760905845155753
0.029991752401276762,-0.020931155703177683,-0.29926859546310863
-0.06967188247630755,0.012130038522980974,-0.102434438764765
0.07189949253375615,0.02246507481457729,-0.12792713127502736
0.18950205691790983,0.014024515690500667,-0.16609620213687365
-0.3579011206071486,-0.04569452842207133,0.15999576284108968
-0.2597349179007616,-0.041238095664356295,0.2784935290707611
-0.14864622114082912,-0.06840295147164337,0.35111412056743946
0.36192861897365536,0.014762026377023054,0.1383111690011094
0.394964106550951,0.03073324480070758,-0.06020430519157401
0.11843697978416388,-0.027646602997179616,-0.3489420729135565
0.31245949008995283,0.012134281290065078,-0.20334635476466528
-0.018578491307083174,-0.08179516657237615,0.47052484822976226'''

initial_coords_right = '''0.4783496546203587,0.03191714428730719,0.030931526400675972
0.03786342141938446,0.005915358945289405,0.13436147158616243
-0.1255310961500387,0.025962135992213912,0.14544681214135052
-0.23631065758495548,0.019470023126354465,0.14487622834520336
0.005047447661171345,0.02452232753259131,0.014143822329090873
-0.1508659142620152,0.03382897012449566,-0.013828720260797647
-0.265389115431465,0.027568448960906544,-0.033551290274477424
0.13441479432093825,-0.017784499814935864,-0.18511518361574883
0.049342753632412834,-0.017475376230939584,-0.24760905845155753
-0.029991752401276762,-0.020931155703177683,-0.29926859546310863
0.06967188247630755,0.012130038522980974,-0.102434438764765
-0.07189949253375615,0.02246507481457729,-0.12792713127502736
-0.18950205691790983,0.014024515690500667,-0.16609620213687365
0.3579011206071486,-0.04569452842207133,0.15999576284108968
0.2597349179007616,-0.041238095664356295,0.2784935290707611
0.14864622114082912,-0.06840295147164337,0.35111412056743946
-0.36192861897365536,0.014762026377023054,0.1383111690011094
-0.394964106550951,0.03073324480070758,-0.06020430519157401
-0.11843697978416388,-0.027646602997179616,-0.3489420729135565
-0.31245949008995283,0.012134281290065078,-0.20334635476466528
0.018578491307083174,-0.08179516657237615,0.47052484822976226'''


def init():
    # get all objects in a scene
    obs = bpy.data.objects

    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    if not bpy.context.scene.objects.get("left_root"):
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()

        for ob in obs:
            if ob.type == "CAMERA":
                ob.select_set(False)

        coords_raw_left = np.array(
            [[float(coord) for coord in s.split(",")] for s in initial_coords_left.split("\n")]
        )

        coords_raw_right = np.array(
            [[float(coord) for coord in s.split(",")] for s in initial_coords_right.split("\n")]
        )

        coords_raw_left -= coords_raw_left[0]
        coords_left = map_coords(coords_raw_left, "coords")
        setup_joints(coords_left.keys(), prefix="left_", mode="root")
        create_bones(bones, coords_left, prefix="left_")

        coords_raw_right -= coords_raw_right[0]
        coords_right = map_coords(coords_raw_right, "coords")
        setup_joints(coords_right.keys(), prefix="right_", mode="root")
        create_bones(bones, coords_right, prefix="right_")


def process_bones(frame_coords: np.ndarray, root_position: np.ndarray = None, hand: str = 'left'):
    """
    Assign quaternions to the bones, writes keyframes if cptr_recording is true to frame_idx position
    :param frame_coords: quaternion array, (21, 4)
    :type frame_coords: np.ndarray
    :param root_position: root coordinate, (1, 3)
    :type root_position: np.ndarray
    :param hand: 'left' or 'right' hand to be processed
    :type hand: str
    """
    assert hand in ['right', 'left'], "Hand should be 'right' or 'left'"

    coords_raw = [Quaternion(quat) for quat in frame_coords]
    coords = map_coords(coords_raw, "quats")

    obj = bpy.data.objects[f"{hand}_root"]
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = coords["root"]
    if root_position is not None:
        obj.location = root_position

    obj.keyframe_insert(data_path="rotation_quaternion", index=-1)
    obj.keyframe_insert(data_path="location", index=-1)

    for joint_name, bone_quat in list(coords.items())[1:]:
        obj = bpy.data.objects[f"{hand}_Skeleton"].pose.bones[hand + "_" + joint_name]
        obj.rotation_mode = "QUATERNION"
        obj.rotation_quaternion = bone_quat.normalized()

        obj.keyframe_insert(data_path="rotation_quaternion", index=-1)


init()
with open('./file_with_quats.txt', 'r') as f:
    quats = np.array([[[float(qqq) for qqq in qq.split(',')] for qq in q.split('\n')[:-1]] for q in f.read().split('frame\n')[1:]])
    
frame_idx = 0
for quat in quats:
    bpy.context.scene.frame_set(frame_idx)
    bpy.data.scenes["Scene"].frame_end = frame_idx + 1
    process_bones(quat, hand='left')
    frame_idx += 1
