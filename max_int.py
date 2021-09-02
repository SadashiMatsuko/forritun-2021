num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
# Forrit sem finnur stærstu töluna sem slegin er inn. Svo lengi sem hún sé <=0
max_int = 0 

while num_int > 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))    # Do not change this line
print("The maximum is", max_int)    # Do not change this line