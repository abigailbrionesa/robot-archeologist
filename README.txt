Abigail Briones
abrione3@u.rochester.edu

I implemented the additional features (see code and comments)

1. Doubly Linked Path
2. Advanced Energy Managment and Trap Penalties
3. Dynamic Grid Visualization
4. Path Learning and Memory Optimization
5. If maze created with invalid character, default to open cell type
6. Colors, underline, strong text (attractive visuals)

Challenges and Solutions
1. IndexError (list index our of range) in test case of empty grid, AttributeError -> Handle gracefully with if statement in display_location, find_start, and move
2. I had to review the slides and my implementation of linked lists to verify correctedness
3. I spent time brainstorming how to improve my program
4. I had issue with PathNode attribute name, I fixed it by adding underscore when it was required
5. When using the doubly linked list and pathnode, I had to modify other parts of my code to access the cell in node
6. I learnt how to modify visuals in the terminal
7. I had some problems with the removed last function, I fixed it by keeping things in correct order
8. At first I got confused and I thought I had to manually create the cells -> The class takes care of that
9. I confused self._path.add_cell = self._current_cell  with self._path.add_cell(self._current_cell), so I fixed it
10. I did not want energy levels to be negative (impossible), so I created the function update_energy to safely modify it
11. among many other challenges and solutions