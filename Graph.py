class Graph():
	def __init__(self, num_vertices):
		self.num_vertices = num_vertices
		self.num_edges = 0
		self.neighbor_list = [[] for i in range(num_vertices)]
		self.weights = [[] for i in range(num_vertices)]
		self.neighbors_sorted = True
		self.components=[0]*num_vertices
		self.num_components=-1
		self.parents=[-1]*num_vertices
		
		self.ancestor=None
		self.levels=None

		
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
	
	def edges(self):
		return [(u,v,w) for u in self.vertices() for v,w in self.neighbors_with_weights(u) if u < v]
	
	def dfs(self,u,component=1):
		for v in self.neighbor_list[u]:
			if not self.components[v]:
				self.components[v]=component
				self.dfs(v,component)
				self.parents[v]=u
                
				
	def get_connected_components(self):
		component=0
		for i,v in enumerate(self.components):
			if v==0:
				component+=1
				self.components[component]
				self.dfs(i,component)
		self.num_components=component
		return self.num_components
		
	def is_connected(self):
		if self.num_components==-1:
			self.get_connected_components()
			
		return self.num_components==1

	def is_tree(self):
		return self.is_connected() and self.num_edges==self.num_vertices-1
	
	
	def get_parent(self,node):
		return self.parents[node]
	
	def dfs_levels(self,u,parent,level,level_d):
		level_d[u]=level
		for v in self.neighbor_list[u]:
			if v!=parent:
				self.dfs_levels(v,u,level+1,level_d)

	def get_ancestor_matrix(self):
		matrix = [self.parents]
		for i in range(32):
			new_level=[]
			for i,v in enumerate(matrix[-1]):
				new_level.append(0 if v==0 else matrix[-1][matrix[-1][i]])
			matrix.append(new_level)
		self.ancestor=matrix
			
	def complete_ancestors(self,root):
		level_d={}
		self.dfs_levels(root,0,0,level_d)
		self.levels=level_d
		self.get_ancestor_matrix()
		        
	def get_ancestor(self,n,node):
		
		while n:
			node=self.ancestor[(n&-n)-1][node]   
			n-=n&-n
		return node
	
	def get_LCA(self,root,A,B):
		root=0
		if not self.is_tree():
			return None
		if self.ancestor==None:
			self.complete_ancestors(root)
		dif=abs(self.levels[A]-self.levels[B])

		if dif>0:
			if self.levels[A]>self.levels[B]:
				A=self.get_ancestor(dif,A)
			else:
				B=self.get_ancestor(dif,B)

		min_level=0
		max_level=self.levels[A]
		while min_level<max_level:
			mid_level=(max_level+min_level+1)//2

			if self.get_ancestor(self.levels[A]-mid_level,A) == self.get_ancestor(self.levels[B]-mid_level,B):
				min_level=mid_level
			else:
				max_level=mid_level-1
		return self.get_ancestor(self.levels[A]-max_level,A)
        