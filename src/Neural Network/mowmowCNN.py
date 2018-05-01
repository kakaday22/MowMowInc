from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.data_utils import shuffle, to_categorical
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
from tflearn.data_utils import image_preloader
# Data Loading and Categorization
databook = 'data/mowmow_text.txt'
X, Y = image_preloader(databook, image_shape=(128, 128), mode='file',
                       categorical_labels=False, normalize=False)
Y = to_categorical(Y, 4)
print("-- Textbook Import Complete.")

testbook = 'data/mowmow_test.txt'
X_test, Y_test = image_preloader(testbook, image_shape=(128, 128), mode='file',
                                 categorical_labels=False, normalize=False)
Y_test = to_categorical(Y_test, 4)
print("-- Testbook Import Complete.")

# Real-time Data Preprocessing
img_prep = ImagePreprocessing()
img_prep.add_featurewise_zero_center()
img_prep.add_featurewise_stdnorm()
print("-- Data Preprocessing Complete.")

# Real-time Data Augmentation
img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle=25.)
print("-- Data Augmentation Complete.")

# Convolutional Network
network = input_data(shape=[None, 128, 128, 3], data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 5, activation='relu', bias=True, weights_init='uniform_scaling')
network = max_pool_2d(network, 2)
network = conv_2d(network, 64, 5, activation='relu', bias=True, weights_init='uniform_scaling')
network = conv_2d(network, 64, 5, activation='relu', bias=True, weights_init='uniform_scaling')
network = max_pool_2d(network, 2)
network = fully_connected(network, 256, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 128, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 64, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 32, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 3, activation='softmax')
network = regression(network, optimizer='adam', loss='categorical_crossentropy',
                     learning_rate=0.000005)

# Train using classifier
model = tflearn.DNN(network, tensorboard_verbose=0, tensorboard_dir='logs/',
                    best_checkpoint_path='checkpoints/best/', best_val_accuracy=0.88)
model.fit(X, Y, n_epoch=250, shuffle=True, validation_set=(X_test, Y_test),
          show_metric=True, batch_size=16, run_id='mowmow_cnn')