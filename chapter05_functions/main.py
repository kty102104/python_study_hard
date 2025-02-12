'''
1. 함수(Function) : 특정 작업을 수행하는 코드 블럭을 정의하는 방법

예를 들어 '사진을 찍는다'라는 행위에 대해 생각해보면,
1) 주머니에서 폰을 꺼내고,
2) 잠금 화면을 풀고,
3) 카메라를 켜고,
4) 사진을 찍고자 하는 대상에 폰을 조준하고,
5) 셔터를 누른다.

라고 볼 수 있겠습니다. 그런데 컴퓨터는 시키는대로만 하기 대문에 사진을 찍기 위해서는 1) - 5)까지의 명령어를
입력해줘야만 합니다.
하지만 '사진을 찍는다'라는 함수 내에 1) - 5)의 명령어들을 미리 입력하고 나서, '사진을 찍는다'라는 명령어를
실행시키기만 하면 1) - 5)까지의 명령을 순서대로 수행하는 것을 함수의 개념이라고 볼 수 있습니다.

주요 수업 예시로는 reeborg's world에서 turn_right()를 정의하는 방법이었습니다.\

함수 정의
def turn_right():
    turn_left()
    turn_left()
    turn_left()

함수 호출
turn_right()

2. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드
    3) 사용자 함수

3. 함수 용어 정리(멘토 파이썬에도 있음)
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def를 떠올리셔야 합니다. def : define)
    2) 인수(argument) : 함수에 전달할 입력(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값/결과값/리턴값(return) : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미.

4. (사용자) 함수의 형식 :
def 함수_이름(매개변수):
    실행문

변수 = 함수_이름(argument)
'''
# 외부에서 실제로 우리가 만든 사용자 함수를 호출하는 사례 -> from - import와 합쳐서 생각할 것
# play_hangman()

# 함수 정의
# def write_name(name):
#     print(f"당신의 이름은 {name}입니다.")
#
#
# 함수 호출
# write_name("안근수")
#
# def write_name_age(name, age):  # 매개변수가 복수인 사례 / 함수 정의
#     print(f"당신의 이름은 {name}이고, 나이는 {age}살입니다.")
#
# write_name_age("안근수", 38)
# write_name_age(age=10, name="안근순")  # 이게 python 상황에서는 매너임. keyword argument

'''
우리가 예를 들어 input("이름을 입력하세요 >>> ")을 이용해서 이것을 name 변수에 담았다고 가정하면,
name = input("이름을 입력하세요 >>> ")라고 작성해왔습니다. 즉, 저희는 여태까지 함수의 결과값을
변수에 담아오고 있었습니다.

파이썬 내장 함수는 이미 함수가 정의돼 있고, 함수 호출만 잘 하면 됩니다.
사용자 함수는 개발자 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 생각하시면 됩니다.

내장 함수 예시
print() / type() / int() / float() / str() / input()

2. 메서드(method) :특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함돼있는 함수
사실 함수와 메서드는 동일한 개념이지만. 호출 방식에 있어서의 차이가 있습니다.
함수는 독립적으로 사용이 가능하지만, 메서드는 특정 객체를 통해서만 호출 할 수 있습니다.

'''
# eng_name = input("당신의 입력을 소문자로 입력하세요. >>> ").upper()
# # input()은 함수, .upper()는 method
# print(eng_name)

'''
함수(매서드)의 유형
'''
# # 매개변수 x / 리턴 x
# def call1():
#     print("[ x ㅣ x ]")
# # 매개변수 o / 리턴 x
# def call2(str_type):
#     print("[ o ㅣ x ]")
# # 매개변수 x / 리턴 o
# def call3():
#     print("[ x ㅣ x ]")
#     return "안녕하세요"
# # 매개변수 o / 리턴 o
# def call4(str_type):
#     print("[ o ㅣ o ]")
#     return f"안녕하세요 제 이름은 {str_type}입니다."
#
# call1()
# call2("안근수")    # argument를 입력했지만 실행문을 확인한 결과 해당 argument가 사용되지 않음
# call3() # 안녕하세요는 출력되지 않음.
# print(call3())
# print(call4("안근수"))

