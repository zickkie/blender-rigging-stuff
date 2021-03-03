import bpy
import bmesh
from mathutils import Vector

### Variables
# Total distance of all the selected vertices' pairs
total_dist = 0
# Amount of all the selected vertices
selection_count = 0
# List of selected vertices' indices
selected_indices = []
# Dictionary of vertices and distances between them (value is equal to distance between (item-1) and item)
dist_dic = {}
# Dictionary of vertices and weights of the active-pose-bone-affected vertex group based on distance
weights_dic = {}
# Mesh object, mesh, armature
for object in bpy.context.selected_objects:
    if object.type == "MESH":
        ob = object
    else:
        arm = object
me = ob.data

### Functions
def distance_vec(point1: Vector, point2: Vector) -> float:
    """Calculate distance between two points."""
    return (point2 - point1).length

def cumulative(dict, range_end) -> float:
    """Calculate cumulative total of dictionary (keys are vertices' indices)
    values from key = 1 to key = given integer"""
    cumulative_sum = 0
    for i in range(1, range_end+1):
        cumulative_sum += dict[i]
    return cumulative_sum

# Switching from weight paint mode to edit mode
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
bpy.ops.object.mode_set(mode='EDIT')
# Sorting vertces by selection
bpy.ops.mesh.sort_elements(type='SELECTED')

# Creating BMesh from active mesh
bm = bmesh.from_edit_mesh(me)

# Snapping 3D Cursor to active vertex
bpy.context.scene.cursor.location = bm.select_history.active.co
# Sorting vertces by distance from 3D Cursor and creating list of their indices
bpy.ops.mesh.sort_elements(type='CURSOR_DISTANCE')
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.mode_set(mode='EDIT')
for v in me.vertices:
    if v.select:
        selected_indices.append(v.index)
selected_indices.sort()
print(selected_indices)

# Re-assigning BMesh
bm.free()
bm = bmesh.from_edit_mesh(me)

# Filling dictionary with verts indices & their pairs distnace and calculating total distance
for item in selected_indices:
    if item == selected_indices[-1]:
        break
    else:
        dist_dic[item+1] = distance_vec(me.vertices[item].co, me.vertices[item+1].co)

total_dist = sum(dist_dic.values())

# Filling dictionary with verts indices & their weights
for item in selected_indices:
    if item != selected_indices[-1] and item != selected_indices[0]:
        weights_dic[item] = 1 - cumulative(dist_dic, item) / total_dist


# Assigning vertices to a group defined by armature's active pose bone
# with weights defined by weights_dic

# Checking does this group already exist, otherwise create such group
if ob.vertex_groups.get(arm.data.bones.active.name) is None:
    group = ob.vertex_groups.new(name = arm.data.bones.active.name)
else:
    group = ob.vertex_groups.get(arm.data.bones.active.name)

# Assigning vertex to a group
bpy.ops.object.mode_set(mode='OBJECT')

for item in selected_indices:
    assign_list = []
    if item == selected_indices[-1]:
        assign_list.append(item)
        group.add(assign_list, 0.0, 'REPLACE' )
    elif item == selected_indices[0]:
        assign_list.append(item)
        group.add(assign_list, 1.0, 'REPLACE' )
    else:
        assign_list.append(item)
        group.add(assign_list, weights_dic[item], 'REPLACE' )

# Switching back to weight paint mode
bpy.ops.object.mode_set(mode='WEIGHT_PAINT')

print(total_dist)
print(dist_dic)
print(weights_dic)

    