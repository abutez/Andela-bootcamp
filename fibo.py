def fibo(x):

   if x <= 1:
       return x
   else:
       return(fibo(x-1) + fibo(x-2))


nterms = int(input("How many terms? "))


if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))