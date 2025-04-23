from django.shortcuts import render
# Create your views here.

def vmg(request):
    return render(request, 'website/mission-vision.html', )