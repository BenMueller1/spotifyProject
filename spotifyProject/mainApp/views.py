from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # NOTE: this finds index.html in the directory that we have told django that template files are located
    # to change this directory, go to settings.py and edit DIRS in TEMPLATES