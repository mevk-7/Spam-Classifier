from django import forms

class Form_spam(forms.Form):
	#form with textArea
	text = forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'form-control'
		}
	))