
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


def isArmstrong(num):
    res = 0
    original_num = num
    num_len = len(str(original_num))

    while num>0:
        rem = num%10
        res = res + int(pow(rem,num_len))
        num = num//10

    if res == original_num:
        return "YES"
    else:
        return "NO"
    


str = "My name is Yashas"

str = str.lower().replace(" ","")

print(str)