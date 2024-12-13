"""
Lab 2
"""

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
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [1, 0]}, 2)
    [2, 0, 1]
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
    stack = [start]
    traversing = []

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
    """
    pass


def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass

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

def recursive_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> recursive_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass


def recursive_adjacency_matrix_bfs(graph: list[list[int]], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0]])
    2
    """
    pass


def adjacency_dict_radius(graph: dict[int: list[int]]) -> int:
    """
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [1]})
    2
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
