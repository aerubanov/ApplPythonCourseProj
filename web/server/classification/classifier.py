import pickle
import pickle
import tensorflow as tf
from tensorflow import keras
import numpy as np

MODEL1_PATH = '/home/cloud/ApplPythonCourseProj/web/server/classification/model34.obj'
MODEL2_PATH = '/home/cloud/ApplPythonCourseProj/web/server/classification/model_34_filt5.obj'
MODEL3_PATH = '/home/cloud/ApplPythonCourseProj/web/server/classification/model_34_filt6.obj'
CLASSES_PATH = '/home/cloud/ApplPythonCourseProj/web/server/classification/classes.txt'
# MODEL_PATH = '/home/anatoly/HDD/Corses/ApplPythonCourseProj/web/server/classification/model.obj'
# CLASSES_PATH = '/home/anatoly/HDD/Corses/ApplPythonCourseProj/web/server/classification/classes.txt'

#with open(MODEL_PATH, 'rb') as f:
#    model = pickle.load(f)

class Model_Assembly():

    def __init__(self):
        with open(MODEL1_PATH, 'rb') as f:
            self.model1 = pickle.load(f)
        with open(MODEL2_PATH, 'rb') as f:
            self.model2 = pickle.load(f)
        with open(MODEL3_PATH, 'rb') as f:
            self.model3 = pickle.load(f)

    def fit(self, X_train, y_train):
        self.model1.fit(X_train, y_train)
        self.model2.fit(X_train, y_train)
        self.model3.fit(X_train, y_train)

    def predict(self, X_test):
        y_1 = self.model1.predict(X_test)
        y_2 = self.model2.predict(X_test)
        y_3 = self.model3.predict(X_test)
        y_predicted = []
        for row in range(X_test.shape[0]):
            class1 = np.argmax(y_1[row])
            class2 = np.argmax(y_2[row])
            class3 = np.argmax(y_3[row])
            if class1 == class2 or class2 == class3:
                y_predicted.append(class2)
            else:
                y_predicted.append(class1)
        return np.array(y_predicted)

model = Model_Assembly()

symbol_dict = {}
with open(CLASSES_PATH, 'r') as f:
    i = 0
    for line in f:
        symbol_dict[i] = line.strip()
        i += 1
