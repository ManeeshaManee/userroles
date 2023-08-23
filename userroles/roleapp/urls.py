from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('staff/', views.staff, name="staff"),
    path('admins/', views.admins, name="admins"),
    path('editor/', views.editor, name="editor"),

]