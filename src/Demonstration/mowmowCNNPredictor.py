from __future__ import division, print_function, absolute_import

import tensorflow as tf
import tflearn
from tflearn.data_utils import shuffle, to_categorical
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
from tflearn.data_utils import image_preloader
import cv2 as cv
import numpy as np

class mowmowCNNPredictor:
	def __init__(self,checkpoint_loc):

		# Real-time Data Preprocessing
		img_prep = ImagePreprocessing()
		img_prep.add_featurewise_zero_center(mean=110.53345696347691)
		img_prep.add_featurewise_stdnorm(std=30.956539195568315)
		print("-- Data Preprocessing Complete.")

		# Real-time Data Augmentation
		img_aug = ImageAugmentation()
		img_aug.add_random_flip_leftright()
		img_aug.add_random_rotation(max_angle=25.)
		print("-- Data Augmentation Complete.")

		# Convolutional Neural Network
		network = input_data(shape=[None, 128, 128, 3])
		network = conv_2d(network, 32, 5, activation='relu', bias=True,
						  weights_init='uniform_scaling')
		network = max_pool_2d(network, 2)
		network = conv_2d(network, 64, 5, activation='relu', bias=True,
						  weights_init='uniform_scaling')
		network = conv_2d(network, 64, 5, activation='relu', bias=True,
						  weights_init='uniform_scaling')
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

		# Set up DNN model & load weights
		self.model = tflearn.DNN(network, tensorboard_verbose=0, tensorboard_dir='logs/')
		self.model.load(checkpoint_loc)

	def predict_type(self,bookdir):
		# Import dataset
		X, Y = image_preloader(bookdir, image_shape=(128, 128), mode='file',
			                   categorical_labels=False, normalize=False)
		Y = to_categorical(Y, 3)
		print("-- Runbook Import Complete.")

		# Predict label
		prediction = self.model.predict(X)
		
		return prediction
