from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def designer(request):
    return render(request,'designer.html')

def exhibitor(request):
    return render(request,'exhibitor.html')

def model(request):
    return render(request,'model.html')

def sponsor(request):
    return render(request,'sponsor.html')

