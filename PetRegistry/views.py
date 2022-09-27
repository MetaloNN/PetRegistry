from django.shortcuts import render
from PetRegistry.models import Pet

# Create your views here.

def index(request):

    pets = Pet.objects.all()


    return render(request, 'PetRegistry/index.html', {'pets': pets})

def form(request):
    
    return render(request, 'PetRegistry/form.html')