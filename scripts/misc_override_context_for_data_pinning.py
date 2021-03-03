import bpy

def get_3dview_override():
  for window in bpy.context.window_manager.windows:
      screen = window.screen
      for area in screen.areas:
          if area.type != 'PROPERTIES':
              continue
          for region in area.regions:
              if region.type != 'WINDOW':
                  continue
              return {'window': window, 'screen': screen, 'area': area, 'region': region}

override = get_3dview_override()
                  
bpy.ops.buttons.toggle_pin(override)