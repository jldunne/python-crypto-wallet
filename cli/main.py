import argparse

import cryptographic


def main():
    # create parser object
    parser = argparse.ArgumentParser(prog='wallet', description="A Python CLI for managing cryptocurrencies")

    # defining arguments for parser object
    parser.add_argument("-kg", "--keygen", type=str, nargs=1, metavar="alias", default=None,
                        help="Generates and stores public and private key pair under supplied alias")

    parser.add_argument("-s", "--sign", type=str, nargs=3, default=None,
                        metavar=("message", "alias", "filename"), help="Signs message with key and stores in filename")

    parser.add_argument("-v", "--verify", type=str, nargs=3, default=None,
                        metavar=("message", "filename", "key alias"), help="Signs message and stores in filename")

    parser.add_argument("-e", "--encrypt", type=str, nargs=3, default=None,
                        metavar=("message", "alias", "filename"),
                        help="Encrypts message with key and stores in filename")

    parser.add_argument("-d", "--decrypt", type=str, nargs=2, default=None,
                        metavar=("filename", "alias"), help="Decrypts filename")

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.keygen is not None:
        print(args.keygen)
        cryptographic.key_gen(args.keygen[0])
    if args.sign is not None:
        print(args.sign)
        cryptographic.sign_and_verify(args.sign[0], args.sign[1])
    if args.encrypt is not None:
        cryptographic.encrypt(args.encrypt[0], args.encrypt[1], args.encrypt[2])
    if args.decrypt is not None:
        cryptographic.decrypt(args.decrypt[0], args.decrypt[1])


if __name__ == "__main__":
    # calling the main function
    main()
