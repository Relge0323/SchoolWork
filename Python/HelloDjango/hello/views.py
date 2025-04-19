from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    # create a string that makes the text
    # appear in the middle of the page and
    # in a bigger font.  use html/css/.js possibly
    return render(request, 'hello/home.html')
