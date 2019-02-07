from django import forms

class TextForm(forms.Form):
    fasta_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Paste fasta here ...'}))

class FileForm(forms.Form):
    fasta_file = forms.FileField()
    
class RadioSelect(forms.Form):
    choices = forms.RadioSelect()
