'''
1. 예외 처리의 필요성
    1) 에외 vs 오류
        에외(exception) : 개발자가 직접 처리할 수 있는 문제
        오류(error) : 개발자가 처리할 수 없는 문제

    2) 에외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해 주는 것이 아니라,
        발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고,
        사용자에게 발생한 문제에 대해 정보를 전달하기 위함.
'''
# 2 / 0
'''
    2 / 0
    ~~^~~
ZeroDivisionError: division by zero
와 같은 방식으로 프로그램이 정상적으로 종료되지 않으며, 보기에 좋지도 않기 때문에,
예외를 처리하면 좋다.

2. 예외 처리
    1) 고전적인 예외 처리
'''
# a = int(input("나누는 수를 입력하세요 >>> "))
# b = int(input("나누어 지는 수를 입력하세요 >>> "))
#
# if a == 0:
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f"b / a = {b/a}")
'''
어떤 값이든 0으로 나눌 수 없기 때문에 if a==0을 통해 0으로 나누는 것을 아예
    시도할 수 없도록 예외 처리를 함.
    
여기서 생각할 수 있는 잠재적인 문제는 :
    1. 어떤 문제가 발생할 지 예상할 수 있어야 미리 대비할 수 있다.
    2. 어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있다.
'''
# from prettytable import PrettyTable
# from error_data import error_data
# table = PrettyTable()
#
# table.field_names = ["순번", "예외 클래스", "의미"]
# for error in error_data:
#     table.add_row(error)
#
# print(table)
'''
+------+---------------------+---------------------------------------------+
| 순번 |     예외 클래스     |                     의미                    |
+------+---------------------+---------------------------------------------+
|  1   |    BaseException    |              최상위 예외 클래스             |
|  2   |      Exception      |       대부분 예외 클래스의 슈퍼 클래스      |
|  3   |   ArithmeticError   |          산술 연산에 문제가 있을 때         |
|  4   |    AttributeError   |           잘못된 속성을 참조할 때           |
|  5   |       EOFError      | 파일에서 더 이상 읽어 들일 테이터가 없을 때 |
|  6   | ModuleNotFoundError |           import할 모듈이 없을 때           |
|  7   |  FileNotFoundError  |           존재하지 않는 파일일 때           |
|  8   |      IndexError     |          잘못된 인덱스를 사용할 때          |
|  9   |      NameError      |        잘못된 이름(변수)을 사용할 때        |
|  10  |     SyntaxError     |               문법이 틀렸을 때              |
|  11  |      TypeError      |   계산하려는 데이터의 유형이 잘못되었을 때  |
|  12  |      ValueError     |    계산하려는 데이터의 값이 잘못되었을 때   |
+------+---------------------+---------------------------------------------+

3. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except 문
    
    형식 :
    
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
'''
# try:
#     a = int(input("나누는 수를 입력하시오 >>> "))
#     b = int(input("나누어지는 수를 입력하시오 >>> "))
#     print(f"b / a = {b/a}")
# except :
#     print("예외가 발생했습니다.")
'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다.
try / except 문을 사용하여 "예외가 발생하였습니다."를 출력할 수 있도록 작성하세요.
'''
# height = input("키를 입력하세요 >>> ")
# height = round(height)
# print(f"입력하신 키는 {height}cm로 처리됩니다.")
'''
위의 코드를 실행하면 오류가 뜨는데, 디버깅을 하지 말고, 예외처리를 통해 지시사항대로 작성하시오.
'''
# try:
#     height = input("키를 입력하세요 >>> ")     # 결과값이 str
#     height = round(height)                  # str을 round 처리할 수 없음 round의 결과값은 float
#     print(f"입력하신 키는 {height}cm로 처리됩니다.")
# except:
#     print("예외가 발생했습니다.")
'''
    2) 특정 예외만 처리하는 방식
        try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨.
        하지만 이상에서 본 것처럼 0으로 나누는 경우와, 정수가 아닌 값을 입력한 경우에
        서로 다른 메시지를 출력한다면, 개발자에게 예외를 처리할 수 있을 만한 정보를
        제공할 수 있음.
        
    2)-1. 0으로 나누려고 하는 경우 -> 0으로 나눌 수 없습니다.
    2)-2. 정수가 아닌 값을 입력한 경우 -> 정수만 입력할 수 있습니다.
    해당 경우 except문 뒤에 처리하고자 하는 예외를 모두 명시하면 됩니다.    
