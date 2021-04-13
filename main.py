import sys
import random

from GraphVisualizer import *
from conectivity import *

if __name__ == "__main__":
	G = Graph(5)
	G.add_edge(0,1,2)
	G.add_edge(0,2,3)
	G.add_edge(1,4,1)
	G.add_edge(1,2,3)
	G.add_edge(2,3,4)
	G.add_edge(3,4,1)
	
	V = GraphVisualizer(G)
	
	V.run()
