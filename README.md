# **Behavioral Cloning** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* README.md summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python3 drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network with multiple layers like cropping, convolution, Dropouts and fully connected Layers (lines 56-70)
The model includes RELU layers to introduce nonlinearity, and the data is normalized in the model using a Keras lambda layer. 

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting. 

The model was trained and validated on the sample data provided in the project with a validation ratio of 20%. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 72). Mean square error was used to evaluate the loss, since this is linear regression problem 

#### 4. Appropriate training data

[Sample driving data](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip) was chosen due to network bandwidth limitations to keep the vehicle driving on the road. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

Earlier I tried the LeNet architecture used in previous project to fit the data, but I observed the vehicle touching the lane lines a few times. Then I tried using the advanced model described in the lesson.

I used the cropping images to remove the unwanted areas in the images and then passing them through series of convolution, dropout and fully connected layers

The final step was to run the simulator to see how well the car was driving around track one. 

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 56-70) consisted of a series of convolution, dropout and fully connected layers, with the output and filter sizes as found in keras documentation

#### 3. Creation of the Training Set & Training Process

I used [Sample driving data](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip) to train the model due to network bandwidth limitations

I used the data augmentation to flip the images to remove the left sided driving bais and also added the left and right camera images to get more data points, like to get vehicle back on the track in case it moves out of the lane so as to recover back

Shuffling was applied in the model fitting and partitioned the dataset into 80:20 ratio for trining and validation

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was 5 as I saw the validation loss becoming stable near 4 to 5th epoch. I used an adam optimizer so that manually training the learning rate wasn't necessary.
