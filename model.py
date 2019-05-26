import csv
import cv2
import numpy as np

lines=[]
with open("./data/driving_log.csv") as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for line in reader:        
        lines.append(line)
        
images=[]
measurements=[]
for line in lines:
    center_path=line[0]
    filename=center_path.split("/")[-1]
    center_path="./data/IMG/" + filename
    image=cv2.imread(center_path)
    images.append(image)
    measurement=float(line[3])
    measurements.append(measurement)
   
X_train=np.array(images)
y_train=np.array(measurements)

from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Lambda
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D

model=Sequential()
model.add(Lambda(lambda x:(x/255.0)-0.5,input_shape=(160,320,3)))
model.add(Conv2D(6,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(Conv2D(6,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(120))
model.add(Dense(84))
model.add(Dense(1))

model.compile(loss='mse',optimizer='adam')
model.fit(X_train,y_train,validation_split=0.2,shuffle=True,epochs=5)

model.save('model.h5')