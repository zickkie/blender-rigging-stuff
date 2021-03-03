import bpy
import random

def random_value(fr):
    return random.randint(-10, 10) * fr

bpy.app.driver_namespace['rvalue'] = random_value