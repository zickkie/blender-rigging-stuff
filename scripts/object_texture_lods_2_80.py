bl_info = {
    "name": "Texture LODs",
    "author": "Arthur Shapiro",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools",
    "description": "Create duplicates of the selected objects that use materials with compressed textures",
    "warning": "",
    "wiki_url": "https://youtu.be/EtPCkogG-I4",
    "category": "Rigging",
    }


import bpy



# Function for Cycles / Eevee
def cycles_lod():
    
    char = ["_"] # list to collect all the Armatures whose children' materials don't
                 # need the low-res duplicates
    high = []
    low = []
    mats = []
    mats_low = []

    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":
            
            if obj.parent is None:
                high.append(obj.name)
                if obj.active_material.name not in mats:
                    mats.append(obj.active_material.name)
            
            elif obj.parent.name not in char:
                high.append(obj.name)
                if obj.active_material.name not in mats:
                    mats.append(obj.active_material.name)
    
    for m in mats:
        
        mat = bpy.data.materials[m]
        
        mat_low = mat.copy()
        mat_low.name = mat.name + "_low"
        
        #tex_low = mat.texture_slots[0].texture.copy()
        #tex_low.name = mat.texture_slots[0].texture.name + "_low"
        
        for n in mat.node_tree.nodes:
            if n.type == "TEX_IMAGE" and n.outputs[1].links[0].to_node.type == "MIX_SHADER":
                im_high = n
                
        im_low = im_high.image.copy()
        print(im_low.name)
        im_low.name = im_high.image.name.split(".png")[0] + "_low.png"
        
        filepath_low = im_high.image.filepath.split("textures")[0] + "textures\\low\\" + im_high.image.filepath.split("textures")[1].split(".png")[0] + "_low" + ".png"
        
        im_low.filepath = filepath_low
        #tex_low.image = im_low
        #mat_low.texture_slots[0].texture = tex_low
        
        mats_low.append(mat_low.name)
        
            
    bpy.ops.object.select_all(action='DESELECT')

    for i in range(len(high)):
        bpy.data.objects[high[i]].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[high[i]]
        
        if (bpy.context.active_object.name + "_low") not in low:
        
            bpy.ops.object.duplicate()
            ob = bpy.context.active_object
            ob.name = high[i] + "_low"  
                    
            ob.active_material = bpy.data.materials[bpy.data.objects[high[i]].active_material.name + "_low"]
            nodes = ob.active_material.node_tree.nodes
            
            im_high = nodes.get("Image Texture")
            
            k = 0
            for n in nodes:
                if n.type == "MIX_SHADER":
                    k += 1
                
            if  k > 1:
                for n in nodes:
                    if "Mix Shader" in n.name and n.inputs[0].links[0].from_node == im_high:
                        mix = n
                    else:
                        mix = nodes.get("Mix Shader.001")
            else:
                mix = nodes.get("Mix Shader")
            
            #nodes.remove(im_high)
            
            if nodes.get("Diffuse BSDF") is not None:
                diffuse = nodes.get("Diffuse BSDF")
            else:
                diffuse = nodes.get("Transparent BSDF")
                
            emission = nodes.get("Emission")
            
            if nodes.get("Image Texture LOW") is None:
                imt_low = nodes.new(type = "ShaderNodeTexImage")
                imt_low.name = "Image Texture LOW"
                imt_low.location = -400, 500

            imt_low = nodes.get("Image Texture LOW")
            
            for nn in bpy.data.objects[high[i]].material_slots[0].material.node_tree.nodes:
                if nn.type == "TEX_IMAGE" and nn.outputs[1].links[0].to_node.type == "MIX_SHADER":
                    imt_high = nn
                
            imt_low.image = bpy.data.images[imt_high.image.name.split(".png")[0] + "_low.png"]
            #bpy.data.images[bpy.data.objects[high[i]].active_material.node_tree.nodes.get(bpy.data.objects[high[i]].active_material.name + " Texture").image.name.split(".png")[0] + "_low.png"]

            links = ob.active_material.node_tree.links
            link_low_1 = links.new(imt_low.outputs[0], diffuse.inputs[0])
            link_low_2 = links.new(imt_low.outputs[0], emission.inputs[0])
            link_low_3 = links.new(imt_low.outputs[1], mix.inputs[0])
            
            for node in nodes:
                if node.type == "TEX_IMAGE" and (len(node.outputs[0].links) + len(node.outputs[1].links)) == 0:
                    nodes.remove(node)

            low.append(ob.name)

            bpy.ops.object.select_all(action='DESELECT')
            
    for ob in bpy.data.objects:
        if ob.name in high:
            ob.hide_viewport = True
        elif ob.name in low:
            ob.hide_render = True


