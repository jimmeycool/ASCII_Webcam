import os

import argparse

from webcam import Webcam, run

parser = argparse.ArgumentParser(description='''
    ASCII Console Webcam

    Converts the terminal into a webcam display using only
    ASCII charaters. You can specify the dimensions, which
    camera to use, and how to clear the window.
    ''')

parser.add_argument('-w',
                    '--width',
                    type=int,
                    default=80,
                    help="The width in charaters of the screen")
parser.add_argument('-H',
                    '--height',
                    type=int,
                    default=30,
                    help="The height in lines of the screen")
parser.add_argument('-c',
                    '--clear',
                    type=str,
                    default=None,
                    help="Override the clear console command to specified")
parser.add_argument(
    '-d',
    '--deviceid',
    type=str,
    default=0,
    help="Camera id to use, 0 is system default, rest are other cameras")

args = parser.parse_args()


def _get_clear() -> str:
    """
    Gets the clear command for the printer

    Returns:
        str: clear command
    """
    return args.clear or 'cls' if os.name == 'nt' else 'clear'


def main():
    """
    Process the args and run the webcam
    """
    with Webcam(args.deviceid).start() as cam:
        run(cam, args.width, args.height, _get_clear())


if __name__ == '__main__':
    main()