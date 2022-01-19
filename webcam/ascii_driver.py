"""
Module for running the ascii webcam
"""

import os
import sys
from typing import Iterable

import cv2
import numpy as np

from webcam.webcam import Webcam

ASCII_MAP = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
"""
A list of the range of ascii brightness values, starting from
0 brightness to full brightness
"""


def _create_ascii(numbers: Iterable[Iterable[int]]) -> str:
    """
    Converts the list of numbers into a string of ascii
    chars.

    Args:
        numbers (Iterable[Iterable[int]]): 2D array of numbers to convert

    Returns:
        str: String of ascii chars
    """
    return os.linesep.join(
        [''.join([ASCII_MAP[num] for num in row]) for row in numbers])


def print_ascii(numbers: Iterable[Iterable[int]], clear: str) -> None:
    """
    Converts the 2D arrray of

    Args:
        numbers (Iterable[Iterable[int]]): 2D array of numbers to convert
        clear (str): The clear command for clearing the screen
    """
    os.system(clear)
    sys.stdout.flush()
    sys.stdout.write(_create_ascii(numbers))


def run(cam: Webcam, width: int, height: int, clear: str):
    """
    Runs the ASCII webcam

    Args:
        cam ([type]): Connection to webcam
        width (int): Width of screen
        height (int): Height of screen
        clear (str): The clear command for clearing the screen
    """
    while True:
        grayscale = cam.grey_frame(width, height)

        # init ASCII array with normalized grey img
        normalized = cv2.normalize(grayscale, np.zeros((width, height)), 0,
                                   len(ASCII_MAP) - 1, cv2.NORM_MINMAX)

        print_ascii(normalized, clear)

        sys.stdout.write(
            f'{os.linesep}{os.linesep}Ctrl+C to stop...{os.linesep}')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
