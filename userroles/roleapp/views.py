from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def index(request):
    return render(request, "index.html")

def staff(request):

    return render(request, "staffs.html")



def admins(request):

    return render(request, "admins.html")

def editor(request):
    return render(request, "editors.html" )