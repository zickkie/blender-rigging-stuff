bl_info = {
    "name": "Berry Buds Render Settings",
    "author": "Arthur Shapiro",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "location": "Properties > Render",
    "description": "Specific Render options for Berry Buds renders",
    "warning": "",
    "wiki_url": "",
    "category": "Render"
    }

import bpy

def specify(samples):
    
    scene = bpy.context.scene
    
    # Render    
    scene.cycles.feature_set = 'SUPPORTED'
    scene.cycles.device = 'CPU'
    scene.cycles.shading_system = True
    
    # Dimensions
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    
    # Aspect Ratio & Frame Rate
    scene.render.pixel_aspect_x = 1.0
    scene.render.pixel_aspect_y = 1.0
    scene.render.fps = 25
    
    # Output
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGB'
    scene.render.image_settings.color_depth = '8'
    scene.render.image_settings.compression = 15
    
    # Sampling
    scene.cycles.progressive = 'PATH'
    scene.cycles.seed = 0
    scene.cycles.sample_clamp_direct = 0.0
    scene.cycles.sample_clamp_indirect = 0.0
    scene.cycles.light_sampling_threshold = 0.01
    
    scene.cycles.samples = samples
    scene.cycles.preview_samples = samples
    
    # Geometry
    scene.cycles.volume_step_size = 0.1
    scene.cycles.volume_max_steps = 1024
    
    # Light Paths
    scene.cycles.transparent_max_bounces = 12
    scene.cycles.transparent_min_bounces = 12
    
    scene.cycles.max_bounces = 0
    scene.cycles.min_bounces = 0
    
    scene.cycles.diffuse_bounces = 0
    scene.cycles.glossy_bounces = 0
    scene.cycles.transmission_bounces = 0
    scene.cycles.volume_bounces = 0
    
    scene.cycles.use_transparent_shadows = False
    scene.cycles.caustics_reflective = False
    scene.cycles.caustics_refractive = False
    scene.cycles.blur_glossy = 0.0
    
    #Perfomance
    scene.render.threads_mode = 'AUTO'

# Set render options Class    
class bb_render_parameters(bpy.types.Operator):
    """Set the most important render options"""
    bl_idname = "render.bb_render_parameters"
    bl_label = "Set Berry Buds Render Parameters"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        specify(bpy.context.scene.samples_number)
            
        return {'FINISHED'}
    

def menu(self, context):
    
    scene = context.scene
    layout = self.layout
    box = layout.box()
    box.label(text = "Berry Buds Render Options")
    row = box.row()
    row = box.row()
    row.prop(context.scene, 'samples_number', text = 'Number of Samples')
    row = box.row()
    row.operator("render.bb_render_parameters", text="Set")

 
 
# Register    
def register():
    
    bpy.types.Scene.samples_number = bpy.props.IntProperty(
        name = "Number of Samples",
        default = 32,
        min = 16,
        max = 128,
        description = "Number of Samples to use in Render"
        )
    
    bpy.utils.register_class(bb_render_parameters)
    bpy.types.RENDER_PT_render.prepend(menu)


def unregister():
    
    bpy.types.RENDER_PT_render.remove(menu)
    bpy.utils.unregister_class(bb_render_parameters)
    

    del bpy.types.Scene.samples_number

if __name__ == "__main__":
    register()
