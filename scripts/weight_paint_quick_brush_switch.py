bl_info = {
    "name": "Weight Paint Brush Quick Change",
    "author": "Arthur Shapiro",
    "version": (0, 1),
    "blender": (2, 83, 0),
    "location": "View 3D -> Alt-D in Weight Paint Mode",
    "description": "Switch between Add and Subtract brushes for Weight Paint Draw Tool (at first execution switching to Draw Tool itself with Add Brush will be done",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging"
    }


import bpy
from bpy.types import Operator


class Weight_Paint_Brush_Switch (Operator):
    """Switch between Add and Subtract brushes for Weight Paint Draw Tool"""
    bl_label = "Weight Paint Brush Quick Change"
    bl_idname = "object.weight_paint_brush_switch"
    bl_option = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        
        if context.object and context.object.mode == "WEIGHT_PAINT":
            
            add_brush = None
            subtract_brush = None
            
            for brush in bpy.data.brushes:
                if "Add" in brush.name:
                    add_brush = brush
                elif "Subtract" in brush.name:
                    subtract_brush = brush
            
            if add_brush is None or subtract_brush is None:
                self.report({"WARNING"}, "No relevant brush names have been found")
                
            else:
                if context.tool_settings.weight_paint.brush == add_brush:
                    context.tool_settings.weight_paint.brush = subtract_brush
                    self.report({"INFO"}, "Active Brush is Subtract")
                elif context.tool_settings.weight_paint.brush == subtract_brush:
                    context.tool_settings.weight_paint.brush = add_brush
                    self.report({"INFO"}, "Active Brush is Add")
                else:
                    context.tool_settings.weight_paint.brush = add_brush
                    self.report({"INFO"}, "Active Brush is Add")
   
        return {'FINISHED'}

addon_keymaps = []

def register():
    
    bpy.utils.register_class(Weight_Paint_Brush_Switch)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name ='3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new("object.weight_paint_brush_switch", type= 'D', value = 'PRESS', alt = True)
        addon_keymaps.append((km, kmi))

def unregister():
    
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    bpy.utils.unregister_class(Weight_Paint_Brush_Switch)

if __name__ == "__main__":
    register()