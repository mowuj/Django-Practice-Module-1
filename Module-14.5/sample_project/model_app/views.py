from django.shortcuts import render
from . models import PracticeModel
from . forms import PracticeModelForm
# Create your views here.
def index(request):
    form=PracticeModelForm
    return render (request,'index.html',{'form':form})