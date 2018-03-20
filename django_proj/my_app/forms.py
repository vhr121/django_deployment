from my_app.models import User
from django.forms import ModelForm

class My_form(ModelForm):
    class Meta:
        model=User
        fields = '__all__'

form = My_form()
