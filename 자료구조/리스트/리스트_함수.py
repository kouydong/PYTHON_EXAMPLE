# len(리스트) 함수를 이용 하여 배열 요소의 크기 확인
name = ['홍길동', '임꺽정', '고길동', '신사임당']
print(len(name))  # 4

# list.append(element) : '리스트' 마지막 위치에 '요소' 추가
name.append("둘리")
print("이름들 :", name)  # ['홍길동', '임꺽정', '고길동', '신사임당', '둘리']

# list.insert(index, element) : '리스트' 특정 '인덱스'에 '요소' 추가(이후 요소의 인덱스 n+1)
name.insert(2,"장영실")
print("이름들 :", name)  # ['홍길동', '임꺽정', '장영실', '고길동', '신사임당', '둘리']

# list.pop(index) : '리스트' 요소 index 위치에 요소 반환 후 요소 제거
print("4번째 이름 :", name.pop(4))
print("이름들 :", name)

# list.remove(element) : '리스트' 내에서 '요소' 찾아 제거
name.remove("고길동")
print("이름들 :", name)








