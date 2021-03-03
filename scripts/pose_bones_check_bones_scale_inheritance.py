import bpy

ob = bpy.context.active_object
bones = ob.pose.bones
root = bones["Root"]
treshold = 0.9999
channel = 1
bones_list = []

for bone in bones:
    scale = bone.matrix_channel.to_scale()[channel]
    if scale < (root.scale[channel] * treshold) or scale > (root.scale[channel] / treshold):
        bones_list.append(bone.name)
    
print(f"Found {str(len(bones_list))} bones with wrong scale inheritance:")
for item in bones_list:
    print(item)