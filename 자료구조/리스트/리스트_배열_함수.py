items = []


def insert(index, element):
    # items 배열 특정 index 위치에 새로운 element 추가
    items.insert(index, element)


def delete(index):
    # items 배열 삭제
    return items.pop(index)


def getEntry(index):
    # index 위치에 element 추출
    return items[index]


def isEmpty():
    # items 배열 길이 리턴
    return len(items) == 0


def size():
    # items 배열  길이 리턴
    return len(items)


def clear():
    # items 배열 초기화(전역 변수로 선언 후 초기화 가능)
    items = []


def find(index):
    # items 배열 인덱스 값 반환??
    return items.index(index)


def replace(index, element):
    # items 배열 특정 인덱스에 새로운 요소 추가
    items[index] = element


def sort():
    # items 배열 오름 차순 정렬
    items.sort()


def merge(element):
    # items 배열 값 추가
    items.extend(element)


# 디폴트 메시지
def display(msg="ArrayList"):
    # 메시지, 사이즈, items 배열 내용 출력
    print(msg, size(), items)


insert(0, 10)       # [10]
insert(0, 20)       # [20, 10]
insert(size(), 40)  # [20, 10, 40]
insert(2, 50)       # [20, 10, 50, 40]
display("배열 리스트 insert() 함수 테스트")


sort()              # [10, 20, 40, 50]
display("배열 리스트 sort() 함수 테스트")

replace(2, 90)      # [10, 20, 90, 50]
display("배열 리스트 items[index] 함수 테스트")

# 한줄에 여러 문장을 표시할 경우 ';'를 사용
delete(2);delete(size() -1);delete(0)
display("배열 리스트 pop() 함수 테스트")

anotherItems = [1,2,3]
merge(anotherItems)
display("배열 리스트 extend() 함수 테스트")

clear()
display("배열 리스트 목록 전체 삭제")











