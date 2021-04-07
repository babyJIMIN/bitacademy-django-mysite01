from django.urls import path

import main.views
import guestbook.views
import board.views
import user.views

urlpatterns = [
    path('', main.views.index, name='index'),

    path('user/signupform', user.views.signupform, name='user/signupform'),
    path('user/signinform', user.views.signinform, name='user/signinform'),
    path('user/updateform', user.views.updateform, name='user/updateform'),
    path('user/joinsuccess', user.views.joinsuccess, name='user/joinsuccess'),
    path('user/singup', user.views.signup, name='user/signup'),
    path('user/signin', user.views.signin, name='user/signin'),
    path('user/logout', user.views.logout, name='user/logout'),
    path('user/update', user.views.update, name='user/update'),

    path('guestbook/', guestbook.views.index, name='guestbook/'),
    path('guestbook/add', guestbook.views.add, name='guestbook/add'),
    path('guestbook/delete', guestbook.views.delete, name='guestbook/delete'),
    path('guestbook/deleteform', guestbook.views.deleteform, name='guestbook/deleteform'),

    path('board/', board.views.index, name='board/'),
    path('board/view', board.views.view, name='board/view'),
    path('board/write', board.views.write, name='board/write'),
    path('board/modify', board.views.modify, name='board/modify'),
]