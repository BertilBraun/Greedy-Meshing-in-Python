from dataclasses import dataclass

@dataclass
class Face:
    position: tuple[int, int, int]
    dimensions: tuple[int, int]
    orientation: str
    type: int
    
GRID_VALUE_TYPE = int
GRID_2D = list[list[GRID_VALUE_TYPE]]
GRID_3D = list[list[list[GRID_VALUE_TYPE]]]