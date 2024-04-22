import math

def area_of_triangle(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

side_a=5
side_b=6
side_c=7

print(f"Area of triangle is : {area_of_triangle( side_a,side_b,side_c)}")
