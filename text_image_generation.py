from PIL import Image
import random as rnd
import numpy as np


class TextImageGenerator(object):
    def __init__(self):
        self.images = list(map(Image.open, ['A.jpg', 'B.jpg', 'C.jpg', 'whitespace_10.jpg']))
        self.width, self.heights = zip(*(i.size for i in self.images))
        self.letters = ['A', 'B', 'C', '_']
        self.letters_dict = {letter: image for letter, image in zip(self.letters, self.images)}
        self.image_height = self.images[0].height

    def generate_string_image(self, text, noise=False, noise_epsilon=0):
        assert text
        # calculate width of the text image
        im_width = 0
        for symbol in text:
            im_width += self.letters_dict[symbol].width

        # create image
        string_image = Image.new('L', (im_width, self.image_height))
        x_offset = 0

        for symbol in text:
            string_image.paste(self.letters_dict[symbol], (x_offset, 0))
            x_offset += self.letters_dict[symbol].width

        if noise:
            string_image = np.array(string_image)
            for i in range(string_image.shape[0]):
                for j in range(string_image.shape[1]):
                    if rnd.random() < noise_epsilon:
                        string_image[i, j] = rnd.randint(0, 256)
            string_image = Image.fromarray(string_image)

        string_image.save('text_string.jpg')
        return string_image


if __name__ == '__main__':
    text_gen = TextImageGenerator()
    text_string_image = text_gen.generate_string_image('ABA_CBCABC__CB')
    text_string_image.show()
