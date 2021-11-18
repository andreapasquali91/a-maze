#This program generates and draws a rectangular maze, with an entrance on one side and one on the opposite side. The walls have two connected components, and there is one (and only one) way from one entrance to the other. To run the program, change "rows" and "columns" as desired inside main(), and interpret using python3. Due to how matplotlib coordinates work, rows and columns may mean the opposite of what you think.

import matplotlib.pyplot as plt
import random
from datetime import date
from datetime import time
from datetime import datetime

#generate a list of all the nodes which are not on a side wall
def GenInnerNodes(rows, columns):
	list=[]
	for i in range(1,rows-1):
		for j in range(1,columns-1):
			list.append([i,j])
	return list

#generate a list of nodes that are on the sides of the rectangle
def GenSideNodes(rows, columns):
	list = []
	for i in range(rows):
		list.append([i,0])
		list.append([i,columns-1])
	for j in range(columns):
		list.append([0,j])
		list.append([rows-1,j])
	return list

#plot the sides of the rectangle minus two random segments, and create the figure object
def DrawSideWalls(rows, columns):
	plt.figure(figsize=(20,20))
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
def FindEmptyNeighbour(node,EmptyList):
	directions = ['N','S','E','W']
	while len(directions)!=0:
		d = random.choice(directions)
		if d=='N':
			newNode = [node[0],node[1]+1]
		elif d=='S':
			newNode = [node[0],node[1]-1]
		elif d=='E':
			newNode = [node[0]+1,node[1]]
		elif d=='W':
			newNode = [node[0]-1,node[1]]
		if newNode in EmptyList:
			return newNode
		else:
			directions.remove(d)
	return False	

#main loop. We keep a list of all the nodes which are still empty, and keep adding walls connecting a random non-empty node to a random empty neighbour.
def Fill(nodes,emptyNodes):
	while len(emptyNodes)!=0:
		node = random.choice(nodes)
		while True:
			nei = FindEmptyNeighbour(node,emptyNodes)
			if nei!=False:
				x=[node[0],nei[0]]
				y=[node[1],nei[1]]
				plt.plot(x,y, c='black', linewidth=.5)
				emptyNodes.remove(nei)
				node = nei
				nodes.append(nei)
			else:break

def main():
	columns = 100
	rows = 80
	SideNodeList = GenSideNodes(rows, columns)
	EmptyNodeList = GenInnerNodes(rows,columns)
	DrawSideWalls(rows, columns)
	Fill(SideNodeList, EmptyNodeList)
	plt.savefig(str(columns)+"x"+str(rows)+"_"+datetime.now().strftime("%H%M%S"), bbox_inches='tight')
	plt.show()

main()
