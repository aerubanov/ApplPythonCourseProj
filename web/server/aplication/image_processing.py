from preprocessing import preprocessing
from classification.classifier import model, symbol_dict
import numpy as np


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
        smbls = [symbol_dict[i] for i in self.classes]
        return ' '.join(smbls)

    def run(self):
        self.preproc_image()
        self.classify_character()
        result = self.pars_expression()
        return result
