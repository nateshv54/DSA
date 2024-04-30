def ConeVolume(radius,height):
    return (1/3)*3.14*(radius**2)*height

r=float(input("Enter Radius of Cone: "))
h=float(input("Enter Height of Cone: "))
print(f"Volume of Cone is : {ConeVolume(r,h)}")