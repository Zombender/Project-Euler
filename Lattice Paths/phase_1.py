RIGHT = 'right'
DOWN = 'down'

class Grid:
    def __init__(self, limit): #4
        self.limit = limit+1
        self.maximum = pow(limit,2)
        self.grid = [[j + i * self.limit + 1 for j in range(self.limit)] for i in range(self.limit)]
        
    def calculate_paths(self):
        quantity = 0
        actual_position = 1
        while (
        self.move(actual_position,direction=RIGHT)==False 
        and self.move(actual_position,direction=DOWN)==False
        ):
            
            pass
    def go(self):
        pass
    def move(self, actual_position, direction):
        x,y = self.find_index(actual_position)
        try:
            match direction:
                case 'right':
                    actual_position = self.grid[x+1][y]
                case 'down':
                    actual_position = self.grid[x][y+1]
        except IndexError:
            return False
        else:
            return actual_position
    
    def find_index(self, number: int): # if index really exists
        for x, y in enumerate(self.grid):
            if number in y:
                return x, y.index(number)

    def __str__(self):
        for row in self.grid:
            print(row)

grid = Grid(4)

print(grid)