import os
import numpy
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D

# some code based on: https://machinelearningmastery.com/handwritten-digit-recognition-using-convolutional-neural-networks-python-keras/

class Network:
    """class for the model input must be of type Dataset"""
    def __init__(self, data, model_type):
        """initialize the model"""
        
        # fix random seed for reproducibility
        seed = 7
        numpy.random.seed(seed)
        
        self.scores = 0
        self.model = Sequential()

        if model_type == "MLP":
            # create model 
            self.model.add(Dense(data.num_pixels, input_dim=data.num_pixels,
                                 kernel_initializer='normal', activation='relu'))
            self.model.add(
                Dense(data.num_classes, kernel_initializer='normal', activation='softmax'))
            self.model.compile(loss='categorical_crossentropy',
                               optimizer='adam', metrics=['accuracy'])
        elif model_type == "smallCNN":
            # create model
            self.model.add(Conv2D(32, (5, 5), input_shape=(1, 28, 28), activation='relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))
            self.model.add(Dropout(0.2))
            self.model.add(Flatten())
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dense(data.num_classes, activation='softmax'))
            # compile model
            self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        elif model_type == "largeCNN":
            # create model
            self.model.add(Conv2D(32, (5, 5), input_shape=(1, 28, 28), activation='relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))
            self.model.add(Conv2D(15, (3, 3), activation='relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))
            self.model.add(Dropout(0.2))
            self.model.add(Flatten())
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dense(50, activation='relu'))
            self.model.add(Dense(data.num_classes, activation='softmax'))
	    # compile model
            self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        elif model_type == "load_model":
            # load json and create model
            json_file = open('./model/model.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            self.model = model_from_json(loaded_model_json)
            # load weights into new model
            self.model.load_weights("./weights/model.h5")
        else:
            print 'unaccepted model type'

    def fit(self, data, verbose_level):
        """find the model weights using training data"""
        self.model.fit(data.x_train, data.y_train, validation_data=(
            data.x_test, data.y_test), epochs=15, batch_size=200, verbose=verbose_level)

    def predict(self, data):
        """use the model to make a prediction"""
        prediction = self.model.predict(x=data, verbose=0)
        predicted_value = numpy.argmax(prediction[0])
        confidence = prediction[0, numpy.argmax(prediction[0])]*100.0
        print "The value is %i, with %.2f%% confidence" % (predicted_value, confidence)

    def final_eval(self, data, verbose_level):
        """evaluate the accuracy and error"""
        # Final evaluation of the model
        self.scores = self.model.evaluate(data.x_test, data.y_test, verbose=verbose_level)
        print "Baseline Error: %.2f%%" % (100 - self.scores[1] * 100)

    def save(self):
        """save the model"""
        # serialize model to JSON
        model_json = self.model.to_json()
        with open("./model/model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        self.model.save_weights("./weights/model.h5")
        print "Saved model to disk"
