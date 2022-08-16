import random

def bs31():

    # 출력 형식
    print("")
    print("베스킨라빈스 써리원 게임")
    print("------------------")
    print("")
    
    # 현재 숫자latest 초기값 할당
    latest = 0

    while latest < 31:

        # 입력 받은 숫자를 리스트로 전환 (스페이스바를 기준으로 나눔)
        my = list(map(int, input("My turn - 숫자를 입력하세요: ").split()))

        # 예외1. 현재 숫자lastest와 연속된 숫자를 입력하지 않았을 경우
        if my != list(range(latest + 1, my[-1] + 1)):
            print("현재 숫자와 연속된 숫자를 입력하세요.")
            print("")
            continue

        # 예외2. 3개 보다 많은 숫자를 입력
        elif len(my) > 3:
            print("3개 이하의 숫자를 입력해주세요.")
            print("")
            continue
        
        # 예외3. 31 이상 숫자를 입력 -> 나의 패배, 컴퓨터의 승리!
        elif my[0] >= 31:
            print("컴퓨터의 승리!")
            print("")
            exit(0)

        # 마지막에 입력 받은 수를 -> 현재 숫자latest에 할당
        latest = my[-1]
        print(f"현재 숫자: {latest}")

        # 컴퓨터가 몇 번 반복할 건지 정하는 함수
        computer_turn_num = random.randint(1, 3)

        # 컴퓨터 반복 수만큼, 현재 숫자latest에 더해주고, 해당 값 출력
        # 현재 숫자lastest 31 이상이 되면 -> 컴퓨터의 패배, 나의 승리!
        for i in range(computer_turn_num):
            latest += 1
            print(f"컴퓨터: {latest}")
            if latest >= 31:
                print("나의 승리!")
                print("")
                exit(0)

        # 컴퓨터 반복 종료 후 현재 숫자latest 출력 
        print(f"현재 숫자: {latest}")
        print("")

# 입력
bs31()