from math import ceil

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from board import models

LIST_COUNT = 10                                 # 페이지당 글 개수

# Create your views here.
def index(request):
    results = models.alllist()
    data = {'postlist' : results}

    # 페이징 처리
    # page = int(request.GET.get('p', '1'))

    # totalcount = models.count()                 # 총 게시글 수
    # boardlist = models.findall(page, LIST_COUNT)

    # pagecount = ceil(totalcount / LIST_COUNT)   # 총 페이지 수
    # curpage = page
    # nextpage = curpage + 1
    # prevpage = curpage - 1

    
    return render(request, 'board/index.html', data)

def view(request):
    postno = request.GET.get('no')
    if postno is None:
        return HttpResponse('잘못된 접근입니다.')

    result = models.findbyno(postno)
    if result is None:
        return HttpResponse('게시글이 존재하지 않습니다.')

    data = {'post' : result}

    models.increment_hit(postno)

    return render(request, 'board/view.html', data)

def writeform(request):
    # Access Control
    authuser = request.session.get("authuser")
    if authuser is None:
        return redirect('user/signin')

    authuser = request.session["authuser"]
    result = models.findbyno(authuser["no"])
    data = {'data' : result}
        
    return render(request, 'board/writeform.html', data)

def write(request):
    # Access Control
    authuser = request.session.get("authuser")
    if authuser is None:
        return redirect('user/signin')

    title = request.POST.get('title')
    contents = request.POST.get('contents')
    user_no = request.session["authuser"]["no"]

    models.write(title, contents, user_no)

    return redirect('board/')

def updateform(request):
    # Access Control
    authuser = request.session.get("authuser")
    if authuser is None:
        return redirect('user/signin')

    postno = request.GET.get('no')
    if postno is None:
        return HttpResponse('잘못된 접근입니다.')

    result = models.findbyno(postno)
    if result is None:
        return HttpResponse('게시글이 존재하지 않습니다.')

    data = {'post' : result}

    return render(request, 'board/updateform.html', data)

def update(request):
    # Access Control
    authuser = request.session.get("authuser")
    if authuser is None:
        return redirect('user/signin')

    postno = request.POST.get('postno')
    if postno is None:
        return HttpResponse('잘못된 접근입니다.')

    result = models.findbyno(postno)
    if result is None:
        return HttpResponse('게시글이 존재하지 않습니다.')

    if authuser['no'] != result['user_no'] :
        return HttpResponse('작성자만 글을 수정할 수 있습니다.')

    title = request.POST.get('title')
    contents = request.POST.get('contents')

    models.update(title, contents, postno)

    return redirect(f'/board/view?no={postno}')

def delete(request):
    # Access Control
    authuser = request.session.get("authuser")
    if authuser is None:
        return redirect('user/signin')

    postno = request.GET.get('no')
    if postno is None:
        return HttpResponse('잘못된 접근입니다.')

    result = models.findbyno(postno)
    if result is None:
        return HttpResponse('게시글이 존재하지 않습니다.')

    if authuser['no'] != result['user_no'] :
        return HttpResponse('작성자만 글을 삭제할 수 있습니다.')

    models.delete(postno)

    return redirect('/board')

def reply(request):
    pass

def comment(request):
    pass

