from django.shortcuts import render
# import request
# Create your views here.
def home(request):
    return render(request,'home/basic.html')