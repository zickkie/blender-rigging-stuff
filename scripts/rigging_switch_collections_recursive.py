import bpy
view_layer = bpy.context.view_layer

def switch_colls(coll, levels=100):
    
    def parent_coll(collection):
        for parent_collection in bpy.data.collections:
            if collection.name in parent_collection.children.keys():
              return parent_collection.name
      
    def recurse_Lights_normal(coll, parent, depth):
        if coll.name == "Lights_normal":
            coll.exclude = True
            return
        else:
            for child in coll.children:
                if child.name == "Lights_normal":
                    child.exclude = True
                    return
                else:
                    recurse_Lights_normal(child, coll,  depth + 1)
    
    def recurse_Lights_flip(coll, parent, depth):
        if coll.name == "Lights_flip":
            coll.exclude = False
            return
        else:
            for child in coll.children:
                if child.name == "Lights_flip":
                    child.exclude = False
                    return
                else:
                    recurse_Lights_flip(child, coll,  depth + 1)
    
    recurse_Lights_normal(coll, parent_coll(coll), 0)
    recurse_Lights_flip(coll, parent_coll(coll), 0)


root_colls = (coll for coll in view_layer.layer_collection.children)
for coll in root_colls:
    switch_colls(coll)