# 이중 for문으로 '함수' 구현 <- input()이 주어지므로, 이중 for문 필요X
# 홀수만 출력
# 결과가 50 이하일 때만 출력

def gugudan(number):

    while number not in range(2, 10): # input()을 2~9 사이 정수값을 받기 위함
        print("2 ~ 9 범위의 숫자를 입력해 주세요.")
        number = int(input("몇 단? : "))

    i = number # 구구단의 첫 번째 항 (2 ~ 9)
    for j in range(1, 10): # 구구단의 두 번째 항 (1 ~ 9)
        result = i * j # 결과
        if j % 2 == 0: # 짝수 번째이면, 처음으로 돌아감
            continue 
        if result <= 50: # 결과가 50 이하일 때만 출력
            print(f"{i} X {j} = {result}")
    
    return True

# 입력
number = int(input("몇 단? : "))
gugudan(number)