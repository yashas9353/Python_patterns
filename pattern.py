# pattern One : 
# * * * * 
# * * * * 
# * * * *
# * * * *
def print_pattern(n: int)-> None:
    """
    Prints a pattern of stars in a square shape.

    Parameters:
    n (int): The number of rows and columns in the pattern.

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> print_pattern(4)
    * * * * 
    * * * * 
    * * * *
    * * * *
    """
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print()

# pattern two : 
# * 
# * *  
# * * * 
# * * * *

def print_patten_each_iterations(n:int) -> None:
    """
    This function prints a pattern of stars where each row has a number of stars equal to the row number.

    Parameters:
    n (int): The number of rows in the pattern.

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> print_patten_each_iterations(4)
    * 
    * *  
    * * * 
    * * * *
    """
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()


def nTriangle(n:int) ->None:
    """
    Prints a pattern of numbers in a right-angled triangle shape.

    Parameters:
    n (int): The number of rows in the pattern. Each row contains numbers from 1 to the row number.

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> nTriangle(4)
    1 
    1 2 
    1 2 3 
    1 2 3 4
    """
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def triangle(n: int) -> None:
    """
    Prints a pattern of numbers in a right-angled triangle shape.

    Parameters:
    n (int): The number of rows in the pattern. Each row contains numbers from 1 to the row number.

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> triangle(4)
    1 
    1 2 
    1 2 3 
    1 2 3 4
    """
    for i in range(1, n+1):  # Loop through each row
        for j in range(1, i+1):  # Loop through each column in the row
            print(i, end=" ")  # Print the current row number
        print()  # Move to the next line


def seeding(n: int) -> None:
    """
    Prints a pattern of stars in a right-angled triangle shape, with the number of stars in each row decreasing.

    Parameters:
    n (int): The number of rows in the pattern. The number of stars in the first row is equal to n, and it decreases by 1 for each subsequent row.

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> seeding(4)
    * * * * 
    * * * 
    * * 
    * 
    """
    for i in range(1,n+1):  # Loop through each row
        for j in range(n,i-1,-1):  # Loop through each column in the row, starting from n and decrementing by 1
            print("*",end=" ")  # Print a star
        print()  # Move to the next line

def nNumberTriangle(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,(n+2)-i):
            print(j,end=" ")
        print()
            
def nStarTriangle(n: int) -> None:
    """
    Prints a pattern of stars in a right-angled triangle shape. The number of stars in each row decreases by 2, starting from 2n-1 in the first row.

    Parameters:
    n (int): The number of rows in the pattern. The number of stars in the first row is equal to 2n-1, and it decreases by 2 for each subsequent row.

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> nStarTriangle(4)
        *
       ***
      *****
     *******
    """
    for i in range(n):  # Loop through each row
        for j in range(i):  # Loop through each space before the stars in the row
            print(" ", end="")
        for k in range((n*2)-(2*i)-1):  # Loop through each star in the row
            print("*", end="")
        for l in range(i):  # Loop through each space after the stars in the row
            print(" ", end="")
        print()  # Move to the next line


def nStarDiamond(n: int) -> None:
    """
    Prints a pattern of stars in a diamond shape. The number of stars in each row increases by 2, starting from 1 in the middle row.

    Parameters:
    n (int): The number of rows in the upper half of the diamond. The number of rows in the lower half will be n-1.

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> nStarDiamond(4)
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    """
    # Print the upper half of the diamond
    for i in range(n):
        # Print spaces before the stars
        for j in range(n-i-1):
            print(" ",end="")
        # Print stars
        for k in range(2*i+1):
            print("*",end="")
        # Print spaces after the stars
        for l in range(n-i-1):
            print(" ",end="")
        print()
    
    # Print the lower half of the diamond
    for j in range(n):
        # Print spaces before the stars
        for i in range(j):
            print(" ",end="")
        # Print stars
        for k in range((n*2)-(2*j)-1):
            print("*",end="")
        # Print spaces after the stars
        for l in range(j):
            print(" ",end="")
        print()

def nStarTriangle(n: int) -> None:
    for i in range(1,(2*n)):
        start = i;
        if i > n:
            start = 2*n-i
        for j in range(start):
            print("*",end="")
        print()
        
def nBinaryTriangle(n: int) -> None:
    """
    Prints a pattern of binary numbers (0s and 1s) in a right-angled triangle shape. 
    The pattern alternates between 0s and 1s in each row, starting with 1 in the first row.

    Parameters:
    n (int): The number of rows in the pattern. 

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> nBinaryTriangle(4)
    1 
    0 1 
    1 0 1 
    0 1 0 1
    """
    start = 1  # Initialize the starting binary number
    for i in range(n):  # Loop through each row
        if i % 2 == 0:  # If the row number is even, start with 1
            start = 1
        else:  # If the row number is odd, start with 0
            start = 0
        for j in range(i+1):  # Loop through each column in the row
            print(start, end=" ")  # Print the current binary number
            start = 1 - start  # Alternate between 0 and 1
        print()  # Move to the next line

def nLetterTriangle(n: int) -> None:
    """
    Prints a pattern of letters in a right-angled triangle shape. 
    The pattern starts with the letter 'A' in the first row and continues with the next letter in the alphabet for each subsequent row.

    Parameters:
    n (int): The number of rows in the pattern. 

    Returns:
    None. The function prints the pattern directly.

    Example:
    >>> nLetterTriangle(4)
    A 
    A B 
    A B C 
    A B C D
    """
    for i in range(n):  # Loop through each row
        for j in range(i+1):  # Loop through each column in the row
            print(chr(65+j),end=" ")  # Print the current letter using ASCII value
        print()  # Move to the next line