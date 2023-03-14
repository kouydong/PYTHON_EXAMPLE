dan = int(input("구구단 입력"))
n = 2
print("while 구구단 출력")
while n < 10:
    print("%d x %d = " % (dan, n), dan * n)
    n += 1

print("for 구구단 출력")
for n in range (2, 10, 1):
    print("%d x %d = %d" % (dan, n, dan * n))

# for "초기값 변수" in range("최대값") : '초기값=1' 및 '증감값=1' 자동 설정 e.g.)
# for "초기값 변수" in range("초기값", "최대값") : '증감값=1' 자동 설정
# for "초기값 변수" in range("초기값", "최대값", "증감값")
# for '초기값 변수' in "리스트" : 리스트 각 요소별 출력
# for '초기값 변수' in "문자열' : 문자열 각 문자 출력






