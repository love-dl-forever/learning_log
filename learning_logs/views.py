from django.shortcuts import render

# Create your views here.
def index(request):
    """学习笔记首页"""
    return render(request,'learning_logs/index.html')