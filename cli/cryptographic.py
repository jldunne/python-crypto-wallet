import os
from pathlib import Path

import rsa
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

PROJ_PATH = os.path.expanduser('~/wallet_files') + '/'
KEY_PATH = 'keys/'
SIGNED_PATH = 'signed_messages/'
DIGEST_PATH = 'digest/'
ENC_PATH = 'encrypted_messages/'


def key_gen():
    random_generator = Random.new().read
    rsa_key = RSA.generate(2048, random_generator)

    # Create folder for public and private keys if not exists
    if not os.path.exists(os.path.expanduser('~/wallet_files/keys')):
        os.makedirs(os.path.expanduser('~/wallet_files/keys'))

    # Save keys to folder
    f = open(PROJ_PATH + KEY_PATH + 'public.pem', 'wb')
    f.write(rsa_key.publickey().exportKey())
    f.close()

    f = open(PROJ_PATH + KEY_PATH + 'private.pem', 'wb')
    f.write(rsa_key.exportKey())
    f.close()

    # Print success message to console
    print("Saved keys successfully to ~/wallet_files/keys/")


def load_keys():
    private_key_path = Path(PROJ_PATH + KEY_PATH + 'private.pem')
    public_key_path = Path(PROJ_PATH + KEY_PATH + 'public.pem')
    if not (private_key_path.is_file() and public_key_path.is_file()):
        raise FileNotFoundError("Keys not found! Use the --keygen option to generate and try again")

    with open(private_key_path, 'r') as f:
        private_key = RSA.import_key(f.read())
    with open(public_key_path, 'r') as f:
        public_key = RSA.import_key(f.read())

    return private_key, public_key


def load_signature_digest(file):
    signed_msg_path = Path(PROJ_PATH + SIGNED_PATH + file)
    digest_path = Path(PROJ_PATH + DIGEST_PATH + file)
    if not (signed_msg_path.is_file() and digest_path.is_file()):
        raise FileNotFoundError("Files not found! Use the --sign option to generate and try again")

    with open(signed_msg_path, 'rb') as f:
        signed_msg = f.read()
    with open(digest_path, 'rb') as f:
        digest = f.read()

    return signed_msg, digest


def sign(message, file):
    # load keys
    private_key, public_key = load_keys()

    # generate digest and signed msg
    digest = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(digest)

    # Save signed message
    if not os.path.exists(os.path.expanduser('~/wallet_files/signed_messages')):
        os.makedirs(os.path.expanduser('~/wallet_files/signed_messages'))

    # Save digest
    if not os.path.exists(os.path.expanduser('~/wallet_files/digests')):
        os.makedirs(os.path.expanduser('~/wallet_files/digests'))

    # Save signed msg
    f = open(PROJ_PATH + SIGNED_PATH + file, 'wb')
    f.write(signature)
    f.close()

    # Save digest
    f = open(PROJ_PATH + DIGEST_PATH + file, 'wb')
    f.write(digest)
    f.close()

    print(F"Saved signed message and digest correctly to {file}")


def verify(file):
    private_key, public_key = load_keys()
    signed_msg, digest = load_signature_digest(file)

    try:
        pkcs1_15.new(public_key).verify(digest, signed_msg)
    except ValueError:
        print("The signature isn't valid!")

    print("The signature is valid!")


def encrypt(message, file):
    if not os.path.exists(os.path.expanduser('~/wallet_files/encrypted_messages')):
        os.makedirs(os.path.expanduser('~/wallet_files/encrypted_messages'))

    private_key, public_key = load_keys()
    encrypted_msg = rsa.encrypt(message.encode(), public_key)

    # Save encrypted msg
    f = open(PROJ_PATH + ENC_PATH + file, 'wb')
    f.write(encrypted_msg)
    f.close()

    print(F"Saved encrypted message correctly to {file}")


def decrypt(encrypted_msg):
    encrypted_msg_path = Path(PROJ_PATH + ENC_PATH + encrypted_msg)
    if not encrypted_msg_path.is_file():
        raise FileNotFoundError(F"Encrypted message {encrypted_msg} not found - please check ~/encrypted_messages")

    with open(encrypted_msg_path, 'rb') as f:
        encrypted_message = f.read()

    public_key, private_key = load_keys()

    dec_message = rsa.decrypt(encrypted_message, private_key).decode()
    print(F"Success! Decrypted message is {dec_message}")
