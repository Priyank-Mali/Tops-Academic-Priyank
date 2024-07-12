from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name' , 'last_name' , 'email' , 'mobile']
        # fields = '__all__'

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}),
        #     'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last Name'}),
        #     'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),
        #     'mobile' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Mobile Number'}),
        # }
