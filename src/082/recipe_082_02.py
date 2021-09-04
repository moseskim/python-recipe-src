fruits_list = ["바나나", "사과", "귤"]
for fruit in map(lambda x: "★" + str(x) + "★", fruits_list):
    print(fruit)
