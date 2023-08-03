def initialise(V):
    global dis, Next
    for i in range(V):
        for j in range(V):
            dis[i][j] = graph[i][j]
            if (graph[i][j] == INF):
                Next[i][j] = -1
            else:
                Next[i][j] = j


def constructPath(u, v):
    global graph, Next
    if (Next[u][v] == -1):
        return {}
    path = [u]
    while (u != v):
        u = Next[u][v]
        path.append(u)
    return path


def floydWarshall(V):
    global dist, Next
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if (dis[i][k] == INF or dis[k][j] == INF):
                    continue
                if (dis[i][j] > dis[i][k] + dis[k][j]):
                    dis[i][j] = dis[i][k] + dis[k][j]
                    Next[i][j] = Next[i][k]


def printPath(path):
    n = len(path)
    for i in range(n - 1):
        print(path[i], end=" -> ")
    print(path[n - 1])


if __name__ == '__main__':
    MAXM, INF = 14, 10 ** 7
    dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
    Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]

    V = 14


    graph = [
        #      ora , zer , ara ,  tim , lug ,meh ,dob  cra ,rim , sib , fag   pit, , buc  , gio
        [INF, 71, INF, INF, INF, INF, INF, INF, INF, 151, INF, INF, INF, INF],  # ora
        [71, INF, 75, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],  # zer
        [INF, 75, INF, 118, INF, INF, INF, INF, INF, 140, INF, INF, INF, INF],  # ara
        [INF, INF, 118, INF, 111, INF, INF, INF, INF, INF, INF, INF, INF, INF],  # tim
        [INF, INF, INF, 111, INF, 70, INF, INF, INF, INF, INF, INF, INF, INF],  # lugoj
        [INF, INF, INF, INF, 70, INF, 75, INF, INF, INF, INF, INF, INF, INF],  # mehadia
        [INF, INF, INF, INF, INF, 75, INF, 120, INF, INF, INF, INF, INF, INF],  # dobreta
        [INF, INF, INF, INF, INF, INF, 120, INF, 146, INF, INF, 138, INF, INF],  # craio
        [INF, INF, INF, INF, INF, INF, INF, 146, INF, 80, INF, 97, INF, INF],  # rimni
        [151, INF, 140, INF, INF, INF, INF, INF, 80, INF, 99, INF, INF, INF],  # sibiu
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 99, INF, INF, 211, INF],  # fagaras
        [INF, INF, INF, INF, INF, INF, INF, 138, 97, INF, INF, INF, 101, INF],  # pitesti
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 211, 101, INF, 90],  # bucha
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 90, INF]  # giu
    ]
    # I hate this graph


    initialise(V)
    floydWarshall(V)
    print("len of the best way from ara to bucha is : " , dis[2][12])

    path = []

    # Path from node 2 to 12
    print("Shortest path from 2 to 12 is :\n", end="")
    path = constructPath(2, 12)
    printPath(path)
