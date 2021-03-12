# function when the user visits the urls

from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Homepage')
    return render(request, 'homepage.html')


def about(request):  # sent back simple response
    # return HttpResponse('about')
    return render(request, 'about.html')
