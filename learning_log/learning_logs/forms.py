from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm): 
    class Meta: 
        model = Topic 
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['title','text']
        labels = {'title': '','text': ''}
        widgets = {'title': forms.Textarea(attrs={'cols': 80,'rows': 1}),
                    'text': forms.Textarea(attrs={'cols': 80})}