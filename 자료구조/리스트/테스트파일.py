def last_index_of(element):
    for i in range(len(list)):
        if element == list[i]:
            index = list.index(element)
            print("인덱스", index)
    return ""


# print("사이즈 => ", len(list))
# last_index = list.remove(list)

# print ("마지막 인덱스 ", last_index)
list = ["20", "4", "22", "44", "22"]

print("역순 정렬 ", last_index_of("22"))

print("인덱스 찾기 ", list.index("44"))