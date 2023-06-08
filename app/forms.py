from django import forms
from app.models import *
class Topicform(forms.Form):
    topic_name=forms.CharField(max_length=100)
