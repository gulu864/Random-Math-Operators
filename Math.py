import math
print("Mathematical functions")
var=int(input("Enter a number:"))
var1=int(input("Enter a negative number"))
print("Copy Sign:", math.copysign(var,var1))
print("GCD(Greatest Common Divisor):", math.gcd(var,var1))
print("LCM(Lowest Common Multiple):", math.lcm(var,var1))

print("Ceiling number (7.989):", math.ceil(7.898))
print("Floor number(7.989):", math.floor(7.898))