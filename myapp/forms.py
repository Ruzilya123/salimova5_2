from django import forms

CHOICES = (
    ('fant', 'фантастика'),
    ('science', 'научное')
)

class Form(forms.Form):
    title = forms.CharField(label='название', max_length=100)
    url = forms.CharField(label='ссылка', max_length=100)
    content = forms.CharField(label='контент', max_length=100)
    is_pub = forms.BooleanField(label='публиковать?')
    categories = forms.ChoiceField(label='категория', choices=CHOICES)
    date_of_pub = forms.DateField(label='дата публикации')

