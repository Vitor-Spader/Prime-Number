#calculador de numero primo
import math

class p_number():
    
    def __init__(self,num,num_threads=None):
        self.num = num
        self.num_threads = num_threads
    
    def __str__(self) -> str:
        return "return prime numbers"
    def prime_calc(self):

        if self.num < 2:
            return False
        elif self.num == 2:
            return True
        if (self.num % 2) == 0:
            return False
        count = 0
        for x in range(2,int(math.sqrt(self.num))):
            if (self.num % x) == 0:
                count += 1
                break
        if count == 0 :
            return True
        else:
            return False
p = []
for x in range(0,50000000):
    p.append(p_number(x))
    print(x,":","prime" if p[x].prime_calc() else "its not prime")