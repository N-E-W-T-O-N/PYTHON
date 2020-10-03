#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:25:35 2020

@author: newton
"""
import tensorflow as tf
from tensorflow import keras
import  numpy as np
print(tf.__version__)
from tensorflow.keras import datasets
#download idmb review
imdb = keras.datasets.imdb 
(train_data,train_labels),(test_data,test_lables)=imdb.load_data(num_words=10000)

for x in  train_data:
    print(x)
print(train_labels)    