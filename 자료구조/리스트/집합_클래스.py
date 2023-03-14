# 집합의 특성 : 순서가 없고 중복을 허용 하지 않음
class Set:  # 집합 클래스

    # 생성자
    def __init__(self):
        self.items = []

    # 집합 크기
    def size(self):
        return len(self.items)

    # 집합 출력
    def display(self, msg):
        print(msg, self.items)

    # 집합 포함 여부
    def contains(self, item):
        return item in self.items

    # def contains(self, item):
    #     for i in range(len(self.items)):
    #         if self.items[i] == item :
    #             return True
    #     return False

    # 집합 삽입
    def insert(self, element):
        if element not in self.items:
            self.items.append(element)

    # 집합 삭제
    def delete(self, element):
        if element in self.items:
            self.items.remove(element)

    # 합집합
    def union(self, set_b):
        set_c = Set()
        set_c.items = list(self.items)
        for element in set_b.items:
            if element not in self.items:
                set_c.items.append(element)
        return set_c

    # 교집합
    def intersection(self, set_b):
        set_c = Set()  # Collection 저장을 위한 Set 클래스 생성
        for element in set_b.items:
            if element in self.items:
                set_c.items.append(element)
        return set_c

    # 차집합
    def difference(self, set_b):
        set_c = Set()  # Collection 저장을 위한 Set 클래스 생성
        for element in self.items:
            if element not in set_b.items:
                set_c.items.append(element)
        return set_c


set_a = Set()
set_a.insert("휴대폰")  # '휴대폰' 추가
set_a.insert("지갑")  # '지갑' 추가
set_a.insert("손수건")  # '손수건' 추가
set_a.display("중간 set_a:")  # 'set_a' 출력
set_a.delete("손수건")  # "손수건" 삭제
set_a.delete("발수건")  # "발수건" 존재하지 않음
set_a.display("최종 set_a:")  # 'set_a' 출력


set_b = Set()
set_b.insert("빗")  # '빗' 추가
set_b.insert("파이썬 자료 구조")  # '파이썬 자료 구조' 추가
set_b.insert("야구공")  # '야구공' 추가
set_b.insert("지갑")  # '지갑' 추가
set_b.display("중간 seb_b:")  # 'set_b' 출력
set_b.insert("빗")  # 집합의 경우 순서가 없고 중복을 허용 하지 않음
set_b.display("최종 seb_b:")  # 'set_b' 출력


print("집합의 표현")
set_a.union(set_b).display("합집합 U :")
set_a.intersection(set_b).display("교집합 ^:")
set_a.difference(set_b).display("차집합 -:")
