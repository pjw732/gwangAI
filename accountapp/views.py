from django.http import HttpResponse        # HttpResponse(화면에 띄울 값)
from django.shortcuts import render     # render(변수, 불러올 파일)

# Create your views here.


def Hello_world(request):
    return render(request, 'base.html')