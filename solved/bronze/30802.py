N = int(input())
 
size_list = list(map(int, input().split()))

total_bundles = 0

T, P = map(int, input().split())

for size_count in size_list:
    bundles = (size_count + T - 1) // T  # 올림 계산
    total_bundles += bundles

# 몫 구하기
quotient = N // P  
# 나머지 구하기  
remainder = N % P  

print(total_bundles)
print(f"{quotient} {remainder}") 

