bl_info = {
    "name": "Material Slots Optimizer",
    "author": "Arthur Shapiro",
    "version": (1, 0),
    "blender": (2, 80, 0),
    'location': 'Properties -> Materials',
    "description": "Removes unused material slots from active MESH object without visual changes",
    "warning": "",
    "category": "Rigging"
}

import bpy


# FUNCTION
def cleanup():
    
    ob = bpy.context.active_object

    unique_colours = []
    unique_colours_indices = []
    indices_to_remove = []

        
    for i in range(len(ob.material_slots)):
        
        ob.active_material_index = i
        current_colour = []
        for k in range(4):
            current_colour.append(ob.active_material.node_tree.nodes["Emission"].inputs[0].default_value[k])
        
        
        if current_colour not in unique_colours:
            
            unique_colours.append(current_colour)
            unique_colours_indices.append(i)
        
        else:
            
            if i not in indices_to_remove:
                indices_to_remove.append(i)
            
            for poly in ob.data.polygons: 
                if poly.material_index == i:
                    print("was " + str(poly.material_index))
                    ind = unique_colours.index(current_colour)
                    poly.material_index = unique_colours_indices[ind]
                    print("becomes " + str(poly.material_index))


    for i in reversed(range(len(ob.material_slots))):
        
        ob.active_material_index = i
        
        if ob.active_material_index in indices_to_remove:
            bpy.ops.object.material_slot_remove()
            

# CLASS                
class OBJECT_OT_cleanup_materials(bpy.types.Operator):
    bl_label = 'Optimize material slots for this object'
    bl_idname = 'object.cleanup_materials'
    bl_description = 'Optimize material slots for this object'
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT" and context.active_object.type == "MESH"

    def execute(self, context):
        
        cleanup()
        
        self.report({'INFO'}, "Done!")

        return {'FINISHED'}
    

# DRAW FUNCTION
def cleanup_button_draw(self, context):
    
    layout = self.layout
    box = layout.box()
    row = box.row()
    row.label(text="Material slots: %s" % len(bpy.context.active_object.material_slots))
    row = box.row()
    row.operator('object.cleanup_materials', text = 'Optimize materials for this object', icon = 'MATERIAL')
    

# REGISTRATION
def register():

    bpy.types.EEVEE_MATERIAL_PT_context_material.prepend(cleanup_button_draw)

    bpy.utils.register_class(OBJECT_OT_cleanup_materials)


def unregister():

    bpy.types.EEVEE_MATERIAL_PT_context_material.remove(cleanup_button_draw)

    bpy.utils.unregister_class(OBJECT_OT_cleanup_materials)



if __name__ == "__main__":
    register()