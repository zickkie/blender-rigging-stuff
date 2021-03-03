##############
# Pole Angle #
# by Jerryno #
##############

import bpy
import numpy

arm_obj = bpy.data.objects['rig_penguin']

def signed_angle(vector_u, vector_v, normal):
    # Normal specifies orientation
    angle = vector_u.angle(vector_v)
    if vector_u.cross(vector_v).angle(normal) < 1:
        angle = -angle
    return angle

def get_pole_angle(base_bone, ik_bone, pole_location):
    pole_normal = (ik_bone.tail - base_bone.head).cross(pole_location - base_bone.head)
    projected_pole_axis = pole_normal.cross(base_bone.tail - base_bone.head)
    return signed_angle(base_bone.x_axis, projected_pole_axis, base_bone.tail - base_bone.head)

base_bone = arm_obj.pose.bones['IK.upper_arm.R']
ik_bone   = arm_obj.pose.bones['IK.lower_arm.R']
pole_bone = arm_obj.pose.bones['penguin.IK.arm.pole.R']

pole_angle_in_radians = get_pole_angle(
    base_bone,
    ik_bone,
    pole_bone.matrix.translation)

print("Pole angle: {}".format(numpy.rad2deg(pole_angle_in_radians)))