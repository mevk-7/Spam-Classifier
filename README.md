# Spam-Classifier
SPAM_CLF 	: Codes and other file for training models
			: File include :- Data_set.csv provide data for training classifier
						   :- Spam.py python script to trained model
						   :- Spam.ipynb Python jupyter notebook for same
						   :- spam.pickle binary file of  saved trained naivebayes model
						   :- vect.pickle binary file of CountVectorize
			Approach used: extract text from html text and remove all non alpha-numeric word and the counter vectorize it and then use naive bayes to train model

env 		:Python virtual environment 
			:To activate in windows type in terminal:env/Scripts/activate
			:In linux type :source env/Scripts/activate

spam 		:django folder
			:folder included  :- home,spam,templates
							  :  home -> home app to for spam detection
							  :  spam -> main spam django project folder
							  :  templates -> all  templates saved here

How to run: 		0. Activate virtual environment 
			1. Go to spam folder
			2. Run manage.py runserver on terminal
			3. Note local address display on terminal
			4. Go to that address on browser
			5. Now enter your forum text
			6. Hit submit button
			7. Message will be dispaly that post is spam or not	


Refrences:  1.http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
			2.https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
			3.https://stackoverflow.com/questions/4511412/currently-best-spam-filter-algorithm
			4.https://www.crummy.com/software/BeautifulSoup/bs4/doc/
			5.http://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayess
