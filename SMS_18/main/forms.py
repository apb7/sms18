
from django import forms
import re
from django.core import validators

class TransactionForm(forms.Form):
	stockname = forms.CharField(required = True,max_length=50)
	units = forms.IntegerField(required = True)