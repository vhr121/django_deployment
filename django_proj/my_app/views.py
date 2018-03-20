from django.shortcuts import render
from my_app.forms import My_form
# Create your views here.
def about(request):
    return render(request,'my_app/about.html')

def register(request):
    form=My_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            dict={}
            form.save()
            return render(request,'my_app/thanks.html',context=dict)


    dict={'my_form':form}
    return render(request,'my_app/register.html',context=dict)
