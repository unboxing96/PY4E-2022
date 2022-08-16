def wrong_guest_book(guest_book):
    
    # 문서 생성
    f = open("wrong_guest_book.txt", "w")
    f.write(guest_book)
    f.close()

    # 생성한 문서 읽기
    ff = open("wrong_guest_book.txt", "r")
    lines = ff.readlines() # ['김갑,123456789\n', '이을,010-1234-5678\n', '박병,010-5678-111\n', '최정,111-1111-1111\n', '정무,010-3333-3333']

    for line in lines:
        line = line.strip()                              # 문자열 끝에 개행(\n) 지워줌
        name, number = line.split(",")
        if number[:3] == "010":                          # 조건1
            if number[3] == "-" and number[8] == "-":    # 조건2
                if len(number) == 13:                    # 조건3
                    continue                             # 충족하면 pass, 아니라면 잘못 쓴 방명록 출력
        
        print(f"잘못 쓴 사람: {name}")
        print(f"잘못 쓴 번호: {number}")
        print("")

    return True

# 입력
guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

wrong_guest_book(guest_book)

