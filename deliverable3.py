# -*- coding: utf-8 -*-
"""Final project Blanche F.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HcEFTu1Y86wI-dY_BuQLqs52blkzgqse

###### FINAL PROJECT DELIVERABLE 2

We will follow the steps:


*   Analzyze the dataset
* Prepare the dataset
* Create the model
* compile the model
* fit the model
* evaluate the model

## Import statements
"""

#!pip install tensorflow-gpu==2.0.0-beta1

from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import os

import tensorflow as tf
from IPython.display import display, Image

import pathlib
import glob
import pickle
from imutils import paths
import cv2
#import tensorflow_datasets as tfds
from keras.models import Model, Sequential
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, Flatten, Dense, Dropout,merge,Reshape
from keras.layers.normalization import BatchNormalization
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard
import random
#from scipy.misc import imresize

"""## Load the data"""

#https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip
#       NOT WORKING
#data_dir = tf.keras.utils.get_file(origin='http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip', fname='photos',   extract=True )
#data_dir = pathlib.Path(data_dir)
#!wget -O a3_face_dataset.tar.gz https://www.dropbox.com/s/4nmsiafyvw0o5fx/a3_face_dataset.tar.gz?dl=0
#!tar xzf a3_face_dataset.tar.gz
#!ls

#print(data_dir)
#image_count = len(list(data_dir.glob('div2k/_train_HR/')))
#print(image_count)

!wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip
!wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_HR.zip

!mkdir div2k
!unzip -q DIV2K_train_HR.zip -d div2k
!unzip -q DIV2K_valid_HR.zip -d div2k

!ls

#hr_train_dir='div2k/DIV2K_train_HR/'
 imgPaths = list(paths.list_images(r"./div2k/DIV2K_train_HR/"))
 print(imgPaths)
 print(len(imgPaths))
 photosPaths = list(glob.glob('./div2k/DIV2K_train_HR/*.png'))
 print(len(photosPaths))

imgPaths2 = list(paths.list_images(r"./div2k/DIV2K_valid_HR/"))
 print(imgPaths2)
 print(len(imgPaths2))
 photosPaths2 = list(glob.glob('./div2k/DIV2K_valid_HR/*.png'))
 print(len(photosPaths2))

#display 2 images
sample_images = glob.glob('./div2k/DIV2K_train_HR/*.png')[:2]
for file_path in sample_images:
  display(Image(file_path))

def plot_rgb_img(img):
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.axis('off')
  plt.show()

#!wget -O cats_dog_dataset.tar.gz https://www.dropbox.com/s/1tbop84bk5mesmm/cats_dog_dataset.tar.gz?dl=0
#!tar xzf cats_dog_dataset.tar.gz
#!ls

#imgPaths = list(paths.list_images(r"./training_dataset/"))
#print(imgPaths)
#photosPaths2 = list(glob.glob('./training_dataset/cats/*.jpg'))
#print(len(photosPaths2))
#photos = np.stack([cv2.imread(str(x), cv2.IMREAD_GRAYSCALE) for x in photosPaths2])

#os.listdir()
#file = open("data.pkl", "wb")
#for i in range(len(photosPaths2)):
 # im = Image.open(photosPaths2[i])
  #pickle.dump(im, file)

#data = pickle.load(open('data.pkl', 'rb'))

#data_dir2 = tf.keras.utils.get_file(origin='https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz', fname='flower_photos', untar=True)
#data_dir2 = pathlib.Path(data_dir2)

#image_count = len(list(data_dir2.glob('*/*.jpg')))
#print(data_dir2)
#print(image_count)

"""## Put the images into a list or array"""

#img= np.array(data_dir)
# data_dir = pathlib.Path(data_dir)
#imgPaths = list(paths.list_images(data_dir))
#photosPaths2 = list(glob.glob('./photos/*.png'))
#random.shuffle(imgPaths)
#images=glob.glob('./photos/*.png')

#photosPaths = list(glob.glob('./photos/*.png'))
#photos = np.stack([cv2.imread(str(x), cv2.IMREAD_GRAYSCALE)  for x in photosPaths])
#photos = np.stack([cv2.imread(str(x), cv2.IMREAD_GRAYSCALE) for x in photosPaths2])
#display 3 images to see if it works...
#for image_path in photos[:3] :
  #  display.display(Image.open(str(image_path)))
#print(data_dir)

#data=[]
#for imgPath in photosPaths2:
	#Read the image into a numpy array using opencv
	#all the read images are of different shapes
	#image = cv2.imread(imgPath)
	#resize the image to be 1400x1400 pixels (ignoring aspect ratio)
	#image = cv2.resize(image, (1400, 1400))
	#flatten the images
	#image_flatten = image.flatten()
	#Append each image data 1D array to the data list
	#data.append(image_flatten)
#data=np.array(data)


#photos = np.stack([cv2.imread(str(x), cv2.IMREAD_GRAYSCALE) for x in photosPaths])
hr_train_dir='div2k/DIV2K_train_HR'
data = []
for imgPath in photosPaths: 
   #print(image)
   img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
	 #flatten the images
	 #image_flatten = image.flatten()
   img_resize = cv2.resize(img,(1400,1400))
   data.append(img)

