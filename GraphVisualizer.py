from Graph import *
import random
import pygame

MOUSELEFT = 1
MOUSEMIDDLE = 2
MOUSERIGHT = 3

def rand_point(w,h):
	return (random.random()*w,random.random()*h)

def d2(P,Q):
	dx = (P[0]-Q[0])
	dy = (P[1]-Q[1])
	return dx*dx + dy*dy

class GraphVisualizer:
	def __init__(self, graph, w=800, h=600):
		self.w,self.h = w,h
		pygame.init()
		self.window = pygame.display.set_mode((w, h))
		self.window.fill((0, 0, 0))
		self.G = graph
		self.pos = [rand_point(w,h) for v in self.G.vertices()]
		self.selected_vertex = -1
		self.hover_vertex = -1
		self.edge_start = -1
		
	def run(self):
		self.running = True
		
		while self.running:
			self.mousepos = pygame.mouse.get_pos()
			self.hover_vertex = self.find_hover_vertex()
			
			self.update()
			
			self.window.fill((0, 0, 0))
			self.render()
			pygame.display.update()
			
			self.HandleEvents()

		pygame.quit()

	def HandleEvents(self):
		for event in pygame.event.get():
			if   event.type == pygame.QUIT:			 self.running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:  self.OnMousePress(event.button)				
			elif event.type == pygame.MOUSEBUTTONUP:	self.OnMouseRelease(event.button)
			elif event.type == pygame.KEYDOWN:		  self.OnKeyPress(event.key)
			elif event.type == pygame.KEYUP:			self.OnKeyRelease(event.key)
	
	def OnMousePress(self,btn):
		if btn == MOUSELEFT:
			self.selected_vertex = self.hover_vertex
		elif btn == MOUSERIGHT:
			self.edge_start = self.hover_vertex


	def OnMouseRelease(self,btn):
		if btn == MOUSELEFT:
			self.selected_vertex = -1
		elif btn == MOUSEMIDDLE:
			self.G.add_vertex()
			self.pos.append(self.mousepos)
		elif btn == MOUSERIGHT:
			if self.edge_start != -1 and self.edge_start != self.hover_vertex:
				self.G.add_edge(self.edge_start,self.hover_vertex)
				self.edge_start = -1
				

	def OnKeyPress(self,key):
		if key == pygame.K_ESCAPE:
			self.running=False
		pass


	def OnKeyRelease(self,key):
		print(key)
		pass
	
	def update(self):
		

		if self.selected_vertex != -1:
			self.pos[self.selected_vertex] = self.mousepos
	
	def hovering_over(self, v):
		return d2(self.pos[v],self.mousepos) < 65
	
	def find_hover_vertex(self):
		for v in self.G.vertices():
			if self.hovering_over(v):
				return v
		return -1
	
	def render(self):
		
		for e in self.G.edges():			
			pygame.draw.line(self.window, color=(150,255,0), start_pos=self.pos[e[0]], end_pos=self.pos[e[1]],width=3)
			
		for e in self.prim:
			pygame.draw.line(self.window, color=(150,0,255), start_pos=self.pos[e[0]], end_pos=self.pos[e[1]],width=15)
			
		for e in self.kruskal:
			pygame.draw.line(self.window, color=(255,0,0), start_pos=self.pos[e[0]], end_pos=self.pos[e[1]],width=10) 
			 
		if self.edge_start != -1:
			pygame.draw.line(self.window, color=(255,155,10), start_pos=self.pos[self.edge_start], end_pos=self.mousepos,width=3)
			
		for v in self.G.vertices():
			color = (255,150,0) if v == self.hover_vertex else (0,150,255)
			
			pygame.draw.circle(self.window,color=color,center=self.pos[v],radius=8)
