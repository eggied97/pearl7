__author__ = 'Egbert'

import RSA


p,q = 29,31 #given in the excersise
m = 4       #Message we want to encrypt

mRSA = RSA.RSA(p,q) #initialize the RSA instance

#Set the public key to 11:
    # e = 3 => 840 / 3 = 280 (not a gcd of 1)
    # e = 5 => 840 / 5 = 168 (not a gcd of 1)
    # e = 7 => 840 / 7 = 120 (not a gcd of 1)
    # e = 11 => 840 / 11 = 76.363636 (GCD of 1, so this is the smallest e)
mRSA.setPublicKey(11)


encrypted = mRSA.encrypt_message(m)
decrypted = mRSA.decrypt_message(encrypted)

print("encrypted : decrypted | {} : {}".format(encrypted, decrypted))

