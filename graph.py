from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)

    def add_edges(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self,start):
        visited=set()
        queue=[start]
        traversal=[]

        while queue:
            vertex=queue.pop(0)
            if vertex not in visited:
                traversal.append(vertex)
                visited.add(vertex)
                queue.extend([v for v in self.graph[vertex] if v not in visited])
        return traversal
    
    def dfs(self,start):
        visited=set()
        pass


    



demo=Graph()

demo.add_edges(2,3)
demo.add_edges(1,3)
demo.add_edges(2,4)
demo.add_edges(5,3)
demo.add_edges(6,2)

print(demo.graph)


print(demo.bfs(6))