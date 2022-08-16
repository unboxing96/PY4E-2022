
#컴퓨터
import random




def rsp(my):
    computer = random.randint(0, 2)
    
    #한글로 입력 시, 비교를 위해 숫자로 변환
    if my == "가위":
        my = 0
    
    elif my == "바위":
        my = 1
    
    elif my == "보":
        my = 2

    #케이스마다 결과값 반환
    if computer == my:
        result = "무승부!"
    # 차이가 1일 때 뿐만 아니라, -2일 때도 같은 결과
    elif computer - my == 1 or computer - my == -2:
        result = "컴퓨터 승리!"
    else:
        result = "나의 승리!"

    print(f"나: {my}")
    print(f"컴퓨터: {computer}")
    print(result)

    return True


my = input("하나를 선택하여 입력하세요('가위(0)', '바위(1)', '보(2)'): ")
rsp(my)
