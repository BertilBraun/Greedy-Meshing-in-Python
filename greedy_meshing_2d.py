from defines import GRID_2D, Face

def greedy_meshing_2d(grid: GRID_2D) -> list[Face]:
    rows, cols = len(grid), len(grid[0])
    # initialize merged = True if cell == 0, False otherwise
    merged = [[grid[y][x] == 0 for x in range(cols)] for y in range(rows)]
    rectangles = []

    for y in range(rows):
        for x in range(cols):
            if not merged[y][x]:
                # Start of a new rectangle
                width, height = 1, 1

                # Find the width
                while x + width < cols and not merged[y][x + width] and grid[y][x + width] == grid[y][x]:
                    width += 1

                # Find the height
                all_row_match = True
                while y + height < rows and all_row_match:
                    for i in range(width):
                        if x + i >= cols or merged[y + height][x + i] or grid[y + height][x + i] != grid[y][x]:
                            all_row_match = False
                            break
                    if all_row_match:
                        height += 1

                # Add the rectangle and mark cells as merged
                rectangles.append(Face(
                    position=(x, y),
                    dimensions=(width, height),
                    orientation="front",
                    type=grid[y][x]
                ))
                for dy in range(height):
                    for dx in range(width):
                        merged[y + dy][x + dx] = True

    return rectangles


if __name__ == "__main__":
    # Test with the example grid
    grid = [
        [1, 1, 2, 2],
        [1, 1, 2, 2],
        [3, 3, 4, 4],
    ]

    faces = greedy_meshing_2d(grid)
    
    print(faces)

    expected_faces = [
        Face((0, 0, 0), (2, 2), 1),
        Face((2, 0, 0), (2, 2), 2),
        Face((0, 2, 0), (2, 2), 3),
        Face((2, 2, 0), (2, 2), 4),
    ]
    assert faces == expected_faces, f"Expected {expected_faces}, got {faces}"
