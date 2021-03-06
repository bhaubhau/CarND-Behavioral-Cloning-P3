import csv
import cv2
import numpy as np

data_folder="./SampleData/"

lines=[]
with open(data_folder + "driving_log.csv") as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for line in reader:        
        lines.append(line)
        
images=[]
measurements=[]
for line in lines:
    center_path=line[0]
    filename=center_path.split("/")[-1]
    center_path=data_folder + "IMG/" + filename
    image=cv2.imread(center_path)
    images.append(image)
    
    left_path=line[1]
    filename=left_path.split("/")[-1]
    left_path=data_folder + "IMG/" + filename
    image=cv2.imread(left_path)
    images.append(image)
    
    right_path=line[2]
    filename=right_path.split("/")[-1]
    right_path=data_folder + "IMG/" + filename
    image=cv2.imread(right_path)
    images.append(image)
    
    measurement=float(line[3])
    measurements.append(measurement)
    measurements.append(measurement+0.2)
    measurements.append(measurement-0.2)
   
augmented_images, augmented_measurements=[], []
for image,measurement in zip(images, measurements):
    augmented_images.append(image)
    augmented_measurements.append(measurement)
    augmented_images.append(cv2.flip(image,1))
    augmented_measurements.append(measurement*-1.0)

X_train=np.array(augmented_images)
y_train=np.array(augmented_measurements)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

model=Sequential()
model.add(Lambda(lambda x:(x/255.0)-0.5,input_shape=(160,320,3)))
model.add(Cropping2D(cropping=((70,25),(0,0))))
model.add(Conv2D(24,(5,5),strides=(2,2),activation="relu"))
model.add(Dropout(0.2))
model.add(Conv2D(36,(5,5),strides=(2,2),activation="relu"))
model.add(Conv2D(48,(5,5),strides=(2,2),activation="relu"))
model.add(Conv2D(64,(3,3),activation="relu"))
model.add(Dropout(0.3))
model.add(Conv2D(64,(3,3),activation="relu"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse',optimizer='adam')
model.fit(X_train,y_train,validation_split=0.2,shuffle=True,epochs=5)

model.save('model.h5')