#print(data[0])
print(len(data))
#print(train_data.shape)

hr_valid_dir='div2k/DIV2K_valid_HR'
data2 = []
for imgPath in photosPaths2: 
   #print(image)
   img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
	 #flatten the images
	 #image_flatten = image.flatten()
   img_resize = cv2.resize(img,(1400,1400))
   data2.append(img)

#print(data[0])
print(len(data2))

#plot_rgb_img(data[1])

"""## PREPROCESSING: SHUFFLE THE DATA"""

# Shuffle the data
print(len(data))
shuffled_images = []
while data:
    i = random.randrange(len(data))
    shuffled_images.append(data[i])
    del data[i]
#.reshape(1400,1400)
data=shuffled_images
train_data = np.ndarray(shape=(len(shuffled_images), 1400, 1400,3), dtype=np.float32)
#train_data = np.ndarray(shape=(len(shuffled_images),3, 1400, 1400), dtype=np.float32)
#train_data=np.array(shuffled_images[:])
print(train_data.dtype)
print(train_data.shape)


# same for validation data
shuffled_images2 = []
while data2:
    i = random.randrange(len(data2))
    shuffled_images2.append(data2[i])
    del data2[i]
#.reshape(1400,1400)
data2=shuffled_images2
#valid_data = np.ndarray(shape=(len(shuffled_images2),3, 1400, 1400), dtype=np.float32)
valid_data = np.ndarray(shape=(len(shuffled_images2), 1400, 1400,3), dtype=np.float32)
print(valid_data.dtype)
print(valid_data.shape)

"""## Reshape photos for training"""

#photos_reshape = np.expand_dims(photos, axis=3)
#print(photos_reshape)

#train_datagen = ImageDataGenerator(rescale=1./255)
#train_generator = train_datagen.flow_from_directory(
#    directory=r"a3_face_dataset/",
#    target_size=(1400,1400),
#    color_mode="rgb",
#    batch_size=32,
#    class_mode="binary",
#    shuffle=True,
#    seed=123
#)

"""## Define the architecture of the model"""

def create_model():
  x = Input(shape=(1400, 1400, 3)) 

  # Encoder
  e_conv1 = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
  pool1 = MaxPooling2D((2, 2), padding='same')(e_conv1)
  batchnorm_1 = BatchNormalization()(pool1)
  e_conv2 = Conv2D(32, (3, 3), activation='relu', padding='same')(batchnorm_1)
  pool2 = MaxPooling2D((2, 2), padding='same')(e_conv2)
  batchnorm_2 = BatchNormalization()(pool2)
  e_conv3 = Conv2D(16, (3, 3), activation='relu', padding='same')(batchnorm_2)
  h = MaxPooling2D((2, 2), padding='same')(e_conv3)


  # Decoder
  d_conv1 = Conv2D(64, (3, 3), activation='relu', padding='same')(h)
  up1 = UpSampling2D((2, 2))(d_conv1)
  d_conv2 = Conv2D(32, (3, 3), activation='relu', padding='same')(up1)
  up2 = UpSampling2D((2, 2))(d_conv2)
  d_conv3 = Conv2D(16, (3, 3), activation='relu')(up2)
  up3 = UpSampling2D((2, 2))(d_conv3)
  r = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(up3)

  model = Model(x, r)
  model.compile(optimizer='adam', loss='mse')
  return model

gaussian_auto_encoder = create_model()

"""## test"""

# create autoencoder model
input_img = Input(shape=(1400, 1400, 1))
def encoder(input_img):
    conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
    conv1 = BatchNormalization()(conv1)
    conv1 = Conv2D(32, (3,3), activation='relu', padding='same')(conv1)
    conv1 = BatchNormalization()(conv1)
    conv1 = Conv2D(32, (3,3), activation='relu', padding='same')(conv1)
    conv1 = BatchNormalization()(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool1)
    conv2 = BatchNormalization()(conv2)
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv2)
    conv2 = BatchNormalization()(conv2)
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv2)
    conv2 = BatchNormalization()(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(pool2)
    conv3 = BatchNormalization()(conv3)
    conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv3)
    conv3 = BatchNormalization()(conv3)
    conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv3)
    conv3 = BatchNormalization()(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(pool3)
    conv4 = BatchNormalization()(conv4)
    conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv4)
    conv4 = BatchNormalization()(conv4)
    conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv4)
    conv4 = BatchNormalization()(conv4)
    conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv4)
    conv5 = BatchNormalization()(conv5)
    conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv5)
    conv5 = BatchNormalization()(conv5)
    conv5 = Conv2D(512, (3, 3), activation='sigmoid', padding='same')(conv5)
    conv5 = BatchNormalization()(conv5)
    return conv5,conv4,conv3,conv2,conv1

