grid = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
'''
#(0,0)(1,1)(2,2)(3,3)
#(0,1)(1,2)(2,3)(3,4)
#(0,2)(1,3)(2,4)(3,5)
#(0,3)(1,4)(2,5)(3,6)

def create_grid(grid: str):
    grid = grid.strip()
    grid = grid.split('\n')
    real_grid = [list(map(int,fila.split())) for fila in grid]
    return real_grid


new_grid = create_grid(grid)