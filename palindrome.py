# Program to check if a number is a palindrome

#=====================================================================================
#                  Method1: While loop
#=====================================================================================

def isPalindrome1( number ):
    num     = number                          # Assign value of number to num
    reverse = 0                               # Assign 0 to reverse
    
    # Negative integers are mot palindromic
    if ( number < 0 ):
        return False
    
    # loop until num has no digit but 0
    while ( num != 0 ):
        reverse = (10 * reverse) + (num % 10) # adding last digit of num to reverse
        num   //= 10                          # remove last digit from num

    return (number == reverse)

#=====================================================================================
#                Method2: For loop with arrays
#=====================================================================================

def isPalindrome2( number ):
    reverse = 0                               # Assign 0 to reverse

    # Negative integers are mot palindromic
    if ( number < 0 ):
        return False

    div_by_base10 = [ number // (1*(10**i)) for i in range(len(str(number))) ]
    last_digits   = [ i % 10 for i in div_by_base10 ]

    for last_digit in last_digits:
        reverse = 10 * reverse + last_digit

    return (number == reverse)

#=======================================================================================
#              Method3: recursion, reverse of an integer
#=======================================================================================

def reverse( number ):
    return reverseNumber(number, 0)

def reverseNumber(number, reverse):
    if (number == 0):
        return reverse
    return reverseNumber(number // 10, 10 * reverse + number % 10)

def isPalindrome3( number ):
    return (number == reverse(number) if number > 0 else False)

#=======================================================================================
#            Method4: string reverse
#=======================================================================================

def isPalindrome4( number ):
    number = str(number)
    return ( number == number[::-1] if int(number) > 0 else False)

#=======================================================================================
#           Main
#=======================================================================================

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
