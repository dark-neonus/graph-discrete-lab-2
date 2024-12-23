"""
Lab 2
"""

from collections import deque
import time
import random
import itertools

def read_incidence_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the incidence matrix of a given graph
    """
    incidence_matrix = []
    m, n = 0, 0
    lst = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().strip(';').split(' -> ')
            if line[0].isdigit():
                n = int(line[0])
                m += 1
                lst.append(line)
        for row in range(n+1):
            row_ = []
            for col in range(m):
                if str(row) == lst[col][0]:
                    row_.append(1)
                elif str(row) == lst[col][1]:
                    row_.append(-1)
                elif str(row) == lst[col][0] and str(row) == lst[col][1]:
                    row_.append(2)
                else:
                    row_.append(0)
            incidence_matrix.append(row_)
    return incidence_matrix


def read_adjacency_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the adjacency matrix of a given graph
    """
    adjacency_matrix = []
    m, n = 0, 0
    lst = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().strip(';').split(' -> ')
            if line[0].isdigit():
                n = int(line[0])
                m += 1
                lst.append(line)
        for row in range(n+1):
            row = []
            for _ in range(n+1):
                row.append(0)
            adjacency_matrix.append(row)
        for line_ in lst:
            adjacency_matrix[int(line_[0])][int(line_[1])] = 1
    return adjacency_matrix

def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict: the adjacency dict of a given graph
    """
    adjacency_dict = {}
    adjacency_matr = read_adjacency_matrix(filename)
    for i, row in enumerate(adjacency_matr):
        adjacency_dict[i] = []
        for j, el in enumerate(row):
            if el == 1:
                adjacency_dict[i].append(j)
    return adjacency_dict

def iterative_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [3], 2: [3], 3: [2, 4], 4: []}, 0)
    [0, 1, 3, 2, 4]
    >>> iterative_adjacency_dict_dfs({0: [1, 2, 3], 1: [4, 5], 2: [], 3: [7], 4: [6], 5: [], 6: [], 7: []}, 0)
    [0, 1, 4, 6, 5, 2, 3, 7]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [], 2: [3], 3: [4, 5], 4: [], 5: []}, 0)
    [0, 1, 2, 3, 4, 5]
    >>> graph = {0: [1, 2, 3], 1: [0, 4], 2: [0, 5, 6], 3: [0, 7], 4: [1, 8], 5: [2, 9, 10], 
    ... 6: [2, 11], 7: [3, 12], 8: [4, 13], 9: [5], 10: [5], 11: [6], 12: [7], 
    ... 13: [8, 14], 14: [13]}
    >>> iterative_adjacency_dict_dfs(graph, 0)
    [0, 1, 4, 8, 13, 14, 2, 5, 9, 10, 6, 11, 3, 7, 12]
    >>> graph = {0: [2, 1, 3], 1: [0, 4, 5], 2: [0], 3: [0, 7], 4: [1, 6], 5: [1], 6: [4], 7: [3]}
    >>> iterative_adjacency_dict_dfs(graph, 0)
    [0, 1, 4, 6, 5, 2, 3, 7]
    """
    visited = set()
    stack = []
    traversing = []
    for _, vertix in enumerate(graph, start=start):
        stack.append(vertix)
        while stack:
            vertix = stack.pop()
            if vertix not in visited:
                visited.add(vertix)
                traversing.append(vertix)
            for neigbour in sorted(graph[vertix], reverse=True):
                if not neigbour in visited:
                    stack.append(neigbour)
    return traversing

