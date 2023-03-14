score = int(input("점수를 입력 하세요"))

# 등급 출력
if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
elif score >= 70:
    print("C 등급")
elif score >= 70:
    print("D 등급")
else:
    print("F 등급")


# 홀수/짝수 출력
if score % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 조건문 블록 내에서 실행 문이 한 문장인 경우 한 줄 작성 가능
if score % 2 == 0: print("짝수임")
else: print("홀수임")
