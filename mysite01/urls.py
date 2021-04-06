from django.urls import path

import main.views
import guestbook.views
import board.views

urlpatterns = [
    path('', main.views.index, name='index'),

    path('guestbook/', guestbook.views.index, name='guestbook/'),
    path('guestbook/add', guestbook.views.add, name='guestbook/add'),
    path('guestbook/delete', guestbook.views.delete, name='guestbook/delete'),
    path('guestbook/deleteform', guestbook.views.deleteform, name='guestbook/deleteform'),

    path('board/', board.views.index, name='board/'),
]