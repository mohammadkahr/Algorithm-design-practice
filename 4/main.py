import sys


def dijkstra(graph, source):
    vertex_count = len(graph)
    shortest_distances = [sys.maxsize] * vertex_count
    visited = [False] * vertex_count
    parents = [-1] * vertex_count

    shortest_distances[source] = 0

    for _ in range(vertex_count):
        nearest_vertex = -1
        shortest_distance = sys.maxsize

        for vertex in range(vertex_count):
            if not visited[vertex] and shortest_distances[vertex] < shortest_distance:
                nearest_vertex = vertex
                shortest_distance = shortest_distances[vertex]

        visited[nearest_vertex] = True

        for vertex in range(vertex_count):
            edge_distance = graph[nearest_vertex][vertex]

            if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex]:
                parents[vertex] = nearest_vertex
                shortest_distances[vertex] = shortest_distance + edge_distance

    print_solution(shortest_distances, parents, source)


def print_solution(distances, parents, source):
    vertex_count = len(distances)

    for vertex in range(vertex_count):
        if vertex != source:
            print(f"The path to the node {vertex}: distance = {distances[vertex]}, \tdistance =", end=" ")
            print_path(vertex, parents)
            print()


def print_path(current_vertex, parents):
    if current_vertex == -1:
        return

    print_path(parents[current_vertex], parents)
    print(f"-> {current_vertex}", end="")


# matrix
graph = [
    [0,  4,  0,  0,  0,  0,  0,  8,  0],
    [4,  0,  8,  0,  0,  0,  0,11,  0],
    [0,  8,  0,  7,  0,  4,  0,  0,  2],
    [0,  0,  7,  0,  9,14,  0,  0,  0],
    [0,  0,  0,  9,  0,10,  0,  0,  0],
    [0,  0,  4,14,10,  0,  0,  2,  0],
    [0,  0,  0,  0,  0,  0,  0,  1,  6],
    [8,11,  0,  0,  0,  2,  1,  0,  7],
    [0,  0,  2,  0,  0,  0,  6,  7,  0]
]

source_node = 0
dijkstra(graph, source_node)
