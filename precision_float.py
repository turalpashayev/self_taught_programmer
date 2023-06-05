# Representing precise decimals

# Import decimal module, Decimal class and getcontext function
from decimal import Decimal, getcontext
# Set the precision to any desired number. I used 10 below.
getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2)) # output: 3.300000000

print(1.1+2.2)  # output: 3.3000000000000003