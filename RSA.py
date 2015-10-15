__author__ = 'Egbert'
import methods
import random

log = True

#*******************
# RSA INSTANCE
#*******************
#
# You need to initialize this class with a Prime P and Q.
# In This init phase we then calculate all the necessary variables needed for the RSA crypto system
# If this init has finished you can call encrypt_message and decrypt_message to encrypt or decrypt a message with the
# given P and Q primes.
#
# For excersie 7.6 we added the function setPublicKey.
# This is because we need to give the SMALLEST exponent e in this excersice, and not a random one.
# So by calling this function (With a exponend e we calculated ourselfs),it generates a new private key,
# and we are off to the races.
#
#*******************

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = self.getModulus(p, q)
        self.mTotient = self.totient(p,q)
        self.publicKey = self.get_public_key(self.mTotient)
        self.privateKey = self.get_private_key(self.publicKey, self.mTotient)

        if(log):
            print("****************")
            print("**RSA_instance**")
            print("****************")
            print("N = {}".format(self.n))
            print("totient = {}".format(self.mTotient))
            print("Public Key = (N,e) = ({},{})".format(self.n, self.publicKey))
            print("Private Key = {}".format(self.privateKey))
            print("****************")

    def encrypt_message(self, m):
        #return m^e mod n
        return methods.modMacht(m, self.publicKey, self.n)

    def decrypt_message(self, m):
        #return m^d mod n
        return methods.modMacht(m, self.privateKey, self.n)

    def totient(self, p, q):
        return (p-1) * (q-1)

    def getModulus(self, p,q):
        return p*q

    def get_e(self, mTotient):
        e = 1
        t = 0

        while not methods.isProbablePrime(e) and not t == 1:            #run this loop until e is a prime, with a gcd of 1 with mTotient.
            e = random.randint(3, mTotient)                             #get random number between 3 and your mTotient
            t, x, y = methods.extendedEuclidianAlgorithm(e,mTotient)    #Use the xEA to determine the GCD.

        return e

    def get_public_key(self, mTotient):
        return self.get_e(mTotient)

    def get_private_key(self, e, mTotient):
        t,x,y = methods.extendedEuclidianAlgorithm(e, mTotient)

        d = x % mTotient
        return d

    def setPublicKey(self , e):
        self.publicKey = e
        self.privateKey = self.get_private_key(e, self.mTotient)

        if(log):
            print(">>RSA_INSTANCE: Changed the public key (and corresponding private key) to :")
            print(">>RSA_INSTANCE: publickey (N,e) = ({},{})".format(self.n, self.publicKey))
            print(">>RSA_INSTANCE: privateKey (d) = ({})".format(self.privateKey))