def decoder(conv5,conv4,conv3,conv2,conv1):
    up6 = merge([conv5, conv4], mode='concat', concat_axis=3)
    conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')(up6)
    conv6 = BatchNormalization()(conv6)
    conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv6)
    conv6 = BatchNormalization()(conv6)
    conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv6)
    conv6 = BatchNormalization()(conv6)
    up7 = UpSampling2D((2,2))(conv6)
    up7 = merge([up7, conv3], mode='concat', concat_axis=3)
    conv7 = Conv2D(128, (3, 3), activation='relu', padding='same')(up7)
    conv7 = BatchNormalization()(conv7)
    conv7 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv7)
    conv7 = BatchNormalization()(conv7)
    conv7 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv7)
    conv7 = BatchNormalization()(conv7)
    up8 = UpSampling2D((2,2))(conv7)
    up8 = merge([up8, conv2], mode='concat', concat_axis=3)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(up8)
    conv8 = BatchNormalization()(conv8)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv8)
    conv8 = BatchNormalization()(conv8)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv8)
    conv8 = BatchNormalization()(conv8)
    up9 = UpSampling2D((2,2))(conv8)
    up9 = merge([up9, conv1], mode='concat', concat_axis=3)
    conv9 = Conv2D(32, (3, 3), activation='relu', padding='same')(up9)
    conv9 = BatchNormalization()(conv9)
    conv9 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv9)
    conv9 = BatchNormalization()(conv9)
    conv9 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv9)
    conv9 = BatchNormalization()(conv9)
    decoded_1 = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(conv9)
    return decoded

"""*   Dataset preparation
*   Shuffle the dataset
* Create a noisy dataset
* Use the loss function

## Create the model
"""

input_img = Input(shape=(1400, 1400, 1))
conv5,conv4,conv3,conv2,conv1 = encoder(input_img)
autoencoder = Model(input_img, decoder(conv5,conv4,conv3,conv2,conv1))
autoencoder.summary()
#autoencoder.compile(loss=   , optimizer = RMSprop())

"""## Compile the model"""

autoencoder.compile(loss='mean_squared_error', optimizer = RMSprop())
# opt = keras.optimizers.Adam(learning_rate=0.003, beta_1=0.9, beta_2=0.999, amsgrad=True)
# autoencoder.compile(optimizer=opt, loss='binary_crossentropy')

"""## Train the model"""

def add_gaussian_blur(data):
  dst = cv2.GaussianBlur(data, (3, 3), cv2.BORDER_DEFAULT)
  return dst

def add_blur(data):
  i = 0 
  end = len(data)
  output_data = []
  while i < end:
    output_data.append(add_gaussian_blur(data[i]))
    i+=1
  return np.array(output_data)

print(train_data.shape)

#x_train_noisy = add_blur(train_data)
#x_valid_noisy = add_blur(valid_data)

#x_train=train_data
#x_valid=valid_data
noise_factor = 0.5
x_train_noisy = train_data + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=train_data.shape) 
x_valid_noisy = valid_data + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=valid_data.shape) 

x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_valid_noisy = np.clip(x_valid_noisy, 0., 1.)

np_epoch=100
gaussian_auto_encoder.fit(train_data_noisy, train_data, 
                epochs=np_epoch,
                batch_size=128,
                shuffle=True,
                validation_data=(valid_data_noisy, valid_data),
                callbacks=[TensorBoard(log_dir='/tmp/tb', histogram_freq=0, write_graph=False)])

np_epoch=100
autoencoder.fit(x_train_noisy, x_train, 
                epochs=np_epoch,
                batch_size=128,
                shuffle=True,
                validation_data=(x_valid_noisy, x_valid),
                callbacks=[TensorBoard(log_dir='/tmp/tb', histogram_freq=0, write_graph=False)])

"""## Test the model and evaluate accuracy"""

#x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape) 
#x_test_noisy = np.clip(x_test_noisy, 0., 1.)

denoise_photos = autoencoder.predict(x_test_noisy)

plt.figure(figsize=(15,8))
x=10
for i in range(x):
    #display the original photo
    ax = plt.subplot(2, x, i+1)
    plt.imshow(x_test[i].reshape(1400,1400))
    plt.plasma()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # display reconstructed photo
    ax = plt.subplot(2, x, i+x+1)
    plt.imshow(denoise_photos[i].reshape(1400,1400))
    plt.plasma()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

N = np.arange(0,np_epoch )
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
#plt.plot(N, H.history["accuracy"], label="train_acc")
#plt.plot(N, H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy - 95 to 100")
plt.xlabel("Epoch number")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig("training_performance_100.png")
plt.show()

"""### SAVE THE MODEL"""

# autoencoder.save("---.model")

"""### deploy the model

# export the model
"""

'''
!apt-get install python3-venv
!python3 -m venv .tensorflowjs-env
!source .tensorflowjs-env/bin/activate
!pip3 install tensorflowjs
!deactivate


!source .tensorflowjs-env/bin/activate
!mkdir denoiser
!tensorflowjs_converter --input_format keras NAMEOFMODEL denoiser
!deactivate

#export the model on my computer
!zip -r denoiser.zip denoiser
from google.colab import files
files.download('denoiser.zip')

'''