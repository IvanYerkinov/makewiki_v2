from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Page
        fields = ['title', 'author', 'content']

# class nameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', maxlength=100)
