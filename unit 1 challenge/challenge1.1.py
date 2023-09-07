def fact(n):
 if n==0 or n==1:
  return 1
 else :
  return n*fact(n-1)
 
num=9
res=fact(num)

print("The factorial of ", num,  " is ", res)
      