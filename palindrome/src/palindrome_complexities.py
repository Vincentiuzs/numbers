import palindrome
import time

def run():

    with open("results/while_loop_python.csv","a") as f:
        f.write("Number,Time,Palindrome,Digits")

        for number in range(0, 1000000):
            total = 0

            for i in range(0,100):
                start = time.time()
                palin = palindrome.isPalindrome1(number)
                end   = time.time()
                
                difference = end - start
                total += difference
            
            time_taken = total / 100;

            f.write("\n" + str(number) + "," + str(time_taken) + "," + str(palin) + "," +  str(len(str(number))))

    with open("results/for_loop_arrays_python.csv","a") as f:
        f.write("Number,Time,Palindrome,Digits")

        for number in range(0, 1000000):
            total = 0

            for i in range(0,100):
                start = time.time()
                palin = palindrome.isPalindrome2(number)
                end   = time.time()
                
                difference = end - start
                total += difference

            time_taken = total / 100;
            f.write("\n" + str(number) + "," + str(time_taken) + "," + str(palin) + "," + str(len(str(number))))

    with open("results/recursion_reverse_integer_python.csv","a") as f:
        f.write("Number,Time,Palindrome,Digits")

        for number in range(0, 1000000):
            total = 0

            for i in range(0,100):
                start = time.time()
                palin = palindrome.isPalindrome3(number)
                end   = time.time()
                
                difference = end - start
                total += difference

            time_taken = total / 100;
            f.write("\n" + str(number) + "," + str(time_taken) + "," + str(palin) + "," + str(len(str(number))))

    with open("results/string_reverse_python.csv","a") as f:
        f.write("Number,Time,Palindrome,Digits")

        for number in range(0, 1000000):
            total = 0

            for i in range(0,100):
                start = time.time()
                palin = palindrome.isPalindrome4(number)
                end   = time.time()
                
                difference = end - start
                total += difference

            time_taken = total / 100;
            f.write("\n" + str(number) + "," + str(time_taken) + "," + str(len(str(number))))


if __name__ == "__main__":
    run()

