import random
import string

# ascii 문자열로 생성하는 경우
rtext1 = ''.join(random.choices(string.ascii_letters, k=5))
print(rtext1)

# ascii 문자와 숫자로 생성하는 경우
rtext2 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
print(rtext2)
