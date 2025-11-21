# A program that uses recursive functions to find all palindromic primes between two integers N, M, supplied as input
#Vincent T Mukwevo MKWVIN004
# 24/04/2024

import sys
sys.setrecursionlimit (30000)

def primefinder(N,count):
    sys.setrecursionlimit (30000)
    if count < N:
       if N%(count) == 0:
          return False
       else:
         count +=1
       return True and (primefinder(N,count))
    else: return True

def palindrome(testprime):
    if len(testprime)> 1:
      if (testprime[0] == testprime[-1]) and palindrome(testprime[1:-1]):
        return True
      else:
        return False
    else: return True

def palindromeprinter(N,M):
   if N <= M:
      if primefinder(N,2):
        if palindrome(str(N)):
           print(N)
      N=N+1
      palindromeprinter(N,M)
   return

# obtaining the user input
lowerlim = int(input('Enter the starting point N:\n'))
Upperlim = int(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
palindromeprinter(lowerlim,Upperlim)