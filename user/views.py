from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from user import models

# Create your views here.
def signupform(request):
    return render(request, 'user/signupform.html')

def signinform(request):
    return render(request, 'user/signinform.html')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')



def signup(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    models.insert(name, email, password, gender)

    return redirect('user/joinsuccess')

def signin(request):
    email = request.POST.get('email', False)
    password = request.POST.get('password', False)

    result = models.findby_email_and_password(email, password)
    if result is None:
        return HttpResponseRedirect('/user/signinform?result=fail')

    request.session["authuser"] = result    # 튜플로 저장
    return redirect('index')

def logout(request):
    # Delete a session value
    del request.session['authuser']
    return redirect('index')

def updateform(request):
    # Access Control
    authuser = request.session.get("authuser")
    if authuser is None:
        return redirect('index')

    no = authuser["no"]
    # Set a session value
    result = models.findbyno(no)
    data = {'authuser' : result}

    return render(request, 'user/updateform.html', data)

def update(request):
    # Access Control
    authuser = request.session.get("authuser")
    if authuser is None:
        return redirect('index')

    no = authuser['no']
    name = request.POST.get('name')
    password = request.POST.get('password')
    gender = request.POST.get('gender')

    models.update(name, password, gender, no)

    # session 처리
    update_authuser = models.findbyno(no)
    request.session['authuser'] = update_authuser

    return redirect('index')