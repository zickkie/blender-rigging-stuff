import bpy

for obj in bpy.data.objects:
    if obj.type == "MESH" or obj.type == "ARMATURE":
        if obj.animation_data is not None:
            for driver in obj.animation_data.drivers:
                if "brow_mustache" in driver.data_path:
                    driver.data_path = driver.data_path.replace("brow_mustache", "mustaches_upper")
                for var in driver.driver.variables:
                    if "brow_mustache" in var.name:
                        var.name = var.name.replace("brow_mustache", "mustaches_upper")
                    for tgt in var.targets:
                        if "brow_mustache" in tgt.data_path:
                            tgt.data_path = tgt.data_path.replace("brow_mustache", "mustaches_upper")
                    
        if obj.data is not None:
            if obj.data.animation_data is not None:
                for driver in obj.data.animation_data.drivers:
                    if "brow_mustache" in driver.data_path:
                        driver.data_path = driver.data_path.replace("brow_mustache", "mustaches_upper")
                    for var in driver.driver.variables:
                        if "brow_mustache" in var.name:
                            var.name = var.name.replace("brow_mustache", "mustaches_upper")
                        for tgt in var.targets:
                            if "brow_mustache" in tgt.data_path:
                                tgt.data_path = tgt.data_path.replace("brow_mustache", "mustaches_upper")
        
        
for obj in bpy.data.objects:
    if (obj.type == "MESH" or obj.type == "ARMATURE") and obj.animation_data is not None:
        for driver in obj.animation_data.drivers:
            driver.driver.expression += " "
            driver.driver.expression = driver.driver.expression[:-1]
                
    if obj.data is not None:
        if (obj.type == "MESH" or obj.type == "ARMATURE") and obj.data.animation_data is not None:
            for driver in obj.data.animation_data.drivers:
                driver.driver.expression += " "
                driver.driver.expression = driver.driver.expression[:-1]
        