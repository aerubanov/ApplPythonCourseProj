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
        # plt.figure(figsize=(10,10))
        # for i in range(7):
        #    plt.subplot(5,5,i+1)
        #    plt.xticks([])
        #    plt.yticks([])
        #    plt.grid(False)
        #    plt.imshow(imgs[i])
        n = len(imgs)
        imgs = np.concatenate(imgs)
        imgs = imgs.reshape(n, 28, 28, 1)
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


if __name__ == '__main__':
    p = ImageProcessor('photo.jpg', 'out.jpg')
    print(p.run())
