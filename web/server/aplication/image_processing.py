from preprocessing import preprocessing


class ImageProcessor:

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.letters = None

    def preproc_image(self):
        self.letters = preprocessing.letters_extract(self.path, self.out_path)

    def classify_character(self):
        pass

    def pars_expression(self):
        return "x^2+2*x+5"

    def run(self):
        self.preproc_image()
        self.classify_character()
        result = self.pars_expression()
        return result
