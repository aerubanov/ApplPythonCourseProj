import pickle
import os

with open(os.path.join(os.pardir, 'classification/model.obj'), 'rb') as f:
    model = pickle.load(f)

symbol_dict = {}
with open(os.path.join(os.pardir, 'classification/classes.txt'), 'r') as f:
    i = 0
    for line in f:
        symbol_dict[i] = line.strip()
        i += 1
