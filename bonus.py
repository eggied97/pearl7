import methods
import RSA
import time

__author__ = 'Egbert'

BITLENGTH_PRIME = 512

start = 0
startBase = 0


#Function to generate 2 primes, p and q, wich have a N which is an odd bit length
def generate_p_and_q():
    p = methods.getPrime(BITLENGTH_PRIME)
    q = methods.getPrime(BITLENGTH_PRIME)

    while methods.log2(p*q) % 2 == 0: #if n is even, generate new p and q
        if RSA.log: print("bitLength of N ({}) was not odd".format(methods.log2(p*q)))
        p = methods.getPrime(BITLENGTH_PRIME)
        q = methods.getPrime(BITLENGTH_PRIME)

    return p, q



checkIfWeNEedToGenerateOwnPrimes = input("Should i generate my own primes, or do you give me my primes? (give or generate)")

if(checkIfWeNEedToGenerateOwnPrimes == "give"):
    p = int (input("Prime P is: "))
    q = int (input("Prime q is: "))

    print("We are now using p={} , q={}".format(p,q))
else:
    print("I'm now going to generate the primes P and Q, with bit length: {}".format(BITLENGTH_PRIME))
    print("------------------------")
    print("generating primes P and Q")

    bitlength = input("What bit size do P and Q need to be? (fill in the bitsize (>= 16 bits), or blank for the standard {})"
                               .format(BITLENGTH_PRIME))

    if not bitlength == "":             #check if input is not empty (then we use default bitlength
        if(int (bitlength) >= 16):      #check if bitlength is over 16 bits
            BITLENGTH_PRIME = bitlength

    start = startBase = time.clock()    #start the timing

    p, q = generate_p_and_q()           #generate P and Q (these we not given earlier)

    print("This took {} seconds".format(time.clock() - start))
    print("P = {}".format(p))
    print("q = {}".format(q))
    print("bit-size modulo N : {}".format(methods.log2(p*q)))
    print("------------------------")

start = time.clock()

message = 88357295638463824038562958736483910039478

messageInput = input("Which message do you want to encrypt and decrypt? (leave blank for the bonus excersise text ({}))"
                     .format(message))

if not messageInput == "":
    message = int (messageInput)

print("Message to encrypt and decrypt = {}".format(message))
print("------------------------")
print("Now we are going to setup the RSA instance")
start = time.clock()

mRSA = RSA.RSA(p,q)     #generate RSA Instance

print("This took {} seconds".format(time.clock() - start))
print("------------------------")
print("Now we are going to encrypt.")
start = time.clock()

encrypted = mRSA.encrypt_message(message) #encrypt the message

print("This took {} seconds".format(time.clock() - start))
print("plaintext => cypher")
print("{} => {}".format(message, encrypted))
print("------------------------")
print("Now we are going to decrypt.")
start = time.clock()

decrypted = mRSA.decrypt_message(encrypted) #decrypt the encrypted message

print("This took {} seconds".format(time.clock() - start))
print("cypher => plaintext")
print("{} => {}".format(encrypted, decrypted))
print("Is the decrypted encrypted message the same as the original? : {}".format(message == decrypted))
print("------------------------")
print("We are done now, total time was : {} seconds".format(time.clock() - startBase))




