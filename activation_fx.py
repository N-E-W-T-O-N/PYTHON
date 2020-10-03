#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:10:52 2019

@author: NEWTON

"""


import  numpy as np

def sigmoid(X,W,b):
    return 1.0/(1.0+np.exp(-(np.dot(W.T,X))+b))

def tanh(X,W,b):
    z=np.exp(-(np.dot(W.T,X)+b))
    return (np.exp(z)-np.exp(-z))/(np.exp(z)+np.exp(-z))

def relu(X,W,b):
    x=np.dot(W.T,X)+b
    return np.maximum(x,0)

def softmax(X,W,b):
    z_exp =np.exp(np.dot(W,X)+b)
    print(z_exp)
    z_exp_sum= np.sum(z_exp)
    print(z_exp_sum)
    return z_exp/z_exp_sum

W=np.array([0.1,0.2,0.3])
X=np.array([0.2,0.1,0.3])
b=1.5  

print(sigmoid(W,X,b))
print(tanh(W,X,b)) 
print(relu(W,X,b))
print(softmax(W,X,b)) 