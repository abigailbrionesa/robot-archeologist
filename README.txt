# The Robot Archaeologist Adventure

**CSC 171: Introduction to Computer Science — Project 2**

## Overview
This project simulates an autonomous exploring robot navigating an ancient temple. The robot moves through a maze, collects treasures, avoids traps, and records its journey using a linked list. The purpose of this project is to practice object-oriented programming, linked structures, and interactions between multiple classes in Python.

---

## Learning Objectives
- **Object-Oriented Programming**: Define classes (`Robot`, `Grid`, `Cell`, `LinkedPath`) that interact to simulate a robot exploring a temple.
- **Linked Structures**: Implement a singly linked list to track the robot’s memory of visited cells.
- **State & Behavior Simulation**: Update and maintain the robot’s energy, position, and treasures through method interactions.
- **Modular Design**: Demonstrate encapsulation and proper method interfaces.

---

## Class Structure

### `Cell`
Represents a single cell in the temple grid.

**Attributes**:
- `row`, `col`: integer coordinates
- `type`: `'wall'`, `'open'`, `'treasure'`, `'trap'`, `'start'`, `'exit'`
- `next`: reference to another `Cell` object (used for the linked path)

### `LinkedPath`
Stores the robot’s memory as a singly linked list.

**Methods**:
- `add_cell(cell)`: Adds a cell to the path.
- `remove_last()`: Removes the most recent cell (for backtracking).
- `show_path()`: Displays all visited cells.

### `Grid`
Represents the temple layout.

**Methods**:
- `get_cell(row, col)`: Returns the `Cell` at specific coordinates.
- `is_valid(row, col)`: Checks if the robot can move to a cell.
- `display()`: Prints the grid layout.

**Legend**:
- `#` - wall
- `.` - open path
- `T` - treasure
- `X` - trap
- `S` - start
- `E` - exit

### `Robot`
Models the archaeologist robot.

**Attributes**:
- `name`: Robot identifier (e.g., `R-171`)
- `grid`: Reference to a `Grid` object
- `energy`: Remaining energy (starts at 20)
- `path`: `LinkedPath` of visited cells
- `current_cell`: Current position
- `treasures`: Count of collected treasures

**Methods**:
- `find_start()`: Locate the starting cell
- `move(direction)`: Move in one of four directions (`up`, `down`, `left`, `right`)
- `backtrack()`: Undo the last move
- `show_memory()`: Display visited cells
