import random
from random import randint

low = int(input('Lower limit >> '))
up = int(input('Upper limit >> '))

for i in range(100):
    answer = random.randint(low, up)
    print(answer)