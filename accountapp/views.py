from django.http import HttpResponse        # HttpResponse(화면에 띄울 값)
from django.shortcuts import render     # render(변수, 불러올 파일)

# Create your views here.


def hello_world(request):

    temp = request.POST.get('input_text')

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html',
                      context={'text': temp})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'POST METHOD'})