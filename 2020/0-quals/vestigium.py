import numpy as np

test_cases = int(input())

matrices = []

for case in range(test_cases):
    matrix_size = int(input())
    li = []
    for _ in range(matrix_size):
        line = input().split(" ")
        t = []
        for number in line:
            t.append(int(number))
        li.append(t)
    matrices.append([matrix_size, np.array(li, np.int32)])

for case_number, data in enumerate(matrices):
    matrix_size = data[0]
    matrix = data[1]

    # Compute the trace
    trace = 0
    for i in range(matrix_size):
        trace += matrix[i, i]

    # Find rows with repeated elements
    rows_with_duplicates = 0
    for row in range(matrix_size):
        seen = []
        for number in matrix[row]:
            if number in seen:
                rows_with_duplicates += 1
                break
            else:
                seen.append(number)

    # Find columns with repeated elements
    cols_with_duplicates = 0
    for col in range(matrix_size):
        seen = []
        for number in matrix[:,col]:
            if number in seen:
                cols_with_duplicates += 1
                break
            else:
                seen.append(number)

    print("Case #{}: {} {} {}".format(case_number+1, trace, rows_with_duplicates, cols_with_duplicates))