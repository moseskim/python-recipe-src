dl = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(dl)
print(dl[1])      # 0에서 시작해 1번째 리스트를 참조
print(dl[1][0])   # 0에서 시작해 1번째 리스트의 0번째 요소를 참조
dl[1][0] = "X"    # 0에서 시작해 1번째 리스트의 0번째 요소를 업데이트
print(dl)
