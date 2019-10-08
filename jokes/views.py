from django.shortcuts import redirect, render, get_object_or_404
from jokes.models import *


# Create your views here.
def list_jokes(request):
    jokes = Joke.objects.order_by('date')

    if 'q' in request.GET:
        jokes = jokes.filter(text__icontains=request.GET['q'])

    context = {
        'jokes': jokes,
    }

    return render(request, 'list_jokes.html', context)


def view_joke(request, id):
    joke = get_object_or_404(Joke, pk=id)

    context = {
        'joke': joke,
    }

    return render(request, 'view_joke.html', context)


def add_joke(request):
    context = {

    }

    if request.method == 'POST':
        if 'text' in request.POST:
            joke_text = request.POST['text']
            joke = Joke(text=joke_text)
            joke.save()

            return redirect('view_joke', joke.id)

    return render(request, 'add_joke.html', context)
