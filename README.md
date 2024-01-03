# Greedy Meshing

## Project Description

This project implements a 2D and 3D greedy meshing algorithm in Python. Greedy meshing is a technique used to optimize the rendering of voxel-based graphics by merging adjacent voxels (or 'blocks') into larger cuboids, thereby reducing the complexity of the mesh. This is particularly useful in computer graphics, games, and simulations to improve performance.

The repository contains two main Python scripts:

- `greedy_meshing_2d.py`: Implements 2D greedy meshing, which is a subroutine of the 3D meshing process.
- `greedy_meshing_3d.py`: Extends the 2D greedy meshing to three dimensions, allowing for the generation of a simplified mesh from a 3D voxel grid.

## Problem Definition

Given a voxel grid, where each voxel is defined by an int type, the goal is to generate a reduced set of faces required to represent the external surface of the structure formed by the solid voxels. This reduction in the number of faces is achieved by merging adjacent voxels that share the same face. This achieves a simplified mesh that has at most 8x the number of faces that a perfect mesh would have [https://0fps.net/2012/06/30/meshing-in-a-minecraft-game/#:~:text=mesh%20actually%20is%3A-,Theorem,-%3A%C2%A0The%20greedy](reference).

## Implementation Details

### `greedy_meshing_3d.py`

- The script defines a `Face` data class to represent each face of the mesh.
- It utilizes the `greedy_meshing_2d` function from `greedy_meshing_2d.py` for handling the 2D aspects of the meshing process.
- The `greedy_meshing_3d` function takes a 3D voxel grid as input and outputs a list of `Face` objects, each representing a face of the mesh. These faces can then be used to generate a mesh for rendering.

### Example Usage

```python
# Define a voxel grid
voxel_grid = [
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
]

# Generate the mesh faces
faces = greedy_meshing_3d(voxel_grid)

# Output the generated faces
print(f"Generated {len(faces)} faces:")
for face in faces:
    print(face)
```

## Installation

No additional installation is required, as the project uses standard Python libraries.

## Contributing

Contributions to the project are welcome.
