# python-crypto-wallet

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