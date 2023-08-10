from django.shortcuts import render

# Create your views here.
def marvel_bootstrap(request):
    return render(request,'marvel_bootstrap.html')
