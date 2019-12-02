from flask import Flask

PHOTO_DIR = 'images/'
OUTPUT_DIR = 'out_images/'

app = Flask(__name__)
app.config['DATABASE'] = 'sqlite:///images.db'
app.config['TEST_DATABASE'] = 'sqlite:///test_images.db'
app.config['UPLOAD_FOLDER'] = PHOTO_DIR
app.config['OUT_FOLDER'] = OUTPUT_DIR

