import bpy
ob = bpy.context.active_object

for mod in ob.modifiers:
    if ".L" in mod.name:
        if mod.name.replace(".L", ".R") not in ob.modifiers:
            mir_mod = ob.modifiers.new(mod.name.replace(".L", ".R"), mod.type)
            mir_