from django.shortcuts import render

# Create your views here.
def firstb(request):
    return render(request, 'firstb.html')

def secondb(request):
    return render(request, 'secondb.html')
