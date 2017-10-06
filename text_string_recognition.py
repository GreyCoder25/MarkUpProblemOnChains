from PIL import Image
import random as rnd

images = list(map(Image.open, ['A.jpg', 'B.jpg', 'C.jpg', 'whitespace.jpg']))
widths, heights = zip(*(i.size for i in images))

height = max(heights)
width = 500


def generate_string(images, size, length):

    string_image = Image.new('RGB', size)
    x_offset = 0

    while x_offset != size[0]:
        next_letter = images[rnd.randint(0, len(images) - 1)]
        if next_letter.size[0] < size[0] - x_offset:
            string_image.paste(next_letter, (x_offset, 0))
            x_offset += next_letter.size[0]
        else:
            string_image.paste(images[-1], (x_offset, 0))
            x_offset += 1

    string_image.save('text_string.jpg')


def weights_init():


generate_string(images, (width, height), 8)

