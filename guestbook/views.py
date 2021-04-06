from django.shortcuts import render, redirect
from guestbook.models import Guestbook

# Create your views here.
def index(request):
    results = Guestbook.objects.all()
    data = {'guestbooklist' : results}
    return render(request, 'guestbook/index.html', data)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.content = request.POST['content']

    guestbook.save()

    return redirect('guestbook/')

def delete(request):
    guestbook = Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password'])
    guestbook.delete()
 
    return redirect('guestbook/')
def deleteform(request):
    return render(request, 'guestbook/deleteform.html')