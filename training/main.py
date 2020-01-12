from __future__ import absolute_import, division, print_function
from data import test_data, test_labels, train_data, train_labels
import json

import tensorflow as tf
import keras

# be sure tensorflow loaded
print(tf.__version__)
# data info
print("data train: {}".format(len(train_data)))
print("data test: {}".format(len(test_data)))

# TODO
# display some prediction
# create app to predict a picture

model = keras.Sequential()
model.add(keras.layers.Conv2D(filters=16, kernel_size=2, padding="same",
                              activation='relu', input_shape=(64, 64, 3)))
model.add(keras.layers.MaxPooling2D(pool_size=2))
model.add(keras.layers.Conv2D(filters=32, kernel_size=2, padding="same", activation="relu"))
model.add(keras.layers.MaxPooling2D(pool_size=2))
model.add(keras.layers.Conv2D(filters=64, kernel_size=2, padding="same", activation="relu"))
model.add(keras.layers.MaxPooling2D(pool_size=2))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(2, activation="softmax"))  # 2 represent output layer neurons
model.summary()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_data, train_labels, batch_size=50, epochs=20, verbose=1)

accuracy = model.evaluate(test_data, test_labels, verbose=1)
print("Test accuracy: {}".format(accuracy[1]))
model.save("models/cells.h5")