'''
call3() / call4() 유형에서 함수 내에 print()를 집어넣어두면 main 단계에서
print() 함수를 입력할 필요가 없어 훨씬 편할 것 같은데
왜 return 형태로 입력해서 main단계에서 일일이 print() 함수를 입력해야 하냐.

함수형 프로그래밍(Functional Programming) : 특정한 함수1의 결과값이
    또 다른 함수2의 argument로 사용되는 것을 의미합니다.
    그리고 함수2의 결과값이 함수3의 argument로 사용되는 것이 반복된다면.
'''
# 사용자 정의 함수를 정의
# def introduce(name, address):
#     return f"제 이름은 {name}이고, {address}에 삽니다."
# # 함수 1 : input함수 -> 파이썬 내장 함수
# name = input("이름을 입력하세요 >>> ")
# address = input("사는 곳을 입력하세요 >>> ")
#
# # 함수1의 결과값들을 함수2인 사용자정의 함수의 argument로 사용
# introduce(name, address)
'''
우리가 사용해본 메서드의 예시 .lower() / .upper() / .title() -> str에 딸린 것들
    append() -> 자료형이 list에 종속돼있는 메서드로 리스트의 가장 마지마가 인덱스에 요소를 추가하는
            메서드
'''
# li = [1, 2, 3]
# print(li)
# li.append(4)    # 메서드 호출
# print(li)       # 함수 호출
'''
700원 짜리 음료수를 뽑을 수 있는 자파기 프로그램을 구현하세요. 돈을 넣으면 몇 잔의 음료수를 뽑을 수
있는지, 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 합니다.

함수 정의
- 반환값 : 없음(call1-4중 어떤 유형일지 고려하세요)
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    # 함수 구현
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''
# 최초 연구본
def vending_machine(money):     # return 값 없고 매개변수가 없으니까 call2() 형식으로 정의했습니다.
    price = 700
    max_drinks = money // price     # 최대음료개수를 구한 이유 : 1. 반복횟수를 계산하기 위해서
    for i in range(max_drinks + 1):     # 0, 1, 2, 3, 4 대입하면서 5번의 반복이 일어납니다.
        charge = money - (price * i)
        print(f"음료수 = {i}개, 잔돈 = {charge}원")
# 이상의 코드의 경우에는 charge가 혹시 다른 함수의 argument가 된다면 변수선언을 하겠지만
# 굳이 print()함수로 마무리 짓는다면(즉, return으로 함수가 마무리되는게 아니라면),
# 일일이 변수를 선언할 필요성을 잘 모르겠긴 합니다.

# vending_machine(5000)

# 최근에 제가 짜는 방식

def vending_machine2(money):
    for i in range((money//700) + 1):
        print(f"음료수 = {i}개, 잔돈 = {money-(700*i)}원")

def vending_machine3(money):
    number = 0
    while number*700 <= money:
        print(f"음료수 = {number}개, 잔돈 = {money-700*number}원")
        number += 1

# vending_machine2(3000)

'''
프로젝트 내 파일 전체 검색 = ctrl + shift + f
예제 : 구구단 출력하기

함수 정의 : 
함수 이름 : multiply
매개변수 : 정수 n

함수 실행
multiply(dan)

실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3
...
3 x 11 = 33
'''
def multiply(n):
    for i in range(1,12,1):         # range(시작값, 종료값, 증감값)
        print(f"{n} x {i} = {n*i}")

def multiply2(n):
    i = 1
    while i < 12:
        print(f"{n} x {i} = {n*i}")
        i += 1

def multiply3(n):
    for i in range(11):
        print(f"{n} x {i+1} = {n*(i+1)}")

# dan = int(input("몇 단을 출력하시겠습니까? >>> "))  # input의 결과값(return)의 자료형은 str이므로 연산 불가능 -> int() 형변환 필요
# multiply3(dan)

'''
예제 : 숫자를 입력한 횟수만큼 비어있는 리스트에 숫자를 추가하기
문제 : 비어있는 리스트 list01을 선언하고 그 안에 입력받은 횟수만큼 숫자 추가하기

함수 정의 : add_numbers()
매개변수 : 정수 n

함수 호출
add_numbers(last_num)

실행 예
숫자 몇 까지 입력하시겠습니까? >>> 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
# def add_numbers(n):
#     for i in range(n):
#         list01.append(i+1)
#     print(list01)
#
# list01 = []
# last_num = int(input("숫자 몇 까지 입력하시겠습니까? >>> "))
# add_numbers(last_num)
'''
예제 : 짝수와 홀수의 개수 세기
문제 : list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의 :
함수 이름 : count_even_odd
매개변수 : numbers(요소는 모두 정수일 것)

함수 실행
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행 예

짝수의 개수 : 5개
홀수의 개수 : 5개

'''
# li = [1,2,3,4,5,6]
#
# print(li)

'''
이상의 코드는 실행했을 때 전체 list가 출력되고, 이를 함수의 argument 혹은 수학적인 연산에
사용할 수 없다는 한계가 있습니다.
그래서 특정한 리스트 내의 요소를 산출하는 방식을 배우겠습니다.

그러면 list명 뒤에 [] 하고 인덱스 넘버를 지정하고 그 주소지에 있는 요소를 산출할 수 있다.
'''
# 일반 for문을 이용한 방법
# for i in range(len(li)):
#       print(li[i])

# 향상된 for 문을 이용한 방법
# for num in li:
#     print(num)

# 일반 for문
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"짝수의 개수 : {even_count}\n홀수의 개수 : {odd_count}")

# count_even_odd([1,2,3,4,5,6,7,8,9,10])

# 향상된 for문 사용한 사례
def count_even_odd2(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"짝수의 개수 : {even_count}\n홀수의 개수 : {odd_count}")

# count_even_odd2([1,2,3,4,5,6,7,8,9,10])

