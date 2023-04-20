path = "2-1.txt"
matrix_size = 0
vis = []
dist = 0


def mass_to_matrix(mass):
    global matrix_size
    global vis
    matrix_size = int(mass.pop(0))
    vis = [False for i in range(matrix_size)]
    matrix = []
    for i in mass:
        matrix.append([int(x) for x in i.split(" ") if x.isdigit()])
    return matrix
def txt_reader(path):
    file = open(path, "r")
    text = file.read()
    mass = text.split("\n")
    return mass_to_matrix(mass)


def DFS(matrix, u, vis, dist):
    vis[u] = True

    for i in range(matrix_size):
        if matrix[u][i] != 0 and not vis[i]:
            dist[0] += matrix[u][i]
            print(dist[0])
            DFS(matrix, i, vis, dist)


def postman(matrix):
    vis = [False] * matrix_size
    dist = [0]

    DFS(matrix, 0, vis, dist)

    for i in range(matrix_size):
        if not vis[i]:
            return -1

    return dist[0]


if __name__ == '__main__':
    matrix = txt_reader(path)
    shortest = postman(matrix)
    if shortest != -1:
        print(f"Найкоротший шлях дорівнює = {shortest}")
    else:
        print("Шлях не знайдено")
