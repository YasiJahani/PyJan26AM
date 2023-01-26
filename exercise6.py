
def isPrime(number):
    """
    Parameter:
        number (an int)
    Return:
        a bool: True if number is a prime number False if not
        
    Step1:
        test the argument received to ensure it is an int > 1
    Step2:
        with the help of a loop try to divide the argument received 
        ("number") by 2,3,4,5, up to number-1
        For instance, if number is 17 you can test: 2,3,4,5,...,15,16
        Ex: if number % 2 == 0 then 2 is a divisor of number
        As soon as you find a divisor of "number" you can return False
    Step3:
        At the end of the loop, you will have tested all possible
        divisor of number, you can return True: "number" is a 
        prime number
    """
    # Step 1
    if not isinstance(number, int) or number <= 1:
        raise Exception(f"Wrong argument {number}")
        # print(f"Wrong argument received: {number}!")
        # return None
        
    # Step 2
    divisor=2
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 1
        
    # Step 3
    return True

val=input("Enter an int: ")
val=int(val)
if isPrime(val):
    print(f"{val} is a prime number")
else:
    print(f"{val} is not a prime number")
    
# print("5?:",isPrime(5))
# print("12?:",isPrime(12))
# print("17?:",isPrime(17))
# print("5.2?:",isPrime(5.2))

