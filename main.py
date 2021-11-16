import cv2
import numpy as np


def write():
    text = "helloworld45"
    img_path = "tree.jpg"
    new_path = "tree_newrrrr.png"

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

            h_index = 0
            v_index = 0
            c_index = 0
            for char in text_bit:
                for bit in char:
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

            for _ in range(8):
                img[h_index, v_index, c_index] = 0

                if c_index == c-1:
                    c_index = 0
                    v_index += 1
                else:
                    c_index += 1

                if v_index == v:
                    v_index = 0
                    h_index += 1

        cv2.imwrite(new_path, img)


def extract_text(bits):
    index = 0
    list_words = ''
    word = []
    for i in range(len(bits)):
        word.append(bits[i])
        index += 1
        if index == 7:
            print(word, end=' ')
            word = int(''.join(word),2)
            print(word, end=' ')
            if word == 0:
                return list_words

            word = chr(word)
            print(word)
            list_words += word

            word = []
            index = 0

    return list_words

def read():
    img_path = "tree_newrrrr.png"
    img = cv2.imread(img_path)

    if img is None:
        print("image empty")
    else:
        h,v,c = img.shape

        bits = []
        for i in range(h):
            for j in range(v):
                for k in range(c):
                    bits.append(img[i,j,k])

        binairies = lambda x: '1' if not x % 2 == 0 else '0'
        bits  = [binairies(num) for num in bits]
        import pdb; pdb.set_trace()
        list_words = extract_text(bits)
        print()
        print(list_words)



if __name__ == '__main__':
    write()
    read()
