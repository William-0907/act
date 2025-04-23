from django.shortcuts import render

def chart(request):
    return render(request, 'chartjs/chart.html')

