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
        if not self._head:
            self._head = cell
        else:
            prev_head = self._head
            cell._next = prev_head
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
        
        for i in range(self._rows):
            current_row = []
            for j in range(self._cols):
                cell_type = self._char_to_type(layout[i][j])
                current_row.append(Cell(row=i, col=j, type=cell_type))
            self._grid.append(current_row)
        
    def _char_to_type(self, ch):
            legend = {'#':'wall', '.': 'open','T':'treasure','X':'trap','S':'start','E':'exit'}
            return legend[ch]

    def get_cell(self,row,col):
        '''
        returns the Cell at the given coordinates
        '''
        return self._grid[row][col]
    
    def is_valid(self,row,col):
        '''
        returns True if movement to that position is possible (not a wall # or outside bounds)
        '''
        if row > self._rows or col > self._cols:
            print('outside bounds')
            return False
        index = row * self._cols + col
        if self._grid[index]._type == 'wall':
            print('you found a wall')
            return False
        return True
    
    def display(self):
        for row in range(self._rows):
            for col in range(self._cols):
                ch = self._grid[row][col]._type
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
        self._path = LinkedPath(None) #represents the visited cells
        self._current_cell = None #current location
        self._treasures_collected = 0
    
    def _find_start(self):
        '''
        locates the starting cell 'S' in the grid
        '''
        for i in range(1,self._grid + 1):
            if self._grid[i] == 'S':
                starting_index = i
        return starting_index
    
    def move(self,direction):
        if direction == 'up':
            self._current_cell = self._current_cell - self._grid._rows
        elif direction == 'down':
            self._current_cell = self._current_cell + self._grid._rows
        elif direction == 'left':
            self._current_cell = self._current_cell - 1
        elif direction == 'right':
            self._current_cell = self._current_cell + 1
        else:
            print('invalid direction')
            return
        self._energy -= 1
        self._path.add_cell = self._current_cell
        
        # update: robot's current coordinates and cell type
        print(f'Robot is in cell of type {self._current_cell._type} at ({self._current_cell._row},{self._current_cell._col})')
        
        if self._current_cell._type == 'treasure':
            print(f'Amazing! You have found a treasure. Now you have {self._treasures_collected} treasures collected.')
            self._treasures_collected += 1
        elif self._current_cell._type == 'traps':
            print(f'Oh no! Trap encountered. You might considered backtracking')
        elif self._current_cell._type == 'exit':
            print(f'Congratulations! Exit founded. ')
            print(f'You have collected {self._treasures_collected} treasures, and your remaining energy is {self._energy}')
        self.show_memory()
        
        print(f"Robot's energy remaining: ", self._energy)
        return
    
    def backgrack(self):
        '''
        removes the most recent cell from the linked path and moves the robot back to the previous cell
        '''
        previous_pos = self._path.remove_last
        self._current_cell = previous_pos
        return
    
    def show_memory(self):
        '''
        displays the current linked path of visited cells'''
        self._path.show_path()
        return
    
# Student Email: abrione3@u.rochester.edu
# Favorite Movie: Shutter Island (I do not usually watch movies)

def main():
    
    temple_layout = [
    ['#', 'S', '.', 'T', '#'],
    ['#', '.', '#', '.', 'X'],
    ['#', '.', '.', '.', 'E']
    ]
    
    temple_grid = Grid(grid=temple_layout)
    
    temple_grid.display