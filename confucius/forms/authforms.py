from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from confucius.models import Account, ConferenceAccountRole


class AdminAccountForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30)
    is_active = forms.BooleanField(required=False)

    class Meta:
        model = Account

    def __init__(self, *args, **kwargs):
        super(AdminAccountForm, self).__init__(*args, **kwargs)
        try:
            self.fields['first_name'].initial = self.instance.first_name
            self.fields['last_name'].initial = self.instance.last_name
            self.fields['is_active'].initial = self.instance.is_active
        except Exception:
            pass

    def save(self, *args, **kwargs):
        if self.instance.pk == None:
            self.instance = Account.objects.create(self.cleaned_data[''], "kikou", self.cleaned_data['last_name'])

        self.instance.user.first_name = self.cleaned_data['first_name']
        self.instance.user.last_name = self.cleaned_data['last_name']
        self.instance.user.is_active = self.cleaned_data['is_active']
        self.instance.user.save()
        return super(AdminAccountForm, self).save(*args, **kwargs)


class ConferenceAccountRoleForm(forms.ModelForm):
    class Meta:
        model = ConferenceAccountRole
        widgets = {
            'role': CheckboxSelectMultiple(),
        }
