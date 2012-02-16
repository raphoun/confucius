from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from confucius.models import Account
from confucius.widgets import ForeignKeySearchInput


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        widgets = {
            'languages': ForeignKeySearchInput(),
        }
        
class AdminAccountForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30)
    
    class Meta:
        model = Account
        widgets = {
            'languages': CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(AdminAccountForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.first_name
        self.fields['last_name'].initial = self.instance.last_name
            
    def save(self, *args, **kwargs):
        self.instance.user.first_name = self.cleaned_data['first_name']
        self.instance.user.last_name = self.cleaned_data['last_name']
        self.instance.user.save()
        return super(AdminAccountForm,self).save(*args, **kwargs)
