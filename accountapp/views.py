from django.http import HttpResponse        # HttpResponse(화면에 띄울 값)
from django.shortcuts import render     # render(변수, 불러올 파일)

# Create your views here.


def hello_world(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD'})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'POST METHOD'})