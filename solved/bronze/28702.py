# 문제
# FizzBuzz 문제는 
# $i = 1, 2, \cdots$ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

#  
# $i$가 
# $3$의 배수이면서 
# $5$의 배수이면 “FizzBuzz”를 출력합니다.
#  
# $i$가 
# $3$의 배수이지만 
# $5$의 배수가 아니면 “Fizz”를 출력합니다.
#  
# $i$가 
# $3$의 배수가 아니지만 
# $5$의 배수이면 “Buzz”를 출력합니다.
#  
# $i$가 
# $3$의 배수도 아니고 
# $5$의 배수도 아닌 경우 
# $i$를 그대로 출력합니다.
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?

# 입력
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다. 각 문자열의 길이는 
# $8$ 이하입니다. 입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.

# 출력
# 연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요.

fizzbuzz = [input().strip() for _ in range(3)]

def fb_str(n: int) -> str:
    if n % 15 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)

# 1) 숫자가 포함된 경우: 그 숫자를 기준으로 인덱스 보정
for idx, s in enumerate(fizzbuzz):
    if s.isdigit():
        base = int(s)
        n0 = base - idx  # 첫 줄이 가리키는 실제 숫자
        print(fb_str(n0 + 3))
        break
else:
    # 2) 전부 단어인 경우: 주기 15를 이용해 매칭되는 시작점을 찾기
    for start in range(1, 16 * 2):  # 충분한 범위에서 탐색
        if fb_str(start) == fizzbuzz[0] and fb_str(start + 1) == fizzbuzz[1] and fb_str(start + 2) == fizzbuzz[2]:
            print(fb_str(start + 3))
            break