
def digit_extraction(N: int)-> None:
    while N > 0:
        rem = N%10
        print(rem,end=" ")
        N = N//10

def digit_count(N: int)-> None:
    count = 0
    while N>0:
        count += 1
        N = N//10
    return count

def reverse_digit(N:int)-> None:
    reverse = 0
    while N>0:
        rem = N%10
        reverse = (reverse*10)+rem
        N = N//10

    return reverse

print(reverse_digit(15))

