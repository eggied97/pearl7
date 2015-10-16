__author__ = 'Egbert'

from random import randrange, getrandbits
from itertools import repeat

DEBUG = False

#Modular Arrithmatic:

def modMacht(base, power, n):
    if DEBUG: print(">>Methods: base|macht|n : {}|{}|{}".format(base, power, n))
    result = 1
    base = base % n     #mod n the base

    while power > 0:    #cycle through until the power is 0
        if(power % 2) == 1: #If the power is odd
            result = (result*base) % n #it is a one, so multiply the awnser with the base

        power >>= 1 #Bitshift the power 1 bit to the right (remove the last binary digit (11101 => 1110).
        base = base**2 % n #square the base becasue we went up a bit

    return result


#implementation of the extended euclidian algorithm, following the pseudo code that was delivered via de slides.
def extendedEuclidianAlgorithm(a,b):
    if b == 0:
        t = a
        x = 1
        y = 0
        if DEBUG: print(">>Methods: t={} | x={} | y={}".format(t, x, y))

        return

    aOld = a
    bOld = b

    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1

    while b > 0:
        q = a // b
        r = a % b
        x = x2 - q * x1
        y = y2 - q * y1

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

        if DEBUG: print(">>Methods: q={} | r={} | x={} | y={} | a={} | b={} | x2={} | x1={} | y2={} | y1={}"
                        .format(q, r, x, y, a, b, x2, x1, y2, y1))

    t = a
    x = x2
    y = y2

    awnser = aOld*x+bOld*y

    if DEBUG: print(">>Methods: t={} | x={} | y={} | a*x + b*y = t => {}*{} + {}*{} = {} => {}={} "
                    .format(t, x, y, aOld, x, bOld, y, t, awnser, t))

    return t, x, y

#This is a check to see if a number is prime through the Miller-Rabin method.
#For more information see: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test?oldformat=true
def isProbablePrime(n, t = 7):
        def isComposite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True

        assert n > 0
        if n < 3:
            return [False, False, True][n]
        elif not n & 1:
            return False
        else:
            s, d = 0, n - 1
            while not d & 1:
                s += 1
                d >>= 1
        for _ in repeat(None, t):
            if isComposite(randrange(2, n)):
                return False
        return True


#get a random prime of bitlength N
def getPrime(n):
    p = getrandbits(n)              #get random number, with bitlength N
    while not isProbablePrime(p):   #Repeat this until you have a prime
        p = getrandbits(n)
    return p

#Fast, and reliable way to compute the log2 of a very large sum of primes
def log2(n):
    i = 0
    while n:
        n //= 2
        i += 1
    return i
