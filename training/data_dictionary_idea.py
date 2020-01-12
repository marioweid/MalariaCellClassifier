import os
from PIL import Image
import numpy as np

# malaria cell dataset numbers
# images per label : 13779
# different shapes: 13737
# max shape-x value: 385
# max shape-y value: 394

# directory to dataset
para_path = "D:/DataSets/cell_images/Parasitized_test"
uninfected_path = "D:/DataSets/cell_images/Uninfected_test"

# labels
para_label = "parasitized"
uninfected_label = "uninfected"


# returns train data and test data in shape [{"image":np.array,"label":string}]
def load_data(data_dir, label):
    data_dir = os.path.abspath(data_dir)
    all_data = []
    train = []
    test = []

    # load all images and resize them to 400,400
    for image in os.listdir(data_dir):
        if image.endswith(".png"):
            pair = {}
            img = Image.open(os.path.join(data_dir, image))
            img = img.resize((400, 400), Image.ANTIALIAS)
            pair["image"] = np.array(img.convert('RGB'))
            pair["label"] = label
            all_data.append(pair)

    # split data to 70% train and 30% test
    for i in range(len(all_data)):
        if i <= 0.7 * len(all_data):
            train.append(all_data[i])
        else:
            test.append(all_data[i])

    return train, test


# Load data from dir
parasitized_train, parasitized_test = load_data(para_path, para_label)
uninfected_train, uninfected_test = load_data(uninfected_path, uninfected_label)

'''
visualize parasitized data
for i in range(10):
    print(parasitized_train[i])
    print(parasitized_test[i])
print("para train: {}".format(len(parasitized_train)))
print("para test: {}".format(len(parasitized_test)))

visualize uninfected data
for i in range(10):
    print(uninfected_train[i])
    print(uninfected_test[i])
print("uninfected train: {}".format(len(uninfected_train)))
print("uninfected test: {}".format(len(uninfected_test)))
'''

# some extra data preprocessing
train_data = parasitized_train + uninfected_train
test_data = parasitized_test + uninfected_test

for image in range(len(train_data)):
    train_data[image]["image"] = train_data[image]["image"] / 255.0

for image in range(len(test_data)):
    test_data[image]["image"] = test_data[image]["image"] / 255.0

np.random.shuffle(train_data)
np.random.shuffle(test_data)
