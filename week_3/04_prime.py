# 소수의 개수 출력
# range(n, m+1) 반복
# (이중 for) 반복문 요소 num을 range(2, num)로 반복
# num % i == 0이면 카운트
# 카운트 0이면 result 카운트

def count_prime_number(n, m):

    if n < 2: # 소수는 2부터
        n = 2
    
    result = 0 # 마지막에 출력할 '소수개수' 변수
    for num in range(n, m+1):
        
        num_cnt = 0 # 반복 요소 num이 소수인지 검증하기 위한 변수
        for i in range(2, num): # 자기 자신을 빼야 하니까 range(2, num)
            if num % i == 0:
                num_cnt += 1
        
        if num_cnt == 0: # 반복문 다 돌았는데 약수가 0개면
            result += 1

    print(f"소수개수 {result}")
    return True

# 입력
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)