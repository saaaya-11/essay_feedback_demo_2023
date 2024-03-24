from django import forms

class essayForm(forms.Form):
    essay=forms.CharField(widget=forms.Textarea)

