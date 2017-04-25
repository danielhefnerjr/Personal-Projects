# implements a simple A* algorithm on a grid using manhattan distance for the heuristic
# cannot move diagonally
# node: (x,y)


from queue import PriorityQueue
from collections import defaultdict
from tkinter import *

class AStarApp(Tk):
    def __init__(self, maxX, maxY, width, height, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.maxX = maxX
        self.maxY = maxY
        
        self.canvas = Canvas(self, width=width, height=height, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side='top', fill='both', expand='true')

        
        cellwidth = width / (maxX)
        cellheight = height / (maxY)
        self.cells = [[0 for i in range(maxX)] for j in range(maxY)]
        for i in range(maxX):
            for j in range(maxY):
                x1 = i*cellwidth
                x2 = (i+1)*cellwidth
                y1 = j*cellheight
                y2 = (j+1)*cellheight
                self.cells[i-1][j-1] = self.canvas.create_rectangle(x1,y1,x2,y2,fill='white',tags='rect',outline='black')

    def h(self, n, goal):
        return abs(goal[0]-n[0]) + abs(goal[1]-n[1])

    def a_star(self,start,goal):
        self.canvas.itemconfig(self.cells[start[0]][start[1]], fill="red")
        self.canvas.itemconfig(self.cells[goal[0]][goal[1]], fill="red")
        visited = []
        frontier = []
        cameFrom = {}

        gValue = defaultdict(lambda: float('Inf'))
        gValue[start] = 0

        fValue = defaultdict(lambda: float('Inf'))
        fValue[start] = self.h(start,goal)

        frontier.append(start)

        while not len(frontier) == 0:
            # slow, could maybe use priority queue? (but fValue might change after insertion)
            curr = sorted(frontier,key=lambda n: fValue[n])[0]


            if curr == goal:
                return self.reconstruct_path(cameFrom, curr)


            if curr != start:
                self.canvas.itemconfig(self.cells[curr[0]][curr[1]], fill="green")
            
            frontier.remove(curr)
            visited.append(curr)
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                neighbor = (curr[0] + i, curr[1] + j)
                if not 0 <= neighbor[0] <= self.maxX or not 0 <= neighbor[1] <= self.maxY:
                    continue
                if neighbor in visited:
                    continue

                temp_gValue = gValue[curr] + 1
                if neighbor not in frontier:
                    frontier.append(neighbor)
                elif temp_gValue >= gValue[neighbor]:
                    continue

                cameFrom[neighbor] = curr
                gValue[neighbor] = temp_gValue
                fValue[neighbor] = gValue[neighbor] + self.h(neighbor, goal)

        return []

    def reconstruct_path(self, cameFrom, curr):
        path = [curr]
        while curr in cameFrom.keys():
            curr = cameFrom[curr]
            path.append(curr)
            self.canvas.itemconfig(self.cells[curr[0]][curr[1]], fill="blue")
        path.reverse()
        return path

    def redraw(self):
        


## interface


if __name__ == '__main__':
    maxX = 30
    maxY = 30
    start = (0,0)
    goal = (20,20)
    width = 500
    height = 500

    app = AStarApp(maxX, maxY, width,height)
    
    path = app.a_star(start,goal)
    app.mainloop()
    

