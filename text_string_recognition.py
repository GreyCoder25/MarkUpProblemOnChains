from PIL import Image
import random as rnd
import numpy as np

images = list(map(Image.open, ['A.jpg', 'B.jpg', 'C.jpg', 'whitespace.jpg']))

widths, heights = zip(*(i.size for i in images))

height = max(heights)
width = 500


def generate_string(letters, size):

    string_image = Image.new('L', size)
    x_offset = 0

    while x_offset != size[0]:
        next_letter = letters[rnd.randint(0, len(letters) - 1)]
        if next_letter.size[0] < size[0] - x_offset:
            string_image.paste(next_letter, (x_offset, 0))
            x_offset += next_letter.size[0]
        else:
            string_image.paste(letters[-1], (x_offset, 0))
            x_offset += 1

    string_image.save('text_string.jpg')
    return string_image


def weights_init(letters, text_string):

    text_string = np.array(text_string)

    n = text_string.shape[1]
    k = len(letters)
    weights = {}
    char_keys  = [chr(i) for i in range(97, 97 + k - 1)] + [' ']

    for char, image in zip(char_keys, letters):
        weights[char] = np.empty(n - image.size[0] + 1)
        curr_image = np.array(image)
        for i in range(text_string.shape[1] - image.size[0] + 1):
            weights[char][i] = ((text_string[:, i:i + curr_image.shape[1]] - curr_image) ** 2).sum()
            # print("Calculated weight: ", weights[char][i])

    return weights


text_string_image = generate_string(images, (width, height))
weights = weights_init(images, text_string_image)
print(weights)
