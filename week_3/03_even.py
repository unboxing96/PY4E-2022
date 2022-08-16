# 2개 숫자 사이 짝수만 출력
# 중앙값 짝수면? 출력 홀수면? pass


# 중앙값 
def median(a, b):

    num_li = range(a, b+1)

    if len(num_li) % 2 == 0: # 짝수일 떄, 중앙값: 평균
        result = (a + b) / 2
    else:
        result = num_li[int(len(num_li) / 2)] # 홀수일 때, 중앙값: 가운데 index 값
        
    return result


def find_even_number(n, m):

    print("")
    print(f"첫 번째 수 입력: {n}")
    print(f"첫 번째 수 입력: {m}")

    med = median(n, m) # 중앙값을 미리 구함

    num = []
    for num in range(n, m+1):
        if num % 2 == 0: # 짝수일 때만 출력

            if num == med: # 입력 받은 숫자가 중앙값이면 출력
                print(f"{num} 중앙값")
            
            print(f"{num} 짝수")
    
    return True

# 입력
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)
