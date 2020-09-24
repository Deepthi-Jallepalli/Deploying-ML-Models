from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
from sklearn.externals import joblib


classifier = Sequential()
classifier.add(Convolution2D(32,3,3,input_shape = (256,256,3),activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Flatten())
classifier.add(Dense(128, activation = 'relu'))
classifier.add(Dense(1, activation = 'sigmoid'))
classifier.compile(optimizer='adam',loss = 'binary_crossentropy',metrics=['accuracy'])
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('training_set',  batch_size=32, class_mode='binary')
test_set = test_datagen.flow_from_directory('test_set', batch_size=32, class_mode='binary')
model = classifier.fit_generator(training_set, epochs=10, validation_data=test_set, nb_val_samples=200)
test_image = image.load_img('person_0979.jpg', target_size=(256, 256))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
prediction = classifier.predict(test_image)
training_set.class_indices
joblib.dump(model, 'image_classification-model.model')
    print('Model Training Finished: {}'.format(training_set)