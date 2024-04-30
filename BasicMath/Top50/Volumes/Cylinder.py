def cylindervolume(radius,height):
    return 3.14*(radius**2)*height

r=float(input("Enter radius : "))
h=float(input("Enter height: "))
print("Volume of Cylinder is: ",cylindervolume(r,h))