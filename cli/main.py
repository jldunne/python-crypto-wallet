import os
from Crypto.PublicKey import RSA
from Crypto import Random

def key_gen(bits=2048):
    random_generator = Random.new().read
    rsa_key = RSA.generate(bits, random_generator)
    return rsa_key.exportKey(), rsa_key.publickey().exportKey()

def sign:

def verify:

def encrypt:

def decrypt:














