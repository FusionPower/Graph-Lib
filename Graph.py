class Graph():
	def __init__(self, num_vertices):
		self.num_vertices = num_vertices
		self.num_edges = 0
		self.neighbor_list = [[] for i in range(num_vertices)]
		self.weights = [[] for i in range(num_vertices)]
		self.neighbors_sorted = True
		self.component=[0]*num_vertices
		self.num_components=-1
		self.parents=[-1]*num_vertices
		
	def vertices():
		return range(num_vertices)
	
	def add_edge(self, x, y, w = 1.):
		self.neighbor_list[x].append(y)
		self.neighbor_list[y].append(x)
		self.weights[x].append(w)
		self.weights[y].append(w)
		self.num_edges += 1
	
	def add_vertex(self):
		self.num_vertices += 1
		self.neighbor_list.append([])
		self.weights.append([])
		return self.num_vertices - 1
	
	def neighbors(self, x):
		return self.neighbor_list[x]
	
	def neighbors_with_weights(self, x):
		return zip(self.neighbor_list[x], self.weights[x])
	
	def vertices(self):
		return range(self.num_vertices)
	
	def degree(self, x):
		return len(self.neighbor_list[x])
	
	def connected(self, x, y):
		self.sort_neighbors()
		return busqueda_binaria(y, self.neighbor_list[x])
	
	def sort_neighbors(self):
		if self.neighbors_sorted:
			return
		for u in self.vertices():
			self.neighbor_list[u], self.weights[u] = zip(*sorted(list(self.neighbors_with_weights(u))))
		self.neighbors_sorted = True
	
	def edges(self):
		return [(u,v,w) for u in self.vertices() for v,w in self.neighbors_with_weights(u) if u < v]
	
	def dfs(self,u,component=1):
		for v in self.neighbor_list[u]:
			if not self.components[v]:
				self.dfs(v,component)
				self.parents[v]=u
				
	def get_connected_components(self):
		component=0
		
		for i,v in enumerate(self.components):
			if v==0:
				component+=1
				self.dfs(i,component)
		self.num_components=component
		return self.components
		
	def is_connected(self):
		if self.num_components==-1:
			self.get_connected_components()
			
		return self.num_components==1

	def is_tree(self):
		return self.is_connected() and self.num_edges==self.num_vertices
	
	
	def get_parent(self,node):
		return self.parents[node]
		
	 
