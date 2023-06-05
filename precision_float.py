# Representing precise decimals

from decimal import Decimal, getcontext
getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))

print(1.1+2.2)