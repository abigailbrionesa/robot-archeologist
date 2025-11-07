# CSC 171 { Project 2: The Robot Archaelogist Adventure }
# Abigail Briones
# abrione3@u.rochester.edu

class Cell:
    '''
    represents a single location in the grid
    preconditions:
    - the provided coordinates and type must correspond to a valid grid cell
    postconditions:
    - a Cell object is created with no linkage (next = None)
    '''
    def __init__(self,row,col,type):
        self._row = row
        self._col = col
        self._type = type
        self._next = None
    
    def __str__(self):
        return f'[<{self._type}> cell at ({self._row},{self._col})]'
        
class LinkedPath:
    '''
    represents the robot's memory of visited cells as a singly linked list
    preconditions:
    - input parameter cell must be a valid Cell object
    postconditoins
    - for add_cell, the linked list contains one additional node, and head points to the new cell
    - for remove_last, the most recent node is removed and the list size decreases by one
    '''
    def __init__(self):
        self._head = None
        self._size = 0
    
    def add_cell(self,cell):
        '''
        adds a new cell to the beginning of the list
        '''
        cell._next = self._head
        self._head = cell
        self._size += 1
        
    def remove_last(self):
        '''
        removes the most recently added cell (head of the list)
        '''
        if not self._head:
            print('error empty')
        else:
            last = self._head
            self._head = self._head._next
            self._size -= 1
            return last
    
    def __iter__(self):
        current = self._head
        while current:
            yield current
            current = current._next
        
    def show_path(self):
        '''
        prints a textual representation of all visited cells
        '''
        textual_cells = [str(cell) for cell in self]
        return ("[" + " -> ".join(textual_cells) + "]")
    
class InvalidGridCharacterError(Exception):
    pass
class InvalidMovementError(Exception):
    pass


class Grid:
    '''
    represents the archeological site
    encapsulates the temple layout, providing safe access to cells and movement validation
    preconditions:
    - input grid layout must contain valid characters
    postconditoins:
    - a grid of Cell objects is constructed with correct type mapping
    '''

    def __init__(self,layout):
        # layout: 2d list of characters representing the maze
        # rows, cols: dimensions of the grid
        # grid: 2d list of Cell objects

        self._rows = len(layout)
        self._cols = len(layout[0])
        self._grid = []
        print('Loading grid...')
        for i in range(self._rows):
            current_row = []
            for j in range(self._cols):
                try:
                    cell_type = self._char_to_type(layout[i][j])
                except InvalidGridCharacterError as e:
                    print(e, '(adding cell of type "open" instead)')
                    cell_type = 'open'
                current_row.append(Cell(row=i, col=j, type=cell_type))
            self._grid.append(current_row)
        print('Temple Layout created!')
        
    def _char_to_type(self, ch):
        legend = {'#':'wall', '.': 'open','T':'treasure','X':'trap','S':'start','E':'exit'}
        if ch not in legend:
            raise InvalidGridCharacterError(f"Error: '{ch}' is an invalid grid character")
        return legend[ch]
        
    def _type_to_char(self, type):
        legend = {'wall':'#', 'open':'.', 'treasure':'T', 'trap':'X', 'start':'S', 'exit':'E'}
        return legend[type]

    def get_cell(self,row,col):
        '''
        returns the Cell at the given coordinates
        '''
        if self.is_valid(row,col):
            return self._grid[row][col]
        return
    
    def is_valid(self,row,col):
        '''
        returns True if movement to that position is possible (not a wall # or outside bounds)
        '''
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            return False
        if self._grid[row][col]._type == 'wall':
            return False
        return True
    
    def display(self):
        print('Temple Layout:')
        for row in range(self._rows):
            for col in range(self._cols):
                ch = self._type_to_char(self._grid[row][col]._type)
                print(ch, end=' ')
            print('')

