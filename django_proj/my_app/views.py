from django.shortcuts import render
from my_app.forms import User_details_form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def about(request):
    return render(request,'my_app/about.html')

def register(request):
    user_form=User_details_form(data=request.POST)
    registered=False
    if request.method == 'POST':

        if user_form.is_valid():
            registered=True
            print("working")
            dict={}
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            return render(request,'my_app/thanks.html',context=dict)

    dict={'User_Form':user_form,'is_registered':registered}
    return render(request,'my_app/register.html',context=dict)

def login_user(request):

    if request.method=='POST':

            dict={}
            u_name=request.POST.get('user_name')
            u_password=request.POST.get('user_password')
            user=authenticate(username=u_name,password=u_password)
            if user:

                if user.is_active:
                    # Log the user in.
                    login(request,user)

                    # Send the user back to some page.
                    # In this case their homepage.
                    return HttpResponseRedirect(reverse('index'))


            else:
                return render(request,'my_app/login_user.html',context={"message":"Invalid username or password"})

    return render(request,'my_app/login_user.html',context={"message":"Please enter the login details"})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
