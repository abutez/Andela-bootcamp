# function to test various data types
def data_type(n):
# condititonal statements for string,boolean, lists and integer
  if isinstance(n,str):
    return len(n)
  elif isinstance(n,type(None)):
      return"no value"
  elif isinstance(n,bool):
            return (n)
  elif isinstance(n,int):
            if n<100:
              return "less than 100"
            elif n>100:
              return"more than 100"
            else:
              return"equal to 100"

  elif isinstance(n,list):
    if len(n)>=3:
        return n[2]
    else:
        return None