import bpy

scene = bpy.context.scene
ob = bpy.data.objects["GEO_Cat_body"]
modifier = ob.modifiers["Phys_Body"]

override = {'scene': scene, 'active_object': ob, 'point_cache': modifier.point_cache}

bpy.ops.ptcache.bake(override, bake=True)
