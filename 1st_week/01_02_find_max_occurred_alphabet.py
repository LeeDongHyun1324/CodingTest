#문자열 최빈값(가장 많이 나온 값) 찾기

# 완전 탐색 (Brute-force)
# def find_max_occurred_alphabet(string):
#     alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
#                       "t", "u", "v", "w", "x", "y", "z"]
#
#     max_occurrence = 0
#     max_alphabet = alphabet_array[0]
#
#     for alphabet in alphabet_array:
#         occurrence = 0
#         for char in string:
#             if char == alphabet:
#                 occurrence += 1
#
#         if occurrence > max_occurrence:
#             max_occurrence = occurrence
#             max_alphabet = alphabet
#
#     return max_alphabet

# 카운팅 정렬 기법 응용 (Counting-based approach)
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))

def find_alphabet_occurrence(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1





result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 = ", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 = ", result("we love algorithm"))
print("정답 = b 현재 풀이 값 = ", result("best of best youtube"))