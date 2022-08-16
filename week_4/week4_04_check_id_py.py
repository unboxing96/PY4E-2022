# 분기점 설정이 핵심
# 타입에 유의

def check_id(a):

    isBool = True # 분기점마다 조건에 True False 확인 위한 변수
    front, back = a.split("-") # "-" 기준으로 앞자리, 뒷자리 변수 할당

    if a[6] == "-" and len(a) == 14: # 조건1

        if back[0] == "1" or back[0] == "3": # 조건2, 타입에 유의
            gender = "남자"
        elif back[0] == "2" or back[0] == "4":
            gender = "여자"
        else:
            isBool = False # 뒷자리 첫 글자가 0, 1, 3, 4가 아니면 False
    
    if isBool: # False가 아닐 때만 진행
    
        if 0 <= int(front[:2]) <= 21: # 조건3, 타입에 유의
            answer = input("2000년 이후 출생자인가요? (O, X) ") 

            if answer != "O": # O가 아니면, False
                isBool = False

    if isBool: # False가 아닐 때만 진행
        print(f"{front[:2]}년 {front[2:4]}월 {gender}", end="\n")
        print("")

    else:
        print("잘못된 번호입니다.")
        print("올바른 번호를 입력해주세요.")
        print("")

# 입력
a = "500629-2222222"
check_id(a)