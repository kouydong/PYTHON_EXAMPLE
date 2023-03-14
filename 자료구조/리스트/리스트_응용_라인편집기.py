def myLineEditor():
    list = []

    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, 1-파일읽기, s-저장, q-종료 =>")

    if command == "i":                         # 삽입연산
        list_index = int(input("입력행 번호:"))   # 사입할 행번호 입력
        str = input("입력행 내용.")              #
        list.insert(listIndex)                 # 리스트 데이터 추가
    elif command == "d":
        listIndex = ""