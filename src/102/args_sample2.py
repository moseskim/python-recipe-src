from sys import argv

if 3 <= len(argv):
    print(argv[0])
    print(argv[1])
    print(argv[2])
else:
    print("인수를 3개 입력해 주십시오.")
