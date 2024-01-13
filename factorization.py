## Copyright (c) MB SOFTWARE. All rights reserved.

class Factor:
    def __init__(self, n) -> None:
        self.base = n
        self.exponent = 1
    
    def __repr__(self) -> str:
        return f"{self.base}{superscript(self.exponent)}"
    
    def __str__(self) -> str:
        return f"{self.base}{superscript(self.exponent)}"

    def increase_exponent(self):
        self.exponent += 1

    def value(self):
        return self.base**self.exponent


class Factorization:
    def __init__(self, n, factors_list) -> None:
        self.n = n
        self.factors = factors_list

    def __repr__(self) -> str:
        return f"{self.n} = {' '.join(map(str, self.factors))}"
    
    def check(self):
        v = 1
        for factor in self.factors:
            v*=factor.value()
        return self.n == v

def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)]) 


def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True


def find_prime_divisors(n):
    if isPrime(n): return [n]
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            if isPrime(i):
                divisors.add(i)
            p = n//i
            if isPrime(p):
                divisors.add(p)
    return list(sorted(divisors))


def find_factorization(n):
    if n == 1: return Factorization(1,[Factor(1)])
    prime_divisors = find_prime_divisors(n)
    factors = list()
    for divisor in prime_divisors:
        factor = Factor(divisor)
        new_divisor = divisor*divisor
        while n%new_divisor == 0:
            factor.increase_exponent()
            new_divisor *= divisor
        factors.append(factor)
    return Factorization(n, factors) 


def main():
    n = int(input("Enter the number you want to factorize: ").strip())
    f = find_factorization(n)
    if f.check():
        print(find_factorization(n))
    else:
        print("Sorry... I have some problems.")

if __name__ == "__main__":
    main()