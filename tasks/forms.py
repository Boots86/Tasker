from django import forms

from models import *

class GroupForm(forms.Form):
	title = forms.CharField(max_length=255, label='Group Title', widget=forms.Textarea(
		attrs={
			'class': 'form-control'
		}
	))

	class Meta:
		model = Group

class CardForm(forms.Form):
	content = forms.CharField(max_length=255, label='', widget=forms.Textarea(
		attrs={
			'class': 'form-control',
			'placeholder': 'Add a New Card',
			'rows': '4'
		}
	))
	group_id = forms.IntegerField(widget=forms.HiddenInput())

	class Meta:
		model = Card