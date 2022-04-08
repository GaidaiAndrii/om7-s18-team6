from django import forms

from authentication.models import CustomUser


class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 'is_active']


    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        self.fields['email'] = forms.CharField(
            widget=forms.EmailInput(attrs={'placeholder': ('Email address')})
        )

        self.fields['password'] = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'placeholder': ('Password')
            }),
            error_messages={
                'required': ('Please enter your password.'),
            }) 

        