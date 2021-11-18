# a-maze
Draw random mazes in python

This program generates and draws a rectangular maze, with an entrance on one side and one on the opposite side. 
The walls have two connected components, and there is one (and only one) way from one entrance to the other. 
To run the program, change "rows" and "columns" as desired inside main(), and interpret using python3. 
Due to how matplotlib coordinates work, rows and columns may mean the opposite of what you think.

The algorithm is as follows:
- draw the side walls, with two entrances.
- repeat(
        - choose a random node which is the end of a wall segment
        - find a neighbouring node which does not touch any wall segment
        - draw a new wall segment between the two)
  until every node is the end of a wall segment.
  
I believe the implementation is reasonably efficient, with the very notable exception of everything matplotlib.
