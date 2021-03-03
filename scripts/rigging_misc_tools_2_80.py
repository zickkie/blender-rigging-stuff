bl_info = {
    "name": "Miscellaneous Tools",
    "author": "Arthur Shapiro",
    "version": (1, 0),
    "blender": (2, 82),
    "location": "View3D > Tools",
    "description": "Miscellaneous Tools for Rigging",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"}
    
import bpy
import random
from math import radians
from bpy.props import PointerProperty
from mathutils import *
from bpy_extras.io_utils import unpack_list


####################################
########### ADDITIONAL #############
########### FUNCTIONS  #############
####################################

def rand():
    return str(random.randint(-100, 100))

# Shapes creating functions

def shapesCreateFK():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 
        
    bpy.ops.mesh.primitive_circle_add(vertices=32, radius=0.5, fill_type='NOTHING', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0, 0.5, 0), rotation=(1.570796, 0, 0))
    bpy.context.active_object.name = ("shape_FK." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj
   
    
def shapesCreateIKmain():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 
                
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name = ("shape_IK." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.context.active_object.scale[0] = 0.35
    bpy.context.active_object.scale[1] = 0.5
    bpy.context.active_object.scale[2] = 0.25
    bpy.context.active_object.location[1] = 0.5
    bpy.context.active_object.rotation_euler[1] = 1.570796
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj
  
    
def shapesCreateIKadd():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 

    bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=0.08, depth=1, enter_editmode=False, align='WORLD', location=(0, 0.5, 0), rotation=(-1.570796, 0, 0))
    bpy.context.active_object.name = ("shape_IK_add." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj
  
    
def shapesCreateIKstr():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 

    bpy.ops.mesh.primitive_cylinder_add(vertices=10, radius=0.12, depth=1, enter_editmode=False, align='WORLD', location=(0, 0.5, 0), rotation=(-1.570796, 0, 0))
    bpy.context.active_object.name = ("shape_IK_str." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj


def shapesCreateINT():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 

    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(0, 0.5, 0))
    bpy.context.active_object.scale[0] = 0.3
    bpy.context.active_object.scale[2] = 0.3
    bpy.context.active_object.name = ("shape_INT." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj


def shapesCreateTweaks():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
        
    #for vert in bpy.context.active_object.data.vertices:
        #print("(" + str(vert.co[0]) + ", " + str(vert.co[1]) + ", " + str(vert.co[2]) + "), ")

    verts = [(-2.0, 0.3085744380950928, 0.0),
    (-2.0601999759674072, 0.3026452660560608, 0.0),
    (-2.118086338043213, 0.28508561849594116, 0.0),
    (-2.1714346408843994, 0.2565702795982361, 0.0),
    (-2.2181949615478516, 0.2181951254606247, 0.0),
    (-2.2565701007843018, 0.17143483459949493, 0.0),
    (-2.285085439682007, 0.11808644980192184, 0.0),
    (-2.302645206451416, 0.06020006537437439, 0.0),
    (-2.3085741996765137, 2.3272934868145967e-07, 0.0),
    (-2.302645206451416, -0.06019959971308708, 0.0),
    (-2.285085439682007, -0.11808599531650543, 0.0),
    (-2.2565701007843018, -0.1714344471693039, 0.0),
    (-2.2181949615478516, -0.21819473803043365, 0.0),
    (-2.1714346408843994, -0.25656992197036743, 0.0),
    (-2.118086099624634, -0.2850852608680725, 0.0),
    (-2.0601999759674072, -0.30264484882354736, 0.0),
    (-1.9999998807907104, -0.30857396125793457, 0.0),
    (-1.9398000240325928, -0.3026447892189026, 0.0),
    (-1.881913661956787, -0.28508514165878296, 0.0),
    (-1.828565239906311, -0.2565698027610779, 0.0),
    (-1.7818049192428589, -0.2181946039199829, 0.0),
    (-1.7434297800064087, -0.17143428325653076, 0.0),
    (-1.7149145603179932, -0.1180858165025711, 0.0),
    (-1.6973549127578735, -0.060199372470378876, 0.0),
    (-1.6914258003234863, 5.073916895526054e-07, 0.0),
    (-1.697355031967163, 0.060200370848178864, 0.0),
    (-1.7149147987365723, 0.11808677017688751, 0.0),
    (-1.7434301376342773, 0.1714351773262024, 0.0),
    (-1.781805396080017, 0.21819542348384857, 0.0),
    (-1.8285657167434692, 0.2565705180168152, 0.0),
    (-1.8819142580032349, 0.2850857973098755, 0.0),
    (-1.9398006200790405, 0.30264538526535034, 0.0),
    (0.0, 0.0, 0.0)]

    edges = [(0, 1),   (1, 2),   (2, 3),   (3, 4),   (4, 5), 
             (5, 6),   (6, 7),   (7, 8),   (8, 9),   (9, 10), 
             (10, 11), (11, 12), (12, 13), (13, 14), (14, 15),
             (15, 16), (16, 17), (17, 18), (18, 19), (19, 20),
             (20, 21), (21, 22), (22, 23), (23, 24), (24, 25),
             (25, 26), (26, 27), (27, 28), (28, 29), (29, 30),
             (30, 31), (31, 0),  (24, 32)]
             
    faces = []

    mesh = bpy.data.meshes.new(name = "shape_tweaks." + rand())
    mesh.from_pydata(verts, edges, faces)
    ob = bpy.data.objects.new(("shape_tweaks." + rand()), mesh)
    bpy.data.collections["shapes"].objects.link(ob)
    obj = bpy.data.objects[ob.name]
    obj.scale[0] = obj.scale[1] = obj.scale[2] = 0.5
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.select_all(action='DESELECT')

#for i in range(len(bpy.context.active_object.data.vertices)):
    #edges.append("(" + str(i) + ", " + str(i+1) + ")")
    
#print(edges)
    
    return obj


def shapesCreateParents():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 

    bpy.ops.mesh.primitive_cube_add(size=0.25, enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name = ("shape_parents." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj

def shapesCreatePoleParents():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 

    bpy.ops.mesh.primitive_uv_sphere_add(segments=4, ring_count=5, radius=0.098, enter_editmode=False, location=(0, 0, 0))

    bpy.context.active_object.name = ("shape_pole_parents." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj


def shapesCreatePole():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 

    bpy.ops.mesh.primitive_circle_add(radius=0.25, enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name = "Run away, but we're running in circles " + rand()
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_circle_add(radius=0.25, enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name = "Run away, but we're running in circles " + rand()
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.object.rotation_euler[0] = 1.570796
    bpy.ops.mesh.primitive_circle_add(radius=0.25, enter_editmode=False, location=(0, 0, 0))
    bpy.context.object.rotation_euler[1] = 1.570796
    bpy.context.active_object.name = "Run away, but we're running in circles " + rand()
    bpy.ops.object.select_all(action='DESELECT')

    for obj in bpy.data.objects:
        if "Run away, but we're running in circles " in obj.name:
             obj.select_set(True)

    bpy.ops.object.join()
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    bpy.context.active_object.name = ("shape_pole." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj

def shapesCreatePoleParent():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)
     
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["shapes"] 

    bpy.ops.mesh.primitive_circle_add(radius=0.18, enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name = "Feed the flame 'cause we can't let go " + rand()
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_circle_add(radius=0.18, enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name = "Feed the flame 'cause we can't let go " + rand()
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.object.rotation_euler[0] = 1.570796
    bpy.ops.mesh.primitive_circle_add(radius=0.18, enter_editmode=False, location=(0, 0, 0))
    bpy.context.object.rotation_euler[1] = 1.570796
    bpy.context.active_object.name = "Feed the flame 'cause we can't let go " + rand()
    bpy.ops.object.select_all(action='DESELECT')

    for obj in bpy.data.objects:
        if "Feed the flame 'cause we can't let go " in obj.name:
             obj.select_set(True)

    bpy.ops.object.join()
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    bpy.context.active_object.name = ("shape_pole_parent." + rand())
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj


def shapesCreatePoleFK():
    
    sh =  0
    
    for col in bpy.data.collections:
        if col.name == "shapes":
            sh = 1      
    if sh == 0:       
        shapes = bpy.data.collections.new("shapes")
        bpy.context.scene.collection.children.link(shapes)

    verts = [( 0,    -0.125,  0    ),
            ( 0,      0.125,  0    ),
            ( 0,      0,      0.125),
            ( 0,      0,     -0.125),
            ( 0.125,  0,      0    ),
            (-0.125,  0,      0    )]

    edges = [(0, 1), (2, 3), (4, 5)]
             
    faces = []

    mesh = bpy.data.meshes.new(name = "shape_FK_pole." + rand())
    mesh.from_pydata(verts, edges, faces)
    ob = bpy.data.objects.new(("shape_FK_pole." + rand()), mesh)
    bpy.data.collections["shapes"].objects.link(ob)
    obj = bpy.data.objects[bpy.context.active_object.name]
    bpy.ops.object.select_all(action='DESELECT')
    
    return obj


# Creates Bone Custom Property 
def create_property(bone, property, min, max):
    ob = bpy.context.active_object
    pbone = bpy.data.objects[ob.name].pose.bones[bone]
    pbone[property] = min
    if "_RNA_UI" not in pbone.keys():
                pbone["_RNA_UI"] = {}
    pbone["_RNA_UI"].update({property: {"min":min, "max":max, "soft_min":min, "soft_max":max}})

# Functions of getting the optimal IK pole angle calculated from existing bones location
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


# Creates list of bones that contain defined prefix and place names of such bones in hierarchical order (from parent to child)
def hierarchicalBonesList(prefix):
    
    bpy.ops.object.mode_set(mode='EDIT')
    
    list = [bone.name for bone in bpy.context.object.data.edit_bones if bone.name.startswith(prefix) and bone.select == True]
    print(prefix + " list is ")
    print(list)
    list_hie = []
    zero_bone = ""
    
    for bone in bpy.context.object.data.edit_bones:
        if bone.name in list and bone.parent is None:
            zero_bone = bone.name
            print("current zero bone is " + zero_bone)
            list_hie.append(zero_bone)
    
    bpy.ops.armature.select_all(action='DESELECT')
    bpy.context.object.data.edit_bones[zero_bone].select=True
    bpy.context.object.data.edit_bones[zero_bone].select_head=True
    bpy.context.object.data.edit_bones[zero_bone].select_tail=True
    bpy.context.object.data.edit_bones.active = bpy.context.object.data.edit_bones[zero_bone]
    
    for i in range(len(list) - 1):
        bpy.ops.armature.select_hierarchy(direction='CHILD')
        list_hie.append(bpy.context.active_bone.name)
    
    return list_hie
    
    
# Makes bones chains    
def makeChains(FK, IK, IK_s, tweaks):
    
    FKs_list = []
    IKs_list = []
    INTs_list = []
    DEFs_list = []
    IK_STRs_list = []
    tweaks_list = []
    tweak_parents_list = []
    
    ob = bpy.context.active_object
    armature_name = ob.name
    bones = ob.pose.bones
    
    list = []
    for bone in bpy.context.selected_pose_bones:
            list.append(bone.name)
    print("selected at start bones ")
    print(list)
    
    bpy.ops.object.mode_set(mode='EDIT')
 
#######################    
### CREATING CHAINS ###
#######################    
    
    DEFs_list = hierarchicalBonesList("DEF")
    print("final DEFs list is ")
    print(DEFs_list)
    
    # INT
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.armature.select_all(action='DESELECT')
    for bone in bpy.context.object.data.edit_bones:
        if bone.name in DEFs_list:
            bone.select = True
            bone.select_head = True
            bone.select_tail = True
    bpy.ops.armature.duplicate(do_flip_names=False)
    for bone in bpy.context.object.data.edit_bones:
        if bpy.context.object.data.edit_bones[bone.name].select == True:
            bone.name = bone.name.replace("DEF", "INT")
            bone.name = bone.name[:-4]
            bone.use_connect = False
    INTs_list = hierarchicalBonesList("INT")
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='DESELECT')
    for bone in bpy.context.active_object.data.bones:
        if bone.name in list:
            bone.select = True
    
    # FK        
    if FK == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.duplicate(do_flip_names=False)
        for bone in bpy.context.object.data.edit_bones:
            if bpy.context.object.data.edit_bones[bone.name].select == True:
                bone.name = bone.name.replace("DEF", "FK")
                bone.name = bone.name[:-4]
                bone.use_connect = False
        FKs_list = hierarchicalBonesList("FK")        
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='DESELECT')
        for bone in bpy.context.active_object.data.bones:
            if bone.name in list:
                bone.select = True
        
        
    
    # IK
    if IK == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.duplicate(do_flip_names=False)
        for bone in bpy.context.object.data.edit_bones:
            if bpy.context.object.data.edit_bones[bone.name].select == True:
                bone.name = bone.name.replace("DEF", "IK")
                bone.name = bone.name[:-4]
        IKs_list = hierarchicalBonesList("IK" + DEFs_list[0][3])        
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='DESELECT')
        for bone in bpy.context.active_object.data.bones:
            if bone.name in list:
                bone.select = True
        
        
    
    # IK with sretching
    if IK_s == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.duplicate(do_flip_names=False)
        for bone in bpy.context.object.data.edit_bones:
            if bpy.context.object.data.edit_bones[bone.name].select == True:
                bone.name = bone.name.replace("DEF", "IKstr")
                bone.name = bone.name[:-4]
        IK_STRs_list = hierarchicalBonesList("IKstr")        
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='DESELECT')
        for bone in bpy.context.active_object.data.bones:
            if bone.name in list:
                bone.select = True
    
    
    # disconnecting last DEF bone
    bpy.ops.object.mode_set(mode='EDIT')
    for bone in bpy.context.object.data.edit_bones:
        if bone.name == DEFs_list[-1]:
            bone.use_connect = False
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='DESELECT')
    for bone in bpy.context.active_object.data.bones:
        if bone.name in list:
            bone.select = True
    
    # tweaks
    if tweaks == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.duplicate(do_flip_names=False)
        for bone in bpy.context.object.data.edit_bones:
            if bpy.context.object.data.edit_bones[bone.name].select == True:
                bone.name = bone.name.replace("DEF", "tweak")
                bone.name = bone.name[:-4]
                bone.use_connect = False
     
        # hierarchical list creating   
        tweaks_list = hierarchicalBonesList("tweak")
        print(tweaks_list)   

        for bone in bpy.context.object.data.edit_bones:
            if bone.name in tweaks_list:
                bone.tail = (bpy.context.object.data.edit_bones[DEFs_list[tweaks_list.index(bone.name)]].head + bpy.context.object.data.edit_bones[DEFs_list[tweaks_list.index(bone.name)]].tail) / 2
        
        bpy.ops.armature.select_all(action='DESELECT')
        
        if FK == True:
            
            # hierarchical list creating
            tweak_parents_list = []
            
            for bone in bpy.context.object.data.edit_bones:
                if bone.name in tweaks_list:
                    bone.select = True
                    bone.select_head = True
                    bone.select_tail = True
            bpy.ops.armature.duplicate(do_flip_names=False)
            for bone in bpy.context.object.data.edit_bones:
                if bpy.context.object.data.edit_bones[bone.name].select == True:
                    bone.name = bone.name[:-4] + ".parent"
                    # hierarchical list updating
                    tweak_parents_list.append(bone.name)
            print(tweak_parents_list)
            bpy.ops.armature.select_all(action='DESELECT')
            
            if IK == False:
                
                # MCH-DEF "hand"
                for bone in bpy.context.object.data.edit_bones:
                    if bone.name == DEFs_list[-1]:
                        bone.select = True
                        bone.select_head = True
                        bone.select_tail = True
                        bpy.context.object.data.edit_bones.active = bone
                bpy.ops.armature.duplicate(do_flip_names=False)
                bpy.ops.armature.switch_direction()
                bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[DEFs_list[-1]]
                bpy.context.object.data.edit_bones.active.name = bpy.context.object.data.edit_bones[DEFs_list[-1]].name.replace("DEF", "MCH-DEF")
                mch_def_bone = bpy.context.object.data.edit_bones.active.name
                bpy.context.object.data.edit_bones.active.use_connect = False
        
        if IK == True:
            
            for bone in bpy.context.object.data.edit_bones:
                if bone.name == DEFs_list[-1]:
                    bone.select = True
                    bone.select_head = True
                    bone.select_tail = True
                    bpy.context.object.data.edit_bones.active = bone
            
            # MCH-IK "hand"
            bpy.ops.armature.duplicate(do_flip_names=False)
            bpy.context.object.data.edit_bones.active.tail = (bpy.context.object.data.edit_bones[DEFs_list[-1]].head + bpy.context.object.data.edit_bones[DEFs_list[-1]].tail) / 2
            bpy.context.object.data.edit_bones.active.name = bpy.context.object.data.edit_bones.active.name.replace("DEF", "MCH-IK")[:-4]
            mch_ik_bone = bpy.context.object.data.edit_bones.active.name
            if IK_s == True:
                bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[IK_STRs_list[-2]]
            else:
                bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[IKs_list[-2]]
            bpy.context.object.data.edit_bones.active.use_connect = True
            bpy.ops.armature.select_all(action='DESELECT')
            
            
            # MCH-DEF "hand"
            for bone in bpy.context.object.data.edit_bones:
                if bone.name == DEFs_list[-1]:
                    bone.select = True
                    bone.select_head = True
                    bone.select_tail = True
                    bpy.context.object.data.edit_bones.active = bone
            bpy.ops.armature.duplicate(do_flip_names=False)
            bpy.ops.armature.switch_direction()
            bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[DEFs_list[-1]]
            bpy.context.object.data.edit_bones.active.name = bpy.context.object.data.edit_bones[DEFs_list[-1]].name.replace("DEF", "MCH-DEF")
            mch_def_bone = bpy.context.object.data.edit_bones.active.name
            bpy.context.object.data.edit_bones.active.use_connect = False
        
    
    else:
        if IK == True:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.armature.select_all(action='DESELECT')
            for bone in bpy.context.object.data.edit_bones:
                if bone.name == DEFs_list[-1]:
                    bone.select = True
                    bone.select_head = True
                    bone.select_tail = True
                    bpy.context.object.data.edit_bones.active = bone
            
            # MCH-IK "hand"
            bpy.ops.armature.duplicate(do_flip_names=False)
            bpy.context.object.data.edit_bones.active.tail = (bpy.context.object.data.edit_bones[DEFs_list[-1]].head + bpy.context.object.data.edit_bones[DEFs_list[-1]].tail) / 2
            bpy.context.object.data.edit_bones.active.name = bpy.context.object.data.edit_bones.active.name.replace("DEF", "MCH-IK")[:-4]
            mch_ik_bone = bpy.context.object.data.edit_bones.active.name
            if IK_s == True:
                bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[IK_STRs_list[-2]]
            else:
                bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[IKs_list[-2]]
            bpy.context.object.data.edit_bones.active.use_connect = True
            bpy.ops.armature.select_all(action='DESELECT')
        
    # MCH-FK "hand"   
    if FK == True:
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='DESELECT')
        for bone in bpy.context.object.data.edit_bones:
            if bone.name == FKs_list[-1]:
                bone.select = True
                bone.select_head = True
                bone.select_tail = True
                bpy.context.object.data.edit_bones.active = bone
        bpy.ops.armature.duplicate(do_flip_names=False)
        bpy.context.object.data.edit_bones.active.tail = (bpy.context.object.data.edit_bones[FKs_list[-1]].head + bpy.context.object.data.edit_bones[FKs_list[-1]].tail) / 2
        bpy.context.object.data.edit_bones.active.name = bpy.context.object.data.edit_bones.active.name.replace("FK", "MCH-FK")[:-4]
        mch_fk_bone = bpy.context.object.data.edit_bones.active.name
        bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[FKs_list[-2]]
        bpy.context.object.data.edit_bones.active.use_connect = False
        bpy.context.object.data.edit_bones.active.use_inherit_scale = False
        bpy.context.object.data.edit_bones[FKs_list[-1]].parent = bpy.context.object.data.edit_bones[mch_fk_bone]
        bpy.context.object.data.edit_bones[FKs_list[-1]].use_connect = False
        bpy.context.object.data.edit_bones[FKs_list[-1]].use_inherit_scale = True
                            
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='DESELECT')
    for bone in bpy.context.active_object.data.bones:
        if bone.name in list:
            bone.select = True

#################    
### PARENTING ###
################# 
    
    # DEF.hand
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.context.object.data.edit_bones[DEFs_list[-1]].parent = bpy.context.object.data.edit_bones[INTs_list[-1]]
    bpy.context.object.data.edit_bones[DEFs_list[-1]].use_connect = False
    bpy.ops.object.mode_set(mode='POSE')

    if IK == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        for bone in bpy.context.object.data.edit_bones:
            if bone.name == IKs_list[-1]:
                bone.parent = None
        bpy.ops.object.mode_set(mode='POSE')
    
    if IK_s == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        for bone in bpy.context.object.data.edit_bones:
            if bone.name == IK_STRs_list[-1]:
                bpy.context.object.data.edit_bones.remove(bone)
        bpy.ops.object.mode_set(mode='POSE')
    
    if tweaks == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        for bone in bpy.context.object.data.edit_bones:
            if bone.name in tweaks_list:
                if FK == True:
                    bone.parent = bpy.context.object.data.edit_bones[tweak_parents_list[tweaks_list.index(bone.name)]]
                    
                else:
                    bone.parent = bpy.context.object.data.edit_bones[INTs_list[tweaks_list.index(bone.name)]]
                    bone.use_inherit_scale = False
       
        if FK == True:
            for bone in bpy.context.object.data.edit_bones:
                if bone.name in tweak_parents_list:
                    bone.parent = bpy.context.object.data.edit_bones[INTs_list[tweak_parents_list.index(bone.name)]]
        
        bpy.ops.object.mode_set(mode='POSE')

#######################  
### IK POLE TARGETS ###
#######################
    
    if IK == True:
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='DESELECT')
        
        # creating IK pole parent with the same roll (simply duplicating) as the last bone in IK chain
        for bone in bpy.context.object.data.edit_bones:
            if bone.name == IKs_list[-2]:
                bone.select = True
                bone.select_head = True
                if len(IKs_list) > 2:
                    bpy.context.object.data.edit_bones[IKs_list[-3]].select_tail = True
                bone.select_tail = True
                bpy.context.object.data.edit_bones.active = bone
                for bone in bpy.context.selected_editable_bones:
                    print(bone.name)
                print(bpy.context.active_bone.name)
        bpy.ops.armature.duplicate(do_flip_names=False)
        print(bpy.context.object.data.edit_bones.active.name)
        bpy.context.object.data.edit_bones.active.parent = None
        bpy.context.object.data.edit_bones.active.name = "IK.pole.parent"
        ik_pole_parent_bone = bpy.context.object.data.edit_bones.active.name
        bpy.context.object.data.edit_bones.active.tail = (bpy.context.object.data.edit_bones[IKs_list[-2]].head + bpy.context.object.data.edit_bones[IKs_list[-2]].tail) / 2
        
        # crating IK pole bone
        bpy.ops.armature.select_all(action='DESELECT')
        for bone in bpy.context.object.data.edit_bones:
            if bone.name == ik_pole_parent_bone:
                bone.select = True
                bone.select_head = True
                bone.select_tail = True
                bpy.context.object.data.edit_bones.active = bone
        bpy.ops.armature.duplicate(do_flip_names=False)
        print(bpy.context.object.data.edit_bones.active.name)
        bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[ik_pole_parent_bone]
        bpy.context.object.data.edit_bones.active.use_connect = False
        bpy.context.object.data.edit_bones.active.name = "IK.pole"
        ik_pole_bone = bpy.context.object.data.edit_bones.active.name
        bpy.ops.object.mode_set(mode='POSE')
        
        # crating IK pole as child of IK "hand" bone
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='DESELECT')
        for bone in bpy.context.object.data.edit_bones:
            if bone.name == ik_pole_parent_bone:
                bone.select = True
                bone.select_head = True
                bone.select_tail = True
                bpy.context.object.data.edit_bones.active = bone
        bpy.ops.armature.duplicate(do_flip_names=False)
        print(bpy.context.object.data.edit_bones.active.name)
        bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[IKs_list[-1]]
        bpy.context.object.data.edit_bones.active.use_connect = False
        bpy.context.object.data.edit_bones.active.name = "IK.pole.parent-" + IKs_list[-1]
        ik_pole_hand_bone = bpy.context.object.data.edit_bones.active.name
        bpy.ops.object.mode_set(mode='POSE')
        
        # creating "FK pole" (and its "anchors", parented to each of FK chain bones), 
        # helping to set correct IK pole position when IK-FK snapping - 
        # all just as duplicates of created IK pole bones
        if FK == True:
            
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.armature.duplicate(do_flip_names=False)
            bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[FKs_list[0]]
            bpy.context.object.data.edit_bones.active.use_connect = False
            bpy.context.object.data.edit_bones.active.name = "FK.pole"
            fk_pole_bone = bpy.context.object.data.edit_bones.active.name
            print(fk_pole_bone)
            
            mch_fk_poles_list = []
            for i in range(len(FKs_list)-1):
                bpy.ops.armature.duplicate(do_flip_names=False)
                bpy.context.object.data.edit_bones.active.parent = bpy.context.object.data.edit_bones[FKs_list[i]]
                bpy.context.object.data.edit_bones.active.use_connect = False
                bpy.context.object.data.edit_bones.active.name = "MCH-" + bpy.context.object.data.edit_bones[FKs_list[i]].name + ".pole"
                mch_fk_poles_list.append(bpy.context.object.data.edit_bones.active.name)
            print(mch_fk_poles_list)
            bpy.ops.object.mode_set(mode='POSE')

###################  
### CONSTRAINTS ###
###################

    if tweaks == True:
        
        # all DEFs except the last one
        for bone in bones:
            if bone.name in DEFs_list and bone.name != DEFs_list[-1]:
                
                # Copy Location
                bones[bone.name].constraints.new("COPY_LOCATION")
                bones[bone.name].constraints["Copy Location"].target = ob
                bones[bone.name].constraints["Copy Location"].subtarget = tweaks_list[DEFs_list.index(bone.name)]
                
                # Copy Transforms
                bones[bone.name].constraints.new("COPY_TRANSFORMS")
                bones[bone.name].constraints["Copy Transforms"].target = ob
                bones[bone.name].constraints["Copy Transforms"].subtarget = tweaks_list[DEFs_list.index(bone.name)]
                
                # Damped Track
                bones[bone.name].constraints.new("DAMPED_TRACK")
                bones[bone.name].constraints["Damped Track"].target = ob
                bones[bone.name].constraints["Damped Track"].subtarget = tweaks_list[DEFs_list.index(bone.name)+1]
                
                # Stretch To
                bones[bone.name].constraints.new("STRETCH_TO")
                bones[bone.name].constraints["Stretch To"].target = ob
                bones[bone.name].constraints["Stretch To"].subtarget = tweaks_list[DEFs_list.index(bone.name)+1]
                bones[bone.name].constraints["Stretch To"].volume = "NO_VOLUME"
        
        #DEF "hand"
        for bone in bones:
            if bone.name == mch_def_bone:
                
                # We don't wand the bone of "hand" to be stretched, 
                # so just Damped Track without Stretch To will be OK
                bones[bone.name].constraints.new("DAMPED_TRACK")
                bones[bone.name].constraints["Damped Track"].target = ob
                bones[bone.name].constraints["Damped Track"].subtarget = tweaks_list[-1]
        
        # Adjustable ininheritance of FK scale
        if FK == True:
            for i in range(len(tweak_parents_list)-1):
                bpy.context.active_object.data.bones[tweak_parents_list[i]].use_inherit_scale = False
                bones[tweak_parents_list[i]].constraints.new("COPY_SCALE")
                bones[tweak_parents_list[i]].constraints["Copy Scale"].name = "Copy Scale from FK"
                bones[tweak_parents_list[i]].constraints["Copy Scale from FK"].target = ob
                bones[tweak_parents_list[i]].constraints["Copy Scale from FK"].subtarget = FKs_list[i]
            bpy.context.active_object.data.bones[tweak_parents_list[-1]].use_inherit_scale = False
        
    else:
        
        # all DEFs (except the last one) copy transforms of INTs
        for bone in bones:
            if bone.name in DEFs_list and bone.name != DEFs_list[-1]:
                bones[bone.name].constraints.new("COPY_TRANSFORMS")
                bones[bone.name].constraints["Copy Transforms"].target = ob
                bones[bone.name].constraints["Copy Transforms"].subtarget = INTs_list[DEFs_list.index(bone.name)]
    
    if FK == True:
        
        # all INTs copy transforms of FKs under any circumstances
        for bone in bones:
            if bone.name in INTs_list:
                bones[bone.name].constraints.new("COPY_TRANSFORMS")
                bones[bone.name].constraints["Copy Transforms"].name = "Copy Transforms FK"
                bones[bone.name].constraints["Copy Transforms FK"].target = ob
                bones[bone.name].constraints["Copy Transforms FK"].subtarget = FKs_list[INTs_list.index(bone.name)]
        
        # Preventing FK "hand" scale ininheritance
        bones[mch_fk_bone].constraints.new("COPY_SCALE")
        bones[mch_fk_bone].constraints["Copy Scale"].name = "Copy Scale from FK Lower"
        bones[mch_fk_bone].constraints["Copy Scale from FK Lower"].target = ob
        bones[mch_fk_bone].constraints["Copy Scale from FK Lower"].subtarget = FKs_list[-2]
    
    # IK Constraint for non-stretching bones
    if IK == True:
        
        # Geting the optimal IK pole angle
        #base_bone = bones[IKs_list[0]]
        #ik_bone = bones[IKs_list[-1]]
        #pole_bone = bones[ik_pole_bone]
        #pole_angle_in_radians = get_pole_angle(base_bone,
                                               #ik_bone,
                                               #pole_bone.matrix.translation)
        #pole_angle_in_deg = round(180*pole_angle_in_radians/3.141592, 3)
        
        # Setting the IK Constraint with the evaluated pole angle
        for bone in bones:
            if bone.name == IKs_list[-2]:
                bones[bone.name].constraints.new("IK")
                bones[bone.name].constraints["IK"].target = ob
                bones[bone.name].constraints["IK"].subtarget = IKs_list[-1]
                bones[bone.name].constraints["IK"].pole_target = ob
                bones[bone.name].constraints["IK"].pole_subtarget = ik_pole_bone
                #bones[bone.name].constraints["IK"].pole_angle = pole_angle_in_deg
                bones[bone.name].constraints["IK"].pole_angle = 0
                bones[bone.name].constraints["IK"].chain_count = (len(IKs_list) - 1)
                bones[bone.name].constraints["IK"].use_stretch = True
                
        # MCH - IK bone
        for bone in bones:
            if bone.name == mch_ik_bone:
                bones[bone.name].constraints.new("COPY_TRANSFORMS")
                bones[bone.name].constraints["Copy Transforms"].name = "Copy Transforms IK"
                bones[bone.name].constraints["Copy Transforms IK"].target = ob
                bones[bone.name].constraints["Copy Transforms IK"].subtarget = IKs_list[-1]

        # There are IKs with stretching
        if IK_s == True:
            print("/////IKs = True///////")
            # All INTs except the last one
            for bone in bones:
                if bone.name in INTs_list and bone.name != INTs_list[-1]:
                    bones[bone.name].constraints.new("COPY_TRANSFORMS")
                    bones[bone.name].constraints["Copy Transforms"].name = "Copy Transforms IK"
                    bones[bone.name].constraints["Copy Transforms IK"].target = ob
                    bones[bone.name].constraints["Copy Transforms IK"].subtarget = IK_STRs_list[INTs_list.index(bone.name)]
            
            # Stretchy IK chain switches between copying transforms 
            # of non-stretching chain and getting stretch from its own IK constraint
            
            # 1st Constraint: copy transforms form IK
            for bone in bones:
                if bone.name in IK_STRs_list:
                    bones[bone.name].constraints.new("COPY_TRANSFORMS")
                    bones[bone.name].constraints["Copy Transforms"].name = "Copy Transforms IK"
                    bones[bone.name].constraints["Copy Transforms IK"].target = ob
                    bones[bone.name].constraints["Copy Transforms IK"].subtarget = IKs_list[IK_STRs_list.index(bone.name)]
                    
                    # setting IK stretching in Bone Parameters tab
                    bone.ik_stretch = 0.1
                    
            # 2nd Constraint: self IK
            for bone in bones:
                if bone.name == IK_STRs_list[-2]:
                    bones[bone.name].constraints.new("IK")
                    bones[bone.name].constraints["IK"].name = "Self IK"
                    bones[bone.name].constraints["Self IK"].target = ob
                    bones[bone.name].constraints["Self IK"].subtarget = IKs_list[-1]
                    bones[bone.name].constraints["Self IK"].pole_target = ob
                    bones[bone.name].constraints["Self IK"].pole_subtarget = ik_pole_bone
                    #bones[bone.name].constraints["Self IK"].pole_angle = pole_angle_in_deg
                    bones[bone.name].constraints["Self IK"].pole_angle = 0
                    bones[bone.name].constraints["Self IK"].chain_count = (len(IK_STRs_list)-1)
                    bones[bone.name].constraints["Self IK"].use_stretch = True
                    
            # DEFs should preserve volume even without tweaks-based constraints
            if tweaks == False:
                print("/////tweaks = False///////")
                # All DEFs except the last one
                for bone in bones:
                    if bone.name in DEFs_list and bone.name != DEFs_list[-1]:
                        bones[bone.name].constraints.new("MAINTAIN_VOLUME")
                        bones[bone.name].constraints["Maintain Volume"].name = "IK Maintain Volume"
                        bones[bone.name].constraints["IK Maintain Volume"].mode = "SINGLE_AXIS"
            
        
        else: # There are no IKs with stretching
            
            # All INTs except the last one
            for bone in bones:
                if bone.name in INTs_list and bone.name != INTs_list[-1]:
                    bones[bone.name].constraints.new("COPY_TRANSFORMS")
                    bones[bone.name].constraints["Copy Transforms"].name = "Copy Transforms IK"
                    bones[bone.name].constraints["Copy Transforms IK"].target = ob
                    bones[bone.name].constraints["Copy Transforms IK"].subtarget = IKs_list[INTs_list.index(bone.name)]
        
        # INT - "hand": no matter if there is a stretchy IK chain
        for bone in bones:
            if bone.name == INTs_list[-1]:
                bones[bone.name].constraints.new("COPY_TRANSFORMS")
                bones[bone.name].constraints["Copy Transforms"].name = "Copy Transforms IK"
                bones[bone.name].constraints["Copy Transforms IK"].target = ob
                bones[bone.name].constraints["Copy Transforms IK"].subtarget = mch_ik_bone
        
        # Adjustable IK pole parenting
        bones[ik_pole_parent_bone].constraints.new("COPY_TRANSFORMS")
        bones[ik_pole_parent_bone].constraints["Copy Transforms"].name = "Copy Transforms from IK target"
        bones[ik_pole_parent_bone].constraints["Copy Transforms from IK target"].target = ob
        bones[ik_pole_parent_bone].constraints["Copy Transforms from IK target"].subtarget = ik_pole_hand_bone
                
        # fake FK pole should maintain the middle position among it's anchors 
        # (upper pole, lower pole etc.); it's important to keep in mind 
        # that such scheme works with 3-bone limbs, for other cases you need to 
        # adjust the Copy Transforms constraints power manually 
        # (or use drivers to set transform of FK pole as average transforms of all the FK poles)
        if FK == True:
            for i in range(len(mch_fk_poles_list)):
                bones[fk_pole_bone].constraints.new("COPY_TRANSFORMS")
                bones[fk_pole_bone].constraints["Copy Transforms"].name = str(i) + "_Copy Transforms form MCH-FK pole"
                bones[fk_pole_bone].constraints[str(i) + "_Copy Transforms form MCH-FK pole"].target = ob
                bones[fk_pole_bone].constraints[str(i) + "_Copy Transforms form MCH-FK pole"].subtarget = mch_fk_poles_list[i]
            
            #last constraint has the 50% influence
            if len(bones[fk_pole_bone].constraints) > 1:
                bones[fk_pole_bone].constraints[-1].influence = 0.5
            else:
                bones[fk_pole_bone].constraints[-1].influence = 1.0


###########################################
### CUSTOM PROPERTIES AT IK TARGET BONE ###
###########################################
    parameter_bone = []
    
    if IK == True:
        parameter_bone = IKs_list[-1]
    else:
        parameter_bone = FKs_list[-1]
    
    if FK == True:
        create_property(parameter_bone, "fk_total_scale", 0.0, 1.0)
    
    if IK == True:
        create_property(parameter_bone, "ik_elbow_follow", 0.0, 1.0)
        if IK_s == True:
            create_property(parameter_bone, "ik_stretch", 0.0, 1.0)
        if FK == True:
            create_property(parameter_bone, "fk_ik", 0.0, 1.0)
    
    else:
        if tweaks == True:
            create_property(parameter_bone, "fk_total_scale", 0.0, 1.0)


###############
### DRIVERS ###
###############
    
    if IK == True:
        
        # Elbow follow driver
        driver = ob.driver_add('pose.bones["' + ik_pole_parent_bone + '"].constraints["Copy Transforms from IK target"].influence').driver
        driver.type = "AVERAGE"
        var = driver.variables.new()
        var.targets[0].id = ob
        var.targets[0].data_path = 'pose.bones["' + parameter_bone + '"]["ik_elbow_follow"]'
        
        if IK_s == True:
            
            # IK Stretch driver
            driver = ob.driver_add('pose.bones["' + IK_STRs_list[-2] + '"].constraints["Self IK"].influence').driver
            driver.type = "AVERAGE"
            var = driver.variables.new()
            var.targets[0].id = ob
            var.targets[0].data_path = 'pose.bones["' + parameter_bone + '"]["ik_stretch"]'
            
        if FK == True:
            
            # IK-FK switch driver
            for bone in bones:
                if bone.name in INTs_list:
                    driver = ob.driver_add('pose.bones["' + bone.name + '"].constraints["Copy Transforms IK"].influence').driver
                    driver.type = "AVERAGE"
                    var = driver.variables.new()
                    var.targets[0].id = ob
                    var.targets[0].data_path = 'pose.bones["' + parameter_bone + '"]["fk_ik"]'

            if tweaks == True:
                
                # All axis FK scale driver
                for bone in bones:
                    if bone.name in tweak_parents_list[:-1]:
                        driver = ob.driver_add('pose.bones["' + bone.name + '"].constraints["Copy Scale from FK"].influence').driver
                        driver.type = "SCRIPTED"
                        var = driver.variables.new()
                        var.type= "SINGLE_PROP"
                        var.name = "scale"
                        var.targets[0].id = ob
                        var.targets[0].data_path = 'pose.bones["' + parameter_bone + '"]["fk_total_scale"]'
                        var2 = driver.variables.new()
                        var2.type= "SINGLE_PROP"
                        var2.name = "fkik"
                        var2.targets[0].id = ob
                        var2.targets[0].data_path = 'pose.bones["' + parameter_bone + '"]["fk_ik"]'
                        driver.expression = "scale * (1 - fkik)"
        
    else:
        
        if tweaks == True:
                
            # All axis FK scale driver
            for bone in bones:
                if bone.name in tweak_parents_list[:-1]:
                    driver = ob.driver_add('pose.bones["' + bone.name + '"].constraints["Copy Scale from FK"].influence').driver
                    driver.type = "AVERAGE"
                    var = driver.variables.new()
                    var.targets[0].id = ob
                    var.targets[0].data_path = 'pose.bones["' + parameter_bone + '"]["fk_total_scale"]'

    if FK == True:
        
        # FK "hand" scale inheritance driver
        driver = ob.driver_add('pose.bones["' + mch_fk_bone + '"].constraints["Copy Scale from FK Lower"].influence').driver
        driver.type = "AVERAGE"
        var = driver.variables.new()
        var.targets[0].id = ob
        var.targets[0].data_path = 'pose.bones["' + parameter_bone + '"]["fk_total_scale"]'
    

##############
### SHAPES ###
##############

    for bone in bpy.context.scene.objects[armature_name].pose.bones:
        if "INT." in bone.name:
            bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
            bone.custom_shape = shapesCreateINT()
            
            for obj in bpy.data.objects:
                if obj == bone.custom_shape:
                    obj.name = obj.name.split(".", 1)[0] + "." + bone.name

    if len(FKs_list) > 0:
        
        for bone in bpy.context.scene.objects[armature_name].pose.bones:
           if bone.name in FKs_list:
               bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
               bone.custom_shape = shapesCreateFK()
               
               for obj in bpy.data.objects:
                    if obj == bone.custom_shape:
                        obj.name = obj.name.split(".", 1)[0] + "." + bone.name
    
    if len(IKs_list) > 0:
        
        for bone in bpy.context.scene.objects[armature_name].pose.bones:
           if bone.name in IKs_list[:-1]:
               bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
               bone.custom_shape = shapesCreateIKadd()
               
               for obj in bpy.data.objects:
                    if obj == bone.custom_shape:
                        obj.name = obj.name.split(".", 1)[0] + "." + bone.name
        
        for bone in bpy.context.scene.objects[armature_name].pose.bones:
           if bone.name == IKs_list[-1]:
               bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
               bone.custom_shape = shapesCreateIKmain()
               
               for obj in bpy.data.objects:
                    if obj == bone.custom_shape:
                        obj.name = obj.name.split(".", 1)[0] + "." + bone.name
    
    if len(IK_STRs_list) > 0:
        
        for bone in bpy.context.scene.objects[armature_name].pose.bones:
           if bone.name in IK_STRs_list:
               bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
               bone.custom_shape = shapesCreateIKstr()
               
               for obj in bpy.data.objects:
                    if obj == bone.custom_shape:
                        obj.name = obj.name.split(".", 1)[0] + "." + bone.name
    
    if len(tweaks_list) > 0:
        
        for bone in bpy.context.scene.objects[armature_name].pose.bones:
           if bone.name in tweaks_list:
               bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
               bone.custom_shape = shapesCreateTweaks()
               
               for obj in bpy.data.objects:
                   if obj == bone.custom_shape:
                       obj.name = obj.name.split(".", 1)[0] + "." + bone.name
    
    for bone in bpy.context.scene.objects[armature_name].pose.bones:
        if bone.name == "IK.pole":
            bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
            bone.custom_shape = shapesCreatePole()
            
            for obj in bpy.data.objects:
                if obj == bone.custom_shape:
                    obj.name = obj.name.split(".", 1)[0] + "." + bone.name
    
    for bone in bpy.context.scene.objects[armature_name].pose.bones:
        if ".parent" in bone.name: 
            bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
            bone.custom_shape = shapesCreateParents()
            
            for obj in bpy.data.objects:
                if obj == bone.custom_shape:
                    obj.name = obj.name.split(".", 1)[0] + "." + bone.name
        
        if FK == True:
            if bone.name == mch_fk_bone:
                bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
                bone.custom_shape = shapesCreateParents()
                
                for obj in bpy.data.objects:
                    if obj == bone.custom_shape:
                        obj.name = obj.name.split(".", 1)[0] + "." + bone.name
    
    for bone in bpy.context.scene.objects[armature_name].pose.bones:
        if ".parent" in bone.name and "pole" in bone.name:
            bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
            bone.custom_shape = shapesCreatePoleParents()
            
            for obj in bpy.data.objects:
                if obj == bone.custom_shape:
                    obj.name = obj.name.split(".", 1)[0] + "." + bone.name
    
    for bone in bpy.context.scene.objects[armature_name].pose.bones:
        if ".pole" in bone.name and "FK" in bone.name:
            bpy.data.objects[armature_name].data.bones[bone.name].show_wire = True
            bone.custom_shape = shapesCreatePoleFK()
            
            for obj in bpy.data.objects:
                if obj == bone.custom_shape:
                    obj.name = obj.name.split(".", 1)[0] + "." + bone.name


########### Parent each of Selected Objects to a Bone ###########

def bone_parents():
    parent = bpy.context.active_pose_bone.name

    bpy.ops.object.posemode_toggle()
    bpy.ops.object.mode_set(mode='OBJECT')

    armature = bpy.context.active_object
    print(armature)
    print(armature.name)

    obs = [ob.name for ob in bpy.context.selected_objects if ob.type!='ARMATURE']
    print(obs)


    bpy.ops.object.select_all(action='DESELECT')


    for ob in bpy.context.scene.objects:
        if ob.name in obs:
            ob.select_set(True)
            bpy.context.scene.cursor.location = ob.location
            bpy.ops.object.select_all(action='DESELECT')
            armature.select_set(True)
            bpy.context.view_layer.objects.active = armature        
            ob.select_set(False)
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.armature.bone_primitive_add(name = ob.name)
    #          bpy.ops.object.mode_set(mode='POSE')
            bpy.context.object.data.edit_bones[ob.name].parent = bpy.context.object.data.edit_bones[parent]
            bpy.ops.object.mode_set(mode='OBJECT')
            ob.select_set(True)
    #        bpy.context.object.data.parent = parent
            bpy.ops.object.mode_set(mode='POSE')
            for b in bpy.context.active_object.data.bones:  
                if b.name == ob.name:
                    b.select = True  
                else:
                    b.select = False
            o=bpy.context.object
            b=o.data.bones[ob.name]
            bpy.context.active_object.data.bones.active = b 
            #bpy.ops.object.armature_add(enter_editmode=False)
            #bpy.context.active_object.name = "arm_" + ob.name
            
    #        bpy.ops.object.select_all(action='DESELECT')
            
            bpy.ops.object.parent_set(type='BONE', xmirror=False, keep_transform=False)
            bpy.ops.pose.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')

            bpy.ops.object.select_all(action='DESELECT')
            
            
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
            ob.driver_remove('hide_viewport')
            drv = ob.driver_add('hide_viewport')
            if is_cyclic == True:
                drv.modifiers.remove(drv.modifiers[0])
                drv.keyframe_points.add(count = 3)
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
                drv.keyframe_points.add(count = 3)
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
            ob.driver_remove('hide_viewport')
            bpy.data.objects[ob.name].hide_viewport = 0
            
            
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
                    ob.driver_remove('hide_viewport')
                    drv = ob.driver_add('hide_viewport')
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
    
    case: bpy.props.IntProperty()
    
    curve_hooks_count: bpy.props.IntProperty(
        name = "Spline Curves Counter",
        default = 0,
        min = 0,
        description = "Integer Property being used to divide spline chains"
        )
        
    curve_hooks_quantity: bpy.props.IntProperty(
        name = "Number of Hooks",
        default = 2,
        min = 2,
        description = "Number of Hooks determining the Bezier Points Location"
        )
    
    curve_hooks_subdivide: bpy.props.IntProperty(
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
            lc = bpy.context.scene.cursor.location
            for i in range(self.curve_hooks_quantity):
                bpy.ops.object.empty_add(type='PLAIN_AXES')
                bpy.context.object.name = str(count) + "_curve_hook_" + str(ns)
                bpy.context.object.location = bpy.context.scene.cursor.location
                ns += 1
                lc[0] += 1
            bpy.context.scene.cursor.location[0] -= bpy.data.scenes["Scene"].start_value
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
            bpy.context.scene.collection.objects.link(ob)
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = ob
            bpy.context.scene.objects[ob.name].select_set(True)
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
                bpy.context.view_layer.objects.active = obj2
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
            bpy.context.view_layer.objects.active = bpy.data.objects[str(bpy.context.scene.curve_hooks_count) + "_SplineCurve"]
            bpy.ops.object.mode_set(mode = "EDIT")
            k = 0
            for i in range(len(bpy.data.curves[bpy.context.active_object.data.name].splines[0].bezier_points)):
                bpy.ops.curve.select_all(action='SELECT')
                bpy.ops.object.hook_reset(modifier = (str(bpy.context.scene.curve_hooks_count) + "_curve_hook_" + str(k)))
                k += 1    
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            for obj in bpy.data.objects:
                if obj.name.startswith(str(bpy.context.scene.curve_hooks_count) + "_curve_hook_"):
                    bpy.context.scene.objects[obj.name].select_set(True)
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
    
    max_angle: bpy.props.FloatProperty(
        name = "Max Angle",
        default = 1,
        description = "Angle Limit"
        )
    name: bpy.props.StringProperty(
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
    
    name: bpy.props.StringProperty(
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
    
    case: bpy.props.IntProperty()
    
    name_sel: bpy.props.StringProperty(
        name = "Find Name",
        default = "Object",
        description = "Select objects whose name contains the specified characters"
        )
    
    name_source: bpy.props.StringProperty(
        name = "Source Name",
        default = "name_1",
        description = "Source part of the Object Name to be replaced"
        )
    
    name_target: bpy.props.StringProperty(
        name = "Target Name",
        default = "name_2",
        description = "Target part of the Object Name used to Replace"
        )
    
    prefix: bpy.props.StringProperty(
        name = "Prefix",
        default = "_",
        description = "Prefix to add before Object's base name"
        )
    
    suffix: bpy.props.StringProperty(
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
                        bpy.context.scene.objects[ob.name].select_set(True)
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
    
    base_name: bpy.props.StringProperty(
        name = "Base Name",
        default = "Object",
        description = "Base-name for the selected objects"
        )
        
    sep: bpy.props.StringProperty(
        name = "Separator",
        default = "_",
        description = "Separator between the base-name and integer value"
        )
    
    start_value: bpy.props.IntProperty(
        name = "Start Value",
        default = 0,
        description = "Value of the integer part of the name to start from",
        min = 0
        )      
        
    reverse: bpy.props.BoolProperty(
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
    
    case: bpy.props.IntProperty()
    
    driver_property: bpy.props.StringProperty(
        name = "Bone Custom Property",
        default = "stages",
        description = "Custom property of the bone being used as the drivers' target"
        )
        
    inc_zero: bpy.props.BoolProperty(
        name="Include Zero",
        description="Create Zero Stage",
        default = False
        )
        
    driver_property_existing: bpy.props.StringProperty(
        name = "Existing Bone Custom Property",
        default = "stages",
        description = "Existing custom property of the bone being used as the drivers' target"
        )
    
    starting_stage: bpy.props.IntProperty(
        name = "Starting Stage",
        default = 0,
        description = "Objects become visible starting this stage"
        ) 
    
    bone_name: bpy.props.StringProperty(
        name = "Bone Name",
        default = "Root",
        description = "Bone with custom property being used as the drivers' target"
        )
        
    is_cyclic: bpy.props.BoolProperty(
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


############################################
##### Add drivers to active material   #####
##### of selected object               #####
############################################


### EEVEE ###

class OBJECT_OT_add_material_drivers(bpy.types.Operator):
    """Add bone property based material driver"""
    bl_label = "Add bone property based material driver"
    bl_idname = "object.add_material_drivers"
    bl_option = {'REGISTER', 'UNDO'}
    
    def execute (self, context):
        
        for obj in bpy.context.selected_objects:
            
            if obj.type != "ARMATURE":
                ob = obj
                
            else:
                arm = obj
        
        
        # Create custom property for bone to set the driver path later
        arm.pose.bones[arm.data.bones.active.name][bpy.context.scene.mat_driver_property] = 0.0
        
        if "_RNA_UI" not in arm.pose.bones[arm.data.bones.active.name].keys():
            arm.pose.bones[arm.data.bones.active.name]["_RNA_UI"] = {}
            
        arm.pose.bones[arm.data.bones.active.name]["_RNA_UI"].update({bpy.context.scene.mat_driver_property: {"min":0.0, "max":float(bpy.context.scene.mat_colour_lines_number - 1), "soft_min":0.0, "soft_max":float(bpy.context.scene.mat_colour_lines_number - 1)}})

        
        # Create Material Driver (Eevee Emission Node)
        
        mat = ob.active_material
        node_tree = ob.active_material.node_tree
        
        if node_tree.animation_data is not None:
            if node_tree.animation_data.drivers is not None:
                for driver in node_tree.animation_data.drivers:
                    node_tree.animation_data.drivers.remove(driver)
    
        new_drv = node_tree.driver_add('nodes["Emission"].inputs[0].default_value')

        
        for ind in range (4): 
            
            for driver in node_tree.animation_data.drivers:
                if "Emission" in driver.data_path and driver.array_index == ind:
                    drv = driver
                    
            drv.modifiers.remove(drv.modifiers[0])
            
            drv.driver.type = 'SCRIPTED'
            drv.driver.expression = 'var'
                    
            drv.keyframe_points.add(count = bpy.context.scene.mat_colour_lines_number)
            
            co = []
            handles = []
            
            lines = []
            lines.append(bpy.context.scene.mat_colour_line_01)
            lines.append(bpy.context.scene.mat_colour_line_02)
            lines.append(bpy.context.scene.mat_colour_line_03)
            lines.append(bpy.context.scene.mat_colour_line_04)
            lines.append(bpy.context.scene.mat_colour_line_05)
            lines.append(bpy.context.scene.mat_colour_line_06)
            lines.append(bpy.context.scene.mat_colour_line_07)
            lines.append(bpy.context.scene.mat_colour_line_08)
            lines.append(bpy.context.scene.mat_colour_line_09)
            lines.append(bpy.context.scene.mat_colour_line_10)
            
            for i in range(bpy.context.scene.mat_colour_lines_number):
                co.append((float(i), float(lines[i].strip('][').split(', ')[ind])))
                handles.append((float(i), float(lines[i].strip('][').split(', ')[ind])))
    
            
            for i in range(bpy.context.scene.mat_colour_lines_number):
                drv.keyframe_points[i].co = co[i]
                drv.keyframe_points[i].interpolation ='LINEAR'
                drv.keyframe_points[i].handle_left_type = 'FREE'
                drv.keyframe_points[i].handle_right_type = 'FREE'
                drv.keyframe_points[i].handle_left = handles[i]
                drv.keyframe_points[i].handle_right = handles[i]
            
            
                
            var = drv.driver.variables.new()
            var.name='var'
            var.type='SINGLE_PROP'
            target = var.targets[0]
            target.id = arm 
            target.data_path = 'pose.bones["%s"]["%s"]' % (arm.data.bones.active.name, bpy.context.scene.mat_driver_property)
            
            drv.driver.type = 'AVERAGE'
            
            
            
        return {'FINISHED'}
    

### Grease Pencil ### 
   
class OBJECT_OT_add_material_drivers_gpencil(bpy.types.Operator):
    """Add bone property based material driver (Grease Pencil)"""
    bl_label = "Add bone property based material driver (Grease Pencil)"
    bl_idname = "object.add_material_drivers_gpencil"
    bl_option = {'REGISTER', 'UNDO'}
    
    def execute (self, context):
        
        for obj in bpy.context.selected_objects:
            
            if obj.type != "ARMATURE":
                ob = obj
                
            else:
                arm = obj
        
        
        # Create custom property for bone to set the driver path later
        arm.pose.bones[arm.data.bones.active.name][bpy.context.scene.mat_driver_property] = 0.0
        
        if "_RNA_UI" not in arm.pose.bones[arm.data.bones.active.name].keys():
            arm.pose.bones[arm.data.bones.active.name]["_RNA_UI"] = {}
            
        arm.pose.bones[arm.data.bones.active.name]["_RNA_UI"].update({bpy.context.scene.mat_driver_property: {"min":0.0, "max":float(bpy.context.scene.mat_colour_lines_number - 1), "soft_min":0.0, "soft_max":float(bpy.context.scene.mat_colour_lines_number - 1)}})

        
        # Create Material Driver (Grease Pencil Stroke & Fill)
        
        mat = ob.active_material
        
        if bpy.context.scene.is_grease_pencil_stroke is True:
            
            if mat.animation_data is not None:
                if mat.animation_data.drivers is not None:
                    for driver in mat.animation_data.drivers:
                        if driver.data_path == 'grease_pencil.color':
                            mat.animation_data.drivers.remove(driver)
    
            new_drv = mat.driver_add('grease_pencil.color')

            
            for ind in range (4): 
                
                for driver in mat.animation_data.drivers:
                    if "grease_pencil" in driver.data_path and driver.array_index == ind:
                        drv = driver
                        
                drv.modifiers.remove(drv.modifiers[0])
                
                drv.driver.type = 'SCRIPTED'
                drv.driver.expression = 'var'
                        
                drv.keyframe_points.add(count = bpy.context.scene.mat_colour_lines_number)
                
                co = []
                handles = []
                
                lines = []
                lines.append(bpy.context.scene.mat_colour_line_01)
                lines.append(bpy.context.scene.mat_colour_line_02)
                lines.append(bpy.context.scene.mat_colour_line_03)
                lines.append(bpy.context.scene.mat_colour_line_04)
                lines.append(bpy.context.scene.mat_colour_line_05)
                lines.append(bpy.context.scene.mat_colour_line_06)
                lines.append(bpy.context.scene.mat_colour_line_07)
                lines.append(bpy.context.scene.mat_colour_line_08)
                lines.append(bpy.context.scene.mat_colour_line_09)
                lines.append(bpy.context.scene.mat_colour_line_10)
                
                for i in range(bpy.context.scene.mat_colour_lines_number):
                    co.append((float(i), float(lines[i].strip('][').split(', ')[ind])))
                    handles.append((float(i), float(lines[i].strip('][').split(', ')[ind])))
        
                
                for i in range(bpy.context.scene.mat_colour_lines_number):
                    drv.keyframe_points[i].co = co[i]
                    drv.keyframe_points[i].interpolation ='LINEAR'
                    drv.keyframe_points[i].handle_left_type = 'FREE'
                    drv.keyframe_points[i].handle_right_type = 'FREE'
                    drv.keyframe_points[i].handle_left = handles[i]
                    drv.keyframe_points[i].handle_right = handles[i]
                
                
                    
                var = drv.driver.variables.new()
                var.name='var'
                var.type='SINGLE_PROP'
                target = var.targets[0]
                target.id = arm 
                target.data_path = 'pose.bones["%s"]["%s"]' % (arm.data.bones.active.name, bpy.context.scene.mat_driver_property)
                
                drv.driver.type = 'AVERAGE'
        
        if bpy.context.scene.is_grease_pencil_fill is True:
            
            if mat.animation_data is not None:
                if mat.animation_data.drivers is not None:
                    for driver in mat.animation_data.drivers:
                        if driver.data_path == 'grease_pencil.fill_color':
                            mat.animation_data.drivers.remove(driver)
    
            new_drv = mat.driver_add('grease_pencil.fill_color')

            
            for ind in range (4): 
                
                for driver in mat.animation_data.drivers:
                    if "grease_pencil" in driver.data_path and driver.array_index == ind:
                        drv = driver
                        
                drv.modifiers.remove(drv.modifiers[0])
                
                drv.driver.type = 'SCRIPTED'
                drv.driver.expression = 'var'
                        
                drv.keyframe_points.add(count = bpy.context.scene.mat_colour_lines_number)
                
                co = []
                handles = []
                
                lines = []
                lines.append(bpy.context.scene.mat_colour_line_01)
                lines.append(bpy.context.scene.mat_colour_line_02)
                lines.append(bpy.context.scene.mat_colour_line_03)
                lines.append(bpy.context.scene.mat_colour_line_04)
                lines.append(bpy.context.scene.mat_colour_line_05)
                lines.append(bpy.context.scene.mat_colour_line_06)
                lines.append(bpy.context.scene.mat_colour_line_07)
                lines.append(bpy.context.scene.mat_colour_line_08)
                lines.append(bpy.context.scene.mat_colour_line_09)
                lines.append(bpy.context.scene.mat_colour_line_10)
                
                for i in range(bpy.context.scene.mat_colour_lines_number):
                    co.append((float(i), float(lines[i].strip('][').split(', ')[ind])))
                    handles.append((float(i), float(lines[i].strip('][').split(', ')[ind])))
        
                
                for i in range(bpy.context.scene.mat_colour_lines_number):
                    drv.keyframe_points[i].co = co[i]
                    drv.keyframe_points[i].interpolation ='LINEAR'
                    drv.keyframe_points[i].handle_left_type = 'FREE'
                    drv.keyframe_points[i].handle_right_type = 'FREE'
                    drv.keyframe_points[i].handle_left = handles[i]
                    drv.keyframe_points[i].handle_right = handles[i]
                
                
                    
                var = drv.driver.variables.new()
                var.name='var'
                var.type='SINGLE_PROP'
                target = var.targets[0]
                target.id = arm 
                target.data_path = 'pose.bones["%s"]["%s"]' % (arm.data.bones.active.name, bpy.context.scene.mat_driver_property)
                
                drv.driver.type = 'AVERAGE'
            
            
            
        return {'FINISHED'}
               
        

########################################
##### Each of the selected objects #####
##### will be parented to its own  #####
##### bone. Such bones will be     #####
##### parented to active bone      #####
########################################

class OBJECT_OT_ob_bone_parenting(bpy.types.Operator):
    """Batch parenting of selected objects to created bones"""
    bl_label = "Parent selected objects to created bones"
    bl_idname = "object.bone_parenting"
    bl_option = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bone_parents()
            
        return {'FINISHED'}
    

########################################
##### Bones creating Class, that   #####
##### helps to create IK/FK/tweaks #####
##### chains from already created  #####
##### deforming bones (DEFs)       #####
########################################

class POSE_PT_rigging_chains_creating(bpy.types.Operator):
    """Create Bones Chains for Limbs Rigging"""
    bl_label = "Create Bones Chains for Limbs Rigging"
    bl_idname = "pose.rigging_chains_creating"
    bl_option = {'REGISTER', 'UNDO'}
        
    def execute(self, context):
        
        makeChains(FK = bpy.context.scene.create_FK, IK = bpy.context.scene.create_IK, IK_s = bpy.context.scene.create_IK_stretch, tweaks = bpy.context.scene.create_tweaks)
            
        return {'FINISHED'}
    

########################################
##### Recalculating IK pole degree #####
########################################

class POSE_PT_recalculating_IK_pole_degree(bpy.types.Operator):
    """Recalculating IK pole degree"""
    bl_label = "Recalculating IK pole degree"
    bl_idname = "pose.recalculating_ik_pole_degree"
    bl_option = {'REGISTER', 'UNDO'}
        
    def execute(self, context):
        
        ob = bpy.context.active_object
        bones = ob.pose.bones
        
        #Getting the IK chains lists
        bpy.ops.object.mode_set(mode='POSE')
        
        for bone in bpy.context.selected_pose_bones:
            for con in bone.constraints:
                if con.type == "IK":
                    pole_bone_name = con.pole_subtarget
                    pole_bone = bones[pole_bone_name]
                    ik_bone_name = con.subtarget
                    ik_bone = bones[ik_bone_name]
                    m = con.chain_count
    
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='DESELECT')
        for bone in bpy.context.object.data.edit_bones:
            if bone.name == ik_bone:
                bone.select = True
                bone.select_tail = True
                bone.select_head = True
                bpy.context.object.data.edit_bones.active = bpy.context.object.data.edit_bones[bone.name] 
        for i in range(m-1):
            bpy.ops.armature.select_hierarchy(direction='PARENT')
        base_bone_name = bpy.context.object.data.edit_bones.active.name
        base_bone = bones[base_bone_name]
        bpy.ops.object.mode_set(mode='POSE')
    
        pole_angle_in_radians = get_pole_angle(base_bone,
                                               ik_bone,
                                               pole_bone.matrix.translation)
        
        pole_angle_in_deg = round(180*pole_angle_in_radians/3.141592, 3)
        print(pole_angle_in_deg)
        
        bpy.ops.object.mode_set(mode='POSE')
        # Setting the IK Constraint with the evaluated pole angle
        for bone in bones:
            for con in bone.constraints:
                if con.type == "IK":
                    con.pole_angle = pole_angle_in_deg


        return {'FINISHED'}

####################################
############# PANELS ###############
####################################

class misc_tools_panel_spline(bpy.types.Panel):
    bl_label = "Spline IK"
    bl_idname = "OBJECT_PT_miscellaneous_tools_spline_ik"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
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
    bl_region_type = "UI"
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
    bl_region_type = "UI"
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
    bl_region_type = "UI"
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
    bl_region_type = "UI"
    bl_category = "Misc Tools"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()
        row = box.row()
        row.label(text="Add Drivers (Objects Visibility)", icon = "RESTRICT_VIEW_ON")
        
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
        
        box = layout.box()
        row = box.row()
        row.label(text="Add Material Drivers", icon = "MATERIAL")
        row = box.row()
        row.label(text = "Name of Bone Property")
        row = box.row()
        row.prop(context.scene, "mat_driver_property", text = "")
        row = box.row()
        row.label(text = "Material Driver Points Amount")
        row = box.row()
        row.prop(context.scene, "mat_colour_lines_number", text = "")
        
        for i in range(bpy.context.scene.mat_colour_lines_number):
            if i != 10:
                row = box.row()
                row.prop(context.scene, ("mat_colour_line_0" + str(i+1)), text = "")
            else:
                row = box.row()
                row.prop(context.scene, "mat_colour_line_10", text = "")
        
        row = box.row()
        row.prop(context.scene, "is_grease_pencil", text = "Grease Pencil", icon = "OUTLINER_OB_GREASEPENCIL", toggle = True)
        if bpy.context.scene.is_grease_pencil is True:
            row = box.row()
            row.prop(context.scene, "is_grease_pencil_stroke", text = "Stroke", toggle = True)
            row.prop(context.scene, "is_grease_pencil_fill", text = "Fill", toggle = True)
        
        row = box.row()
        if bpy.context.scene.is_grease_pencil is False:
            row.operator(OBJECT_OT_add_material_drivers.bl_idname, text = 'Set Driver', icon = "DRIVER")
        else:
            row.operator(OBJECT_OT_add_material_drivers_gpencil.bl_idname, text = 'Set Driver', icon = "DRIVER")
        
        
class misc_tools_panel_parenting(bpy.types.Panel):
    bl_label = "Parenting"
    bl_idname = "OBJECT_PT_miscellaneous_tools_parenting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Misc Tools"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        col = layout.column()
        col.operator(OBJECT_OT_ob_bone_parenting.bl_idname, text = 'Parent to Bones', icon = "BONE_DATA")
        
class misc_tools_rigging_chains_creating(bpy.types.Panel):
    bl_label = "Chains Creating"
    bl_idname = "POSE_PT_miscellaneous_tools_rigging_chains_creating"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Misc Tools"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        col = layout.column()
        row = col.row()
        row.prop(context.scene, "create_FK", text ="FK", icon = "DECORATE_DRIVER", toggle = True)
        row.prop(context.scene, "create_IK", text ="IK", icon = "CON_KINEMATIC", toggle = True)
        
        if bpy.context.scene.create_FK == False and bpy.context.scene.create_IK == False:
            row = col.row()
            row.label(text = "Select at least one chain type", icon = "ERROR")
        
        else:
            row = col.row()
            row.label(text = "Additional bones")
            row = col.row()
            row.prop(context.scene, "create_tweaks", text = "Tweaks", icon = "TRACKER", toggle = True)
            
            if bpy.context.scene.create_IK == True:
                row.prop(context.scene, "create_IK_stretch", text ="Stretchy IK", icon = "CON_STRETCHTO", toggle = True)
            
            if bpy.context.selected_pose_bones is None or len(bpy.context.selected_pose_bones) == 0:
                row = col.row()
                row.label(text = "Select deforming Bones!", icon = "ERROR")
            
            else:
                l = []
                m = []
                e = True
                e2 = False
                for bone in bpy.context.selected_pose_bones:
                    l.append(bone.name)
                    if bone.name.startswith("IK"):
                        m.append(bone.name)
                for item in l:
                    if "DEF" not in item:
                        e = False
                if len(m) > 0:
                    e2 = True
                        
                if e == True:
                    row = col.row()
                    cr = row.operator(POSE_PT_rigging_chains_creating.bl_idname, text = 'Create Rigging Chains', icon = "ARMATURE_DATA")
                
                else:
                    row = col.row()
                    row.label(text = "Check DEFs naming!", icon = "ERROR")
         
         
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
                ('selected','Selected Only','Run naming only for Selected Objects / Bones','RESTRICT_SELECT_OFF',0),
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

classes = (
    OBJECT_OT_add_curve_hooks,
    OBJECT_OT_convert_and_limited_dissolve,
    OBJECT_OT_convert_and_beautify,
    OBJECT_OT_select_namesakes,
    OBJECT_OT_batch_names,
    OBJECT_OT_add_custom_drivers,
    OBJECT_OT_add_material_drivers,
    OBJECT_OT_ob_bone_parenting,
    POSE_PT_rigging_chains_creating,
    POSE_PT_recalculating_IK_pole_degree,
    OBJECT_OT_add_material_drivers_gpencil,
    misc_tools_panel_spline,
    misc_tools_panel_convert_curves,
    misc_tools_panel_naming,
    misc_tools_panel_batch_rename,
    misc_tools_panel_drivers,
    misc_tools_panel_parenting,
    misc_tools_rigging_chains_creating
)

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
    
    bpy.types.Scene.create_FK = bpy.props.BoolProperty(
        name="Create FK",
        description="Create Forward Kinematics Bones Chain",
        default = False
        )
    
    bpy.types.Scene.create_IK = bpy.props.BoolProperty(
        name="Create FK",
        description="Create Inverse Kinematics Bones Chain",
        default = False
        )
    
    bpy.types.Scene.create_IK_stretch = bpy.props.BoolProperty(
        name="Create stretchy IK",
        description="Create Inverse Kinematics Bones Chain with Stretching Parameter",
        default = False
        )
    
    bpy.types.Scene.create_tweaks = bpy.props.BoolProperty(
        name="Create Tweaks",
        description="Create additional Tweaks for deforming Bones",
        default = False
        )
        
    bpy.types.Scene.mat_colour_line_01 = bpy.props.StringProperty(
        name = "Material Colour #1",
        default = "",
        description = "Material Colour #1"
        )
    
    bpy.types.Scene.mat_colour_line_02 = bpy.props.StringProperty(
        name = "Material Colour #2",
        default = "",
        description = "Material Colour #2"
        )
    
    bpy.types.Scene.mat_colour_line_03 = bpy.props.StringProperty(
        name = "Material Colour #3",
        default = "",
        description = "Material Colour #3"
        )
        
    bpy.types.Scene.mat_colour_line_04 = bpy.props.StringProperty(
        name = "Material Colour #4",
        default = "",
        description = "Material Colour #4"
        )
        
    bpy.types.Scene.mat_colour_line_05 = bpy.props.StringProperty(
        name = "Material Colour #5",
        default = "",
        description = "Material Colour #5"
        )
        
    bpy.types.Scene.mat_colour_line_06 = bpy.props.StringProperty(
        name = "Material Colour #6",
        default = "",
        description = "Material Colour #6"
        )
        
    bpy.types.Scene.mat_colour_line_07 = bpy.props.StringProperty(
        name = "Material Colour #7",
        default = "",
        description = "Material Colour #7"
        )
        
    bpy.types.Scene.mat_colour_line_08 = bpy.props.StringProperty(
        name = "Material Colour #8",
        default = "",
        description = "Material Colour #8"
        )
        
    bpy.types.Scene.mat_colour_line_09 = bpy.props.StringProperty(
        name = "Material Colour #9",
        default = "",
        description = "Material Colour #9"
        )
        
    bpy.types.Scene.mat_colour_line_10 = bpy.props.StringProperty(
        name = "Material Colour #10",
        default = "",
        description = "Material Colour #10"
        )
        
    bpy.types.Scene.mat_colour_lines_number = bpy.props.IntProperty(
        name = "Amount of colour points",
        default = 2,
        min = 2,
        max = 10,
        description = "Amount of colour points"
        )
        
    bpy.types.Scene.mat_driver_property = bpy.props.StringProperty(
        name = "Bone Custom Property",
        default = "night_mode",
        description = "Bone Custom Property for Material Driver"
        )
    
    bpy.types.Scene.is_grease_pencil = bpy.props.BoolProperty(
        name="Object type is Grease Pencil",
        description="Object type is Grease Pencil",
        default = False
        )
    
    bpy.types.Scene.is_grease_pencil_stroke = bpy.props.BoolProperty(
        name="Grease Pencil uses Stroke",
        description="Grease Pencil uses Stroke",
        default = False
        )
    
    bpy.types.Scene.is_grease_pencil_fill = bpy.props.BoolProperty(
        name="Grease Pencil uses Fill",
        description="Grease Pencil uses Fill",
        default = False
        )
                
    from bpy.utils import register_class
    
    for cls in classes:
        register_class(cls)


########## UNREGISTER ##########
    
def unregister():
    
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
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
    del bpy.types.Scene.create_FK
    del bpy.types.Scene.create_IK
    del bpy.types.Scene.create_IK_stretch
    del bpy.types.Scene.create_tweaks
    del bpy.types.Scene.mat_colour_line_01
    del bpy.types.Scene.mat_colour_line_02
    del bpy.types.Scene.mat_colour_line_03
    del bpy.types.Scene.mat_colour_line_04
    del bpy.types.Scene.mat_colour_line_05
    del bpy.types.Scene.mat_colour_line_06
    del bpy.types.Scene.mat_colour_line_07
    del bpy.types.Scene.mat_colour_line_08
    del bpy.types.Scene.mat_colour_line_09
    del bpy.types.Scene.mat_colour_line_10
    del bpy.types.Scene.mat_colour_lines_number
    del bpy.types.Scene.is_grease_pencil
    del bpy.types.Scene.is_grease_pencil_stroke
    del bpy.types.Scene.is_grease_pencil_fill
    
if __name__ == "__main__":
    register()