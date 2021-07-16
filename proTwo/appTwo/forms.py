from django import forms
from appTwo.models import User

#CREATE CLASS
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    