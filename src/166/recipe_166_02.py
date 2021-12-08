def full_to_half(full):
  full_code = ord(full)
  start_code = int('0xfee0', 16)  # 전각 시작 코드
  space_code = int('0x3000', 16)  # 전각 공백

  if full_code >= start_code:
      result = full_code - start_code
  elif full_code == space_code:
      result = 32  # 0x0020
  else:
      result = full_code

  return chr(result)

text = 'ｐｙｔｈｏｎ! ３０２ ２０２１－０２－０５'
print(''.join(list(map(full_to_half, text))))
