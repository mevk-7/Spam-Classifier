#load trained model and Countvectorize which is already saved in SPAM_CLF folder

import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os
def predict_spam(string):
	#find absolute path in pre trained models
	my_dir =os.path.dirname(os.path.abspath(__file__))
	vect_dir =os.path.join(my_dir,'vect.pickle')
	model_dir= os.path.join(my_dir,'spam.pickle')
	#load trained models
	vect = pickle.load(open(vect_dir,'rb'))
	model = pickle.load(open(model_dir,'rb'))
	#extract text from html
	soups = BeautifulSoup(string,'html5lib')
	string = soups.text
	templist = string.split()
	#remove words which are not alpha numeric
	string= ' '.join([word for word in templist if (word.isalnum() or word == '.')])
	#predict  and return it
	return model.predict(vect.transform([string]))
    
