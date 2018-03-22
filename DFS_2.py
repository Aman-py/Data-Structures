class graph:
    def __init__(self,graph_dict={}):
        self.graph_dict = graph_dict
        self.stack = []
        self.visited = {}

    def get_vertex(self):
        if self.graph_dict == None:
            print(None)
        else:
            return self.graph_dict.keys()

    def get_edge(self,vertex):
        return self.graph_dict[vertex]

    def set_vertex(self,vertex):
        self.graph_dict[vertex] = []

    def set_edges(self,vertex,edge):
        if edge not in self.graph_dict.keys():
            graph().set_vertex(self,edge)
        if vertex not in self.graph_dict.keys():
            graph().set_vertex(self,vertex)
        else:
            self.graph_dict[vertex].append(edge)
            
    def printgraph(self):
        return self.graph_dict

    def push(self,node):
        return self.stack.append(node)

    def pop(self,node):
        return self.stack.pop(node)

    def DFSnode(self,start,visited):
        visited[start] = True
        print(start)

        for j in self.graph_dict[start]:
            if visited[j] == False:
                graph().DFSnode(j,visited)

    def DFS(self,start):
        visited = [False]*len(self.graph_dict)
        graph().DFSnode(start,visited)
        
graph().set_vertex(0)
graph().set_vertex(1)
graph().set_vertex(2)
graph().set_vertex(3)
graph().set_vertex(4)

graph().set_edges(0,1)
graph().set_edges(0,4)
graph().set_edges(1,0)
graph().set_edges(1,4)
graph().set_edges(1,2)
graph().set_edges(1,3)

graph().set_edges(2,1)
graph().set_edges(2,3)

graph().set_edges(3,1)
graph().set_edges(3,4)
graph().set_edges(3,2)

graph().set_edges(4,1)
graph().set_edges(4,0)
graph().set_edges(4,3)

print(graph().get_edge(0))
print(graph().get_edge(1))
print(graph().get_edge(2))
print(graph().get_edge(3))
print(graph().get_edge(4))

print(graph().get_vertex())

print(graph().printgraph())

graph().DFS(0)
