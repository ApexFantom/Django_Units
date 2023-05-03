from .models import Students
from django.forms import ModelForm

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'second_name']