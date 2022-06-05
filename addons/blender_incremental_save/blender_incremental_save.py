bl_info = {
    "name": "Blender Incremental Save",
    "author": "Arthur Shapiro",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "File menu",
    "warning": "",
    "description": "Incremental Save: adds 1 to the last digital part of the current File Name",
    "category": "System"
}


import bpy
import os

# Split the current file name to digits and letters parts
def seperate_string_number(string):
    previous_character = string[0]
    groups = []
    newword = string[0]
    for x, i in enumerate(string[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            groups.append(newword)
            newword = i

        previous_character = i

        if x == len(string) - 2:
            groups.append(newword)
            newword = ''
        
        state = False
        for item in groups:
            if item.isdigit():
                state = True
    return groups, state

# Define what the digits should the next name consist of
def next_name(filename, count):
    if not seperate_string_number(filename)[1]:
        return filename + str(count) # E.g. add "1" if the current name has no digits at all
    else:
        filename_list = seperate_string_number(filename)[0]
        filename_list.reverse() # We want to take only the last digital part of the name
        for i in range(len(filename_list)):
            if filename_list[i].isdigit():
                last_number = int(filename_list[i])
                next_number = last_number + count
                if len(str(next_number)) > len(str(last_number)): # 09 -> 10 instead of 09 -> 010
                    base = filename_list[i].split(str(last_number))[0][:-1]
                else:
                    base = filename_list[i].split(str(last_number))[0]
                if int(filename_list[i]) == 0: # Add floating zeroes and have 000 -> 001 instead of 000 -> 1
                    filename_list[i] = base + str(next_number).zfill(len(filename_list[i]))
                else:
                    filename_list[i] = base + str(next_number)
                break
        filename_list.reverse()
        return ''.join(filename_list)
            


class BIS_OT_incremental_save(bpy.types.Operator):
    """Incremental Save"""
    bl_idname = "wm.incremental_save"
    bl_label = "Incremental Save"

    def execute(self, context):

        if not bpy.data.is_saved: # Save file if it hasn't been saved at all
            bpy.ops.wm.save_as_mainfile('INVOKE_DEFAULT')
            return {'FINISHED'}

        file = bpy.data.filepath
        name = os.path.splitext(os.path.basename(file))[0] # File name before the extension
    
        directory_name = os.path.dirname(file)

        directory_files = [] # Collect all the files in the directory
        for item in sorted(os.listdir(directory_name)):
             if item.endswith('.blend'):
                directory_files.append(os.path.splitext(item)[0])

        # Compare the name that we want to take as the next one
        # with all the exeisting names in the directory,
        # and if there is a match then add 1 to the count parameter
        # until we have the number that makes file name unique again (make name great again!) 
        def next_realtive_name(current_name, count):
            while next_name(name, count) in directory_files:
                count += 1
                next_realtive_name(current_name, count)
            return next_name(current_name, count)

        new_name = next_realtive_name(name, 1) + ".blend" # Don't forget to bring the extension back

        inc_path = os.path.join(directory_name, new_name)
        bpy.ops.wm.save_as_mainfile(filepath = inc_path) # Save it

        self.report({'INFO'}, "Incremental Saved " + new_name)

        return {'FINISHED'}


# Draw this operator in File Menu
def bis_menu(self, context):
    col = self.layout.column(align=True)
    row = col.row(align=True)
    row.operator(BIS_OT_incremental_save.bl_idname, icon='COPY_ID', text="Incremental Save")


def register():
    bpy.utils.register_class(BIS_OT_incremental_save)
    bpy.types.TOPBAR_MT_file.prepend(bis_menu)

def unregister():
    bpy.utils.unregister_class(BIS_OT_incremental_save)
    bpy.types.TOPBAR_MT_file.remove(bis_menu)

