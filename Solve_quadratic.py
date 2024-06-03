import math
# import keyword
#function to solve the quadratic equation
# print(keyword.kwlist)
def solve_quadratic(a, b, c):
    discriminant = b**2 -4*c*a

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant))/(2*a)
        root2 = (-b - math.sqrt(discriminant))/(2*a)
        return("Two real roots is:",root1,root2)
    elif discriminant == 0:
        root = (-b + math.sqrt(discriminant))/(2*a)
        return("One real root: ",root)
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part,imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return ("Two real roots:",root1,root2)

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

result = solve_quadratic(a,b,c)
print(result)