import cv2
import numpy as np

# Read data and set data as uint8
img = np.loadtxt('input_question_4', dtype='uint8')

# Use cv2.connectedComponents to carry out '8-connectivity' operation
res, labels = cv2.connectedComponents(img, connectivity=8)

with open('output_question_4.txt', 'w') as f:
    for label in labels:
        for p in label:
            f.write(str(p) + ' ')
        f.write('\n')

