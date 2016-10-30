
def primes(number):
    if number>1:
        for numb in range(2, number):

            if number%numb==0:

                return False
            else:
                continue
        return True
    else:
         return False





def primes_list(number):
    our_primes=[]
    for numb in range(2,number+1):
        if primes(numb):
           our_primes.append(numb)
    return our_primes
print primes_list(10)






