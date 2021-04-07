from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

def view(request):
    return render(request, 'board/view.html')

def write(request):
    return render(request, 'board/write.html')

def modify(request):
    return render(request, 'board/modify.html')

def reply(request):
    pass

def comment(request):
    pass
