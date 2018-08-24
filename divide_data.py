import os
import numpy as np
import shutil

directory = 'flower_photos'
for folder in os.listdir(directory):
    for img in os.listdir(directory + '/' + folder):
        if np.random.rand(1) < 0.2:
            if not os.path.isdir(directory + '/test/' + folder):
                os.makedirs(directory + '/test/' + folder)
            shutil.move(directory + '/' + folder + '/' + img, directory + '/test/' + folder + '/' + img)
        else:
            if not os.path.isdir(directory + '/train/' + folder):
                os.makedirs(directory + '/train/' + folder)
            shutil.move(directory + '/' + folder + '/' + img, directory + '/train/' + folder + '/' + img)
