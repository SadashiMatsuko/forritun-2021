n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 1
b = 2
c = 3
print('1')
print('2')
print('3')
for i in range(n):
    if i >= 3:
        d = a + b + c
        print(d)
        a = b
        b = c
        c = d
