import random

def guess_number():

    # 숫자 3개 생성
    number_list = []
    for _ in range(3):
        number_list.append(random.randint(0, 100))

    # 오름차순 정렬
    number_list.sort()

    # 최소, 중간, 최대
    number_name = ["최솟값", "중간값", "최댓값"]

    # 사용된 숫자 리스트
    used_number = []

    # 시도 횟수 카운트
    cnt = 1

    while True:

        print("")
        print(f"{cnt}차 시도")
        my = int(input("숫자를 예측해보세요: "))
        print("")

        cnt += 1

        if my in number_list:
            # number_list의 index를 number_name에 넣어, 최소 중간 최대 구분
            print(f"숫자를 맞추셨습니다! {my}는 {number_name[number_list.index(my)]}입니다.")
            print("게임 종료")
            print(f"{cnt}번 시도만에 예측 성공")
            break
        
        else:
            if my in used_number:
                print("이미 예측에 사용한 숫자입니다.")
            else:
                used_number.append(my)
                print(f"{my}는 없습니다.")
                
                if my < number_list[0]:
                    print(f"{my}는 최솟값보다 작습니다.")
                elif number_list[0] < my < number_list[1]:
                    print(f"{my}는 최솟값보다 크고, 최댓값보다 작습니다.")
                else:
                    print(f"{my}는 최댓값보다 큽니다.")
            continue
    
    return True

# 입력
guess_number()