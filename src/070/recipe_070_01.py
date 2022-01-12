# 청구 요금 계산 함수
def calc_billing_amount(unit_prices, units, fees, tax_rate):
    return (unit_prices * units + fees) * tax_rate


# 위치 인수를 이용한 함수 호출(단가 1000원, 수량 1개, 수수료 500원, 소비세율 1.1)
x = calc_billing_amount(100, 10, 50, 1.1)

# 결과 출력
print(x)
