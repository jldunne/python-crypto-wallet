# python-crypto-wallet

## Overview
The purpose of the wallet is to generate public and private key pairs, and to perform some basic cryptographic operations. It will take the form of a Python command line tool.

### Features
Below are the implementation details of each of the wallet features.

### Key Generation
- Generate a random private key (find good source of randomness for this)
- Use crypto library to generate public key
- Store these in some data structure that is saved to memory - so that we don't lose the keys when we exit the program

### Key Management
- Keys need to be read from memory and it is possible that we have multiple keys with various aliases. Maybe we have a keystore where the user can choose which key is the active key, or which they would like to use to sign the transactions

### Signing Messages
- Sign text messages with private keys

### Verifying Signatures
- Verify keys with public key, digest and signature

### Encrypting Messages
- Use python cryptography library to encrypt

### Decrypting Messages
- Use python cryptography library to decrypt

## Install
Instructions for installation and testing has been done on MacOS.

Clone the project, then start a Python virtual environment in the project root. For example:

```
python3 -m venv myenv
source myenv/bin/activate
```

Install from requirements

`pip install -r requirements.txt`

Navigate to `cli/` to use the commands provided

## Usage
All parameters are passed as strings to the CLI

### Key Generation
`python3 main.py --keygen <key alias>`

### Signing and verification
`python3 main.py --sign <message> <key alias>`

### Encrypt
`python3 main.py --encrypt <message to encrypt> <key alias> <output filename>`

### Decrypt
`python3 main.py --decrypt <encrypted file> <key alias>`