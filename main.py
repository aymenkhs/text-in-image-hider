import cv2
import numpy as np

def bin_to_decimal(binary):
    binary

def main():
    text = "hello world!"
    img_path = "tree.jpg"
    new_path = "tree_new.jpg"

    img = cv2.imread(img_path)

    if img is None:
        print("image empty")
    else:

        h,v,c = img.shape

        if len(text)+1 > h*v:
            raise ValueError()
        else:
            to_bin = lambda n: list(bin(n).replace("0b", ""))
            text_bit = [to_bin(ord(char)) for char in text]
            print(text_bit)

            h_index = 0
            v_index = 0
            c_index = 0
            for char in text_bit:
                for bit in char:
                    print(h_index, v_index, c_index)
                    pixel = img[h_index, v_index, c_index]
                    pixel_b = to_bin(pixel)
                    pixel_b[-1] = bit
                    img[h_index, v_index, c_index] = int("".join(pixel_b),2)

                    if c_index == c-1:
                        c_index = 0
                        v_index += 1
                    else:
                        c_index += 1

                    if v_index == v:
                        v_index = 0
                        h_index += 1
        cv2.imwrite(new_path, img)


if __name__ == '__main__':
    main()
