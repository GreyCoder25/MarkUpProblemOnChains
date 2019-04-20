import numpy as np
from io import StringIO
# import os

from mark_up import TObject, general_mark_up
from text_image_generation import TextImageGenerator


def create_task(letters_dict, text_image):
    text_image = np.array(text_image)
    n_objects = text_image.shape[1] + 1         # +1 because of first fake object to make computations simpler
    neighbors = []
    for letter in letters_dict:
        neighbors.append(letters_dict[letter].width)

    objects = [TObject(i, list(letters_dict.keys()), neighbors) for i in range(n_objects)]
    for letter in letters_dict:
        objects[0].q[letter] = 0
    for image in letters_dict:
        for obj in objects[1:]:
            if obj.index >= letters_dict[image].width:
                for k_ in letters_dict:
                    obj.g[obj.index - letters_dict[image].width][k_][image] =\
                        ((text_image[:, obj.index - letters_dict[image].width:obj.index] - np.array(letters_dict[image]))**2).sum()
    return objects


if __name__ == '__main__':
    # text string recognition
    text_image_generator = TextImageGenerator()
    text_image = text_image_generator.generate_string_image('ABC_BACC_CABABB', noise=True, noise_epsilon=0.96)
    text_image.show()
    objects = create_task(text_image_generator.letters_dict, text_image)
    labeling = general_mark_up(objects)
    print(labeling)