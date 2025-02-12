file_modes = [
    ("입력", "r", "read", "읽기", "오류 발생", "읽기"),
    ("출력", "w", "write", "쓰기", "새로 생성", "새로 생성"),
    ("", "a", "append", "추가", "새로 생성", "추가"),
    ("", "x", "exclusive", "배타적 추가", "새로 생성", "오류 발생")
]

# from prettytable import PrettyTable

# from file_modes import file_modes
# table = PrettyTable()
# table.field_names = ["분류", "종류", "의미", "설명", "파일이 없을 때 동작", "파일이 있을 때 동작"]
# for mode in file_modes:
#     table.add_row(mode)
# print(table)

# table2 = PrettyTable()
# table2.field_names = ["종류", "의미", "설명"]
# table2.add_row(("t", "text", "텍스트 파일"))
# table2.add_row(("b", "binary", "바이너리 파일(텍스트 파일 외의 모든 파일)"))
# print(table2)

# table3 = PrettyTable()
# table3.field_names = ["모드", "설명"]
# table3.add_row(["rt", "텍스트 파일 읽기 모드"])
# table3.add_row(["rb", "바이너리 파일 읽기 모드"])
# table3.add_row(["wt", "텍스트 파일 쓰기 모드"])
# table3.add_row(["wb", "바이너리 파일 쓰기 모드"])
# table3.add_row(["at", "텍스트 파일 추가 모드"])
# table3.add_row(["ab", "바이너리 파일 추가 모드"])
# table3.add_row(["xt", "텍스트 파일 배타적 추가 모드"])
# table3.add_row(["xb", "바이너리 파일 배타적 추가 모드"])
# print(table3)
