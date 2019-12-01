#!/usr/bin/env python
# coding: utf-8


import pickle
import tensorflow as tf
from tensorflow import keras
import numpy as np


class Model_Assembly():

    def __init__(self):
        with open('model34.obj', 'rb') as f:
            self.model1 = pickle.load(f)
        with open('model_34_filt5.obj', 'rb') as f:
            self.model2 = pickle.load(f)
        with open('model_34_filt6.obj', 'rb') as f:
            self.model3 = pickle.load(f)

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
