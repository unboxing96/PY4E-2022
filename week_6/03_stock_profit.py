# .split(",")
# .split("/")
# 수익률 계산 (수익률 = (매도 평균가 - 매수 평균가) / 매수 평균가 * 100)
# 수익률 기준으로 정렬,lambda


def stock_profit(stocks, sells):
    # 종목 별로 split
    # ['삼성전자/10/85000', '카카오/15/130000', 'LG화학/3/820000', 'NAVER/5/420000']
    stock_list = stocks.split(",")

    # 최종 결과 리스트
    final = []

    for i in range(len(stock_list)):
        # 종목명, 개수, 매수가로 split
        name, ea, buy_price = stock_list[i].split("/")
        
        buy_price = int(buy_price)          # int로 매수가 형변환
        sell_price = sells[i]               # index로 매도가 변수에 할당
        
        # 수익률 계산
        PnL = (sell_price - buy_price) / buy_price * 100
        
        # 이름, 수익률 순으로 저장
        final.append([name, PnL])
    
    # 수익률을 기준으로, 내림차순 정렬
    final.sort(key = lambda x: x[1], reverse=True)

    # 출력 형식
    for stock in final:
        print(f"{stock[0]}의 수익률: {stock[1] : .3}")
        
    return True



# 입력
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stock_profit(stocks, sells)