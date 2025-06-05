from django import forms
from .models import Car, Brand

class CarForm(forms.Form):
    model = forms.CharField(label='Model', max_length=100)
    brand = forms.CharField(label='Brand', max_length=100)
    year = forms.IntegerField(label='Year')
    value = forms.DecimalField(label='Value', max_digits=10, decimal_places=2)
    image = forms.ImageField(label='Image', required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    
    
    def save(self):
      car = Car(
          model=self.cleaned_data['model'],
          brand=self.cleaned_data['brand'],
          year=self.cleaned_data['year'],
          value=self.cleaned_data['value'],
          image=self.cleaned_data['image'],
          description=self.cleaned_data['description']
      )