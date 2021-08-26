import argparse
import cryptographic


def main():
    # create parser object
    parser = argparse.ArgumentParser(prog='wallet', description="A Python CLI for managing cryptocurrencies")

    # defining arguments for parser object
    parser.add_argument("-kg", "--keygen", type=str, nargs=0,
                        metavar="key_name", default=None,
                        help="Generates public and private key pair")

    parser.add_argument("-s", "--sign", type=str, nargs=2, default=None,
                        metavar=("message", "filename"), help="Signs message and stores in filename")

    parser.add_argument("-v", "--verify", type=str, nargs=1, default=None,
                        metavar="filename", help="Signs message and stores in filename")

    parser.add_argument("-e", "--encrypt", type=str, nargs=2, default=None,
                        metavar=("message", "filename"), help="Encrypts message and stores in filename")

    parser.add_argument("-d", "--decrypt", type=str, nargs=1, default=None,
                        metavar="filename", help="Decrypts filename")

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.keygen is not None:
        cryptographic.key_gen()
    if args.sign is not None:
        cryptographic.sign(args)
    if args.verify is not None:
        cryptographic.verify(args)
    if args.encrypt is not None:
        cryptographic.encrypt(args)
    if args.decrypt is not None:
        cryptographic.decrypt(args)


if __name__ == "__main__":
    # calling the main function
    main()
