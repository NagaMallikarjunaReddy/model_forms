from django.shortcuts import render
from app.forms import *
from app.models import *
# Create your views here.
def insert_topic(request):
    TFO=Topicform()
    d={'TFO':TFO}
    if request.method=="POST":
        TFD=Topicform(request.POST)
        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TD=Topic.objects.all()
            d1={'TD':TD}
            return render(request,'display.html',d1)
    return render(request,'topic.html',d)