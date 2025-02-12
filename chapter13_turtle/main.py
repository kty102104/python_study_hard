# turtle이라는 모듈을 사용하고, Turtle, Screen이라는 클래스를 사용한다는 의미
from turtle import Turtle, Screen
import random

# 객체 생성
t = Turtle()        # Turtle 클래스의 객체 생성
screen = Screen()   # Screen 클래스의 객체 생성

t.shape("turtle")
t.color("white")
screen.bgcolor("black")

colors = [
    "dodger blue",
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
]

# def draw_dotted_line(n):
#     for  _ in range(n):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()
#
# times = int(input("몇 번의 반복을 실행하시겠습니까? >>> "))
# draw_dotted_line(times)

# def draw_dotted_line():
#     times = int(input("몇 번의 반복을 실행하시겠습니까? >>> "))
#     for  _ in range(times):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()
#
# draw_dotted_line()

# 한 변의 길이가 150인 정사각형을 그리시오.
# for _ in range(4):
#     t.forward(150)
#     t.left(90)
# 한 변의 길이가 150인 정삼각형을 그리시오.
# for _ in range(3):
#     t.forward(150)
#     t.left(120)
# 한 변의 길이가 150인 정오각형을 그리시오.
# for _ in range(5):
#     t.forward(150)
#     t.left(72)

# for i in range(3,11,):
#     for _ in range(i):
#         t.forward(100)
#         t.left(360/i)

# def draw_polygon(angles):
#     # angles가 3 미만일 경우에는 실행이 안되야 한다는 잠재적인 문제점이 있습니다.
#     if angles < 3:
#         print("도형을 그릴 수 없습니다.")
#     else:
#         t.color(random.choice(colors))
#         for _ in range(angles):
#             t.forward(100)
#             t.left(360/angles)
#
# for i in range(11):
#     draw_polygon(i)

'''
    .heading() 메서드 :
        거북이가 바라보는 방향을 나타내는 속성이고 도(degree)단위로 나타남.
        
        해당 메서드는 콘솔창에 float으로 나타납니다.
        0도 : 동쪽
        90도 : 북쪽
        180도 : 서쪽
        270도 : 남쪽
        
    .setheading() 메서드 :
        특정 각도로 거북이를 회전시키는 메서드
        0도 : 동쪽
        90도 : 북쪽
        180도 : 서쪽
        270도 : 남쪽
'''
# t.forward(50)
# print(t.heading())
# t.left(90)
# t.forward(50)
# print(t.heading())
# t.left(120)
# print(t.heading())
# t.setheading(0)
# t.forward(100)

# for _ in range(360//7):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading() + 10)

# 이상의 코드를 응용하여 draw_spirograph(size_of_gap)로 함수화하시오.

# def draw_spirograph(size_of_gap):
#     for _ in range(360//size_of_gap):
#         t.circle(100)
#         t.color(random.choice(colors))
#         t.setheading(t.heading() + size_of_gap)
#
# draw_spirograph(30)

# 아까 위에서 함수화한 draw_figures를 참조하여 정삼각형부터 정십각형까지
# 도형마다 색깔이 임의적으로 바뀌면서, 점선으로 도형을 그릴 수 있도록 코드를 작성하시오.

t.speed(0)

def draw_dotted_lines(n):
    for  _ in range(n):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

def draw_side():
    draw_dotted_lines(10)

def draw_polygon(angles):
    # angles가 3 미만일 경우에는 실행이 안되야 한다는 잠재적인 문제점이 있습니다.
    if angles < 3:
        print("도형을 그릴 수 없습니다.")
    else:
        t.color(random.choice(colors))
        for _ in range(angles):
            draw_side()
            t.left(360/angles)

for i in range(11):
    draw_polygon(i)









screen.exitonclick()
