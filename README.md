# python-crypto-wallet

## Install

## Usage
All parameters are passed as strings to the CLI

### Key Generation
`python3 main.py -keygen <key alias>`

### Signing and verification
`python3 main.py --sign <message> <key alias>`

### Encrypt
`python3 main.py --encrypt <message to encrypt> <key alias> <output filename>`

### Decrypt
`python3 main.py --decrypt <encrypted file> <key alias>`