from django.shortcuts import render
# Create your views here.

def mission(request):
    return render(request, 'website/mission-vision.html', )