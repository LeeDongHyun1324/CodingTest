input = [4, 6, 2, 9, 1]

# 배열의 크기를 1개씩 점차 늘려서 비교하여 삽입 
# [4]
# [4, 6]
# [4, 6, 2] -> [4, 2, 6] -> [2, 4, 6]
# ...
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j] < array[i - j - 1]: # i번째에서 j번째만큼 떨어진 인덱스 
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))