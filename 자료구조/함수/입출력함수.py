# input('출력 문자열') : '출력 문자열' 출력 하고 사용자 입력값 문자열 반환
# JAVA Scanner scanner = new Scanner(System.in)
name = input("당신의 이름을 입력하세요")
hobby = input("취미가 무엇입니까?")
age = int(input("나이가 몇 살 입니까?"))
score = float(input("평균 학점이 얼마입니까?"))

# print('문자열1', '문자열n', .... end='마지막 문자열') : '문자열1' 부터 '문자열n' 까지 출력 및 '마지막 문자열' 출력 후 종료
# end 값의 기본 값은 '\n' 임
# sep 값을 통해 각 문자열 구분자 추가 가능 합니다.
# JAVA System.out.print() 함수 유사
print('당신의 이름은 : ', name, end=' ')
print('당신의 취미는 : ', hobby, end=' ')
print('당신의 나이는 : ', age, end=' ')
print('당신의 학점은 : ', score, end=' ')

# % 값을 통해 각 문자열 포맷팅 가능합니다.
# JAVA System.out.printf() 함수 유사

