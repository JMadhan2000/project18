from django.shortcuts import render

# Create your views here.
def bootstrap2(request):
    return render(request,'bootstrap2.html')

def bootstrap2_cdn(request):
    return render(request,'bootstrap2_cdn.html')

def bootstrap(request):
    return render(request,'bootstrap.html')

def madhan1(request):
    return render(request,'madhan1.html')

def badges(request):
    return render(request,'badges.html')

def button_group(request):
    return render(request,'button_group.html')