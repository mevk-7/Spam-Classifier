

import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import pickle


#read given data sets 
df = pd.read_csv('Data_Set.csv')
df.head()


#replace all nan value with empty string
df['Data'].replace('', np.nan, inplace=True)
df['Label'].replace('', np.nan, inplace=True)


'''uncomment to see no of null row
a=np.where(pd.isnull(df))
for i,j in zip(*a):
    print(i,j)
'''    



#drop all row which contain empty strings 
df.drop(df.index[752], inplace=True)
df.drop(df.index[340], inplace=True)
df.drop(df.index[216], inplace=True)


#convert row to numpy arrays
X = df['Data'].values
Y = df['Label'].values



#extract all text from each html text and stored in different list
Data_set_X =[]
Data_set_Y =[]
for i in range(len(X)):
    try:
        soup= BeautifulSoup(X[i],'html5lib')
        Data_set_X.append(soup.text)
        Data_set_Y.append(Y[i])
    except Exception as e:
        print(i,e)


#remove all character from text which are not alpha numeric
escapes = ''.join([chr(char) for char in range(1, 32)])
for i in range(len(Data_set_X)):
    Data_set_X[i]=  ' '.join([word for word in Data_set_X[i].split() if (word.isalnum() or word == '.')])


#split data into training and testing sets
from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(Data_set_X,Data_set_Y, test_size=0.2, random_state=10)



#counter vectorize words
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(stop_words="english")
vect.fit(train_X)


X_train_df = vect.transform(train_X)
X_test_df = vect.transform(test_X)
type(X_test_df)



#import and train naive bayes model
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
model = MultinomialNB(alpha=1.8)
model.fit(X_train_df,train_y)
pred = model.predict(X_test_df)
accuracy_score(test_y, pred)


print(classification_report(test_y, pred , target_names = ["Ham", "Spam"]))



#store model in file
with open('spam.pickle','wb') as f:
    pickle.dump(model,f)
with open('vect.pickle','wb') as v:
    pickle.dump(vect,v)

'''
to open spam classifire
pickle_in = open('spam.pickle','rb')
model = pickle.load(pickle_in)
'''


'''
Uncomment for testing purpose
def predict_spam(string):
    vect = pickle.load(open('vect.pickle','rb'))
    model = pickle.load(open('spam.pickle','rb'))
    soups = BeautifulSoup(string,'html5lib')
    string = soups.text
    templist = string.split()
    string= ' '.join([word for word in templist if (word.isalnum() or word == '.')])
    return model.predict(vect.transform([string]))
    


string ='Please look at Scilab help files. Scilab help is available on your Scilab installation and online. \r\n\r\nApart from that, you could also watch Scilab Spoken Tutorials- http://spoken-tutorial.org/tutorial-search/?search_foss=Scilab&amp;search_language=English\r\n '
predict_spam(string)

'''
