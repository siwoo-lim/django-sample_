from django.shortcuts import render
from .forms import *

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'write.html', {'form' : form})

def load(request):
    CommentList = CommentData.objects.all()
    return render(request, 'load.html', {'commentlist' : CommentList})