class Robot:
    '''
    models the behavior of the archeologist robot R-171
    preconditions:
    - the grid must contain exactly one starting cell labeled 'S'
    - direction strings must be among {'up', 'down', 'left', 'right'}
    postconditions:
    - move(): the robot's position and energy level are updated
              the new cell is added to the linked path
    - backtrack(): the most recent move is undone, and the linked path is shortened
    '''
    def __init__(self,name,grid):
        self._name = name
        self._grid = grid
        self._energy = 20 #robot's remaining energy
        self._path = LinkedPath() #represents the visited cells
        self._current_cell = None #current location
        self._treasures_collected = 0
    
    def _find_start(self):
        '''
        locates the starting cell 'S' in the grid
        '''
        for i in range(self._grid._rows):
            for j in range(self._grid._cols):
                cell = self._grid._grid[i][j]
                if cell._type == 'start':
                    self._current_cell = cell
                    self._path.add_cell(cell)
                    return cell
        print('  [No starting cell found]')
        return 
    
    def update_energy(self,val):
        
    def move(self,direction):
        if self._energy == 0:
            print(f'Robot {self._name}: I can no longer move. I have no energy.')
        current_row, current_col = self._current_cell._row, self._current_cell._col
        if direction == 'up':
            current_row -= 1
        elif direction == 'down':
            current_row += 1
        elif direction == 'left':
            current_col -= 1
        elif direction == 'right':
            current_col += 1
        else:
            print(f'Robot {self._name}: I can only move up, down, left, or right')
            return
        
        try:
            print(f"Robot {self._name}: Let's move {direction} to ({current_row},{current_col})")
            new_position = self._grid.get_cell(current_row, current_col)
            if new_position is None:
                raise InvalidMovementError(f"Error: '{new_position}' is out of bounds or a wall")
            self._current_cell = new_position
            self._energy -= 1
            print(f'  [Energy level: {self._energy}]')
            self._path.add_cell(self._current_cell)
        
            print(f'  [Robot {self._name} is at {str(self._current_cell)}]')
            
            if self._current_cell._type == 'treasure':
                self._treasures_collected += 1
                print(f'Robot {self._name}: Yay! I have found a treasure. Now I have {self._treasures_collected} of them.')
                self._energy += 2
                print(f'  [Energy level: {self._energy}]')
            elif self._current_cell._type == 'trap':
                print(f'Robot {self._name}: Oh no! I fell into a trap. I will go back')
                self._energy -= 3
                print(f'  [Energy level: {self._energy}]')
                self.backtrack()
                print(f'  [Robot {self._name} backtracked to {self._current_cell}]')
            elif self._current_cell._type == 'exit':
                print(f'Robot {self._name}: Omg! I found the exit. I won')
                print(f'  [Total treasures collected: {self._treasures_collected}]')
                print(f'  [Remaining energy: {self._energy}]')
                print(f'  [Path Memory: {self.show_memory()}]')
            return
    
        except InvalidMovementError:
                print(f'Robot {self._name}: Oh no! I cannot move {direction}')
                
    
    def backtrack(self):
        '''
        removes the most recent cell from the linked path and moves the robot back to the previous cell
        '''
        self._path.remove_last() 
        self._current_cell = self._path._head
        return
    
    def show_memory(self):
        '''
        displays the current linked path of visited cells'''
        return self._path.show_path()
    
# Student Email: abrione3@u.rochester.edu
# Favorite Movie: Shutter Island (I do not usually watch movies)

def main():
    
    print('--- The Robot Archaeologist Adventure ---')
    
    temple_layout = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', 'T', '.', '#'],
    ['#', '.', '#', '.', 'X', '#'],
    ['#', '.', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#', '#']
    ]

    grid = Grid(temple_layout)
    grid.display()
    robot = Robot(name="Abi", grid=grid)
    robot._find_start()
    robot.move("right")
    robot.move("right")
    robot.move("right")
    robot.move("right")


main()