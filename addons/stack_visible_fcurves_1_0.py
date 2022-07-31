bl_info = {
    "name": "Stack Visible Fcurves",
    "author": "Arthur Shapriro",
    "version": (1, 0),
    "blender": (3, 1, 2),
    "location": "Graph Editor > Channel Menu",
    "description": "Moves the Groups that contain Visible FCurves to the Top of the list and expand them",
    "warning": "",
    "doc_url": "",
    "category": "Animation",
}


import bpy
from bpy.types import Operator, Panel

class SVF_OT_Stack_Visible_Fcurves(Operator):
    """Move Visible FCurves to the Top"""
    bl_idname = "graph.stack_visible_fcurves"
    bl_label = "Moves Visible FCurves to the Top"
    bl_options = {'REGISTER', 'UNDO'}
    
    use_expand: bpy.props.BoolProperty(
        name = "Expand",
        default = False,
        description = "Expand"
        )
    
    use_pin: bpy.props.BoolProperty(
        name = "Pin",
        default = False,
        description = "Pin"
        )
    
    
    def execute(self, context):
        
        ob = context.active_object
        action = ob.animation_data.action
        fcurves = action.fcurves
        
        vis_curves = []
        
        for curve in fcurves:
            if not curve.hide:
                vis_curves.append(curve)
            else:
                if curve.group:
                    curve.group.select = False
                    curve.group.show_expanded = False
                    curve.group.show_expanded_graph = False
                    curve.group.use_pin = False
        
        if len(vis_curves) > 0:
            vis_groups = []
            for curve in vis_curves:
                if curve.group:
                    if not curve.group in vis_groups:
                        vis_groups.append(curve.group)
                
                else:
                    if action.groups.get("UNGROUPPED"):
                        curve.group = action.groups.get("UNGROUPPED")
                        curve.group.select = True
                    else:
                        group_new = action.groups.new("UNGROUPPED")
                        curve.group = group_new
                        curve.group.select = True
                    vis_groups.append(curve.group)
            
            for group in vis_groups:
                group.select = True
                group.show_expanded = self.use_expand
                group.show_expanded_graph = self.use_expand
                if self.use_pin:
                    group.use_pin = True
                else:
                    group.use_pin = False
        
            
            bpy.ops.anim.channels_move(direction='TOP')
            
        
        return {'FINISHED'}



def svf_header_button(self, context):
    
    
    col = self.layout.column(align=True)
    row = col.row(align=True)
    row.operator(SVF_OT_Stack_Visible_Fcurves.bl_idname, icon='COLLAPSEMENU', text="Stack Visible")
    
    fcurves_vis_state = False
    
    if (context.active_object and context.active_object.type == "ARMATURE"):
        if context.active_object.animation_data and context.active_object.animation_data.action:
            if len(context.active_object.animation_data.action.fcurves) > 0:
                fcurves_vis_state = True
                
    row.enabled = fcurves_vis_state


def register():
    
    bpy.utils.register_class(SVF_OT_Stack_Visible_Fcurves)
    
    bpy.types.GRAPH_MT_channel.append(svf_header_button)

def unregister():
    
    bpy.utils.unregister_class(SVF_OT_Stack_Visible_Fcurves)

    bpy.types.GRAPH_MT_channel.remove(svf_header_button)

if __name__ == "__main__":
    register()
