from django.shortcuts import render


def dashboard(request):
    return render(request, 'temp_dashboard/index.html')
