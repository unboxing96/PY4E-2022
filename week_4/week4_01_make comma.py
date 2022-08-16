# 정수형을 문자열로 변환
# 뒤에서부터 인덱싱하여 3자리마다 쉼표

def make_comma(num):
    # 메서드 활용을 위해 num 인자를 문자형으로 형변환
    str_num = str(num)

    # comma를 최초로 삽입할 위치를 구하기 위해, 문자열 길이를 3으로 나눈 나머지를 구함
    # 나머지 0이면 index: 3부터 시작
    # 이외에는, index: 나머지 값부터 시작
    if len(str_num) % 3 == 0:
        start_index = 3
    else:
        start_index = len(str_num) % 3

    # comma를 삽입할 인덱스가 문자열의 길이가 작을 때,
    # 인덱스를 4씩 증가시키며, comma 삽입
    # 3이 아니라 4인 이유: "," 문자열이 삽입되기 때문
    while start_index < len(str_num):
        str_num = str_num[:start_index] + "," + str_num[start_index:]
        start_index += 4

    print(str_num)

    return True

# 입력
make_comma(100000000)