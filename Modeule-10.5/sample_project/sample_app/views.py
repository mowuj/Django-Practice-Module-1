from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    data={"name":"ahsan habib","age":27,"birthday":datetime.datetime.now(),'des':'Right now i learn Django','list1':{'i', 'love', "python" },'courses':[
        {
            'id': 1,
            'name': 'Python',
            'from':'Creative IT'
        },
        {
            'id': 2,
            'name': 'React',
            'from':'Programming Hero'
        },
        {
            'id': 3,
            'name': 'CSE Fundamental',
            'from':'Phitron'
        },
    ]}
    return render(request,'home.html',{'data':data})