def recursive_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    >>> recursive_adjacency_dict_dfs({0: [2, 1], 1: [0, 3, 2], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    >>> recursive_adjacency_dict_dfs({0: [], 1: [2], 2: [1, 3], 3: [2, 4], 4: []}, 1)
    [1, 2, 3, 4]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [3, 2], 2: [1], 3: [1], 4: []}, 1)
    [1, 2, 3]
    >>> recursive_adjacency_dict_dfs({}, 0)
    []
    >>> recursive_adjacency_dict_dfs({0: [], 1: [], 2: []}, 0)
    [0]
    >>> recursive_adjacency_dict_dfs({0: [], 1: [0, 2], 2: [0]}, 0)
    [0]
    """
    def recursion_logic(graph: dict[int, list[int]], current_node: int,
                        path: list[int], visit_info: list[bool]) -> list[int]:
        path.append(current_node)
        visit_info[current_node] = True
        for connected_node in sorted(graph[current_node]):
            if not visit_info[connected_node]:
                recursion_logic(graph, connected_node, path, visit_info)

    path = []
    if len(graph) > 0:
        visit_info = [False] * len(graph)
        recursion_logic(graph, start, path, visit_info)
    return path


def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 0)
    [0, 1, 2, 3]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 2)
    [2, 0, 1]
    >>> recursive_adjacency_matrix_dfs([[0, 1], [1, 0]], 0)
    [0, 1]
    >>> recursive_adjacency_matrix_dfs([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0)
    [0]
    >>> recursive_adjacency_matrix_dfs([], 0)
    []
    >>> recursive_adjacency_matrix_dfs([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 1)
    [1, 0, 2]
    """
    def recursion_logic(graph: list[list[int]], current_node: int,
                        path: list[int], visit_info: list[bool]) -> list[int]:
        path.append(current_node)
        visit_info[current_node] = True
        for connected_node, intersection_value in enumerate(graph[current_node]):
            # intersection > 0 avoid hardcoding (== 1) and ad support for pseudograph
            if not visit_info[connected_node] and intersection_value > 0:
                recursion_logic(graph, connected_node, path, visit_info)

    path = []
    if len(graph) > 0:
        visit_info = [False] * len(graph)
        recursion_logic(graph, start, path, visit_info)
    return path

def iterative_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    >>> iterative_adjacency_dict_bfs({0: [1, 2, 3], 1: [4, 5], 2: [6, 7], 3: [7], 4: [1], 5: [1], 6: [2], 7: [2, 3]}, 0)
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> iterative_adjacency_dict_bfs({1: [2, 3], 2: [3, 4, 5, 6], 3: [2, 7], 4: [2, 8], 5: [2, 4, 8], 6: [2], 7: [3], 8: [4, 5]}, 1)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    visited = set()
    queue = []
    traversing = []
    for _, vertix in enumerate(graph, start=start):
        queue.append(vertix)
        while queue:
            vertix = queue.pop(0)
            if vertix not in visited:
                visited.add(vertix)
                traversing.append(vertix)
            for neigbour in sorted(graph[vertix]):
                if not neigbour in visited:
                    queue.append(neigbour)
    return traversing

def bfs_matrix_distance_search(graph: list[list], start: int) -> int:
    """ bfs_matrix_distance_search """
    queue = deque([start])
    visit_info = [False] * len(graph)

    visit_info[start] = True

    distances = [float("inf")] * len(graph)
    distances[start] = 0

    while queue:
        # Remove left element an return it
        current_node = queue.popleft()


        for subnode, intersection_value in enumerate(graph[current_node]):
            if intersection_value == 1:
                if not visit_info[subnode]:
                    if distances[subnode] == float("inf"):
                        distances[subnode] = distances[current_node] + 1
                    queue.append(subnode)
                    visit_info[subnode] = True

    return max(distances)

def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    """
    radius = float("inf")
    for node_start in range(len(graph)):
        radius = min(radius, bfs_dict_distance_search(
                                graph,node_start))

    return 0 if radius == float("inf") else radius

def bfs_dict_distance_search(graph: dict[int: list[int]], start: int) -> int:
    """ bfs_dict_distance_search """
    queue = deque([start])
    visit_info = [False] * len(graph)

    visit_info[start] = True

    distances = [float("inf")] * len(graph)
    distances[start] = 0

    while queue:
        # Remove left element an return it
        current_node = queue.popleft()


        for subnode in graph[current_node]:
            if not visit_info[subnode]:
                if distances[subnode] == float("inf"):
                    distances[subnode] = distances[current_node] + 1
                queue.append(subnode)
                visit_info[subnode] = True

    return max(distances)

def adjacency_dict_radius(graph: dict[int: list[int]]) -> int:
    """
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    """
    radius = float("inf")
    for node_start in graph:
        radius = min(radius, bfs_dict_distance_search(
                                graph,node_start))

    return 0 if radius == float("inf") else radius

def measure_execution_time(func, *args, **kwargs):
    """
    Measures the execution time of a given function.
    
    :param func: function to execute
    :param args: function args
    :param kwargs: function kwargs
    :return: execution time.
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time

