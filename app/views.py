from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.

def index(request):
     return render(request,'home.html')



def add_user(request):
    if 'user' in request.session:
        data=User.objects.get(username=request.session['user'])
        data.email
        
        if request.method=="POST":
                fname=request.POST['fname']
                lname=request.POST['lname']
                uname=request.POST['uname']
                password=request.POST['password']
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)
                user.save()
                return HttpResponse('Data saved')
        else:
                return render(request,'form.html')
    else:
        return redirect(login_user)
            

def login_user(request):

    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['password']
        login=auth.authenticate(username=uname,password=password)
        if login:
            request.session['user']=uname
            auth.login(request,login)
        else:
            return HttpResponse('User not exist')
    else:
        return render(request,'home.html')
    
    
def logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect('index')