import bpy

src_drv = "_L"
dst_drv = "_R"

ob = bpy.context.active_object
active = bpy.context.active_pose_bone
    
k = []
for item in active.keys():
    if item != "_RNA_UI" and src_drv in item and item.replace(src_drv, dst_drv) in active.keys():
        active[item.replace(src_drv, dst_drv)] = active[item]