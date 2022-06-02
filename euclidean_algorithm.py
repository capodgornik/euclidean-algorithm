def checkGreatestNum(num1, num2):
    '''
    Checks to make sure the first number is bigger than the second number. 
    '''
    
    if num1 < num2:
        num3 = num2
        num2 = num1
        num1 = num3
    return((num1, num2))

def findGCD(num1, num2):
    ''' 
    Finds the greatest common divisor between two numbers. 
    '''
    
    num_list = checkGreatestNum(num1, num2)
    
    prev = num_list[0]
    curr = num_list[1]
    while curr != 0:
        next = prev % curr
        prev = curr
        curr = next
    return(prev)
    
def main():

    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    
    gcd = findGCD(first_num, second_num)
    
    print("The GCD of " + str(first_num) + " and " + str(second_num) + " is " + str(gcd))

if __name__ == '__main__':
    main()
