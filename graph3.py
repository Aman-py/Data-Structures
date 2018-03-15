class vertex:
    def __init__(self,Node):
        self.id = Node
        self.con = []

    def connected_to(self,nbr):
        return self.con.append(nbr)

    def get_id(self):
        return self.id

    def printcon(self):
        return self.con

class graph(vertex):
    def __init__(self,graph_dict={}):
        self.graph_dict = graph_dict
        self.vert = []

    def addvertex(self,x):
        temp = vertex(x)
        self.vert.append(temp)
        return self.vert

    def addedge(self,vertex,nbr):
        if vertex not in self.vert:
            return graph().addvertex(vertex)
        if nbr not in self.vert:
            return graph().addvertex(nbr)
        else:
            return connected_to(vertex,nbr)
        
    def graph_d(self):
        graph_dict = {}
        for i in self.vert:
            graph_dict[i] = printcon(i)
        return graph_dict

    def getvertex(self):
        return self.vert
    
graph().addvertex(0)
graph().addvertex(1)
graph().addvertex(2)
graph().addvertex(3)
graph().addvertex(4)
graph().addedge(0,1)
graph().addedge(0,4)
graph().addedge(1,0)
graph().addedge(1,4)
graph().addedge(1,2)
graph().addedge(1,3)
graph().addedge(2,1)
graph().addedge(2,3)
graph().addedge(3,1)
graph().addedge(3,4)
graph().addedge(3,2)
graph().addedge(4,3)
graph().addedge(4,0)
graph().addedge(4,1)
print(graph().getvertex())
