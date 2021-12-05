import codecs

u_text = "\uc81c\uc774\ud38d"
text = codecs.decode(u_text.encode())
print(text)
