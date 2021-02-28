def reverseInteger(num):
  rv = 0

  while num > 0:
    rv = (num % 10) + (rv * 10)
    num = num // 10
  
  return rv



if __name__ == "__main__":
  n = reverseInteger(1234)
  print(n)
