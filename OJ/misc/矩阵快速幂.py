def multiple(A, B)->list:
    n, m = len(A), len(A[0])
    r, c = len(B), len(B[0])
    if m != r:
        print("UNMATCHED MATRIXES")
    else:
        C = [[0 for _ in range(c)]for _ in range(n)]
        # 三重循环
        for i in range(n):
            for j in range(c):
                for k in range(m):
                    C[i][j] += A[i][k]*B[k][j]
        return C

def ksm(matrix, times)->list:
    if times <= 1:
        return matrix
    else:
        if times % 2 == 0:
            matrix = multiple(matrix, matrix)
        else:
            matrix = multiple(matrix, matrix)
            matrix = multiple(matrix, matrix)
        return ksm(matrix, int(times//2))

# 测试

li1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(ksm(li1, 3))
