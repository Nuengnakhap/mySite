from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:poll_id>/', views.detail, name='poll_detail'),
    path('detail/<int:poll_id>/create-comments/', views.comment, name='poll_comment'),
    path('detail/<int:poll_id>/question/', views.create_q, name='poll_question'),
    path('create/', views.create, name='create_poll'),
    # path('detail/<int:poll_id>/update/', views.update, name='update_poll'),
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('detail/<int:poll_id>/update/', views.update, name='update_poll'),
    path('delete/<int:poll_id>/', views.delete_poll, name='delete_poll'),
]
