def inc_triangle(n):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    for i in range(0, n+1):
        for j in range(0, i):
            print("* ", end="")
        print()

def dec_triangle(n):
    for i in range(0, n+1):
        for j in range(i, n):
            print("* ", end="")
        print()

def right_side_triangle(n):
    for i in range(0, n+1):
        for j in range(i, n+1):
            print("  ", end="")
        for j in range(0, i):
            print("* ", end="")
        print()

inc_triangle(5)
dec_triangle(5)
right_side_triangle(5)