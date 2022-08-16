def bus_fare(age, payment):

    # age 정수형으로 형 변환
    age = int(age)

    if payment == "현금":
        if age < 8:
            charge = 0
        elif age < 14:
            charge = 450
        elif age < 20:
            charge = 1000
        elif age < 75:
            charge = 1300
        else:
            charge = 0
    
    elif payment == "카드":
        if age < 8:
            charge = 0
        elif age < 14:
            charge = 450
        elif age < 20:
            charge = 720
        elif age < 75:
            charge = 1200
        else:
            charge = 0

    print(f"나이: {age}세")
    print(f"지불유형: {payment}")
    print(f"버스요금: {charge}원")



bus_fare(30, "현금")