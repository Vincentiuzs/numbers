/*
 * Program to check if a number is a palindrome. (5 Methods)
 */
import java.util.*;

public class Palindrome
{
	
	/** Private constructor to prevent objects from being created */
	private Palindrome() {}
	
	//===========================================================
	//           Method1: While loop
	//===========================================================
	/**
	 * Checks if a number is a palindrome.
	 * @param number number to check
	 * @return true if number is palindrome else false
	 */
	public static boolean isPalindrome1( int number )
	{
		int 	num = number;   // Assign nvalue of number to num
		int reverse = 0;        // Assign 0 to reverse

		// Negative numbers are not palindromic
		if ( number < 0 ) return false;

		// loop until num has no digit but 0
		while ( num != 0 )
		{
			// add last digit of num to reverse
			reverse = 10 * reverse + num % 10;
			// remove last digit of num
			num /= 10;
		}
		return (number == reverse);
	}

	//===========================================================
        //           Method2: For loop (Equivalent to method1)
        //===========================================================
	/**
         * Checks if a number is a palindrome.
         * @param number number to check
         * @return true if number is palindrome else false
         */
        public static boolean isPalindrome2( int number )
        {
                int reverse = 0;        // Assign 0 to reverse

                // Negative numbers are not palindromic
                if ( number < 0 ) return false;

                // loop until num has no digit but 0
                for (int num = number; num != 0; num /= 10)
                {
                        // add last digit of num to reverse
                        reverse = 10 * reverse + num % 10;
                }
                return (number == reverse);
        }

	//===========================================================
        //           Method2: For loop (with arrays)
        //===========================================================
        /**
         * Checks if a number is a palindrome.
         * @param number number to check
         * @return true if number is palindrome else false
         */
        public static boolean isPalindrome3( int number )
        {
                int reverse = 0;        // Assign 0 to reverse

                // Negative numbers are not palindromic
                if ( number < 0 ) return false;

		int div_by_base10 [] = new int [Integer.toString(number).length()];
		
		//Remove last digit: first element is number
		for (int i = 0; i < div_by_base10.length; i++)
			div_by_base10[i] =  number / (int)Math.pow(10, i);
		
		// Add last digit of each number in div_by_base10 to reverse
		for (int i : div_by_base10)
			reverse = 10 * reverse + i % 10;

		return (number == reverse);

        }



	public static void main(String [] args)
	{
		Scanner input = new Scanner (System.in);
		
		System.out.print("Enter a number: ");
		int number = input.nextInt();
		
		System.out.println();

		System.out.printf( isPalindrome1(number) ? "While Loop: %d is a palindrome.%n%n" 
				: "While loop: %d is not a palindrome.%n%n", number);

		System.out.printf( isPalindrome2(number) ? "For Loop: %d is a palindrome.%n%n"
                                : "For loop: %d is not a palindrome.%n%n", number);

		System.out.printf( isPalindrome3(number) ? "For Loop (w/ arrays): %d is a palindrome.%n%n"
                                : "For loop (w/ arrays): %d is not a palindrome.%n%n", number);
	}
}

