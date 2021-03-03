import bpy

list = []
for bone in bpy.context.selected_pose_bones:
    list.append(bone.name)
list.sort()
print(list)
print('------------')
