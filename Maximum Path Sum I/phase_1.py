numbers = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

'''

def create_grid(grid: str):
    grid = grid.strip()
    grid = grid.split('\n')
    real_grid = [list(map(int,fila.split())) for fila in grid]
    return real_grid

def verify_index(list, index):
    if 0 <= index < len(list):
        return True
    return False

def calculate_path_sum(grid):
    grid = create_grid(numbers)
    for i,downed_row in enumerate(reversed(grid)): #We start from the last row
        origin_index = len(grid) - 1 - i
        if not verify_index(grid, origin_index+1): 
            continue
        if len(grid[origin_index]) == 2:

            left_path = list(map(lambda x: x+grid[1][0]+75,grid[origin_index+1][1]))
            left_path.extend([grid[origin_index+1][0]+grid[1][0]])
            right_path = list(map(lambda x : x+grid[1][1]+75, grid[origin_index+1][1]))
            right_path.extend([grid[origin_index+1][2]+grid[1][1]])
            grid[1][0] = left_path
            grid[1][1] = right_path
            return max(grid[1][0]), max(grid[1][1])
        for j,number in enumerate(grid[origin_index]):
        
            if verify_index(grid[origin_index],j-1) and verify_index(grid[origin_index],j+1): #Chech if a number has left and right numbers
                if isinstance(grid[origin_index+1][j],int): #Verifies that the downed adjacent number is int
                    left_path = number + grid[origin_index+1][j]
                else: #if not, sum all numbers found with 'number' in left side
                    left_path = list(map(lambda x : x+number,grid[origin_index+1][j])) 
                if isinstance(grid[origin_index+1][j+1],int): #Verifies that the downed adjacent number is int
                    right_path = number + grid[origin_index+1][j+1]
                else: #if not, sum all numbers found with 'number' in right side
                    right_path = list(map(lambda x: x+number, grid[origin_index+1][j+1]))
                paths = [left_path]
                paths.extend([right_path])
                if isinstance(paths, list) and all(isinstance(path,list) for path in paths):
                    new_path = []
                    for path in paths:
                        new_path.extend(path)
                else:
                    new_path = paths
                grid[origin_index][j] = new_path
                continue
            if j == 0:
                grid[origin_index][j] += grid[origin_index+1][j]
                continue
            else:
                grid[origin_index][j] += grid[origin_index+1][j+1]
                continue
        pass

left, right = calculate_path_sum(numbers)
print(left)
print(right)
