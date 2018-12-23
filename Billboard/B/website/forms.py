from django.forms import ModelForm
from website.models import *

class Form(ModelForm):
    class Meta:
        model = CommentData
        fields = ['nickname', 'comment']
