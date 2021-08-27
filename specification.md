# Overview

The purpose of the wallet is to generate public and private key pairs, and to perform some basic cryptographic operations. It will take the form of a Python command line tool.

# Features
Below are the implementation details of each of the wallet features.

## Key Generation
- Generate a random private key (find good source of randomness for this)
- Use crypto library to generate public key
- Store these in some data structure that is saved to memory - so that we don't lose the keys when we exit the program

## Key Management
- Keys need to be read from memory and it is possible that we have multiple keys with various aliases. Maybe we have a keystore where the user can choose which key is the active key, or which they would like to use to sign the transactions

## Signing Messages
- Sign text messages with private keys

## Verifying Signatures
- Verify keys with public key, digest and signature - follow this tutorial for more details - https://blog.epalm.ca/signing-and-verifying-with-rsa-keys/

## Encrypting Messages
- Use python cryptography library to encrypt

## Decrypting Messages
- Use python cryptography library to decrypt