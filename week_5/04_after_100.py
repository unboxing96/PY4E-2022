# 달의 마지막 날 리스트
# 지금까지 날짜를 구하는 함수 (년도 바뀌는 것 고려)
# 요일 계산하는 함수

def after_100(month, day, yoil):

    # 출력용 변수
    old_month = month
    old_day = day
    old_yoil = yoil

    # 달의 마지막 날 리스트 (M[0] = 1월, M[1] = 2월, ...)
    M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 요일 리스트
    YO_list = ['월','화','수','목','금','토','일']

    cnt = 1

    # cnt가 100일이 될 때까지, 날짜day가 달month의 마지막 날이 되면 day = 1, month += 1
    while cnt < 100:
        if day == M[month - 1]:
            month += 1
            day = 1
            cnt += 1
            # 12월이 넘어가면 month = 1 초기화
            if month > 12:
                month = 1
        else:
            day += 1
            cnt += 1
    
    # 요일 계산 (입력 받은 요일의 인덱스 + 100을 7로 나눈 나머지 - 인덱스 자리 값(1))
    yoil = YO_list[YO_list.index(yoil) + (100 % 7) - 1]

    print("")
    print(f"{old_month}월 {old_day}일 {old_yoil}요일부터 100일 뒤는 {month}월 {day}일 {yoil}요일")
    print("")

    return True

# 입력
after_100(12, 21, "수")