# Week 8 Homework

# Problem 9 in Section 7.26
def print_tri_number(n):
    for i in range(1, n + 1):
        tri_number = i * (i + 1)//2
        print(tri_number)

print_tri_number(5)
