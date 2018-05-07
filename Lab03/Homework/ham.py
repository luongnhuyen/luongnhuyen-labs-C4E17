from turtle import *

def hw(n):
    for i in range (n):
        print ("Hello world")

def tong(x,y):
    tong = x + y
    print(tong)

def draw_square(x,color):
    pencolor(color)
    for i in range (4):
        forward(90)
        left(90)

def draw_star(x, y, z):
    setup(x)
    setup(y)
    for i in range (5):
        forward(z)
        right(144)

def remove_dollar_sign(s):
    s=s.replace("$","")
    print(s)
    return s

def get_even_list(n):
    even_list=[]
    for i in n:
        if i % 2 == 0:
            even_list.append(i)
    print (even_list)
    return even_list

def is_inside(toado,hcn):
    # if x0 < x < x0 + width and y0 < y < y0 + height:
    if hcn[0] < diem[0] < hcn[0] + hcn[2] and hcn[1] < diem[1] < hcn[1] + hcn[3]:
        print("True")
    else:
        print("False")
