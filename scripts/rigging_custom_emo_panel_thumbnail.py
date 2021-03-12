import bpy
from bpy.types import Panel, EnumProperty, WindowManager
import bpy.utils.previews
from pathlib import Path

import os

# UI
class OBJECT_PT_Cat_Emotions_Thumbnails(bpy.types.Panel):
    bl_label = "Cat Emotions Preview"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        
        ob = context.object
        
        char_thumbs_dict = {
            "Cat": "Cat_Emotions_Thumbnails",
            "Dog": "Dog_Emotions_Thumbnails"
            }
            
        layout = self.layout
        wm = context.window_manager
        row = layout.row()
        
        # This tells Blender to draw the window manager object
        # (Which is our preview)
        row.template_icon_view(context.scene, char_thumbs_dict[ob.data.name], scale = 7.0, show_labels = True)
        
        # Just a way to access which one is selected
        row = layout.row()
        row.label(text= bpy.context.scene.Cat_Emotions_Thumbnails.split("_emo_")[1].split(".")[0])

preview_collections = {}

def Cat_Emotions_generate_previews():
    # We are accessing all of the information that we generated in the register function below
    pcoll = preview_collections["thumbnail_previews"]
    image_location = pcoll.images_location
    VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg')
    
    cat_emotions_enum_items = []
    
    # Generate the thumbnails
    
    for i, image in enumerate(os.listdir(image_location)):
        if image.endswith(VALID_EXTENSIONS) and image.startswith("CAT"):
            filepath = os.path.join(image_location, image)
            thumb = pcoll.load(filepath, filepath, 'IMAGE', force_reload=False)
            cat_emotions_enum_items.append(
                (
                image,
                Path(filepath).stem.split("_emo_")[1],
                Path(filepath).stem.split("_emo_")[0] + " feels " + Path(filepath).stem.split("_emo_")[1],
                thumb.icon_id,
                i)
                )
            
    return cat_emotions_enum_items

def Dog_Emotions_generate_previews():
    # We are accessing all of the information that we generated in the register function below
    pcoll = preview_collections["thumbnail_previews"]
    image_location = pcoll.images_location
    VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg')
    
    dog_emotions_enum_items = []
    
    # Generate the thumbnails
    
    for i, image in enumerate(os.listdir(image_location)):
        if image.endswith(VALID_EXTENSIONS) and image.startswith("DOG"):
            filepath = os.path.join(image_location, image)
            thumb = pcoll.load(filepath, filepath, 'IMAGE', force_reload=False)
            dog_emotions_enum_items.append(
                (
                image,
                Path(filepath).stem.split("_emo_")[1],
                Path(filepath).stem.split("_emo_")[0] + " feels " + Path(filepath).stem.split("_emo_")[1],
                thumb.icon_id,
                i)
                )
            
    return dog_emotions_enum_items

def CAT_update_emotion_pose(self, context):
    emo = context.scene.Cat_Emotions_Thumbnails.split(".")[0]
    bone = context.active_object.pose.bones["emo_Root"]
    
    bone[emo] = 1.0
    for key in bone.keys():
        if key != emo:
            bone[key] = 0.0
    
    

        
def register():
    
    bpy.utils.register_class(OBJECT_PT_Cat_Emotions_Thumbnails)
    
    from bpy.types import Scene
    from bpy.props import StringProperty, EnumProperty
    
    # Create a new preview collection (only upon register)
    pcoll = bpy.utils.previews.new()
    
    # This line needs to be uncommented if you install as an addon
    pcoll.images_location = bpy.path.abspath('//textures')
    
    # This line is for running as a script. Make sure images are in a folder called images in the same
    # location as the Blender file. Comment out if you install as an addon
    #pcoll.images_location = bpy.path.abspath('//images')
    
    # Enable access to our preview collection outside of this function
    preview_collections["thumbnail_previews"] = pcoll
    
    # This is an EnumProperty to hold all of the images
    # You really can save it anywhere in bpy.types.*  Just make sure the location makes sense
    bpy.types.Scene.Cat_Emotions_Thumbnails = EnumProperty(
        items = Cat_Emotions_generate_previews(),
        update = CAT_update_emotion_pose
        )
    
    bpy.types.Scene.Dog_Emotions_Thumbnails = EnumProperty(
        items = Dog_Emotions_generate_previews()
        )
    
def unregister():
    from bpy.types import WindowManager
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    
    del bpy.types.Scene.Cat_Emotions_Thumbnails
    del bpy.types.Scene.Dog_Emotions_Thumbnails
    
    bpy.utils.unregister_class(OBJECT_PT_Cat_Emotions_Thumbnails)
   
if __name__ == "__main__":
    register()
