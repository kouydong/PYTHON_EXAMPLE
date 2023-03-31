# 과제1 - 리스트 삽입/삭제 구현하기

# 제출물
# 00000000_hw1.py
# - 함수파일 코딩하고 00000000 은 학번으로 이름만 바꿔서 제출

# 코딩관련 유의사항
# 공통
# 함수이름은 hw1_00000000 (00000000은 본인 학번으로 변경)
# 함수 내 작성부분1 과 작성부분2 를 작성
# 함수 내 나머지부분은 수정불가. 꼭 필요하다면 별도함수 작성은 가능
# (1) 삽입/삭제 1회 수행 후 종료가 아님. 여러번 반복 수행 가능하여야 함

# 삽입부분
# (2) 리스트에서 '삽입할 위치 숫자'와 / '삽입할 숫자' 두가지를 입력받음
# (3) '삽입할 위치 숫자' 뒤에 '삽입할 숫자' 삽입하고 리스트 출력
# (4) (2)에서 입력받은 위치가 리스트 내 여러개인 경우 제일 앞에 있는 숫자 뒤에 삽입
# (5) (2)에서 입력받은 위치가 리스트에 없으면 예외 안내 화면출력
# (6) 삽입 후 리스트 크기 재계산

# 삭제부분
# (7) 리스트에서 '삭제할 숫자'를 입력받아 삭제
# (8) (7)에서 입력 받은 숫자가 리스트 내 여러 개인 경우 제일 뒤에 있는 숫자만 삭제
# (9) (7)에서 입력 받은 숫자가 리스트에 없으면 예외 안내 화면 출력
# (10) 삭제 후 리스트 크기 재계산

# 평가기준 (작동여부/ 주석내용/ 제출기간)
# - 코딩관련 유의사항 (1)~(10) 작동여부
# - 다른사람이 알아보기 쉽도록 주석이 상세히 달려있는지 여부
# - 제출기간(~4.9(일)) 준수


hw_list = []

def hw1_00000000():


    while True:
        com_1 = input("리스트 크기를 '숫자'로 입력하세요 - ")

        if com_1.isdigit() == True:
            # 리스트 사이즈 저장
            list_sz = int(com_1)
            break

    # 리스트 생성 : (사이즈-순번)*(사이즈-순번)+(사이즈-순번) 로 역순 추가
    for i in range(list_sz, 0, -1):
        k = i * i + i
        hw_list.append(k)

    # 삽입/삭제 부분 시작
    while True:
        print('리스트가 다음과 같이 만들어졌습니다.\n', hw_list)
        com_2 = input("[메뉴선택] i-삽입, d-삭제, 그외-종료=> ")
        flag = False

        # ───────────────────────────────────────────────────────────────────
        # 리스트 크기 재계산
        # ───────────────────────────────────────────────────────────────────
        list_size = len(hw_list)

        # 삽입
        if com_2 == 'i':

            index = input("삽입할 위치를 '숫자'로 입력하세요 - ")

            number = input("삽입할 '숫자'를 입력하세요 - ")
            ########   작성부분1   ##########



        # 삭제
        elif com_2 == 'd':
            # 삭제할 숫자 입력 받음.
            delete_number_string = input("삭제할 '숫자'를 입력하세요 - ")

            print("리스트의 크기", len(hw_list))
            print("리스트의 크기", hw_list)

            aaaa = hw_list.index(int(delete_number_string), len(hw_list), 0)
            print("고의동 값 ", aaaa)
            if delete_number_string.isdigit() == True :

                for i in range(len(hw_list), 0, -1) :
                    if hw_list[i] == int(delete_number_string):
                        print("삭제 시작")
                        hw_list.pop(i)

            else:
                print("입력 받은 값이 ", "'숫자'"," 가 아닙니다.")
                break;


            print("값 :", hw_list)
            print("값2 : ", list_sz)

            # if delete_number.isdigit() == True:

            flag = True
        # 종료
        else:
            break


hw1_00000000()
#
# def insert(index, element):
#     # items 배열 특정 index 위치에 새로운 element 추가
#     hw_list.insert(index, element)
#

# def delete(index):
#     items 배열 삭제
# return hw_list.pop(index)