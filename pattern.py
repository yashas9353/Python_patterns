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