from django.shortcuts import render
from . import forms
from . import classifier
# Create your views here.

def index(request):
	#form for Email detection
	form = forms.Form_spam()
	#method is POST
	if request.method == "POST":
		form = forms.Form_spam(request.POST)
		if form.is_valid():
			#find data in textArea
			string=form.cleaned_data['text']
			#predict it is spam or not
			value = classifier.predict_spam(string)[0]
			print(value)
			#pass prediction to template and render it
			return render(request,'home/index.html',{'form':form,'value':value})

	return render(request,'home/index.html',{'form':form})