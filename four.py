from functools import reduce
from operator import mul

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(mul, spisok)
print(result)