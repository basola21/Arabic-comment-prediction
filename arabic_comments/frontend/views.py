from django.shortcuts import render
from .forms import ArabicForm
from django.contrib import messages
from .models import arabic_input
from .scripts.prediction import predict

def index(request):
    home_page = 'frontend/index.html'
    if request.method == 'POST':
        form = ArabicForm(request.POST)
        prediction = predict(form['arabic_text'].value())
        form['prediction'].value = prediction

        if form.is_valid():
            form = ArabicForm()
            return render(request, home_page ,{'form':form,'prediction':prediction})
        else:
            messages.warning(request, "Please enter a valid comment in arabic")
            return render(request, home_page,{'form':form})
    else:
            
        form = ArabicForm()
        return render(request, home_page ,{'form':form})
