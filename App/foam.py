from django import forms


class shipping(forms.Form):
    firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    lastname = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    country = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your country name'}))
    areaCode = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Area code'}))
    primaryPhone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter your primary Phone'}))
    address1= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your address1'}))
    zipcode= forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter your zipcode'}))