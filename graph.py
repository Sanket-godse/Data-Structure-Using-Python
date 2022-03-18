import collections

class Graph:
    def __init__(self,dic):
        self.graph=dic
    
    def get_edges(self):
        edge=[]
        for i in self.graph:
            for j in self.graph[i]:
                if {i,j} not in edge:
                    edge.append({i,j})
        return edge
    
    def get_vetices(self):
        return list(self.graph.keys())
    
    def add_vertices(self,v):
        if v not in self.graph:
            self.graph[v]=[]
        else:
            return
    
    def add_edges(self,v1,v2):
        # v1,v2=edge[0],edge[1]
        if v1 in self.graph:
            self.graph[v1].append(v2)
            if v2 not in self.get_vetices():
                self.add_vertices(v2)
                self.add_edges(v2,v1)
        else:
            return
        
    def dfs(self,visited,root):
        if root not in visited:
            print(root)
            visited.append(root)
            for neighbours in self.graph[root]:
                self.dfs(visited,neighbours)
    def bfs(self,root):
        visited=set()
        queue=collections.deque([root])
        while queue:
            vrtex=queue.popleft()
            visited.add(vrtex)
            for l in self.graph[vrtex]:
                if l not in visited:
                    queue.append(l)
        return visited

                
            

dic={
    "a":["b","c"],
    "b":["c"],
    "c":["a","b"]
}

g=Graph(dic)
# print(g.graph)
# g.add_edges("a","d")
# print(g.graph)
# print(g.get_vetices())
# g.dfs([],"a")
print(g.bfs("a"))