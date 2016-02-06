graph = {'A': set(['B', 'C']),
         'B': set(['D', 'E']),
         'C': set([ 'F']),
         'D': set([]),
         'E': set([ 'F']),
         'F': set([ 'E'])}


def dfs(graph1,start):
    visited,stack = set(),[start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph1[vertex] -visited)

    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}

print (dfs(graph,'A'))

set1 = set([1,2,3])
set2 = set([2])

print (set1 - set2)