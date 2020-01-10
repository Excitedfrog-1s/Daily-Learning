# coding=utf-8

'''
m = [[0,1,4,65535], [1,0,2,65535], [4,2,0,1], [65535, 65535,1,0]]
n = 4
v = 2
'''

m = [[0, 1, 65535], [1, 0, 2], [65535, 2, 0]]
n = 3
v = 0

# v = 1


def Dijkstra(m, n, v):
    global D
    D = [m[v][i] for i in range(n)]  # Distance for source node to node i
    D[v] = 0  # Distance of source code to itself is 0
    visited = set({})  # Those nodes that are already visited
    unvisited = set([i for i in range(n)])
    visited.add(v)
    unvisited.remove(v)
    while len(visited) != n:
        for i in list(unvisited):
            # Move to the next position in set "unvisited"
            mini = min([D[i] for i in unvisited])
            v = D.index(mini)
            visited.add(v)
            unvisited.remove(v)
            for i in unvisited:  # Update D
                temp = m[v][i] + mini
                if D[i] > temp:
                    D[i] = temp
                print(D)
    print(D)


Dijkstra(m, n, v)
