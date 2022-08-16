# 글a[단어word 위치 + 문자열 길이: ]의 반복

def count_word(a, word):

    # 문서 생성
    txt = open("count_word.txt", "w")
    txt.write(a)
    txt.close

    # 초기 인덱스는 0으로 설정
    start_index = 0
    cnt = 0

    # 인덱스 값이 글의 길이보다 작을 때
    while start_index <= len(a):
        
        if word in a: # 글a 안에 단어word가 있을 때
            cnt += 1 #개수를 카운트
            a = a[a.index(word) + len(word): ] # 글a 를 단어word 이후로 슬라이싱
        else: # 없으면 종료
            break

    print(cnt)
    return True

# 입력

a ="""안녕하세요. 
반갑습니다. 파이썬 공부는 정말 재밌습니다.
"""

count_word(a, "습니다")