# 청구 요금 계산 함수
def calc_billing_amount(unit_prices, units, fees, tax_rate):
    return (unit_prices * units + fees) * tax_rate


x = calc_billing_amount(100, 10, 50, 1.1)
print(x)
