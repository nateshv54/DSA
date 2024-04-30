# cuboid= l*b*h

def cuboidvolume(length,breath,height):
    return length*breath*height

l=float(input("Enter length of cuboid: "))
b=float(input("Enter breath of cuboid "))
h=float(input("Enter height of cuboid : "))
print("Volume of cuboid is :",cuboidvolume(l,b,h))