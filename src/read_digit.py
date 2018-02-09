import os
import numpy
from PIL import Image, ImageOps
import _data_handler
import _model_builder

def read():
    """detect what digit is in ./data/number.jpg"""

    # load json and create model
    base_model = _model_builder.Network(0, model_type="load_model")

    #load image and process
    digit = Image.open("./data/number.jpg").convert("L")
    digit = ImageOps.expand(digit,border=60,fill='black')
    digit = digit.resize((28, 28))

    #flatten the matrix (for input into MLP network todo:CNN)
    digit_flat = numpy.zeros((1, 784))
    counter = 0
    for j in range(0, 28):
        for i in range(0, 28):
            digit_flat[0][counter] = (digit.getpixel((i, j)))/255.0
            counter = counter+1

    #predict
    os.system('clear')
    base_model.predict(digit_flat)

read()
