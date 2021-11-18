#This program generates and draws a rectangular maze, with an entrance on one side and one on the opposite side. The walls have two connected components, and there is one (and only one) way from one entrance to the other. To run the program, change "rows" and "columns" as desired inside main(), and interpret using python3. Due to how matplotlib coordinates work, rows and columns may mean the opposite of what you think.

import matplotlib.pyplot as plt
import random
from datetime import date
from datetime import time
from datetime import datetime

#generate the table. initially every side node is 1 (has a wall) and every inner node is 0 (does not have a wall)
def GenTable(rows,columns):
	table = [[0] * columns for i in range(rows)]
	for i in range(rows):
		table[i][0]=1
		table[i][columns-1]=1
	for j in range(columns):		
		table[0][j]=1
		table[rows-1][j]=1
	return table
		
#plot the sides of the rectangle minus two random segments, and create the figure object
def DrawSideWalls(rows, columns):
	plt.figure(figsize=[20,20])
	x=[0,0]
	y=[0,columns-1]
	plt.plot(x,y, c='black', linewidth=.5)
	x=[rows-1,rows-1]
	y=[0,columns-1]
	plt.plot(x,y, c='black', linewidth=.5)
	x=[0,rows-1]
	y=[columns-1,columns-1]
	plt.plot(x,y, c='black', linewidth=.5)
	x=[0,rows-1]
	y=[0,0]
	plt.plot(x,y, c='black', linewidth=.5)
	#remove two random walls on top and bottom
	i = random.randrange(rows-1)
	x=[i,i+1]
	y=[0,0]
	plt.plot(x,y, c='white', linewidth=1)
	i = random.randrange(rows-1)
	x=[i,i+1]
	y=[columns-1,columns-1]
	plt.plot(x,y, c='white', linewidth=1)
	plt.axis('scaled')
	plt.gca().axes.get_xaxis().set_visible(False)
	plt.gca().axes.get_yaxis().set_visible(False)

#given a node, find a random "empty" node which is adjacent. Empty will mean that no wall ends there.
def FindEmptyNeighbour(node,table,rows,columns):
	directions = ['N','S','E','W']
	random.shuffle(directions)
	for i in range(4):
		if directions[i]=='N' and node[1]!=columns-1 and table[node[0]][node[1]+1]==0:
			return [node[0],node[1]+1]
		elif directions[i]=='S' and node[1]!=0 and table[node[0]][node[1]-1]==0:
			return [node[0],node[1]-1]
		elif directions[i]=='E' and node[0]!=rows-1 and table[node[0]+1][node[1]]==0:
			return [node[0]+1,node[1]]
		elif directions[i]=='W' and node[0]!=0 and table[node[0]-1][node[1]]==0:
			return [node[0]-1,node[1]]
	return False

#main loop. We keep a list of all the nodes which are still empty, and keep adding walls connecting a random non-empty node to a random empty neighbour.
def Fill(table,rows,columns):
	counter=0
	while counter < (rows-2)*(columns-2):
		while True:
			a=random.randint(0,rows-1)
			b=random.randint(0,columns-1)
			if table[a][b]==1:
				node=[a,b]
				break
		while True:
			nei = FindEmptyNeighbour(node,table,rows,columns)
			if nei!=False:
				x=[node[0],nei[0]]
				y=[node[1],nei[1]]
				plt.plot(x,y, c='black', linewidth=.5)
				table[nei[0]][nei[1]] = 1
				counter=counter+1
				node = nei
			else:break

def main():
	columns = 200
	rows = 150
	table=GenTable(rows,columns)
	DrawSideWalls(rows, columns)
	Fill(table,rows,columns)
	plt.savefig(str(columns)+"x"+str(rows)+"_"+datetime.now().strftime("%H%M%S"), bbox_inches='tight')
	plt.show()

main()
