from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
import types, random

from .models import Words, Hangers

debug = True

def initial_view(request):
    global debug
    secret_word = Words.objects.get(pk=random.randint(1, Words.objects.count()))
    hanger = Hangers(request, secret_word.word)
    hanger.save_to_cookies()
    #request.session.flush()
    return render(request, 'hanger/guess.html', {
            'status_message': 'Guess a letter',
            'the_word' : hanger,
            'debug' : debug,
        })
    
def make_a_guess(request):
    new_letter = request.GET.get('guess_letter', '')#[0].upper()
    hanger = Hangers(request)
    if (new_letter.upper() == '*'): #or(not isinstance(secret_word, TheWord)):
        return initial_view(request)
    if not new_letter.isalpha():
        status_msg = 'Enter a letter, please'
    elif hanger.letter_used(new_letter[0].upper()):
        status_msg = '"' + new_letter[0].upper() + '" has already been used'
    else:
        status_msg = 'You entered "' + new_letter[0].upper() + '"'
        if hanger.check_letter(new_letter):
            status_msg += ' and hit!'
            if hanger.solved():
                status_msg += ' You won! Click Restart'
        else:
            status_msg += ' and missed.'
            if hanger.lost():
                status_msg += ' You lost! The word was "' + hanger.secret_word + '". Click Restart'
    return render(request, 'hanger/guess.html', {
            'status_message': status_msg,
            'the_word': hanger,
            'debug' : debug,
    })

def show_me_func(request):
    return HttpResponse(True)