from django import forms

class TextForm(forms.Form):
    fasta_text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Paste fasta here ...'}))

class FileForm(forms.Form):
    fasta_file = forms.FileField()

class RadioSelect(forms.Form):
    choices = forms.RadioSelect()