# 조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
# 조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
# 조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기

import random

# 1. rsp_advanced()에서 변수를 위해 input() 값을 정수형으로 치환하게 됨.
# 2. 이후 '무엇을 냈는지' 출력하기 위헤, input() 값에 해당하는 "가위", "바위", "보"를 반환하는 함수
def num_to_rsp(int): 
    if int == 0:
        result = "가위"
    elif int == 1:
        result = "바위"
    elif int == 2:
        result = "보"
    
    return result
    

def rsp_advanced(games):

    my_result = [0, 0, 0] # 승 무 패
    computer_result = [0, 0, 0] # 승 무 패

    for i in range (1, games + 1):

        computer = random.randint(0, 2)
        my = input("'가위(0), 바위(1), 보(2)' 중에 하나를 선택해 입력해주세요: ")
        
        correct = ["가위", "바위", "보", "0", "1", "2"] # 다른 입력 받으면 재입력 받기
        while my not in correct:
            my = input("'가위(0), 바위(1), 보(2)' 중에 하나를 선택해 입력해주세요: ")

        if my == "가위" or my == "0": # 조건문 쉽게 하기 위해, 입력값을 정수로 변환
            my = 0
        elif my == "바위" or my == "1":
            my = 1
        elif my == "보" or my == "2":
            my = 2

        battle = my - computer # 승패 계산용 변수

        if battle == -1 or battle == 2: # 컴퓨터 승리
            computer_result[0] += 1 # 컴퓨터 1승 추가
            my_result[2] += 1 # 나 1패 추가
            battle_result = "컴퓨터의 승리!"

        elif battle == 1 or battle == -2: # 나의 승리
            computer_result[2] += 1 #컴퓨터 1패 추가
            my_result[0] += 1 # 나 1승 추가
            battle_result = "나의 승리!"

        elif battle == 0: # 무승부
            computer_result[1] += 1 # 컴퓨터 1무 추가
            my_result[1] += 1 # 나 1무 추가
            battle_result = "무승부!"
        
        print("")
        print(f"가위 바위 보: {i-1}")
        print(f"나: {num_to_rsp(my)}")
        print(f"컴퓨터: {num_to_rsp(computer)}")
        print(f"{i} 번째 판 {battle_result}", "\n")
    
    # 총 전적
    print(f"나의 전적: {my_result[0]}승 {my_result[1]}무 {my_result[2]}패")
    print(f"컴퓨터의 전적: {computer_result[0]}승 {computer_result[1]}무 {computer_result[2]}패")

    return True

# 입력
games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)