from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
import types, random

from .models import TheWord

secret_word = 0
debug = True

class TheOnlyView(generic.DetailView):
    model = TheWord
    template_name = 'hanger/index.html'
    
def initial_view(request):
    global secret_word, debug
    secret_word = TheWord.objects.get(pk=random.randint(1, TheWord.objects.count()))
    secret_word.my_init(request)
    request.session.flush() #######################
    return render(request, 'hanger/guess.html', {
            'status_message': 'Guess a letter',
            'the_word' : secret_word,
            'debug' : debug,
        })
    
def make_a_guess(request):
    global secret_word
    new_letter = request.GET.get('guess_letter', '')
    if (new_letter.upper() == '*')or(isinstance(secret_word, int)):
        return initial_view(request)
        #return redirect('initial_view')
    elif new_letter == '' or not new_letter.isalpha():
        status_msg = 'Enter a letter, please'
    elif secret_word.letter_used(new_letter):
        status_msg = '"' + new_letter + '" has been already used'
    else:
        status_msg = 'You entered "' + new_letter.upper() + '"'
        if secret_word.check_letter(new_letter):
            status_msg += ' and hit!'
            if secret_word.solved():
                status_msg += ' You won! Click Restart'
        else:
            status_msg += ' and missed.'
            if secret_word.lost():
                status_msg += ' You lost! The word was "' + secret_word.word + '". Click Restart'
    return render(request, 'hanger/guess.html', {
            'status_message': status_msg,
            'the_word': secret_word,
            'debug' : debug,
    })