from django.shortcuts import render

# Create your views here.
def newIndex(request):
    return render(request,'index.html')