def generate_graph_dict(n: int) -> dict:
    """ Gernerate graph as dict """
    graph = {i: [] for i in range(n)}
    for u, v in itertools.combinations(range(n), 2):
        # Random decide to make edge or not
        if random.choice([True, False]):
            graph[u].append(v)
            graph[v].append(u)
    return graph

def generate_graph_matrix(n: int) -> list:
    """ Gernerate graph as adjacency matrix """
    matrix = [[0] * n for _ in range(n)]
    for u, v in itertools.combinations(range(n), 2):
        # Random decide to make edge or not
        if random.choice([True, False]):
            matrix[u][v] = matrix[v][u] = 1
    return matrix





def run_time_analyze(v_count: int, loops_count: int):
    """ Compare time execution """
    print("\n" * 3)
    print("-" * 30)
    print(f"Vertice count: {v_count}")
    print(f"Loops count: {loops_count}\n")

    # Generate graphs
    graphs_dict = [generate_graph_dict(v_count) for _ in range(loops_count)]
    graphs_matrix = [generate_graph_matrix(v_count) for _ in range(loops_count)]

    # --------------------------------------------
    # Time test for iterative_adjacency_dict_bfs
    def test_iterative_adjacency_dict_bfs(graphs):
        """ Test iterative_adjacency_dict_bfs """
        for graph in graphs:
            iterative_adjacency_dict_bfs(graph, 0)

    iterative_adjacency_dict_bfs_time = round(measure_execution_time(
        test_iterative_adjacency_dict_bfs,
        graphs_dict
    ), 5)
    print(f"> {iterative_adjacency_dict_bfs_time = } s")

    # --------------------------------------------
    # Time test for iterative_adjacency_dict_dfs
    def test_iterative_adjacency_dict_dfs(graphs):
        """ Test iterative_adjacency_dict_dfs """
        for graph in graphs:
            iterative_adjacency_dict_dfs(graph, 0)

    iterative_adjacency_dict_dfs_time = round(measure_execution_time(
        test_iterative_adjacency_dict_dfs,
        graphs_dict
    ), 5)
    print(f"> {iterative_adjacency_dict_dfs_time = } s")

    # --------------------------------------------
    # Time test for recursive_adjacency_dict_dfs
    def test_recursive_adjacency_dict_dfs(graphs):
        """ Test recursive_adjacency_dict_dfs """
        for graph in graphs:
            recursive_adjacency_dict_dfs(graph, 0)

    recursive_adjacency_dict_dfs_time = round(measure_execution_time(
        test_recursive_adjacency_dict_dfs,
        graphs_dict
    ), 5)
    print(f"> {recursive_adjacency_dict_dfs_time = } s")

    # --------------------------------------------
    # Time test for recursive_adjacency_matrix_dfs
    def test_recursive_adjacency_matrix_dfs(graphs):
        """ Test recursive_adjacency_matrix_dfs """
        for graph in graphs:
            recursive_adjacency_matrix_dfs(graph, 0)

    recursive_adjacency_matrix_dfs_time = round(measure_execution_time(
        test_recursive_adjacency_matrix_dfs,
        graphs_matrix
    ), 5)
    print(f"> {recursive_adjacency_matrix_dfs_time = } s")

    # --------------------------------------------
    # Time test for adjacency_matrix_radius
    def test_adjacency_matrix_radius(graphs):
        """ Test adjacency_matrix_radius """
        for graph in graphs:
            adjacency_matrix_radius(graph)

    adjacency_matrix_radius_time = round(measure_execution_time(
        test_adjacency_matrix_radius,
        graphs_matrix
    ), 5)
    print(f"> {adjacency_matrix_radius_time = } s")

    # --------------------------------------------
    # Time test for adjacency_dict_radius
    def test_adjacency_dict_radius(graphs):
        """ Test adjacency_dict_radius """
        for graph in graphs:
            adjacency_dict_radius(graph)

    adjacency_dict_radius_time = round(measure_execution_time(
        test_adjacency_dict_radius,
        graphs_dict
    ), 5)
    print(f"> {adjacency_dict_radius_time = } s")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    for i in range(50, 500, 50):
        run_time_analyze(i, 10)
