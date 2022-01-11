# 청구 요금 계산 함수
def calc_billing_amount(unit_prices, units, fees, tax_rate):
    return (unit_prices * units + fees) * tax_rate


x = calc_billing_amount(tax_rate=1.1, units=10, fees=50, unit_prices=100)
print(x) 