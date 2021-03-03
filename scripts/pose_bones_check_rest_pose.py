import bpy
print('=======\n=======\n=======\n=======\n=======')
bones = bpy.context.active_object.pose.bones
count = 0
for bone in bones:
    for i in range(2):
        if bone.matrix_channel.to_translation()[i] > 0.001 or bone.matrix_channel.to_translation()[i] < -0.001:
            print(bone.name, "location", str(i), str(bone.matrix_channel.to_translation()[i]))
            count += 1
        elif bone.matrix_channel.to_euler()[i] > 0.001 or bone.matrix_channel.to_euler()[i] < -0.001:
            print(bone.name, "rotation", str(i), str(bone.matrix_channel.to_euler()[i]))
            count += 1
        elif bone.matrix_channel.to_scale()[i] > 1.001 or bone.matrix_channel.to_scale()[i] < 0.999:
            print(bone.name, "scale", str(i), str(bone.matrix_channel.to_scale()[i]))
            count += 1
        else:
            pass
if count == 0:
    print ("All is in rest")
else:
    print("Ofsset is found")