input = 20


def find_prime_list_under_number(number):
    prime_list = []
    # 소수는 1과 자기 자신말고 다른 정수와 나눠질 수 없다.
    for n in range(2, number + 1):  # 2 ~ number, 20 미만 숫자 구하기
        for i in prime_list:   # 20 미만인 숫자 중에서 i로 나눴을 때의 소수 구하기
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)