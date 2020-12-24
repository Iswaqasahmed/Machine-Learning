### Linear Regression


If one dependent variable (y) depend on independent variable (x) is know as Regression. \
Type of Linear Regression.  
There are two types of linear regression.           
1. Linear Regression with one Variable. [x].                   
2. Lineaar Regression with more than one Variable. [x1,x2,x3 ... xn]. 

### Equation of Linear Reression With one Variable.
*Y = mx + c.* where Y = output/predict value, X is input. 

### Equation with Multiple Variable.
*Y = m[X1+X2+....Xn] + c.* where Y = output/predict value, Xs are inputs.


### Loss in Regression.
Training a model simply means learning (determining) good values for all the weights and the bias from labeled examples. In supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called empirical risk minimization.

Loss is the penalty for a bad prediction. That is, loss is a number indicating how bad the model's prediction was on a single example. If the model's prediction is perfect, the loss is zero; otherwise, the loss is greater. The goal of training a model is to find a set of weights and biases that have low loss, on average, across all examples. 
## Squared loss: a popular loss function
The linear regression models we'll examine here use a loss function called squared loss (also known as L2 loss). The squared loss for a single example is as follows:


  = the square of the difference between the label and the prediction
  = (observation - prediction(x))2
  = (y - y')2
  
  Mean square error (MSE) is the average squared loss per example over the whole dataset. To calculate MSE, sum up all the squared losses for individual examples and then divide by the number of examples:

