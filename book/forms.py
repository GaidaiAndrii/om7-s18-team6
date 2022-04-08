from django import forms
from django.core.exceptions import ValidationError

from author.models import Author
from book.models import Book


class BookForm(forms.ModelForm):

    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ["name", "description", "count", "authors"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-input'}),
            "description": forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].label_from_instance = lambda obj: f'{obj.name} {obj.surname} {obj.patronymic}'
