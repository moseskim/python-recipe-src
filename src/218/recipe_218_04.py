import zipfile

with zipfile.ZipFile('sample2.zip', 'r')as zf:
    zf.extractall(r'.\output', pwd=b'password')
