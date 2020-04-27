from django import forms
from .models import Link, Comment

class LinkForm(forms.ModelForm):

    class Meta:
        model=Link
        fields=('title', 'url')

    def save(self, commit=True):
        new_link=super().save(commit=False)
        title=self.cleaned_data['title']
        url=self.cleaned_data['url']
        if commit:
            new_link.save()
        return new_link    


class CommentModelForm(forms.ModelForm):
    
    class Meta:
        model=Comment
        fields=('body',)

    def save(self, commit=True):
        newcomment=super().save(commit=False)
        body=self.cleaned_data['body']
        if commit:
            newcomment.save()
        return newcomment    
