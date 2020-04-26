 # we have used keras datasets (be remebered that if datasets is not download it will automatically downloaded [Make sure your connected with internet])
from keras.datasets import boston_housing
# by standard rule of machine learning we have 90% train data and 10% test data
(x_train,y_train),(x_test,y_test) = boston_housing.load_data() 
print("the type of x_train data is ",type(x_train))
print("the type of y_train data is ",type(y_train))
print("###########################################")
print("First Way ")

print("The shape of x_train data ",x_train.shape)
print("The shape of y_train data ",y_train.shape)
print("The shape of x_test data ",x_test.shape)
print("The shape of y_test data ",y_test.shape)
print("###########################################")
print("Second Way ")

print("The row of x_train {0} and column of x_train {1} ".format(x_train.shape[0],x_train.shape[1]))
print("The row of y_train {0} and column of y_train 1 ".format(y_train.shape[0]))
print("The row of x_test {0} and column of x_test {1} ".format(x_test.shape[0],x_test.shape[1]))
print("The row of y_test {0} and column of y_test 1 ".format(y_test.shape[0]))

#importing numpy,keras,keras-sequential,dense layer and activation function
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense,Activation

# Set the validation Data 
x_val = x_train[300:,]
y_val = y_train[300:,]

# Define Model Architecture
model = Sequential()
model.add(Dense(13,input_dim = 13,kernel_initializer='normal',activation='relu'))
model.add(Dense(6,kernel_initializer='normal',activation='relu'))
model.add(Dense(1,kernel_initializer='normal',activation='relu'))


# Compile Model 
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['mean_absolute_percentage_error'])

# Train  the Model 
model.fit(x_train,y_train,batch_size=32,epochs=3,validation_data=(x_val,y_val))
