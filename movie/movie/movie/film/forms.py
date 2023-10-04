from film.models import Movies
from django import forms
# for creating builtin forms in template
class Movieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields="__all__"