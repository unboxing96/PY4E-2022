# 풀이1. 
# from Collections import Counter

# 풀이2.
# kora_king, chosun_king 각각 반복문 돌며 딕셔너리에 추가하며 초기 값 1 설정
# 이미 포함 되어있으면 += 1
# 딕셔너리를 순회하며, 값이 2 이상인 키만 출력 (정종이 3명)

def king(korea_king, chosun_king):
    
    dic = {}

    # 문자열 -> "," 기준 구분한 리스트로
    # ['태조', '혜종', '정종', '광종', '경종' ...]
    korea_king = list(korea_king.split(","))
    chosun_king = list(chosun_king.split(","))

    # 리스트 순회하며, 없으면 추가 후 초기 값: 1, 있으면 += 1
    for kk in korea_king:
        if dic.get(kk, 0):
            dic[kk] += 1
        else:
            dic[kk] = 1

    # 리스트 순회하며, 없으면 추가 후 초기 값: 1, 있으면 += 1
    for ck in chosun_king:
        if dic.get(ck, 0):
            dic[ck] += 1
        else:
            dic[ck] = 1
    
    # 딕셔너리 순회하며, 값이 2 이상인 key를 출력
    # 조건 충족할 때마다 cnt += 1
    cnt = 0
    for k in dic.keys():
        if dic[k] >= 2:
            print(f"조선과 고려에 모두 있는 왕 이름: {k}")
            cnt += 1
    
    # 중복되는 왕 이름 수인 cnt 출력
    print(f"조선과 고려에 모두 있는 왕 이름은 총 {cnt}개 입니다")

    return True


# 왕이름
korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

# 입력
king(korea_king, chosun_king)
