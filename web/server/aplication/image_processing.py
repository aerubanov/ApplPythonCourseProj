from preprocessing import preprocessing
from classification.classifier import model, symbol_dict
import numpy as np

digits = [i for i in range(8, 18)]
let = [i for i in range(74, 100)]
minus_equal = [5, 18]


def is_upper_right(img1, img2):
    # ось у вниз!
    if img2[1][0] + img2[1][1] / 2 < img1[1][0]:
        return True


class ImageProcessor:

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.letters = None
        self.classes = None

    def preproc_image(self):
        self.letters, _ = preprocessing.letters_extract(self.path, self.out_path)

    def classify_character(self):
        imgs = [i[2] for i in self.letters]
        n = len(imgs)
        imgs = np.concatenate(imgs)
        imgs = np.ones((n, 28, 28, 1)) - imgs.reshape(n, 28, 28, 1) / 255
        prediction = model.predict(imgs)
        self.classes = np.argmax(prediction, axis=1)

    def pars_expression(self):
        s = symbol_dict[self.classes[0]]
        prev_letter = self.letters[0]
        prev_class = self.classes[0]
        if self.classes[0] not in digits and self.classes[0] not in let:
            s += ' '
        for i in range(1,len(self.letters)):
            cls = self.classes[i]
            smbl = symbol_dict[cls]
            # знак равно иногда распознается как два минуса
            if prev_class in minus_equal and self.classes[i] in minus_equal:
                s = s[:-3]
                s += ' = '
            else:
                # если выше и левее предыдущего, то добавляем '^'
                if is_upper_right(prev_letter, self.letters[i]):
                    s += '^'
                if cls not in digits and cls not in let:
                    s += ' '
                    s += smbl
                    s += ' '
                else:
                    s += smbl
            prev_letter = self.letters[i]
            prev_class = self.classes[i]
        return s

    def run(self):
        self.preproc_image()
        self.classify_character()
        result = self.pars_expression()
        return result


if __name__ == '__main__':
    p = ImageProcessor('photo2.jpg', 'out.jpg')
    print(p.run())
