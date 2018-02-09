import numpy as np
from PIL import Image

DIGIT = Image.open("./number.jpg").convert("L")
DIGIT = DIGIT.resize((28,28))

DIGIT_FLAT = np.zeros((1,784))

for i in range(0,28):
    for j in range(0,28):
        DIGIT_FLAT[0][i*j + j]= 255-DIGIT.getpixel((i,j))
