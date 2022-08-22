# 평균 점수를 값으로 하는 딕셔너리 생성
# 2중 반복문으로 값에 순위 추가
# 조건대로 출력

def sales_management(member_names, member_records):

    # dic = {key = 이름 : value = 평균 실적}
    dic = {}
    for i in range(6):
        dic[member_names[i]] = sum(member_records[i]) / len(member_records[i])

    # rank_dic = {key = 이름, value = (순위rank, 평균 실적)}
    rank_dic = {}
    # dic을 완전 탐색으로 순회: 
    # 1번을 1번, 2번, 3번, 4번, 5번, 6번과 비교하여 평균 실적이 더 작으면 순위rank += 1
    for k, v in dic.items():
        rank = 1
        for kk, vv in dic.items():
            if v < vv:
                rank += 1
        # 새로운 딕셔너리rank_dic에 (순위, 평균 실적) 순서로 value 저장
        # 기존 딕셔너리dic에 저장하면, 비교 연산자 실행 시 TypeError 발생
        # {'갑돌이': (3, 4.0), '갑순이': (1, 2.8333333333333335)...}
        rank_dic[k] = rank, v
    
    # 조건에 맞춰서 리스트 추가
    # good: 보너스 대상자
    # bad: 면담 대상자
    good = []
    bad = []

    for k, v in rank_dic.items():
        if v[0] in [1, 2]:              # v[0] = rank
            if v[1] > 5:                # v[1] = 평균 실적
                good.append(k)          # k = 이름

        if v[0] in [5, 6]:
            if v[1] <= 3:
                bad.append(k)
    
    # 출력 형식
    for i in good:
        print(f"보너스 대상자: {i}")
    
    print("")

    for i in bad:
        print(f"면담 대상자: {i}")

    return True



# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

# 입력
sales_management(member_names, member_records)