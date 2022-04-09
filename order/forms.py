from django import forms
from django.core.exceptions import ValidationError
from book.models import Book
from order.models import Order


class OrderForm(forms.ModelForm):


    plated_end_at = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Order
        fields = ["user", "book", "plated_end_at"]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f'{obj.first_name} {obj.last_name} {obj.id}'
        self.fields['plated_end_at'] = forms.DateField(widget=forms.SelectDateWidget)
