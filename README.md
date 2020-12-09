## Machine Learning:
1 <a href = '#test'> Bostan </a>




# : #Bostan House Prediction:
Let’s select a popular Keras dataset for developing
a model[Bostan house price dataset]. 


**step-1**
Download the bostan house datasets athough it comes with keras by deafult might be latest version.
not If not aviliable, you can downlaod.
The data is present in an Amazon S2 bucket, which we can
download by using simple Keras commands provided exclusively for the
datasets.


**step-2**
Nature of input[size of row and column] and as well as label
`for more information` <a href = "http://lib.stat.cmu.edu/datasets/boston."> visit here</a>

**step-3**
# Model Architecture and Feature[13 column] and compile step too.
There are two types of model:
<ol> <li>Sequential</li><li>API</li> </ol>
but here we selected only sequential but it's not neccessary to use it you can go with
api.

**step-4**
# Evaluate the model
We have created a simple two-hidden-layer model for the regression
use case. We have chosen MAPE as the metric. Generally, this is not the
best metric to choose for studying model performance, but its advantage
is simplicity in terms of comprehending the results. It gives a simple
percentage value for the error, say 10% error. So, if you know the average
range of your prediction, you can easily estimate what the predictions are
going to look like.

`See the output`

**Notice**
In case if loss value is high it mean your model is trained much.
by increased the size of each epoch the over come the overfitting.

**Summary**
**Our model is trained for bostan like House prediction but it not suitable if you prediction
another house of distanct feature of bostan**

# #test
