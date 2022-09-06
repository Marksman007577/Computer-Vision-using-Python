import cv2
import numpy as np


def read_image(image_path):
    image = cv2.imread(image_path)
    