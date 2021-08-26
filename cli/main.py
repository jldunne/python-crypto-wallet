import os
import argparse
import cryptographic


def main():
    # create parser object
    parser = argparse.ArgumentParser(description="A Python CLI for managing cryptocurrencies")

    # defining arguments for parser object
    parser.add_argument("-kg", "--keygen", type=str, nargs=1,
                        metavar="key_name", default=None,
                        help="Generates public and private key pair under supplied filename")

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.keygen is not None:
        cryptographic.key_gen(args)


if __name__ == "__main__":
    # calling the main function
    main()














