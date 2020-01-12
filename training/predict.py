from keras.models import load_model
from PIL import Image
import numpy as np


def path_to_image(path):
    image = Image.open(path)
    image = image.resize((64, 64), Image.ANTIALIAS)
    image = np.array(image.convert('RGB'))
    return image


def cell_name(label):
    if label == 0:
        return "Parasitized"
    if label == 1:
        return "Uninfected"


def predict_cell(path):
    img = path_to_image(path)
    img = img / 255.0
    # keras only takes list as input
    a = []
    a.append(img)
    a = np.array(a)
    model = load_model("models/cells.h5")
    prediction = model.predict(a, verbose=1)
    print(prediction)
    # get highest propability either closer to 0 or 1
    label_index = np.argmax(prediction)
    print(label_index)
    accuracy = np.max(prediction)
    Cell = cell_name(label_index)
    return Cell
