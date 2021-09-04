count = 0


def func():
    global count
    count += 1
    print("실행 횟수: {}회".format(count))


func()
func()
print("count 값: {}".format(count))
