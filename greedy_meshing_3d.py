from typing import Literal
from defines import GRID_3D, Face, GRID_VALUE_TYPE
from greedy_meshing_2d import greedy_meshing_2d

AXIS = Literal['x', 'y', 'z']

NAME_MAPPING = {
    ('z', +1): "top",
    ('z', -1): "bottom",
    ('y', +1): "front",
    ('y', -1): "back",
    ('x', +1): "right",
    ('x', -1): "left",
}

GRID_SIZE = 3

def greedy_meshing_3d(voxel_grid: GRID_3D) -> list[Face]:
    def is_exposed(x: int, y: int, z: int) -> bool:
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and 0 <= z < GRID_SIZE:
            return voxel_grid[z][y][x] == 0
        return True

    def get_face(grid: GRID_3D, axis: AXIS, index: int, offset: int) -> tuple[list[GRID_VALUE_TYPE], str]:
        face = []
        for y in range(GRID_SIZE):
            row = []
            for x in range(GRID_SIZE):
                if axis == 'z':
                    exposed = is_exposed(x, y, index + offset)
                    row.append(grid[index][y][x] if exposed else 0)
                elif axis == 'y':
                    exposed = is_exposed(x, index + offset, y)
                    row.append(grid[y][index][x] if exposed else 0)
                elif axis == 'x':
                    exposed = is_exposed(index + offset, y, x)
                    row.append(grid[x][y][index] if exposed else 0)
            face.append(row)
        return face, NAME_MAPPING[(axis, offset)]

    faces = []
    # Get each mesh of the voxel grid
    for i in range(GRID_SIZE):
        for offset in [+1, -1]:
            for axis in ['z', 'y', 'x']:
                face, orientation = get_face(voxel_grid, axis, i, offset)
                for mesh in greedy_meshing_2d(face):
                    (x, y) = mesh.position
                    faces.append(Face(
                        position=(x, y, i) if axis == 'z' else (i, x, y) if axis == 'x' else (x, i, y),
                        dimensions=mesh.dimensions,
                        orientation=orientation,
                        type=mesh.type
                    ))

    return faces

# Example voxel grid (GRID_SIZExGRID_SIZExGRID_SIZE) with a torus (a 3d grid with the center column empty)
voxel_grid = [
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
]

faces = greedy_meshing_3d(voxel_grid)

print(f"Generated {len(faces)} faces:")
for face in faces:
    print(face)

expected_faces = [    
    # Top faces:
    Face(position=(0, 0, 2), dimensions=(3, 1), orientation='top', type=1),
    Face(position=(0, 1, 2), dimensions=(1, 2), orientation='top', type=1),
    Face(position=(2, 1, 2), dimensions=(1, 2), orientation='top', type=1),
    Face(position=(1, 2, 2), dimensions=(1, 1), orientation='top', type=1),
    
    # Bottom faces:
    Face(position=(0, 0, 0), dimensions=(3, 1), orientation='bottom', type=1),
    Face(position=(0, 1, 0), dimensions=(1, 2), orientation='bottom', type=1),
    Face(position=(2, 1, 0), dimensions=(1, 2), orientation='bottom', type=1),
    Face(position=(1, 2, 0), dimensions=(1, 1), orientation='bottom', type=1),
    
    # Outside faces:
    Face(position=(0, 0, 0), dimensions=(3, 3), orientation='back', type=1),
    Face(position=(0, 0, 0), dimensions=(3, 3), orientation='left', type=1),
    Face(position=(0, 2, 0), dimensions=(3, 3), orientation='front', type=1),
    Face(position=(2, 0, 0), dimensions=(3, 3), orientation='right', type=1),
        
    # Inside faces:
    Face(position=(1, 0, 0), dimensions=(1, 3), orientation='front', type=1),
    Face(position=(0, 0, 1), dimensions=(3, 1), orientation='right', type=1),
    Face(position=(1, 2, 0), dimensions=(1, 3), orientation='back', type=1),
    Face(position=(2, 0, 1), dimensions=(3, 1), orientation='left', type=1),
]

for face in faces:
    assert face in expected_faces, f"Expected {expected_faces}, got {faces}"