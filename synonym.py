#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:50:43 2019

@author: newton
"""

from nltk.corpus import wordnet as wn
pos={'n':'noun' , 'v':'verb' , 's':'adj(s)' , 'a':'adj' ,'r':'adv'}

for synset in wn.synsets("bad"):
    print("{}:{}".format(pos[synset.pos()],",".join([l.name() for l in synset.lemmas()])))