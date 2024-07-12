from django import forms
from master.models import ProductSubCategory,ProductBrand


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategory
        fields = ['company','model_name','image','ram','price']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = ProductBrand
        fields = ['name']
        