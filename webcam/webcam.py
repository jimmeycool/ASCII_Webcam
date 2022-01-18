"""
Module for interacting with the webcam
"""

from contextlib import contextmanager

import cv2


class Webcam:
    """
    Disposable class for working with the webcam
    """

    def __init__(self, device_num: int = 0):
        """
        Create a webcam object

        Args:
            device_num (int, optional): Device number used
                to pick which webcame to use, 0 is machine default. Defaults to 0.
        """
        self.device_num = device_num
        self.capture = None

    @contextmanager
    def start(self):
        """
        Starts an active connection to a webcam

        Yields:
            Webcam: Active webcam connection from cv2
        """
        try:
            self.capture = cv2.VideoCapture(self.device_num)
            yield self
        finally:
            self.capture.release()

    def grey_frame(self, width: int, height: int):
        """
        Grabs a black and white frame, converts it to greyscale,
        and scales it

        Args:
            width (int): Width of frame
            height (int): Height of frame
        """
        _, frame = self.capture.read()

        return cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
                          (width, height))
