from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'main/index.html')


def handler500(request):
    return render(request, 'main/index.html')