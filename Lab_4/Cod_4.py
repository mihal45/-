path = "4-2.txt"
matrix_size = None

def mass_to_matrix(mass):
    global matrix_size
    matrix_size = int(mass.pop(0))
    matrix = []
    for i in mass:
        matrix.append([int(x) for x in i.split(" ") if x.isdigit()])
    return matrix
def txt_reader(path):
    file = open(path, "r")
    text = file.read()
    mass = text.split("\n")
    return mass_to_matrix(mass)

def searching_BFS(s, f, parent):

    visited = [False] * (matrix_size)
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(matrix[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return True if visited[f] else False

def ford_falkerson(start, finish, matrix):
    parent = [-1] * (matrix_size)
    max_flow = 0

    while searching_BFS(start, finish, parent):

        path_flow = float("Inf")
        s = finish
        while(s != start):
            path_flow = min(path_flow, matrix[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = finish
        while(v != start):
            u = parent[v]
            matrix[u][v] -= path_flow
            matrix[v][u] += path_flow
            v = parent[v]

    return max_flow


if __name__ == '__main__':
    matrix = txt_reader(path)
    start = 0
    finish = 7
    res = ford_falkerson(start, finish, matrix)
    print(f"Maximum_flow   = {res}")
