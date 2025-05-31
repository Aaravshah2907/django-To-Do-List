from django import forms
from .models import ToDoList, Item

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)


    def save(self, user):
        text = self.cleaned_data['name']
        lst = ToDoList(name=text, user=user)
        lst.save()
        return lst