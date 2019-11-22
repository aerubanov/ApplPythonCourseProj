import pickle
import os

with open('/home/cloud/ApplPythonCourseProj/web/server/classification/model.obj', 'rb') as f:
    model = pickle.load(f)

symbol_dict = {}
with open('/home/cloud/ApplPythonCourseProj/web/server/classification/classes.txt', 'r') as f:
    i = 0
    for line in f:
        symbol_dict[i] = line.strip()
        i += 1