class OBJECT_OT_texture_lods(bpy.types.Operator):
    """Create duplicates that use materials with compressed textures"""
    bl_idname = "mesh.texture_lods"
    bl_label = "Make Texture LODs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.scene.render.engine == "BLENDER_RENDER":
            internal_lod()
        
        elif bpy.context.scene.render.engine == "CYCLES":
            cycles_lod()
            
        return {'FINISHED'}
    
    
class OBJECT_OT_create_shadeless_material(bpy.types.Operator):
    """Create shadeless material (Simple Diffuse or Textured) for Cycles Render"""
    bl_idname = "mesh.create_shadeless_material"
    bl_label = "Create Shadeless Material (Diffuse/Textured"
    bl_options = {'REGISTER', 'UNDO'}
    
    case = bpy.props.IntProperty()

    def execute(self, context):

        if self.case == 1:
            
            m = []
            for ob in bpy.context.selected_objects:
                if ob.type == "MESH" or ob.type == "CURVE":
                    for mat in ob.data.materials:
                        if mat.name not in m:
                            
                            mat.use_nodes = True
                            nodes = mat.node_tree.nodes
                            
                            diffuse = nodes.get("Principled BSDF")
                            
                            output = nodes.get("Material Output")
                            output.location = 500, 500
                            
                            emission = nodes.new(type = "ShaderNodeEmission")
                            emission.location = 0, 100
                            
                            light_path = nodes.new(type = "ShaderNodeLightPath")
                            light_path.location = -400, 700
                            
                            RGB = nodes.new(type = "ShaderNodeRGB")
                            RGB.location = -400, 200
                            RGB.outputs[0].default_value = diffuse.inputs[0].default_value
                            
                            MIX = nodes.new(type = "ShaderNodeMixShader")
                            MIX.location = 250, 400
                            
                            links = mat.node_tree.links
                            link1 = links.new(emission.outputs[0], MIX.inputs[2])
                            link2 = links.new(diffuse.outputs[0], MIX.inputs[1])
                            link3 = links.new(light_path.outputs[0], MIX.inputs[0])
                            lnk4 = links.new(RGB.outputs[0], diffuse.inputs[0])
                            lnk5 = links.new(RGB.outputs[0], emission.inputs[0])
                            link_mat = links.new(MIX.outputs[0], output.inputs[0])
                            
                            m.append(mat.name)
        
        elif self.case == 2:
            
            l = []
            for ob in bpy.context.selected_objects:
                if ob.type == "MESH" or ob.type == "CURVE":
                    for mat in ob.data.materials:
                        if mat.name not in l:
                            
                            mat.use_nodes = True
                            nodes = mat.node_tree.nodes
                            
                            diffuse = nodes.get("Principled BSDF")
                            
                            output = nodes.get("Material Output")
                            output.location = 700, 500
                            
                            emission = nodes.new(type = "ShaderNodeEmission")
                            emission.location = 0, 100
                            
                            transp = nodes.new(type = "ShaderNodeBsdfTransparent")
                            transp.location = 300, 400
                            for i in range(3):
                                transp.inputs[0].default_value[i] = 1.0
                            transp.inputs[0].default_value[3] = 1.0
                            
                            light_path = nodes.new(type = "ShaderNodeLightPath")
                            light_path.location = 0, 450
                            light_path.hide = True
                            
                            texture = nodes.new(type = "ShaderNodeTexImage")
                            texture.location = -250, 600
                            texture.name = mat.name + " Texture"
                            
                            
                            MIX_color = nodes.new(type = "ShaderNodeMixShader")
                            MIX_color.location = 300, 300
                            
                            MIX_alpha = nodes.new(type = "ShaderNodeMixShader")
                            MIX_alpha.location = 500, 500
                            
                            links = mat.node_tree.links
                            link1 = links.new(diffuse.outputs[0],MIX_color.inputs[1])
                            link2 = links.new(emission.outputs[0],MIX_color.inputs[2])
                            link3 = links.new(texture.outputs[0],diffuse.inputs[0])
                            link4 = links.new(texture.outputs[0],emission.inputs[0])
                            link5 = links.new(light_path.outputs[0],MIX_color.inputs[0])
                            link5 = links.new(texture.outputs[1],MIX_alpha.inputs[0])
                            link6 = links.new(transp.outputs[0],MIX_alpha.inputs[1])
                            link7 = links.new(MIX_color.outputs[0],MIX_alpha.inputs[2])
                            
                            link_mat = links.new(MIX_alpha.outputs[0], output.inputs[0])
                            
                            l.append(mat.name)
            
        elif self.case == 3:
            
            l = []
            for ob in bpy.context.selected_objects:
                if ob.type == "MESH" or ob.type == "CURVE":
                    for mat in ob.data.materials:
                        if mat.name not in l:
                            
                            mat.use_nodes = True
                            nodes = mat.node_tree.nodes
                            
                            diffuse = nodes.get("Principled BSDF")
                            for i in range(3):
                                diffuse.inputs[0].default_value[i] = mat.diffuse_color[i]
                            
                            output = nodes.get("Material Output")
                            
                            emission = nodes.new(type = "ShaderNodeEmission")
                            emission.location = 0, 100
                            
                            for i in range(3):
                                emission.inputs[0].default_value[i] = diffuse.inputs[0].default_value[i]
                            
                            
                            links = mat.node_tree.links
                            link_mat = links.new(emission.outputs[0],output.inputs[0])
                            
                            for node in nodes:
                                if node.type == "BSDF_PRINCIPLED":
                                    nodes.remove(node)

                            
                            l.append(mat.name)
            
        return {'FINISHED'}


