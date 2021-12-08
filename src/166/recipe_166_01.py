import unicodedata

text = 'ｐｙｔｈｏｎ! ３０２ ２０２１－０２－０５'
print(unicodedata.normalize('NFKC', text))
