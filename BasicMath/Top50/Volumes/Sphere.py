def Sphere(radius):
    return (4/3)*3.14*(radius**3)

r=float(input("Enter radius of sphere: "))
print(f"Volume of sphere is {Sphere(r)}")