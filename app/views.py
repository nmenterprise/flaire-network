from django.shortcuts import render,redirect
from .models import TextModel


def createText(request):
    if request.method == 'POST':
        clipboard_value = request.POST.get('clipboard')
        TextModel.objects.create(clipboard=clipboard_value)
        
        return redirect('https://google.com')
    else:
        return render(request, 'index.html')