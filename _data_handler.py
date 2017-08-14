import os
import numpy
from keras.datasets import mnist
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')

class Dataset:
    """dataset class, right now just used to initialize the data"""

    def __init__(self):
        """initialize data"""
        # load data
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        self.num_pixels = self.x_train.shape[1] * self.x_train.shape[2]

        # one hot encode outputs
        self.y_train = np_utils.to_categorical(self.y_train)
        self.y_test = np_utils.to_categorical(self.y_test)
        self.num_classes = self.y_test.shape[1]


    def preproc_MLP(self):
        """preprocess the data for a MLP network"""
        # flatten 28*28 images to a 784 vector for each image
        self.x_train = self.x_train.reshape(
            self.x_train.shape[0], self.num_pixels).astype('float32')
        self.x_test = self.x_test.reshape(
            self.x_test.shape[0], self.num_pixels).astype('float32')

        # normalize
        self.x_train = self.x_train / 255
        self.x_test = self.x_test / 255

    def preproc_CNN(self):
        """preprocess the data for a CNN"""
        # reshape to be [samples][pixels][width][height]
        self.x_train = self.x_train.reshape(
            self.x_train.shape[0], 1, 28, 28).astype('float32')
        self.x_test = self.x_test.reshape(
            self.x_test.shape[0], 1, 28, 28).astype('float32')

        # normalize
        self.x_train = self.x_train / 255
        self.x_test = self.x_test / 255
