import ast
import os
from hashlib import sha512
from pathlib import Path

from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

PROJ_PATH = os.path.expanduser('~/wallet_files') + '/'
KEY_PATH = 'keys/'
SIGNED_PATH = 'signed_messages/'
DIGEST_PATH = 'digests/'
ENC_PATH = 'encrypted_messages/'


def key_gen(alias):
    random_generator = Random.new().read
    rsa_key = RSA.generate(2048, random_generator)

    # Create folder for public and private keys if not exists
    if not os.path.exists(os.path.expanduser('~/wallet_files/keys')):
        os.makedirs(os.path.expanduser('~/wallet_files/keys'))

    # Save keys to folder
    f = open(PROJ_PATH + KEY_PATH + alias + '.pub', 'wb')
    f.write(rsa_key.publickey().exportKey())
    f.close()

    f = open(PROJ_PATH + KEY_PATH + alias + '.priv', 'wb')
    f.write(rsa_key.exportKey())
    f.close()

    # Print success message to console
    print("Saved keys successfully to ~/wallet_files/keys/")


def load_keys(alias):
    private_key_path = Path(PROJ_PATH + KEY_PATH + alias + '.priv')
    public_key_path = Path(PROJ_PATH + KEY_PATH + alias + '.pub')
    if not (private_key_path.is_file() and public_key_path.is_file()):
        raise FileNotFoundError("Keys not found! Use the --keygen option to generate and try again")

    with open(private_key_path, 'r') as f:
        private_key = RSA.import_key(f.read())
    with open(public_key_path, 'r') as f:
        public_key = RSA.import_key(f.read())

    return private_key, public_key


def sign_and_verify(message, alias):
    # load keys
    private_key, public_key = load_keys(alias)

    hash = int.from_bytes(sha512(message.encode()).digest(), byteorder='big')
    signature = pow(hash, private_key.d, private_key.n)

    hashFromSignature = pow(signature, public_key.e, public_key.n)
    print("Signature valid:", hash == hashFromSignature)


def encrypt(message, alias, file):
    if not os.path.exists(os.path.expanduser('~/wallet_files/encrypted_messages')):
        os.makedirs(os.path.expanduser('~/wallet_files/encrypted_messages'))

    private_key, public_key = load_keys(alias)

    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(message.encode())

    # Save encrypted msg
    f = open(PROJ_PATH + ENC_PATH + file, 'wb')
    f.write(encrypted)
    f.close()

    print(F"Saved encrypted message correctly to {file}")


def decrypt(encrypted_msg, alias):
    encrypted_msg_path = Path(PROJ_PATH + ENC_PATH + encrypted_msg)
    if not encrypted_msg_path.is_file():
        raise FileNotFoundError(F"Encrypted message {encrypted_msg} not found - please check ~/encrypted_messages")

    with open(encrypted_msg_path, 'rb') as f:
        encrypted_message = f.read()

    private_key, public_key = load_keys(alias)

    decryptor = PKCS1_OAEP.new(private_key)
    message = decryptor.decrypt(ast.literal_eval(str(encrypted_message)))

    print(F"Success! Decrypted message is {message}")
