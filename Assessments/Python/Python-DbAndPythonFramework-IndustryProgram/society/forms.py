from django import forms
from .models import Members,Watchmans,Chairmans,Visitors


class ChairmanForm(forms.ModelForm):
    class Meta:
        model = Chairmans 
        fields = ['first_name', 'last_name' , 'email' , 'mobile']

class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['first_name' , 'last_name' , 'email' , 'mobile']


class WatchmenForm(forms.ModelForm):
    class Meta:
        model = Watchmans
        fields = ['first_name' , 'last_name' , 'email' , 'mobile']


class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = '__all__'