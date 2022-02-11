def gcd(x, y):
   gcd = 1
   if x % y == 0:
       return y
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break
   return gcd
n1=int(input("n1:"))
n2=int(input("n2:"))
print("GCD of ",n1," & " ,n2, "=",gcd(n1,n2 ))
