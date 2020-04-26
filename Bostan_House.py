 # we have used keras datasets (be remebered that if datasets is not download it will automatically downloaded [Make sure your connected with internet])
from keras.datasets import boston_housing
# by standard rule of machine learning we have 90% train data and 10% test data
(x_train,y_train),(x_test,y_test) = boston_housing.load_data() 
print("the type of x_train data is ",type(x_train))
print("the type of y_train data is ",type(y_train))
