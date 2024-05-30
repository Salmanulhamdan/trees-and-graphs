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
            print(queue)
            vertex=queue.pop(0)
            print(vertex)
            if vertex not in visited:
                traversal.append(vertex)
                visited.add(vertex)
                # queue.extend(set(self.graph[vertex])-visited)
                queue.extend([v for v in self.graph[vertex] if v not in visited])
        return traversal
    
    def dfs(self,start):
        visited=set()
        stack=[start]
        trversal=[]

        while stack:
            vertex=stack.pop()
            if vertex not in visited:
                trversal.append(vertex)
                visited.add(vertex)
                stack.extend([v for v in self.graph[vertex] if v not in visited])
        return trversal
    

    # def dfs_util(self, vertex, visited):

    #     visited.add(vertex)
    #     print(vertex, end=" ")

    #     for neighbor in self.graph[vertex]:
    #         if neighbor not in visited:
    #             self.dfs_util(neighbor, visited)

    # def Dfs(self, start_vertex):
    #     visited = set()
    #     self.dfs_util(start_vertex, visited)


   


   



    



demo=Graph()

demo.add_edges(2,3)
demo.add_edges(1,3)
demo.add_edges(2,4)
demo.add_edges(5,3)
demo.add_edges(6,2)

# print(demo.graph)


print(demo.bfs(2))
# print(demo.dfs(2))
# print(demo.Dfs(2))
# print(demo.dFs(6))