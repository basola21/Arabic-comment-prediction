from django.forms import ModelForm
from .models import arabic_input


class ArabicForm(ModelForm):

    class Meta :
        model = arabic_input
        fields = "__all__"
    
