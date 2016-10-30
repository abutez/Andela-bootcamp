def fizz_buzz(x):
  if x % 3==0 and x % 5==0:
    return "fizz buzz"
  elif x % 5==0:
      return "buzz"
  elif x % 3==0:
        return " Buzz"
  else:
    return x
print fizz_buzz(58)