/*
 * Program to check if a given number is a palindrome.
 */

#include <iostream>

using namespace std;

//===================================================================
//			    FIRST METHOD
//===================================================================

bool isPalindrome1(int number)
{
	int num     = number;
	int reverse = 0;
	
	// negative numbers are not palindromes
	if ( number < 0 )
		return false;

	while ( num != 0 )
	{
		// Add the last digit of num to reverse
		reverse = (10 * reverse) + (num % 10);
		// remove the last digit of num
		num    /= 10;
	}

	return ( number == reverse );
}

//===================================================================
//                         SECOND METHOD
//===================================================================
int reverseNumber1(int number, int reverse);
int reverse1( int number )
{
	return reverseNumber1(number, 0);
}
int reverseNumber1(int number, int reverse)
{
	// Reverse of a one digit number is that number
	if ( number == 0 ) return reverse;
	// Add last digit of number to reverse and remove from number
	return reverseNumber1( number / 10, 10 * reverse + number % 10);
}
bool isPalindrome2(int number)
{
	return ( number == reverse1(number));
}
//===================================================================
//			  THIRD METHOD
//===================================================================

string reverseNumber2( string number )
{
	if ( number.size() == 1 )
		return number;
	return number[number.size()-1] + reverseNumber2( number.substr(0, number.size()-1) );
}
bool isPalindrome3(int number)
{
	return (number == stoi(reverseNumber2(to_string(number))));
}
int main()
{
	int number;
	cout << "Enter a number: ";
	cin  >> number;
	
	
	if (isPalindrome1(number))
		cout << "Method1: " << number << " is a palindrome." << endl;
	else
		cout << "Method1: " << number << " is not a palindrome." << endl;
	
	  if (isPalindrome2(number))
                cout << "Method2: " << number << " is a palindrome." << endl;
        else
                cout << "Method2: " << number << " is not a palindrome." << endl;

	  if (isPalindrome3(number))
                cout << "Method3: " << number << " is a palindrome." << endl;
        else
                cout << "Method3: " << number << " is not a palindrome." << endl;

}
