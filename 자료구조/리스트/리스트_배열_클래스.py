class ArrayList:
    # 클래스 변수 선언 및 초기화
    def __init__(self):
        self.items = []

    def insert(self, index, element):
        self.items.insert(index, element)

    def delete(self, index):
        return self.items.pop(index)

    def isEmpty(self):
        return len(self.items) == 0

    def getEntry(self, index):
        return self.items[index]

    def clear(self):
        self.items = []

    def find(self, items):
        return self.items.index(items)

    def replace(self, index, element):
        self.items[index] = element

    def sort(self):
        self.items.sort()

    def size(self):
        return len(self.items)

    def merge(self, element):
        self.items.extend(element)

    def display(self, msg="ArrayList"):
        print(msg, "항목수=", len(self.items), self.items)


s = ArrayList()

s.insert(0, 10)         # [10]
s.insert(0, 20)         # [20, 10]
s.insert(s.size(), 40)  # [20, 10, 40]
s.insert(2, 50)         # [20, 10, 50, 40]
s.display("배열 리스트 insert() 클래스 테스트")

s.sort()              # [10, 20, 40, 50]
s.display("배열 리스트 sort() 함수 테스트")

s.replace(2, 90)      # [10, 20, 90, 50]
s.display("배열 리스트 items[index] 함수 테스트")

# 한줄에 여러 문장을 표시할 경우 ';'를 사용
s.delete(2);    s.delete(s.size() -1);    s.delete(0)
s.display("배열 리스트 pop() 함수 테스트")

anotherItems = [1,2,3]
s.merge(anotherItems)
s.display("배열 리스트 extend() 함수 테스트")

s.clear()
s.display("배열 리스트 목록 전체 삭제")