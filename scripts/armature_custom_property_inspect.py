import bpy

active = bpy.context.active_object.pose.bones["Root"]
source = bpy.context.active_object.pose.bones["Root_BACKUP"]


for prop in active.keys():
    
    if prop in source and not prop.startswith("_RNA") and "rigify" not in prop:
        
        print(prop)
        
        if "description" in source['_RNA_UI'][prop].keys():
            tooltip = source["_RNA_UI"][prop]["description"]
        else:
            tooltip = ''
            
        if "default" in source['_RNA_UI'][prop].keys():
            default = source["_RNA_UI"][prop]["default"]
        else:
            default = source["_RNA_UI"][prop]["min"]
        
        active["_RNA_UI"].update({prop:{
        "min": source["_RNA_UI"][prop]["min"],
        "max": source["_RNA_UI"][prop]["max"],
        "soft_min": source["_RNA_UI"][prop]["soft_min"],
        "soft_max": source["_RNA_UI"][prop]["soft_max"],
        "description": tooltip,
        "default": default}})
        
        active.property_overridable_library_set('["' + prop + '"]', True)

for prop in active.keys():
    
    if not prop.startswith("_RNA") and "rigify" not in prop:
        
        print("--------" + prop)
        
        if "default" in active["_RNA_UI"][prop].keys():
        
            active[prop] = active["_RNA_UI"][prop]["default"]