class texture_lods_panel(bpy.types.Panel):
    bl_label = "Texture LODs"
    bl_idname = "OBJECT_OT_texture_lods_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Texture LODs"
    
    @classmethod
    def poll(cls, context):
        return context.object and context.mode == "OBJECT"
    
    def draw (self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()
        box.operator(OBJECT_OT_texture_lods.bl_idname, text = 'Create LODs', icon = "OUTLINER_OB_IMAGE")
        
        box = layout.box()
        row = box.row()
        row.label(text = "Create Shadeless Material", icon = "SHADING_SOLID")
        row = box.row()
        row.label(text = "Cycles (Light Path)", icon = "EVENT_C")
        row = box.row()
        row.prop(context.scene, "mat_enum", expand = True)
        row = box.row()
        sh_mat = row.operator(OBJECT_OT_create_shadeless_material.bl_idname, text = 'Create Cycles', icon = "MATERIAL")
        if bpy.context.scene.mat_enum == "Diffuse":
            sh_mat.case = 1
        else:
            sh_mat.case = 2
        
        row = box.row()
        row.label(text = "Eevee (simple Emission)", icon = "EVENT_E")
    
        row = box.row()
        row.prop(context.scene, "eevee_mat_enum", expand = True)
        if bpy.context.scene.eevee_mat_enum == "Diffuse":
            row = box.row()
            eevee_sh_mat = row.operator(OBJECT_OT_create_shadeless_material.bl_idname, text = 'Create Eevee', icon = "MATERIAL")
            eevee_sh_mat.case = 3
        else:
            row = box.row()
            row.label(text = "Not done yet!")
        


shadeless_material_items = [
                ('Diffuse','Diffuse','Make Diffuse-only shadeless Material',0),
                ('Textured','Textured','Make Textured shadeless Material',1)
                ]

eevee_shadeless_material_items = [
                ('Diffuse','Diffuse','Make Diffuse-only shadeless Material',0),
                ('Textured','Textured','Make Textured shadeless Material',1)
                ]

classes = (
    OBJECT_OT_texture_lods,
    OBJECT_OT_create_shadeless_material,
    texture_lods_panel,
)                

def register():
    
    bpy.types.Scene.mat_enum = bpy.props.EnumProperty(
        items = shadeless_material_items,
        name = "Material Type",
        default = "Diffuse",
        description = "Created Material type"
    )
    
    bpy.types.Scene.eevee_mat_enum = bpy.props.EnumProperty(
        items = eevee_shadeless_material_items,
        name = "Eevee Material Type",
        default = "Diffuse",
        description = "Created Eevee Material type"
    )
    
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    

def unregister():
    
    del bpy.types.Scene.mat_enum
    del bpy.types.Scene.eevee_mat_enum
    
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()