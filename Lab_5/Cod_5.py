graph_1 = "2.txt"
graph_2 = "3.txt"

# маса матриці
def mass_to_matrix(mass):
    matrix = []
    for i in mass:
        matrix.append([int(x) for x in i.split(" ") if x.isdigit()])
    return matrix



def txt_reader(path):
    file = open(path, "r")
    text = file.read()
    mass = text.split("\n")
    return mass_to_matrix(mass)


def isomorphic(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        return False

    row_sum_1 = [sum(row) for row in matrix_1]
    row_sum_2 = [sum(row) for row in matrix_2]
    col_sum_1 = [sum(col) for col in zip(*matrix_1)]
    col_sum_2 = [sum(col) for col in zip(*matrix_2)]
    if sorted(row_sum_1) != sorted(row_sum_2) or sorted(col_sum_1) != sorted(col_sum_2):
        return False

    row_degrees_1 = sorted([row_sum_1[i] for i in range(len(row_sum_1))])
    row_degrees_2 = sorted([row_sum_2[i] for i in range(len(row_sum_2))])
    col_degrees_1 = sorted([col_sum_1[i] for i in range(len(col_sum_1))])
    col_degrees_2 = sorted([col_sum_2[i] for i in range(len(col_sum_2))])
    invariant_1 = ''.join([str(i) for i in row_degrees_1]) + ''.join([str(i) for i in col_degrees_1])
    invariant_2 = ''.join([str(i) for i in row_degrees_2]) + ''.join([str(i) for i in col_degrees_2])

    return invariant_1 == invariant_2

#Ведення матриці
def print_matrix(matrix):
    for i in matrix:
        print(i)

if __name__ == '__main__':
    matrix_1 = txt_reader(graph_1)
    matrix_2 = txt_reader(graph_2)


    res = isomorphic(matrix_1, matrix_2)

#Виведення матриці
    print_matrix(matrix_1)
    print()
    print_matrix(matrix_2)
    print()

    if res:
        print("Ці матриці ізоморфічні")
    else:
        print("Ці матриці не є ізоморфічні")
