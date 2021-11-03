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
#                Method2: For loop
#=====================================================================================

if __name__ == "__main__":

    number = int(input("Enter a number: "))
    
    print("While Loop: {} is a palindrome.".format(number) if isPalindrome1(number) 
            else "While loop: {} is not a palindrome.".format(number))
