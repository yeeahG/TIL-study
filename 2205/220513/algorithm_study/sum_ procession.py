# 예지
# --이렇게 끄적이다가 못품--
answer = [[] for j in range(len(arr1))]
answer
[[], []]

answer[0].append(arr1[0][0]+arr2[0][0])
answer
[[4], []]

answer[0].append(arr1[0][1]+arr2[0][1])
answer
[[4, 6], []]

answer[1].append(arr1[1][0]+arr2[1][0])
answer
[[4, 6], [7]]

answer[1].append(arr1[1][1]+arr2[1][1])
answer
[[4, 6], [7, 9]]


# 준석
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A

# 은혁

