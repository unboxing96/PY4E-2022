


def yearly_payment(monthly_payment):

    #세전 연봉 = 월급 * 12
    sejeon = monthly_payment * 12

    if sejeon <= 1200:
        sehoo = sejeon * (1-0.06)
    elif sejeon <= 4600:
        sehoo = sejeon * (1-0.15)
    elif sejeon <= 8800:
        sehoo = sejeon * (1-0.24)
    elif sejeon <= 15000:
        sehoo = sejeon * (1-0.35)
    elif sejeon <= 30000:
        sehoo = sejeon * (1-0.38)
    elif sejeon <= 50000:
        sehoo = sejeon * (1-0.40)
    else:
        sehoo = sejeon * (1-0.42)

    print(f"세전 연봉: {sejeon: .0f}만원")
    print(f"세후 연봉: {sehoo: .0f}만원")

    return True


monthly_payment = 300
yearly_payment(monthly_payment)