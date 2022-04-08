from django import forms

from author.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        # widgets = {
        #     "name": forms.TextInput(attrs={'class': 'form-input'}),
        #     "surname": forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        # }
