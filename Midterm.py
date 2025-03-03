import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    import math
    area = math.pi * radius ** 2
    return(round(area, 2))

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    triangle = ""
    if n < 4 :
        return("The triangle height should be at least 4.")
    if n >= 4 :
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if  j == 1 or j == i or i == n :
                    triangle += "*"
                else:
                    triangle += " "
        triangle += "\n"
    return triangle.strip()
#*
#**
#* *
#****

            

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    pyramid = " "
    if n < 3 :
        return("The pyramid height should be at least 3.")
    if n >= 3 :
        for i in range(n + 1):
            pyramid += " " * i  + "*" * ( 2 * n - (2 * i + 1) )
            pyramid += "\n"
    return pyramid.strip()

# ----------------------------------------------------------------
#print(area_of_circle(5))
#print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

#print(inverted_pyramid(3))
#print()

#print(inverted_pyramid(4))
#print()

#print(inverted_pyramid(5))
#print()
