import re

text = """101 CF001    커피
102 CF002    커피(대용량)
201 TE01     홍차
202 TE02     홍차(대용량A)
203 TE02     홍차(대용량B)"""

items = re.findall(r'([0-9]+) +([0-9A-Z]+) +(.*)', text)
print(items)
