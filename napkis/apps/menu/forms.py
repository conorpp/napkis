from django import forms

    #menu = raw.get('menu', None)
    #name = raw.get('name', None)
    #decription = raw.get('decription', None)
    #price = raw.get('price', None)
    #date = raw.get('date', None)
    #meal = raw.get('date', None)
    
class MenuItemForm(forms.Form):
    menu = forms.CharField(max_length=10000)
    description = forms.CharField(max_length=10000)
    price = forms.CharField(max_length=10000)
    date = forms.CharField(max_length=10000)
    meal = forms.CharField(max_length=10000)
    name = forms.CharField(max_length=10000)
    