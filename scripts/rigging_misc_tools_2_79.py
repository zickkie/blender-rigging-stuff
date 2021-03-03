bl_info = {
    "name": "Miscellaneous Tools",
    "author": "Arthur Shapiro",
    "version": (1, 0),
    "blender": (2, 79),
    "location": "View3D > Tools",
    "description": "Miscellaneous Tools for Rigging",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"}
    
import bpy
from math import radians
from bpy.props import PointerProperty
from mathutils import Vector, Matrix
from bpy_extras.io_utils import unpack_list


####################################
########### ADDITIONAL #############
########### FUNCTIONS  #############
####################################


########### Create Bone Custom Property ###########

def create_prop(bone, property, start):
    l = len(bpy.context.selected_objects) - 1
    ob = bpy.context.active_object
    pbone = bpy.data.objects[ob.name].pose.bones[bone]
    pbone[property] = start
    if "_RNA_UI" not in pbone.keys():
                pbone["_RNA_UI"] = {}
    pbone["_RNA_UI"].update({property: {"min":start, "max":l, "soft_min":start, "soft_max":l}})
    bpy.ops.pose.group_add()
    bpy.data.objects[ob.name].pose.bone_groups[-1].name = 'Parameter'
    bpy.data.objects[ob.name].pose.bone_groups[-1].color_set = 'THEME01'
    bpy.data.objects[ob.name].pose.bone_groups.active_index = (len(bpy.data.objects[ob.name].pose.bone_groups)-1)
    bpy.ops.pose.select_all(action='DESELECT')
    ob.data.bones[bone].select = True
    bpy.ops.pose.group_assign(type=len(bpy.data.objects[ob.name].pose.bone_groups))


########### Add Object Hide Viewport Driver ###########

def add_viewport(bone, property, is_cyclic, zero):
    names = []
    for ob in bpy.context.selected_objects:
        if ob.name != bpy.context.active_object.name:
            names.append(ob.name)
    names = sorted(names)
    for ob in bpy.context.selected_objects:
        if ob.name != bpy.context.active_object.name:
            k = int(names.index(ob.name))
            ob.driver_remove('hide')
            drv = ob.driver_add('hide')
            if is_cyclic == True:
                drv.modifiers.remove(drv.modifiers[0])
                for i in range(3):
                    drv.keyframe_points.add()
                co = [(float(k), 0.0), ((float(k)+1.0), 1.0), ((float(k)+float(len(names))), 0.0)]
                handles = [[(float(k), 0.0), (float(k), 0.0)], [((float(k)+1.0), 1.0), ((float(k)+1.0), 1.0)], [((float(k)+float(len(names))), 0.0), ((float(k)+float(len(names))), 0.0)]]
                for i in range(len(co)):
                    drv.keyframe_points[i].co = co[i]
                    drv.keyframe_points[i].interpolation ='CONSTANT'
                    drv.keyframe_points[i].handle_left_type = 'FREE'
                    drv.keyframe_points[i].handle_right_type = 'FREE'
                    drv.keyframe_points[i].handle_left = handles[i][0]
                    drv.keyframe_points[i].handle_right = handles[i][1]
                    drv.modifiers.new(type = "CYCLES")
            var = drv.driver.variables.new()
            var.name='stg'
            var.type='SINGLE_PROP'
            target = var.targets[0]
            target.id = bpy.data.objects[bpy.context.active_object.name] 
            target.data_path = 'pose.bones["' + bone + '"]["' + property + '"]'
            if is_cyclic == False:
                drv.driver.expression = '0 if stg == ' + str(k+1) + ' else 1'
            else:
                if zero == True:
                    if k == 0:
                        drv.driver.expression = 'frame * stg / ' + str(len(names)) + ' if stg > 0 else 1'
                    else:
                        drv.driver.expression = 'frame * stg / ' + str(len(names))
                else:
                    drv.driver.expression = 'frame * stg / ' + str(len(names))
                    

########### Add Object Hide Render Driver ###########

def add_render(bone, property, is_cyclic, zero):
    names = []
    for ob in bpy.context.selected_objects:
        if ob.name != bpy.context.active_object.name:
            names.append(ob.name)
    names = sorted(names)
    for ob in bpy.context.selected_objects:
        if ob.name != bpy.context.active_object.name:
            k = int(names.index(ob.name))
            ob.driver_remove('hide_render')
            drv = ob.driver_add('hide_render')
            if is_cyclic == True:
                drv.modifiers.remove(drv.modifiers[0])
                for i in range(3):
                    drv.keyframe_points.add()
                co = [(float(k), 0.0), ((float(k)+1.0), 1.0), ((float(k)+float(len(names))), 0.0)]
                handles = [[(float(k), 0.0), (float(k), 0.0)], [((float(k)+1.0), 1.0), ((float(k)+1.0), 1.0)], [((float(k)+float(len(names))), 0.0), ((float(k)+float(len(names))), 0.0)]]
                for i in range(len(co)):
                    drv.keyframe_points[i].co = co[i]
                    drv.keyframe_points[i].interpolation ='CONSTANT'
                    drv.keyframe_points[i].handle_left_type = 'FREE'
                    drv.keyframe_points[i].handle_right_type = 'FREE'
                    drv.keyframe_points[i].handle_left = handles[i][0]
                    drv.keyframe_points[i].handle_right = handles[i][1]
                    drv.modifiers.new(type = "CYCLES")
            var = drv.driver.variables.new()
            var.name='stg'
            var.type='SINGLE_PROP'
            target = var.targets[0]
            target.id = bpy.data.objects[bpy.context.active_object.name] 
            target.data_path = 'pose.bones["' + bone + '"]["' + property + '"]'
            if is_cyclic == False:
                drv.driver.expression = '0 if stg == ' + str(k+1) + ' else 1'
            else:
                if zero == True:
                    if k == 0:
                        drv.driver.expression = 'frame * stg / ' + str(len(names)) + ' if stg > 0 else 1'
                    else:
                        drv.driver.expression = 'frame * stg / ' + str(len(names))
                else:
                    drv.driver.expression = 'frame * stg / ' + str(len(names))
                    

########### Clear Object Hide Viewport Driver and set to Default ###########

def remove_viewport():
    for ob in bpy.context.selected_objects:
        if ob.type != "ARMATURE":
            ob.driver_remove('hide')
            bpy.data.objects[ob.name].hide = 0
            
            
########### Clear Object Hide Render Driver and set to Default ###########

def remove_render():
    for ob in bpy.context.selected_objects:
        if ob.type != "ARMATURE":
            ob.driver_remove('hide_render')
            bpy.data.objects[ob.name].hide_render = 0
            

########### Add Object Hide Viewport Driver with Existing Armature & Bone ###########
            
def add_viewport_ex(armature, bone, property, start):
    k = 0
    l = []
    for ob in bpy.context.selected_objects:
        l.append(ob.name)
    l.sort()
    while k < len(bpy.context.selected_objects):
        for ob in bpy.context.selected_objects:
            if k < len(bpy.context.selected_objects):
                if ob.name == l[k] and ob.type != "ARMATURE":
                    ob.driver_remove('hide')
                    drv = ob.driver_add('hide')
                    var = drv.driver.variables.new()
                    var.name='stg'
                    var.type='SINGLE_PROP'
                    target = var.targets[0]
                    target.id = armature 
                    target.data_path = 'pose.bones["' + bone + '"]["' + property + '"]'
                    drv.driver.expression = '0 if stg == ' + str(start+k) + ' else 1'
                    k+=1


########### Add Object Hide Render Driver with Existing Armature & Bone ###########

def add_render_ex(armature, bone, property, start):
    k = 0
    l = []
    for ob in bpy.context.selected_objects:
        l.append(ob.name)
    l.sort()
    while k < len(bpy.context.selected_objects):
        for ob in bpy.context.selected_objects:
            if k < len(bpy.context.selected_objects):
                if ob.name == l[k] and ob.type != "ARMATURE":
                    ob.driver_remove('hide_render')
                    drv = ob.driver_add('hide_render')
                    var = drv.driver.variables.new()
                    var.name='stg'
                    var.type='SINGLE_PROP'
                    target = var.targets[0]
                    target.id = armature 
                    target.data_path = 'pose.bones["' + bone + '"]["' + property + '"]'
                    drv.driver.expression = '0 if stg == ' + str(start+k) + ' else 1'
                    k+=1


########### Batch Renaming of the Objects based on their comparative location ###########

def batch_X (rev, path, base, sep, start):
    pos = []
    names = []
        
    for ob in bpy.context.selected_objects:
        ob.name = "It's_a_cold_world_baby_girl,_lovin'_me_is_not_enough"
    for ob in bpy.context.selected_objects:
        pos.append(ob.location[path])
    pos.sort(reverse=rev)
    for ob in bpy.context.selected_objects:
        if (base + "///" + str(pos.index(ob.location[path])+start)) not in names:
            ob.name = base + "///" + str(pos.index(ob.location[path])+start)
        else:
            ob.name = base + "///" + str(pos.index(ob.location[path])+start) + ".001"
        names.append(ob.name)
    for ob in bpy.context.selected_objects:
        if "." in ob.name.split("///")[1]:
            ob.name = base + "///" + str(int(ob.name.split('///')[1].split('.')[0]) + int(ob.name.split('///')[1].split('.')[1]))
    for ob in bpy.context.selected_objects:
        for obj in bpy.context.scene.objects:
            if obj.name == base + sep + "0"*(3 - len(ob.name.split("///")[1]))+ ob.name.split("///")[1]:
                obj.name = base + sep + "0"*(3 - len(ob.name.split("///")[1]))+ ob.name.split("///")[1] + ".001"
        ob.name = base + sep + "0"*(3 - len(ob.name.split("///")[1]))+ ob.name.split("///")[1]


########### Batch Renaming of the Bones based on their comparative Pose location ###########

def batch_X_bone (rev, path, base, sep, start):
    obj = bpy.context.active_object
    pos = []
    names = []
        
    for bone in bpy.context.selected_pose_bones:
        obj.data.bones[bone.name].name = "Find_out_when_you_fuckin'_broke,_love_won't_get_you_on_the_bus"
    for bone in bpy.context.selected_pose_bones:
        pos.append(bone.matrix[path][3])
    pos.sort(reverse=rev)
    for bone in bpy.context.selected_pose_bones:
        if (base + "///" + str(pos.index(bone.matrix[path][3])+start)) not in names:
            obj.data.bones[bone.name].name = base + "///" + str(pos.index(bone.matrix[path][3])+start)
        else:
            obj.data.bones[bone.name].name = base + "///" + str(pos.index(bone.matrix[path][3])+start) + ".001"
        names.append(bone.name)
    for bone in bpy.context.selected_pose_bones:
        if "." in bone.name.split("///")[1]:
            obj.data.bones[bone.name].name = base + "///" + str(int(bone.name.split('///')[1].split('.')[0]) + int(bone.name.split('///')[1].split('.')[1]))
    for bone in bpy.context.selected_pose_bones:
        for bone_all in obj.data.bones:
            if bone_all.name == base + sep + "0"*(3 - len(bone.name.split("///")[1]))+ bone.name.split("///")[1]:
                bone_all.name = base + sep + "0"*(3 - len(bone.name.split("///")[1]))+ bone.name.split("///")[1] + ".001"
        bone.name = base + sep + "0"*(3 - len(bone.name.split("///")[1]))+ bone.name.split("///")[1]
    

####################################
############# CLASSES ##############
####################################

  
############################################
##### Make Spline IK with controls     #####
##### based on provided Empties'       #####
##### location                         #####
############################################ 

class OBJECT_OT_add_curve_hooks(bpy.types.Operator):
    """Add Curve Hooks"""
    bl_label = "Add Curve Hooks"
    bl_idname = "curve.add_hooks"
    bl_option = {'REGISTER', 'UNDO'}
    
    case = bpy.props.IntProperty()
    
    curve_hooks_count = bpy.props.IntProperty(
        name = "Spline Curves Counter",
        default = 0,
        min = 0,
        description = "Integer Property being used to divide spline chains"
        )
        
    curve_hooks_quantity = bpy.props.IntProperty(
        name = "Number of Hooks",
        default = 2,
        min = 2,
        description = "Number of Hooks determining the Bezier Points Location"
        )
    
    curve_hooks_subdivide = bpy.props.IntProperty(
        name = "Spline Armature Subdivision",
        default = 2,
        min = 2,
        description = "Number of Spline Armature Bones"
        )
    
        
    def execute(self, context):
        
        if self.case == 1:
            bpy.ops.object.mode_set(mode='OBJECT')       
            count = self.curve_hooks_count
            ns = bpy.context.scene.curve_hooks_ns
            ns = 0
            lc = bpy.context.scene.cursor_location
            for i in range(self.curve_hooks_quantity):
                bpy.ops.object.empty_add(type='PLAIN_AXES')
                bpy.context.object.name = str(count) + "_curve_hook_" + str(ns)
                bpy.context.object.location = bpy.context.scene.cursor_location
                ns += 1
                lc[0] += 1
            bpy.context.scene.cursor_location[0] -= bpy.data.scenes["Scene"].start_value
            bpy.context.scene.curve_hooks_ns = ns
            bpy.data.scenes["Scene"].curve_hooks_stage = 1
        
        # locate empties to set curve shape
        
        if self.case == 2:
            obj2 = bpy.context.active_object
            bone2 = bpy.context.active_pose_bone
            bpy.ops.object.mode_set(mode='OBJECT')
            #
            ns = bpy.context.scene.curve_hooks_ns
            count = self.curve_hooks_count 
            coords_list = []
            for ob in bpy.data.objects:
                if ob.name.startswith(str(count) + "_curve_hook_"):
                    coords_list.append(ob.location)
            #
            crv = bpy.data.curves.new('spline', 'CURVE')
            crv.dimensions = '3D'
            spline = crv.splines.new(type='BEZIER')
            spline.bezier_points.add(len(coords_list)-1) 
            spline.bezier_points.foreach_set("co", unpack_list(coords_list))
            #
            ob = bpy.data.objects.new(str(count) + "_SplineCurve", crv)
            bpy.context.scene.objects.link(ob)
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = ob
            bpy.data.objects[ob.name].select = True
            ob = bpy.context.active_object
            name = ob.data.name
            lenP = len(bpy.data.curves[name].splines[0].bezier_points)
            #
            k = 0
            for sp in ob.data.splines.active.bezier_points:
                sp.co = bpy.data.objects[str(count) + "_curve_hook_" + str(k)].location
                k += 1
            for sp in ob.data.splines.active.bezier_points:
                sp.handle_left_type = "AUTO"
                sp.handle_right_type = "AUTO"
            bpy.ops.object.origin_set(type = "ORIGIN_GEOMETRY")
            #
            k = 0
            for i in range(lenP):
                bpy.data.objects[ob.name].modifiers.new(name = (str(count) + "_curve_hook_" + str(k)), type = "HOOK")
                bpy.data.objects[ob.name].modifiers[str(count) + "_curve_hook_" + str(k)].object = bpy.data.objects[str(count) + "_curve_hook_" + str(k)]
                k += 1
            #
            k = 0
            bpy.ops.object.mode_set(mode='EDIT')
            for i in range(lenP):
                bpy.ops.curve.select_all(action='DESELECT')
                bpy.data.curves[name].splines[0].bezier_points[k].select_control_point = True
                bpy.data.curves[name].splines[0].bezier_points[k].select_left_handle = True
                bpy.data.curves[name].splines[0].bezier_points[k].select_right_handle = True
                bpy.ops.object.hook_assign(modifier = (str(count) + "_curve_hook_" + str(k)))
                bpy.ops.curve.select_all(action='DESELECT')
                k += 1 
            #
            k = 0
            for i in range(lenP):
                bpy.ops.curve.select_all(action='SELECT')
                bpy.ops.object.hook_reset(modifier = (str(count) + "_curve_hook_" + str(k)))
                k += 1
            bpy.ops.curve.handle_type_set(type='FREE_ALIGN')
            bpy.ops.object.mode_set(mode='OBJECT')
            #
            obj = bpy.ops.object.armature_add(location = bpy.data.objects[str(count) + "_curve_hook_0"].location)
            bpy.context.object.name = str(count) + "_SplineArmature"
            obj = bpy.context.active_object
            k = obj.location
            l = bpy.data.objects[str(count) + "_curve_hook_" + str(ns-1)].location
            bpy.ops.object.mode_set(mode='EDIT')
            for bone in obj.data.edit_bones:
                bone.tail = l - k
            #
            bpy.ops.armature.select_all(action='SELECT')
            bpy.ops.armature.subdivide(number_cuts = (self.curve_hooks_subdivide - 1))
            bpy.ops.armature.calculate_roll(type="GLOBAL_NEG_Y")
            #
            bpy.ops.object.mode_set(mode='POSE')
            bpy.ops.pose.select_all(action='SELECT')
            bpy.ops.pose.rotation_mode_set(type="ZYX")
            #
            obj.pose.bones["Bone.001"].constraints.new("SPLINE_IK")
            obj.pose.bones["Bone.001"].constraints["Spline IK"].name = str(count) + "_Spline_IK"
            obj.pose.bones["Bone.001"].constraints[str(count) + "_Spline_IK"].target = bpy.data.objects[str(count) + "_SplineCurve"]
            obj.pose.bones["Bone.001"].constraints[str(count) + "_Spline_IK"].chain_count = len(obj.pose.bones)
            #
            bpy.ops.pose.armature_apply()
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY")
            for ob in bpy.data.objects:
                if "SplineCurve" in ob.name:
                    bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY")
            bpy.ops.object.select_all(action='DESELECT')         
            ###
            if bpy.context.scene.spline_menu_enum == "create":
                bo = []
                l = []
                for hook in bpy.data.objects:
                    if hook.name.startswith(str(bpy.context.scene.curve_hooks_count)+"_curve_hook"):
                        l.append(hook.name)
                l.sort()
                obj = bpy.ops.object.armature_add(location = bpy.data.objects[str(count) + "_curve_hook_0"].location)
                bpy.context.object.name = "_RIG"
                obj = bpy.context.active_object
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.armature.select_all(action='SELECT')
                bpy.ops.armature.delete()
                for i in range(len(l)):
                    b = obj.data.edit_bones.new(name = "More_money_in_the_bank")
                    b.name = b.name = str(bpy.context.scene.curve_hooks_count) + "_curve_hook_"+str(i)
                    b.head = bpy.data.objects[str(bpy.context.scene.curve_hooks_count) + "_curve_hook_" + str(i)].location - obj.location
                    b.tail = b.head + Vector((0.0, 0.0, 1.0))
                    bo.append(b.name)
                bo.sort()
                bpy.ops.armature.select_all(action='SELECT')
                bpy.ops.armature.calculate_roll(type="GLOBAL_NEG_Y")
                bpy.ops.object.mode_set(mode='POSE')
                bpy.ops.pose.select_all(action='SELECT')
                bpy.ops.pose.rotation_mode_set(type="ZYX")
            ###
            elif bpy.context.scene.spline_menu_enum == "parent":
                bpy.ops.object.select_all(action='DESELECT')
                l = []
                for hook in bpy.data.objects:
                    if hook.name.startswith(str(bpy.context.scene.curve_hooks_count)+"_curve_hook"):
                        l.append(hook.name)
                l.sort()
                bo = []
                bpy.context.scene.objects.active = obj2
                obj = bpy.context.active_object
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.armature.select_all(action='DESELECT')
                for i in range(len(l)):
                    b = obj.data.edit_bones.new(name = "More_money_in_the_bank")
                    b.name = str(bpy.context.scene.curve_hooks_count) + "_curve_hook_"+str(i)
                    b.head = bpy.data.objects[str(bpy.context.scene.curve_hooks_count) + "_curve_hook_" + str(i)].location - obj2.location
                    b.tail = b.head + Vector((0.0, 0.0, 1.0))
                    b.parent = bpy.data.armatures[obj2.data.name].edit_bones[bone2.name]
                    bo.append(b.name)
                    bpy.ops.armature.select_all(action='DESELECT')
                for ed_b in bpy.data.armatures[obj2.data.name].edit_bones:
                    if ed_b.name in bo:
                        ed_b.select = True
                        ed_b.select_tail = True
                        ed_b.select_head = True
                bpy.ops.armature.calculate_roll(type="GLOBAL_NEG_Y")
                bpy.ops.object.mode_set(mode='POSE')
                bpy.ops.pose.rotation_mode_set(type="ZYX")
                
            ###
            i = 0
            bpy.ops.object.mode_set(mode='OBJECT')
            crv = bpy.context.active_object
            for obj in bpy.data.objects:
                if str(bpy.context.scene.curve_hooks_count) + "_SplineCurve" in obj.name:
                    for mod in bpy.data.objects[obj.name].modifiers:
                        if "curve_hook" in mod.name:
                            mod.object = crv
                            mod.subtarget = bo[i]
                            i += 1
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = bpy.data.objects[str(bpy.context.scene.curve_hooks_count) + "_SplineCurve"]
            bpy.ops.object.mode_set(mode='EDIT')
            k = 0
            for i in range(len(bpy.data.curves[bpy.context.active_object.data.name].splines[0].bezier_points)):
                bpy.ops.curve.select_all(action='SELECT')
                bpy.ops.object.hook_reset(modifier = (str(bpy.context.scene.curve_hooks_count) + "_curve_hook_" + str(k)))
                k += 1    
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            for obj in bpy.data.objects:
                if obj.name.startswith(str(bpy.context.scene.curve_hooks_count) + "_curve_hook_"):
                    obj.select = True
            bpy.ops.object.delete()
            bpy.context.scene.curve_hooks_ns += 1
            bpy.context.scene.curve_hooks_count+= 1
            bpy.context.scene.curve_hooks_stage = 0
            
                
        
        if self.case == 3:
            bpy.context.scene.curve_hooks_stage = 0
                  
                  
        return{'FINISHED'}
    
############################################
##### Convert Selected Curves & make   #####
##### a Limited Dissolve Operation to  #####
##### the faces of the resulting Mesh  #####
############################################  
    
class OBJECT_OT_convert_and_limited_dissolve(bpy.types.Operator):
    """Convert selected Curves to a limited dissolves Mesh"""
    bl_label = "Convert & Limited Dissolve"
    bl_idname = "curve.convert_and_limited_dissolve"
    bl_option = {'REGISTER', 'UNDO'}
    
    max_angle = bpy.props.FloatProperty(
        name = "Max Angle",
        default = 1,
        description = "Angle Limit"
        )
    name = bpy.props.StringProperty(
        name = "Name",
        default = "Curve",
        description = "Name of converted Curves"
        )
        
    
    def execute(self, context):
        
        for ob in bpy.context.selected_objects:
            bpy.ops.object.convert(target='MESH')
            bpy.ops.object.join()
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.dissolve_limited(angle_limit=radians(self.max_angle))
            bpy.ops.object.editmode_toggle()
        bpy.context.object.name = self.name
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.ops.object.select_all(action='DESELECT')
        
        return {'FINISHED'}
    
    
############################################
##### Convert Selected Curves &        #####
##### beautify faces of                #####
##### the resulting Mesh               #####
############################################
    
class OBJECT_OT_convert_and_beautify(bpy.types.Operator):
    """Convert selected Curves to a Mesh with beautified faces"""
    bl_label = "Convert & Beautify"
    bl_idname = "curve.convert_and_beautify"
    bl_option = {'REGISTER', 'UNDO'}
    
    name = bpy.props.StringProperty(
        name = "Name",
        default = "Curve",
        description = "Name of converted Curves"
        )
        
    def execute(self, context):
        
        for ob in bpy.context.selected_objects:
            bpy.ops.object.convert(target='MESH')
            bpy.ops.object.join()
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.beautify_fill()
            bpy.ops.object.editmode_toggle()
        bpy.context.object.name = self.name
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.ops.object.select_all(action='DESELECT')
        
        return {'FINISHED'}    


############################################
##### Select objects whose name        #####
##### contains the specified           #####
##### characters, add prefix & suffix  #####
############################################      
    
class OBJECT_OT_select_namesakes(bpy.types.Operator):
    """Select objects-namesakes"""
    bl_label = "Select namesakes"
    bl_idname = "object.select_namesakes"
    bl_option = {'REGISTER', 'UNDO'}
    
    case = bpy.props.IntProperty()
    
    name_sel = bpy.props.StringProperty(
        name = "Find Name",
        default = "Object",
        description = "Select objects whose name contains the specified characters"
        )
    
    name_source = bpy.props.StringProperty(
        name = "Source Name",
        default = "name_1",
        description = "Source part of the Object Name to be replaced"
        )
    
    name_target = bpy.props.StringProperty(
        name = "Target Name",
        default = "name_2",
        description = "Target part of the Object Name used to Replace"
        )
    
    prefix = bpy.props.StringProperty(
        name = "Prefix",
        default = "_",
        description = "Prefix to add before Object's base name"
        )
    
    suffix = bpy.props.StringProperty(
        name = "Suffix",
        default = "_",
        description = "Suffix to add after Object's base name"
        )
        
    
    def execute(self, context):
        
        obj = bpy.context.active_object
        
        if self.case == 1:
            if bpy.context.scene.namesakes_type_enum == 'objects':
                for ob in bpy.context.visible_objects:
                    if self.name_sel in ob.name:
                        bpy.data.objects[ob.name].select = True
            else:
                for bone in bpy.context.visible_pose_bones:
                    if self.name_sel in bone.name:
                        obj.data.bones[bone.name].select = True
        
        if self.case == 2:
            if bpy.context.scene.namesakes_type_enum == 'objects':
                if bpy.context.scene.naming_selection_enum == "selected":
                    for ob in bpy.context.selected_objects:
                        ob.name = ob.name.replace(self.name_source, self.name_target)
                elif bpy.context.scene.naming_selection_enum == "visible":
                    for ob in bpy.context.visible_objects:
                        ob.name = ob.name.replace(self.name_source, self.name_target)
                else:
                    for ob in bpy.context.scene.objects:
                        ob.name = ob.name.replace(self.name_source, self.name_target)
            else:
                if bpy.context.scene.naming_selection_enum == "selected":
                    for bone in bpy.context.selected_pose_bones:
                        bone.name = bone.name.replace(self.name_source, self.name_target)
                elif bpy.context.scene.naming_selection_enum == "visible":
                    for bone in bpy.context.visible_pose_bones:
                        bone.name = bone.name.replace(self.name_source, self.name_target)
                else:
                    for bone in obj.data.bones:
                        bone.name = bone.name.replace(self.name_source, self.name_target)
        
        if self.case == 3:
            if bpy.context.scene.namesakes_type_enum == 'objects':
                if bpy.context.scene.naming_selection_enum == "selected":
                    for ob in bpy.context.selected_objects:
                        ob.name = self.prefix + ob.name
                elif bpy.context.scene.naming_selection_enum == "visible":
                    for ob in bpy.context.visible_objects:
                        ob.name = self.prefix + ob.name
                else:
                    for ob in bpy.context.scene.objects:
                        ob.name = self.prefix + ob.name
            else:
                if bpy.context.scene.naming_selection_enum == "selected":
                    for bone in bpy.context.selected_pose_bones:
                        bpy.data.armatures[obj.data.name].bones[bone.name].name = self.prefix + bpy.data.armatures[obj.data.name].bones[bone.name].name
                elif bpy.context.scene.naming_selection_enum == "visible":
                    for bone in bpy.context.visible_pose_bones:
                        bpy.data.armatures[obj.data.name].bones[bone.name].name = self.prefix + bpy.data.armatures[obj.data.name].bones[bone.name].name
                else:
                    for bone in obj.data.bones:
                        bpy.data.armatures[obj.data.name].bones[bone.name].name = self.prefix + bpy.data.armatures[obj.data.name].bones[bone.name].name
        
        if self.case == 4:
            if bpy.context.scene.namesakes_type_enum == 'objects':
                if bpy.context.scene.naming_selection_enum == "selected":
                    for ob in bpy.context.selected_objects:
                        ob.name = ob.name + self.suffix
                elif bpy.context.scene.naming_selection_enum == "visible":
                    for ob in bpy.context.visible_objects:
                        ob.name = ob.name + self.suffix
                else:
                    for ob in bpy.context.scene.objects:
                        ob.name = ob.name + self.suffix
            else:
                if bpy.context.scene.naming_selection_enum == "selected":
                    for bone in bpy.context.selected_pose_bones:
                        bpy.data.armatures[obj.data.name].bones[bone.name].name = bpy.data.armatures[obj.data.name].bones[bone.name].name + self.suffix
                elif bpy.context.scene.naming_selection_enum == "visible":
                    for bone in bpy.context.visible_pose_bones:
                        bpy.data.armatures[obj.data.name].bones[bone.name].name = bpy.data.armatures[obj.data.name].bones[bone.name].name + self.suffix
                else:
                    for bone in obj.data.bones:
                        bpy.data.armatures[obj.data.name].bones[bone.name].name = bpy.data.armatures[obj.data.name].bones[bone.name].name + self.suffix
        
        return {'FINISHED'}
  
  
############################################
##### Batching names of the selected   #####
##### objects / bones                  #####
##### based on their location          #####
############################################    
    
class OBJECT_OT_batch_names(bpy.types.Operator):
    """Batching names of the selected objects based on their location"""
    bl_label = "Batch names"
    bl_idname = "object.batch_names"
    bl_option = {'REGISTER', 'UNDO'}
    
    base_name = bpy.props.StringProperty(
        name = "Base Name",
        default = "Object",
        description = "Base-name for the selected objects"
        )
        
    sep = bpy.props.StringProperty(
        name = "Separator",
        default = "_",
        description = "Separator between the base-name and integer value"
        )
    
    start_value = bpy.props.IntProperty(
        name = "Start Value",
        default = 0,
        description = "Value of the integer part of the name to start from",
        min = 0
        )      
        
    reverse = bpy.props.BoolProperty(
        name="Reverse",
        description="Reverse Count",
        default = False
        )    
    
    def execute(self, context):
        if bpy.context.scene.batch_type_enum == "objects":
            if bpy.context.scene.loc_enum == "X Location":
                path = 0
            elif bpy.context.scene.loc_enum == "Y Location":
                path = 1
            else:
                path = 2
            rev = self.reverse
            base = self.base_name
            sep = self.sep
            start = self.start_value
            batch_X (rev, path, base, sep, start)
        else:
            if bpy.context.scene.loc_enum == "X Location":
                path = 0
            elif bpy.context.scene.loc_enum == "Y Location":
                path = 1
            else:
                path = 2
            rev = self.reverse
            base = self.base_name
            sep = self.sep
            start = self.start_value
            batch_X_bone (rev, path, base, sep, start)
        
        return {'FINISHED'}
    
############################################
##### Add stages-based drivers         #####
##### to selected objects viewport     #####
##### and/or render visibility         #####
##### targeted to bone custom property #####
############################################

class OBJECT_OT_add_custom_drivers(bpy.types.Operator):
    """Add viewport/render visibility drivers"""
    bl_label = "Add custom drivers"
    bl_idname = "object.add_custom_drivers"
    bl_option = {'REGISTER', 'UNDO'}
    
    case = bpy.props.IntProperty()
    
    driver_property = bpy.props.StringProperty(
        name = "Bone Custom Property",
        default = "stages",
        description = "Custom property of the bone being used as the drivers' target"
        )
        
    inc_zero = bpy.props.BoolProperty(
        name="Include Zero",
        description="Create Zero Stage",
        default = False
        )
        
    driver_property_existing = bpy.props.StringProperty(
        name = "Existing Bone Custom Property",
        default = "stages",
        description = "Existing custom property of the bone being used as the drivers' target"
        )
    
    starting_stage = bpy.props.IntProperty(
        name = "Starting Stage",
        default = 0,
        description = "Objects become visible starting this stage"
        ) 
    
    bone_name = bpy.props.StringProperty(
        name = "Bone Name",
        default = "Root",
        description = "Bone with custom property being used as the drivers' target"
        )
        
    is_cyclic = bpy.props.BoolProperty(
        name="Cyclic Drivers",
        description="Make Drivers get 0 or 1 value according to frame and speed (parameter)",
        default = False
        )    
       
    def execute(self, context):
        
        ob = bpy.context.active_object     
        property = self.driver_property
        start = int(not self.inc_zero)
        is_cyclic = self.is_cyclic
        zero = self.inc_zero
        
        if self.case == 1:
            bone = bpy.context.active_pose_bone.name
            create_prop(bone, property, start)
            add_viewport(bone, property, is_cyclic, zero)
        
        elif self.case == 2:
            bone = bpy.context.active_pose_bone.name
            create_prop(bone, property, start)
            add_viewport(bone, property, is_cyclic, zero)
            add_render(bone, property, is_cyclic, zero)
            
        elif self.case == 3:
            remove_viewport()
            
        elif self.case == 4:
            remove_viewport()
            remove_render()
        
        elif self.case == 5:
            armature = bpy.data.scenes["Scene"].Armature
            bone = self.bone_name
            start = self.starting_stage
            property = self.driver_property_existing
            add_viewport_ex(armature, bone, property, start)
        
        elif self.case == 6:
            armature = bpy.data.scenes["Scene"].Armature
            bone = self.bone_name
            start = self.starting_stage
            property = self.driver_property_existing
            add_render_ex(armature, bone, property, start)
            add_viewport_ex(armature, bone, property, start)
            
        
        return {'FINISHED'}

####################################
############# PANELS ###############
####################################

class misc_tools_panel_spline(bpy.types.Panel):
    bl_label = "Spline IK"
    bl_idname = "OBJECT_PT_miscellaneous_tools_spline_ik"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Misc Tools"
    
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()
        if bpy.context.mode != "OBJECT" and bpy.context.mode != "POSE":
           box.enabled = False
        row = box.row(align = True)
        row.label(text="Slpine Armatures")
        reset = row.operator(OBJECT_OT_add_curve_hooks.bl_idname, text = "", icon = "FILE_REFRESH")
        reset.case = 3
        row = box.row()
        row.label(text = "Number of Bezier Points:")
        row = box.row()
        row.prop(context.scene, "curve_hooks_quantity", text = "")
        row = box.row()
        cr_hooks = row.operator(OBJECT_OT_add_curve_hooks.bl_idname, text = "Locate Points", icon = "NORMALIZE_FCURVES")
        cr_hooks.case = 1
        cr_hooks.curve_hooks_count = bpy.context.scene.curve_hooks_count
        cr_hooks.curve_hooks_quantity = bpy.context.scene.curve_hooks_quantity
        if bpy.context.scene.curve_hooks_stage == 1:
            row.enabled = False
        
        row = box.row()
        row.label(text="Spline Armature length:")
        row = box.row()
        row.prop(context.scene, "curve_hooks_subdivide", text = "")
        row = box.row()
        row = box.row(align = True)
        row.prop(context.scene, "spline_menu_enum", text = "")
        cr_arm = row.operator(OBJECT_OT_add_curve_hooks.bl_idname, text = "Create Spline IK", icon = "CONSTRAINT_BONE")
        cr_arm.case = 2
        cr_arm.curve_hooks_subdivide = bpy.context.scene.curve_hooks_subdivide
        if bpy.context.scene.curve_hooks_stage == 0:
            row.enabled = False
            
            
class misc_tools_panel_convert_curves(bpy.types.Panel):
    bl_label = "Convert Curves"
    bl_idname = "OBJECT_PT_miscellaneous_tools_convert_curves"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Misc Tools"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()
        if bpy.context.mode != "OBJECT" or bpy.context.active_object is None or bpy.context.active_object.type != "CURVE":
            box.enabled = False
        row = box.row()
        row.label(text="Convert Curves")
        row = box.row()
        row.prop(context.scene, "converted_curve_name", text="", icon="SORTALPHA")

        row = box.row()
        row.prop(context.scene, "limited_dissolve_angle", text="Max Angle")
        
        row = box.row()
        p = row.operator(OBJECT_OT_convert_and_limited_dissolve.bl_idname)
        p.name = bpy.context.scene.converted_curve_name
        p.max_angle = bpy.context.scene.limited_dissolve_angle
        
        row = box.row()
        b = row.operator(OBJECT_OT_convert_and_beautify.bl_idname)
        b.name = bpy.context.scene.converted_curve_name


class misc_tools_panel_naming(bpy.types.Panel):
    bl_label = "Naming"
    bl_idname = "OBJECT_PT_miscellaneous_tools_naming"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Misc Tools"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()
        box.label (text = "Naming")
        row = box.row(align = True)
        row.prop(context.scene, "namesakes_type_enum", text=" ", expand = True)
        row = box.row()
        row.label(text="Namesakes")
        row = box.row()
        row.prop(context.scene, "name_select", text="", icon="SORTALPHA")
        row = box.row()
        fn = row.operator(OBJECT_OT_select_namesakes.bl_idname)
        fn.name_sel = bpy.context.scene.name_select
        fn.case = 1
        row = box.row()
        row.label(text="Find & Replace in Objects Names")
        row = box.row()
        row.prop(context.scene, "name_source", text="Replace", icon = "VIEWZOOM")
        row = box.row()
        row.prop(context.scene, "name_target", text="with", icon = "LINE_DATA")
        row = box.row(align=True)
        row.prop(context.scene, "naming_selection_enum", text="Selection", expand = False)
        row = box.row()
        frep = row.operator(OBJECT_OT_select_namesakes.bl_idname, text = "Replace", icon = "FILE_REFRESH")
        frep.case = 2
        frep.name_source = bpy.context.scene.name_source
        frep.name_target = bpy.context.scene.name_target
        row = box.row()
        row.label(text = "Add Prefix / Suffix")
        row = box.row(align = True)
        row.prop(context.scene, "prefix", text="", icon = "FORWARD")
        row.prop(context.scene, "suffix", text="", icon = "BACK")
        row = box.row(align = True)
        pref = row.operator(OBJECT_OT_select_namesakes.bl_idname, text = "Add Prefix", icon = "FORWARD")
        pref.case = 3
        pref.prefix = bpy.context.scene.prefix
        suff = row.operator(OBJECT_OT_select_namesakes.bl_idname, text = "Add Suffix", icon = "BACK")
        suff.case = 4
        suff.suffix = bpy.context.scene.suffix


class misc_tools_panel_batch_rename(bpy.types.Panel):
    bl_label = "Batch Rename"
    bl_idname = "OBJECT_PT_miscellaneous_tools_batch_rename"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Misc Tools"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()
        row = box.row()
        row.label(text="Batch Rename (by Location)")
        row = box.row(align = True)
        row.prop(context.scene, "batch_type_enum", expand = True)
        row = box.row()
        row.prop(context.scene, "loc_enum", expand = True)
        row.prop(context.scene, "reverse", text = "", icon = "ARROW_LEFTRIGHT")
        
        row = box.row(align=True)
        row.label(text="Base-name")
        row.label(text="Separator")
        row.label(text="Start")
        row = box.row(align=True)
        row.prop(context.scene, "base_name", text ="", icon = "SORTALPHA")
        row.prop(context.scene, "separator", text = "")
        row.prop(context.scene, "start_value", text ="")
        row = box.row()
        b = row.operator(OBJECT_OT_batch_names.bl_idname, text = 'Batch Rename', icon = "COLLAPSEMENU")
        b.base_name = bpy.context.scene.base_name
        b.sep = bpy.context.scene.separator
        b.start_value = bpy.context.scene.start_value
        b.reverse = bpy.context.scene.reverse

class misc_tools_panel_drivers(bpy.types.Panel):
    bl_label = "Drivers"
    bl_idname = "OBJECT_PT_miscellaneous_tools_drivers"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Misc Tools"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()
        row = box.row()
        row.label(text="Add Drivers (Objects Visibility)")
        
        row = box.row()
        row.prop(context.scene, "driver_property", text ="", icon = "RNA")
                
        row = box.row(align = True)
        if bpy.context.scene.inc_zero == True:
            inc_zero_ic = "LAYER_ACTIVE"
        else:
            inc_zero_ic = "LAYER_USED"
        row.prop(context.scene, "inc_zero", text ="Zero stage", icon = inc_zero_ic)
        row.prop(context.scene, "is_cyclic", text ="Cyclic Stages", icon = "FILE_REFRESH")
        
        row = box.row(align = True)
        drive_v = row.operator(OBJECT_OT_add_custom_drivers.bl_idname, text = 'View Only', icon = "RESTRICT_VIEW_OFF")
        drive_v.case = 1
        drive_v.driver_property = bpy.context.scene.driver_property
        drive_v.inc_zero = bpy.context.scene.inc_zero
        drive_v.is_cyclic = bpy.context.scene.is_cyclic
        
        drive_r = row.operator(OBJECT_OT_add_custom_drivers.bl_idname, text = 'View+Render', icon = "RESTRICT_RENDER_OFF")    
        drive_r.case = 2
        drive_r.driver_property = bpy.context.scene.driver_property
        drive_r.inc_zero = bpy.context.scene.inc_zero
        drive_r.is_cyclic = bpy.context.scene.is_cyclic
        if bpy.context.mode != 'POSE':
            row.enabled = False
        
        box1 = box.box()
        row = box1.row()
        row.label(text="Remove Drivers", icon = "CANCEL")
        row = box1.row(align = True)
        remove_v = row.operator(OBJECT_OT_add_custom_drivers.bl_idname, text = 'View Only', icon = "RESTRICT_VIEW_ON")
        remove_v.case = 3
        
        remove_v = row.operator(OBJECT_OT_add_custom_drivers.bl_idname, text = 'View+Render', icon = "RESTRICT_RENDER_ON")
        remove_v.case = 4
        
        row = box.row()
        row.label(text = "Add Drivers manually")
        row = box.row()
        row.prop_search(scene, "Armature", context.scene, "objects", icon = "OBJECT_DATA")
        row = box.row()
        row.prop(context.scene, "bone_name", text ="Bone Name", icon = "BONE_DATA")
        row = box.row()
        row.prop(context.scene, "driver_property_existing", text ="Property", icon = "RNA")
        row = box.row()
        row.prop(context.scene, "starting_stage", text ="Starting stage")
        row = box.row(align = True)
        drive_v_manual = row.operator(OBJECT_OT_add_custom_drivers.bl_idname, text = 'View Only', icon = "RESTRICT_VIEW_ON")
        drive_v_manual.case = 5
        drive_v_manual.bone_name = bpy.context.scene.bone_name
        drive_v_manual.driver_property_existing = bpy.context.scene.driver_property_existing
        drive_v_manual.starting_stage = bpy.context.scene.starting_stage
        drive_r_manual = row.operator(OBJECT_OT_add_custom_drivers.bl_idname, text = 'View+Render', icon = "RESTRICT_RENDER_ON")
        drive_r_manual.case = 6
        drive_r_manual.bone_name = bpy.context.scene.bone_name
        drive_r_manual.driver_property_existing = bpy.context.scene.driver_property_existing
        drive_r_manual.starting_stage = bpy.context.scene.starting_stage
        
         
####################################
############## ENUM  ###############
############## LISTS ###############
####################################        
     
        
location_menu_items = [
                ('X Location','X','Path',0),
                ('Y Location','Y','Path',1),
                ('Z Location','Z','Path',2),
                ]

spline_menu_items = [
                ('create','Create New Armature','Create new Armature to control Spline IK','OUTLINER_OB_ARMATURE',0),
                ('parent','Parent to Active Bone','Create new Bones in existing Armature to control Spline IK','BONE_DATA',1),
                ]

naming_selection_items = [
                ('selected','Selected Only','Run naming only for Selected Objects / Bones','GROUP',0),
                ('visible','All Visible','Run naming for All Visible Objects / Bones','RESTRICT_VIEW_OFF',1),
                ('scene','All in Scene / Armature','Run naming for All Objects in Scene / Armature','SCENE_DATA',2),
                ]
                
namesakes_type_items = [
                ('objects','Objects','Run naming for Objects','MESH_CUBE',0),
                ('bones','Bones','Run naming for Bones of Active Armature Object','BONE_DATA',1),
                ]

batch_type_items = [
                ('objects','Objects','Run naming for Objects','MESH_CUBE',0),
                ('bones','Bones','Run naming for Bones of Active Armature Object','BONE_DATA',1),
                ]
    
    
####################################
########### REGISTRATION ###########
####################################        

########## REGISTER ##########

def register():
    
    bpy.types.Scene.converted_curve_name = bpy.props.StringProperty(
        name = "Curve Name",
        default = "Curve",
        description = "Name of the Mesh converted from selected Curves"
        )
        
    bpy.types.Scene.limited_dissolve_angle = bpy.props.FloatProperty(
        name = "Max Angle",
        default = 1,
        description = "Amgle Limit for Limited Dissolve Operation"
        )
        
    bpy.types.Scene.name_select = bpy.props.StringProperty(
        name = "Find Name",
        default = "Object",
        description = "Name of the Mesh converted from selected Curves"
        )
        
    bpy.types.Scene.driver_property = bpy.props.StringProperty(
        name = "Bone Custom Property",
        default = "stages",
        description = "Custom property of the bone being used as the drivers' target"
        )
    
    bpy.types.Scene.inc_zero = bpy.props.BoolProperty(
        name="Include Zero",
        description="Create Zero Stage",
        default = False
        )
    
    bpy.types.Scene.Armature = PointerProperty(type=bpy.types.Object)
    
    bpy.types.Scene.driver_property_existing = bpy.props.StringProperty(
        name = "Existing Bone Custom Property",
        default = "stages",
        description = "Existing custom property of the bone being used as the drivers' target"
        )
    
    bpy.types.Scene.starting_stage = bpy.props.IntProperty(
        name = "Starting Stage",
        default = 0,
        min = 0,
        description = "Objects become visible starting this stage"
        ) 
    
    bpy.types.Scene.bone_name = bpy.props.StringProperty(
        name = "Bone Name",
        default = "Root",
        description = "Bone with custom property being used as the drivers' target"
        )
    
    bpy.types.Scene.base_name = bpy.props.StringProperty(
        name = "Base Name",
        default = "Object",
        description = "Base-name for the selected objects"
        )
        
    bpy.types.Scene.separator = bpy.props.StringProperty(
        name = "Separator",
        default = "_",
        description = "Separator between the base-name and integer value"
        )
    
    bpy.types.Scene.start_value = bpy.props.IntProperty(
        name = "Start Value",
        default = 0,
        description = "Value of the integer part of the name to start from",
        min = 0
        )    
    
    bpy.types.Scene.loc_enum = bpy.props.EnumProperty(items=location_menu_items, description="Path to take into account when bathcing", default="X Location")  
    
    bpy.types.Scene.reverse = bpy.props.BoolProperty(
        name="Reverse",
        description="Reverse Count",
        default = False
        )
    
    bpy.types.Scene.name_source = bpy.props.StringProperty(
        name = "Source Name",
        default = "",
        description = "Source part of the Object Name to be replaced"
        )
    
    bpy.types.Scene.name_target = bpy.props.StringProperty(
        name = "Target Name",
        default = "",
        description = "Target part of the Object Name used to Replace"
        )
                  
    bpy.types.Scene.curve_hooks_count = bpy.props.IntProperty(
        name = "Spline Curves Counter",
        default = 0,
        min = 0,
        description = "Integer Property being used to divide spline chains"
        )
        
    bpy.types.Scene.curve_hooks_quantity = bpy.props.IntProperty(
        name = "Number of Hooks",
        default = 2,
        min = 2,
        max = 256,
        description = "Number of Hooks determining the Bezier Points Location"
        )
    
    bpy.types.Scene.curve_hooks_subdivide = bpy.props.IntProperty(
        name = "Spline Armature Subdivision",
        default = 2,
        min = 2,
        description = "Number of Spline Armature Bones"
        )
    
    bpy.types.Scene.curve_hooks_stage = bpy.props.IntProperty(
        name = "Operators Sequency",
        default = 0,
        min = 0,
        description = "Property to Disable inappropriate Operators Buttons"
        )
    
    bpy.types.Scene.curve_hooks_ns = bpy.props.IntProperty(
        name = "Prefix",
        default = 0,
        min = 0,
        description = "Prefix of Slpine Chains"
        )
    
    bpy.types.Scene.spline_menu_enum = bpy.props.EnumProperty(name = "Spline IK control Method", items=spline_menu_items, description="Create new Armature / Create new Bones & parent it to Active Bone", default="create")
    
    bpy.types.Scene.is_cyclic = bpy.props.BoolProperty(
        name="Cyclic Drivers",
        description="Make Drivers get 0 or 1 value according to frame and speed (parameter)",
        default = False
        ) 
    
    bpy.types.Scene.naming_selection_enum = bpy.props.EnumProperty(name = "Selection of Objects / Bones", items=naming_selection_items, description="Selection of Objects / Bones affected by Naming Operations", default="selected")
    
    bpy.types.Scene.namesakes_type_enum = bpy.props.EnumProperty(items=namesakes_type_items, description="Operations are being conducted for Objects / Bones", default="objects")
            
    bpy.types.Scene.prefix = bpy.props.StringProperty(
        name = "Prefix",
        default = "_",
        description = "Prefix to add before Object's base name"
        )
        
    bpy.types.Scene.suffix = bpy.props.StringProperty(
        name = "Suffix",
        default = "_",
        description = "Suffix to add after Object's base name"
        )
    
    bpy.types.Scene.batch_type_enum = bpy.props.EnumProperty(items=batch_type_items, description="Operations are being conducted for Objects / Bones", default="objects")
                
    bpy.utils.register_module(__name__)


########## UNREGISTER ##########
    
def unregister():
    
    bpy.utils.unregister_module(__name__)
    
    del bpy.types.Scene.converted_curve_name
    del bpy.types.Scene.limited_dissolve_angle
    del bpy.types.Scene.name_select
    del bpy.types.Scene.driver_property
    del bpy.types.Scene.inc_zero
    del bpy.types.Scene.Armature
    del bpy.types.Scene.driver_property_existing
    del bpy.types.Scene.starting_stage
    del bpy.types.Scene.base_name
    del bpy.types.Scene.separator
    del bpy.types.Scene.start_value
    del bpy.types.Scene.loc_enum
    del bpy.types.Scene.reverse
    del bpy.types.Scene.name_source
    del bpy.types.Scene.name_target
    del bpy.types.Scene.curve_hooks_count
    del bpy.types.Scene.curve_hooks_quantity
    del bpy.types.Scene.curve_hooks_subdivide
    del bpy.types.Scene.curve_hooks_stage
    del bpy.types.Scene.curve_hooks_ns
    del bpy.types.Scene.spline_menu_enum
    del bpy.types.Scene.is_cyclic
    del bpy.types.Scene.naming_selection_enum
    del bpy.types.Scene.namesakes_type_enum
    del bpy.types.Scene.prefix
    del bpy.types.Scene.suffix
    del bpy.types.Scene.batch_type_enum
    
register()