from django import forms


class SearchForm(forms.Form):
    search_word = forms.CharField(label="Search!", max_length=100)