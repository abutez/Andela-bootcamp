# a function to identify prime numbers and print out the list
def primes(number):
# an if statement to check weather a given integer is prime or not
    if number>1:
        for numb in range(2, number):
            if number%numb==0:
                return False
            else:
                continue
        return True
    else:
         return False
# function to print a list of prime numbers
def primes_list(number):
    our_primes=[]
    for numb in range(2,number+1):
        if primes(numb):
           our_primes.append(numb)
    return our_primes
print primes_list(10)






