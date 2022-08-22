# 풀이 1. 정규 표현식
# 풀이 2. 6개씩 끊어서

def good_customer(info):
    customers = info.split(",")

    # 중복 없이 1개만 사용된 문자인 .count("세") 만큼 반복해서 빈 리스트 생성
    customer_list = [[] for _ in range(info.count("세"))]

    # 반복하며 문자열을 "," 기준으로 6개씩 묶은 리스트 생성
    # [['abc', '21세', '010-1234-5678', '남자', '서울', '5'], 
    #  ['cdb', '25세', 'x', '남자', '서울', '4'] ...]
    for i in range(len(customers)):
        idx = i // 6               # 6으로 나눈 몫을 기준으로 6개마다 끊어줌
        customer_list[idx].append(customers[i])
    
    # 출력 형식에 맞춰 dic 생성
    dic = {
        "아이디" : [],
        "나이" : [],
        "전화번호" : [],
        "성별" : [],
        "지역" : [],
        "구매횟수" : []
    }

    # 조건에 맞춰 값 append
    for customer in customer_list:
        
        if customer[2] == "x":
            customer[2] = "000-0000-0000"

        dic["아이디"].append(customer[0])
        dic["나이"].append(customer[1])
        dic["전화번호"].append(customer[2])
        dic["성별"].append(customer[3])
        dic["지역"].append(customer[4])
        dic["구매횟수"].append(int(customer[5]))
    
    print(dic)
    print("")

    #  조건에 맞춰 출력
    for customer in customer_list:
        if int(customer[5]) >= 8 and customer[2] != "000-0000-0000":
            print(f"할인 쿠폰을 받을 회원정보= 아이디: {customer[0]}, 나이: {customer[1]}, 전화번호: {customer[2]}, 성별: {customer[3]}, 지역: {customer[4]}, 구매횟수: {customer[5]}")


# 입력

# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

good_customer(info)