'''
# a = int(float(input("나누는 수를 입력하시오 >>> ")))  # str -> float -> int
# b = int(input("나누어지는 수를 입력하시오 >>> "))   # str -> int를 입력할 때 실수 입력하면 예외 발생
# print(f"b / a = {b/a}")
# 예외 예시 - ZeroDivisionError / ValueError

# try:
#     a = int(float(input("나누는 수를 입력하시오 >>> ")))
#     b = int(input("나누어지는 수를 입력하시오 >>> "))
#     print(f"b / a = {b / a}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("정수만 입력할 수 있습니다.")
'''
        거의 모든 예외는 Exception 클래스의 서브 클래스입니다. 따라서 모든 예외는 Exception의
        인스턴스가 됩니다. 다음과 같이 마지막에 작성하는 except 문에 Exception을 명시하면
        예상하지 못한 예외들도 모두 처리할 수 있게 됩니다.
        
형식 :

try:
    코드 작성 영역
except 예외클래스1:
    예외메시지1
except 예외클래스2:
    예외메시지2
.
.
.
except Exception:
    예외메시지n
    
3. 예외 메시지 처리하기

지금까지는 직접 예외 메시지를 만들어서 사용했지만, 기본적으로 예외 메시지를 이미 가지고 있는 경우도
있습니다. 디폴트 에러 메시지를 출력하는 방식에 대해서 학습합니다.

형식 :

try:
    코드 작성 영역
except 예외 클래스 as 예외메시지:
    예외 발생 시 처리 영역
'''
# z = [10, 20, 30, 40, 50]
# try:
#     print(z[10])        # IndexError: list index out of range
# except IndexError as e:
#     print(e)
'''
    4. else / finally 문
        try / except문에 추가로 else와 finally문을 사용할 수 있음.
        else : 예외가 발생하지 않으면 처리되는 구문
        finally : 예외 발생 여부와 관계없이 맨 마지막에 항상 처리되는 구문
        
형식:
try:
    코드 작성 영역
except:
    예외 발생 시 처리 영역
else:
    예외가 없을 시 처리 영역
finally:
    언제나 실행되는 영역
'''
# try:
#     a = int(input("나누는 수를 입력하시오 >>> "))
#     b = int(input("나누어지는 수를 입력하시오 >>> "))
#     chosen_elemtn = b/a
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print(f"b / a = {chosen_elemtn}")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
    5. 강제로 예외 발생 시키기
        어떤 사람의 나이를 정수로 입력 받는 프로그램이 있다고 가정했을 때,
        컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 대문에 예외가 발생하지 않습니다.
        하지만, -1000살이 될 수 없기 때문에 직접 예외를 발생시켜서 처리해야만 합니다.
            -> raise문
            
형식 :

raise 예외클래스()

또는

raise 예외클래스(예외메시지)

raise는 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는 Exception입니다.
'''
# age = int(input("나이를 입력하세요 >>> "))  # 파이썬 상에서는 문제가 없지만 현실 세계에서 생기는 예외
# print(f"당신의 나이는 {age}살입니다.")
# try:
#     raise Exception("강제로 발생시킨 예외")   # 이 경우 멀쩡한 숫자를 입력해도 예외가 발생됩니다.
# except Exception as e:                      # 잘 생각해서 작성하세요 😢
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
'''
    6. 사용자 정의 예외 클래스
'''
# class NegativeAgeError(Exception):
#     """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
#     pass            # 예외를 발생시키기만 하면 되기 때문에 따로 코드 작성할 필요 없음
#                     # -> Exception의 속성 및 메서드를 상속
#
# try:
#     age = int(input("나이를 입력하세요 >>> "))
#     if age < 0:
#         raise NegativeAgeError("나이는 음수일 수 없습니다.")
# except NegativeAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except ValueError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except Exception as e:
#     print("예상할 수 없는 예외가 발생했습니다.")
#     print(e)
# else:
#     print(f"당신의 나이는 {age}살입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
기본 예제

