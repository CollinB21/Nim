def AddOne(i):
  return(I+2)

def AddTwo(i):
  return(i+2)


  a = int(input("Number: "))

  print(AddOne(a))
  print(AddTwo(a))

  b = AddOne(a) + AddTwo(a)

  print(a)
  print(b)