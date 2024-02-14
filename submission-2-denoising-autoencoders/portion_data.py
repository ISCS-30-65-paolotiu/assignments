# I have a folder name pneumonia which contains images
# I want to split the images into train and test, 80% train and 20% test


import os
import random
from PIL import Image


base_folder = './submission-2-denoising-autoencoders'

# Path to the folder containing the images
path = base_folder + '/pneumonia'

# List of all the images in the folder
images = os.listdir(path)

# Shuffle the images
random.shuffle(images)


# Resize images to 64x64
for image in images:
		im = Image.open(os.path.join(path, image))
		im = im.resize((64, 64))
		im.save(os.path.join(path, image))


# Split the images into train and test
train = images[:int(0.8 * len(images))]

test = images[int(0.8 * len(images)):]

# Move the train images to a new folder

train_path = base_folder + '/train'
os.makedirs(train_path, exist_ok=True)
for image in train:
		os.rename(os.path.join(path, image), os.path.join(train_path, image))

# Move the test images to a new folder
test_path = base_folder + '/test'
os.makedirs(test_path, exist_ok=True)
for image in test:
		os.rename(os.path.join(path, image), os.path.join(test_path, image))

# The images have been split into train and test
print('Images have been split into train and test')
		

