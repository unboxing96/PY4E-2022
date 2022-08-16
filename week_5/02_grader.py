

def grader(s, a):

    # [[학생A, 점수], [학생B, 점수], [학생C, 점수], [학생D, 점수], [학생E, 점수]]
    student_list = []
    for s_ in s:
        student_list.append(s_.split(","))

    for student in student_list:
        score = 0
        # 정답 개수만큼 반복
        for i in range(len(student[1])):
            # student[1]을 탐색하며, 정답과 일치 시 score += 10 (타입 일치 유의)
            if student[1][i] == str(a[i]):
                score += 10
        # 한 학생 탐색 종료 시, student에 점수 append
        student.append(score)

    # 점수를 기준으로 내림차순 정렬
    student_list.sort(reverse=True, key=lambda x : x[2])

    for i in range(len(student_list)):
        print(f"학생: {student_list[i][0]}, 점수: {student_list[i][2]}점, {i+1}등")
    
    return True


# 학생 답

s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]
 
# 정답지
a = [3,2,4,2,5,2,4,3,1,2]


# 입력
grader(s, a)