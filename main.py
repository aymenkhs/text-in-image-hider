import cv2
import numpy as np


def put_text(text ,img_path):
    pass

def main():
    text = "hello world!"
    img_path = "tree.jpg"

    img = cv2.imread(img_path)

    if img is None:
        print("image empty")
    else:
        pass


if __name__ == '__main__':
    main()
