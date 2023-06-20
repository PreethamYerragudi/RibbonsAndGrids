import random

def is_valid(grid, ribbon, row, col):
    n = len(grid)

    # Check if the ribbon exceeds the grid boundaries
    if row + 1 > n or col + ribbon > n:
        return False

    # Check for overlaps with existing ribbons in the grid
    for i in range(row, row + 1):
        for j in range(col, col + ribbon):
            if grid[i][j] != 0:
                return False

    return True

def place_ribbons(grid, ribbons, ribbon_index):
    n = len(grid)

    # Base case: All ribbons are placed
    if ribbon_index == len(ribbons):
        return True

    # Try placing the current ribbon at different positions
    ribbon = ribbons[ribbon_index]
    for row in range(n):
        for col in range(n):
            if is_valid(grid, ribbon, row, col):
                # Place the ribbon in the grid
                for j in range(col, col + ribbon):
                    grid[row][j] = ribbon

                # Recursively try to place the remaining ribbons
                if place_ribbons(grid, ribbons, ribbon_index + 1):
                    return True

                # Backtrack: Remove the ribbon from the grid
                for j in range(col, col + ribbon):
                    grid[row][j] = 0

    return False

def ribbon_arrangement(n, k):
    grid = [[0] * n for _ in range(n)]
    ribbons = random.sample(range(2, n + 1), k)

    if place_ribbons(grid, ribbons, 0):
        # Print the ribbon arrangement
        for row in grid:
            print(row)
    else:
        print("No solution exists.")

# Example usage:
ribbon_arrangement(10, 7)
