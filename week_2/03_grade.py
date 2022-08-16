def grader(name, score):
    
    #score는 정수로 형 변환
    score = int(score)

    if score < 60:
        grade = "F"
    elif score < 65:
        grade = "D"
    elif score < 70:
        grade = "D+"
    elif score < 75:
        grade = "C"
    elif score < 80:
        grade = "C+"
    elif score < 85:
        grade = "B"
    elif score < 90:
        grade = "B+"
    elif score < 95:
        grade = "A"
    else:
        grade = "A+"

    print(f"학생이름: {name}")
    print(f"점수: {score}점")
    print(f"학점: {grade}")



grader("이호창", 99)