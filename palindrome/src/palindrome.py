# Program to check if a number is a palindrome
# 4 Methods to check if a number is a palindrome

#=======================================================================================================
#                  Method1: While loop
#=======================================================================================================
def isPalindrome1( number ):
    """ Checks if a number is a palindrome. """
    num     = number                          # Assign value of number to num
    reverse = 0                               # Assign 0 to reverse
    
    # Negative integers are mot palindromic
    if ( number < 0 ):
        return False
    
    # loop until num has no digit but 0
    while ( num != 0 ):
        reverse = (10 * reverse) + (num % 10) # adding last digit of num to reverse
        num   //= 10                          # remove last digit from num
    
    # returns true if number = reverse else false
    return (number == reverse)

#=======================================================================================================
#                Method2: For loop with arrays
#=======================================================================================================

def isPalindrome2( number ):
    """ Checks if a number is a palindrome. """
    reverse = 0                               # Assign 0 to reverse

    # Negative integers are mot palindromic
    if ( number < 0 ):
        return False

    # Remove last digit at every iteration: first element is number
    div_by_base10 = [ number // (10**i) for i in range(len(str(number))) ]
    
    # Add last digit of number to reverse
    for i in div_by_base10:
        reverse = 10 * reverse + i % 10

    # returns true if number = reverse else false
    return (number == reverse)

#=======================================================================================================
#              Method3: recursion, reverse of an integer
#=======================================================================================================
def reverse( number ):
    """ Helper function fo calculating reverse. Calls recursive function: reverseNumber() """
    return reverseNumber(number, 0)

def reverseNumber(number, reverse):
    """ Recursive function for calculating the reverse of a number """
    if (number == 0):       # return reverse if number equals zero
        return reverse

    # recurse until number equals zero. 
    # number // 10 removes last digit of number
    # 10 * reverse + number % 10 adds the last digit to reverse
    return reverseNumber(number // 10, 10 * reverse + number % 10)

def isPalindrome3( number ):
    """ Checks if a number is a palindrome. """
    #return false if number < 0, else check if number is same as reverse
    return (False if int(number) < 0 else number == reverse(number) )

#=======================================================================================================
#            Method4: string reverse
#=======================================================================================================

def isPalindrome4( number ):
    """ Checks if a number is a palindrome. """
    # Converting number to string
    number = str(number)
    # number[::-1] is a reversed string of number. return false if
    # number < 0, else check if number is same as reverse
    return ( number == number[::-1] )

#=======================================================================================================
#           Main
#=======================================================================================================
if __name__ == "__main__":

    number = int(input("Enter a number: "))
    print()

    print("While Loop: {} is a palindrome.".format(number) if isPalindrome1(number) 
            else "While loop: {} is not a palindrome.".format(number))
    print()
    print("For Loop (w/ arrays): {} is a palindrome.".format(number) if isPalindrome2(number)
            else "For loop (w/ arrays): {} is not a palindrome.".format(number))
    print()
    print("Recursion (Reverse of a number): {} is a palindrome.".format(number) if isPalindrome3(number)
            else "Recursion (Reverse of a number): {} is not a palindrome.".format(number))
    print()
    print("String reverse: {} is a palindrome.".format(number) if isPalindrome4(number)
            else "String reverse: {} is not a palindrome.".format(number))