사용자의 점수를 0이상 100이하로 입력받아서 점수가 80점 이상이면 합격, 아니면 불합격을 출력하는
프로그램을 작성하는데, 0이상 100이하의 유효한 값이 아니라면 예외를 발생시키고
'점수는 0이상 100이하입니다.'라는 예외 메시지를 출력하세요. -> 사용자 정의 예외 클래스를 정의해서.
ScoreOutOfRangeError 클래스를 정의해서 사용하겠습니다.
+
입력받는데 예를 들어 백점이라고 입력하면 '점수는 숫자로 입력해야합니다.'라는 메시지를 출력하세요.
예상할 수 없는 예외가 발생시 Exception을 적용하여 디폴트 에러 메시지를 출력하세요.
+
프로그램이 종료되었다는 메시지를 맨 마지막에 작성하세요.
'''
# class ScoreOutOfRangeError(Exception):
#     """사용자가 말도안되는 점수 입력했을 때 발생하는 예외 처리 클래스입니다."""
#     pass
#
# try:
#     score = float(input("점수를 입력하세요 >>> "))
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError("점수는 0 이상 100 이하입니다.")
# except ScoreOutOfRangeError as e:
#     print("점수 범위를 벗어났습니다.")
#     print(e)
# except ValueError as e:
#     print("점수는 숫자로 입력해야합니다.")
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     if score >= 80:
#         print("합격입니다.")
#     else:
#         print("불합격입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
기본적인 예외 처리
사용자로부터 숫자를 입력 받아 해당 숫자를 100으로 나누는 값을 출력하는 프로그램을 작성하시오.
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 예외 메시지를 출력하시오.

1. 사용자로부터 숫자를 입력 받는다.
2. 100을 입력받은 숫자로 나누어 결과를 출력한다.
3. 입력값이 0일 경우, ZeroDivisionError를 처리하여 "0으로 나눌 수 없습니다."라는 메시지를 출력한다.
4. 입력값이 숫자가 아닌 경우, ValueErorr를 처리하여 "숫자만 입력할 수 있습니다."라는 메시지를 출력한다.
5. 예외가 발생하지 않는 경우, "정상적으로 처리되었습니다."라는 메시지를 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
# try:
#     num = float(input("숫자를 입력하세요 >>> "))
#     print(100/num)
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("숫자만 입력할 수 있습니다.")
# except Exception as e:
#     print(e)
# else:
#     print("정상적으로 처리되었습니다.")
# finally:
#     print("프로그램이 종료되었습니다.")

'''
사용자로부터 리스트의 인덱스를 입력 받아 해당 인덱스의 값을 출력하는 프로그램을 작성하시오.
만약 잘못된 인덱스를 입력하면 적절한 예외 메시지를 출력하시오.

지시 사항
1. 미리 정의된 리스트가 있다.
2. 사용자로부터 리스트의 인덱스를 입력받는다.
3. 입력받은 인덱스를 사용하여 리스트의 값을 출력한다.
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메시지를 출력한다.
5. 사람을 의심하고 예상되는 예외를 적용한다.
6. 예외가 발생하지 않은 경우 "정상적으로 처리되었습니다."라는 메시지를 출력한다.
7. 프로그램 종료 메시지를 출력한다.
+
a. 마이너스인덱스는 적용시키지않는다-> 사용자 정의 예외 클래스를 통해서 하겠습니다. NegativeNumIndexError로 이름짓고
'''
# my_list = [10, 20, 30, 40, 50]
#
# class NegativeNumIndexError(Exception):
#     pass
#
# try:
#     index = int(input("인덱스를 입력하세요 >>> "))
#     if index < 0:
#         raise NegativeNumIndexError("마이너스 인덱스는 적용되지 않습니다.")
#     chosen_element = my_list[index]
# except NegativeNumIndexError as e:
#     print(e)
# except IndexError as e:
#     print(e)
#     print("list 범위를 벗어났습니다.")
# except ValueError as e:
#     print(e)
#     print("정수만 입력할 수 있습니다.")
# except Exception as e:
#     print("예측할 수 없는 예외가 발생했습니다.")
#     print(e)
# else :
#     print("정상적으로 출력되었습니다.")
#     print(f"선택된 값은 {chosen_element}입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
사용자로부터 속성명을 입력 받아 객체의 해당 속성을 출력하는 프로그램을 작성하시오.
만약 잘못된 속성을 입력하면 적절한 예외 처리 메시지를 출력하시오.

지시 사항
1. 미리 정의된 클래스와 객체가 있다.
2. 사용자로부터 속성명을 입력받는다.
3. 입력받은 '속성명'을 사용하여 객체의 '속성'을 출력한다.
4. 잘못된 속성을 입력하면 "존재하지 않는 속성입니다."라는 메시지를 출력한다.
5. 예외가 발생하지 않은 경우 "정상적으로 처리되었습니다."라는 메시지를 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
# 미리 정의하는 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person(name="John", age=30)   # keyword argument 적용함

# vars() 함수 : 객체의 속성명-값을 dictionary의 키-값 쌍으로 만들어주는 함수
# 풀이법 1
# try:
#     attribute = input("출력할 속성명을 입력하세요 >>> ").lower()
#     print(vars(person1)[attribute])
# except KeyError:
#     print("존재하지 않는 속성입니다.")
# except Exception as e:
#     print("예측할 수 없는 예외가 발생했습니다.")
#     print(e)
# else:
#     print("정상적으로 처리되었습니다.")
# finally:
#     print("프로그램이 종료되었습니다.")

# 풀이법 2
attribute2 = input("출력할 속성명을 입력하세요 >>> ").lower()
try:
    print(getattr(person1, attribute2))
except AttributeError as e:
    print("존재하지 않는 속성입니다.")
    print(e)
except Exception as e:
    print(e)
else:
    print("정상적으로 처리되었습니다.")
finally:
    print("프로그램이 종료되었습니다.")
