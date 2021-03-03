# Create pack of properties that are common to character rigging
# Properties are creates at active pose bone

import bpy

active = bpy.context.active_pose_bone

keys = [
    'arm_L_FK_parent-hinge',
    'arm_L_Y_Rot_transmission',
    'arm_L_auto_clavicle',
    'arm_L_fk_ik',
    'arm_L_fk_total_scale',
    'arm_L_ik_child_of_chest',
    'arm_L_ik_elbow_follow',
    'arm_L_ik_stretch',
    'arm_R_FK_parent-hinge',
    'arm_R_Y_Rot_transmission',
    'arm_R_auto_clavicle',
    'arm_R_fk_ik',
    'arm_R_fk_total_scale',
    'arm_R_ik_child_of_chest',
    'arm_R_ik_elbow_follow',
    'arm_R_ik_stretch',
    'body_IK_chest',
    'eye_response_L',
    'eye_response_R',
    'head_parent-hinge',
    'head_ik-neck',
    #'head_pupils_tracking',
    'hide_unused',
    'leg_L_fk_ik',
    'leg_L_fk_parent-hinge',
    'leg_L_fk_total_scale',
    'leg_L_ik_child_of_pelvis',
    'leg_L_ik_elbow_follow',
    'leg_L_ik_shin_length',
    'leg_L_ik_stretch',
    'leg_L_ik_thigh_length',
    'leg_R_fk_ik',
    'leg_R_fk_parent-hinge',
    'leg_R_fk_total_scale',
    'leg_R_ik_child_of_pelvis',
    'leg_R_ik_elbow_follow',
    'leg_R_ik_shin_length',
    'leg_R_ik_stretch',
    'leg_R_ik_thigh_length',
    #'pupils_child_of_None-Root-Head',
    'subsurf_level',
    #'tail_fk_ik',
    #'tail_fk_total_scale',
    #'tail_ik_child_of_pelvis',
    #'tail_ik_stretch',
    #'tail_show_additional_tweaks',
    #'tongue_fk_ik',
    #'tongue_fk_total_scale',
    #'tongue_ik_child_of_jaw',
    #'tongue_ik_elbow_follow',
    #'tongue_ik_stretch',
    #'tongue_show_additional_tweaks',
    'tongue_child_of_jaw']

for i in range(len(keys)):
    
    prop = keys[i]
    active[prop] = 0.0
    
    if "_RNA_UI" not in active.keys():
        active["_RNA_UI"] = {}
    # Don't forger to change limits later, e.g. IK part length can vary from 0.5 to 2
    active["_RNA_UI"].update({prop: {"min": 0.0, "max": 1.0, "soft_min": 0.0, "soft_max": 1.0}})
    # All the properties must be library overridable (current pipeleine needs that)
    active.property_overridable_library_set('["' + prop + '"]', True)
    