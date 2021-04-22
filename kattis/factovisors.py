import math
import sys

_sieve_size = 0
bs = []
primes = []


def sieve(upperbound):
  global _sieve_size, bs, primes

  _sieve_size = upperbound+1
  bs = [True] * 10000010
  bs[0] = bs[1] = False
  for i in range(2, _sieve_size):
    if bs[i]:
      for j in range(i*i, _sieve_size, i):
        bs[j] = False
      primes.append(i)

def isPrime(N):
  global _sieve_size, primes
  if N <= _sieve_size:
    return bs[N]
  for p in primes:
    if p * p > N:
      break
    if N % p == 0:
      return False
  return True

def prime_factors(N):
  global primes
  factors = []
  if N == 1 or N == 0:
    return [1]

  for p in primes:
    if p * p > N:
      break
    while N % p == 0:
      N //= p
      factors.append(p)
  if N != 1:
    factors.append(N)

  return factors


def divides(m,n):

    factors = prime_factors(m)

    for i in range(0,n+1):
        n_factors = prime_factors(i)

        for element in n_factors:
            try:
                factors.remove(element)
            except:
                print()
            if len(factors) == 0:
                return True

    if len(factors) != 0:
        return False


sieve(50000)

all_numbers = []*50000

for i in range(2, 50001):

    all_numbers[i] = {}
    f_i = prime_factors(i)

    for element in f_i:

        if element in all_numbers[i]:
            all_numbers[i][element] += 1
        else:
            all_numbers[i][element] = 1



n, m = map(int, input().split())

if divides(m, n):
    print(str(m) + " divides " + str(n) + "!")
else:
    print(str(m) + " does not divides " + str(n) + "!")







