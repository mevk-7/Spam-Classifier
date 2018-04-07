

import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def predict_spam(string):
    vect = pickle.load(open('vect.pickle','rb'))
    model = pickle.load(open('spam.pickle','rb'))
    soups = BeautifulSoup(string,'html5lib')
    string = soups.text
    templist = string.split()
    string= ' '.join([word for word in templist if (word.isalnum() or word == '.')])
    return model.predict(vect.transform([string]))
    
