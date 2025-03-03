'''
문자열 인덱싱(indexing)
print(type("안녕하세요"))를 실행하면
<class 'str'> 나오는 것을 확인할 수 있음
str 이란 string의 줄임말로 '줄'이란 의미를 가지고 있음.
index란 : 문자열을 구성하는 모든 문자에 부여한 고유의 번호. 시작 번호는 0
01234
'''

name = "ahngeunsu"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

'''
마이너스 인덱스 : 문자열의 뒤에서부터 부여하는 번호. 마지막 문자의 인덱스는 '-1'
'''
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])

'''
문자열 슬라이싱(slicing) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나
문장을 추출할 때 사용하는 방법
추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을 
추출하는 방법

형식 : a[시작인덱스:종료인덱스:증감값]
시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 생략하면 끝까지 추출
증감값 : 생략하면 1씩 변화(인덱스넘버가 1씩 증가)
'''

# print(name[:2:])    # 종료인덱스를 포함하지 않는다. 즉 index number2까지 출력하지 않고
                      # 종료 인덱스 앞까지만 출력함

# b = "banana"
# print(b[:4:2])      # 출력값 bn

'''
기본 예시

네 자리 숫자를 입력 받아 그 숫자의 맨 마지막 자리를 출력하시오.
'''

# num = input("네 자리 숫자를 입력하세요 >>> ")
#
# print(num[3])     # 인덱스넘버 사용
# print(num[-1])    # 마이너스인덱스 사용

# num = input("네 자리 숫자를 입력하세요 >>> ")
#
# last_num = int(num[-1])
#
# if last_num % 2 == 0:
#     print(f"맨 마지막 자리의 숫자는 {num[-1]}이고, 맨 마지막 자리의 숫자는 짝수입니다.")
# else:
#     print(f"맨 마지막 자리의 숫자는 {num[-1]}이고, 맨 마지막 자리의 숫자는 홀수입니다.")

'''
응용 예제

미세먼지 저감 활동의 일환으로 차량 2부제를 실시하고자 합니다. 사용자로부터 차량번호를 입력받아 차량 번호가
짝수로 끝나면 '운행가능', 아니면 '운행불가'가 출력되는 프로그램을 작성하세요.
단, 차량번호는 '237가1234'와 같은 형식으로 입력받는다고 가정합니다.
'''

driving_possibility = ""    # 비어있는 str을 변수에 대입(있어도 되고 없어도 됨)
car_num = input("차량번호를 입력하세요 >>> ")
last_num = int(car_num[-1])

# if last_num % 2 == 0:
#     print("운행가능")
#
# else:
#     print("운행불가")
#
# 아래도 가능
#
# if last_num % 2 == 0:
#     driving_possibility = "운행가능"
#     print(f"차량번호 {car_num}은 {driving_possibility}입니다.")
#
# else:
#     driving_possibility = "운행불가"
#     print(f"차량번호 {car_num}은 {driving_possibility}입니다.")




