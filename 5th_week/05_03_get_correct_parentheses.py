from collections import deque

balanced_parentheses_string = "()))((()"

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.

# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
# 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.

# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.

# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

def is_correct_parenthsis(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthsis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)


    return

def change_to_correct_parentheses(string):
    if string == "":
        return ''
    u, v = seperate_to_u_v(string)
    if is_correct_parenthsis(u):
        return u + change_to_correct_parentheses(v)
    return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])

def seperate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(queue))
    return u, v

def reverse_parentheses(string):
    reversed_parentheses_string = ""
    for char in string:
        if char == "(":
            reversed_parentheses_string += ")"
        else:
            reversed_parentheses_string += "("

    return reversed_parentheses_string

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))
