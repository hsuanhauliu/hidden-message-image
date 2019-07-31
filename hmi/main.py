"""
    A simple program that allows you to hide messages in images.
"""


from argparse import ArgumentParser

import hmi


MODES = ['encrypt', 'decrypt']


def main():
    """ Main function """
    mode = parse_inputs()
    check_mode(mode)
    process(mode)


def parse_inputs():
    """ Helper method for parsing user input """
    parser = ArgumentParser(description='Input either encrypt or decrypt.')
    parser.add_argument('mode', type=str, help='show cam while recording')
    args = parser.parse_args()

    return args.mode


def check_mode(mode):
    """ Check to see if mode is valid """
    if mode not in MODES:
        raise ValueError('Choose either encrypt or decrypt')


def process(mode):
    """ Start process depends on the mode """
    if mode == MODES[0]:
        img = input('Input image: ')
        message = input('Input message: ')
        output = input('Output name (press enter to use default name): ')
        if not output:
            hmi.encrypt(message, img)
        else:
            hmi.encrypt(message, img, output_file=output)
    elif mode == MODES[1]:
        img_1 = input('Input image 1: ')
        img_2 = input('Input image 2: ')
        print(hmi.decrypt(img_1, img_2))


if __name__ == '__main__':
    main()
