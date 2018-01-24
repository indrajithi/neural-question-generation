from django import forms

class NameForm(forms.Form):
    textin = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Input a paragraph', 'class': 'myclass'}), max_length=1000 )

class UploadFileForm(forms.Form):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'fileUpload'}))

