import math

def find_roots(a,b,c):
    #calculating discriminant
    discriminant=b**2-4*a*c

    if discriminant>0:
        #Two real distinct roots
        root1=(-b + math.sqrt(discriminant))/(2*a)
        root2=(-b - math.sqrt(discriminant))/(2*a)
        return root1,root2
    
    elif discriminant==0:
        #Two real and equal roots
        root=-b/(2*a)
        return root, root
    else:
        #complex roots
        real_part=-b/(2*a)
        imag_part=math.sqrt(abs(discriminant))/(2*a)

        return (real_part,imag_part), (real_part, -imag_part)
    

a= 10
b=16
c=2
roots=find_roots(a,b,c)
print("Roots: ",roots)