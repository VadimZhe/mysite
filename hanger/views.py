from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import TheWord


class TheOnlyView(generic.DetailView):
    model = TheWord
    template_name = 'hanger/index.html'

def current_guessing(request, max_len):
    last_guessing = request.session.get('guessing', False);
    if not last_guessing:
        last_guessing = '_' * max_len
        request.session['guessing'] = last_guessing
    return last_guessing
    
def simple_view(request):
    first_word = TheWord.objects.get(pk=1).word
    return render(request, 'hanger/guess.html', {
            'status_message': 'Make your guess',
            'guessing': current_guessing(request, len(first_word)),
        })
    #return HttpResponse(first_word.guessing_string())
    
def make_a_guess(request):
    first_word = TheWord.objects.get(pk=1).word
    already_guessed = request.session.get('guessed', '')
    new_letter = request.GET.get('guess_letter', '')
    if new_letter == '' or not new_letter.isalpha():
        status_msg = 'Enter a letter, please'
    elif new_letter.upper() in already_guessed:
        status_msg = '"' + new_letter + '" has been already used'
    else:
        status_msg = 'You entered "' + new_letter.upper() + '"'
        already_guessed += new_letter.upper()
        request.session['guessed'] = already_guessed
    the_guessing = current_guessing(request, len(first_word))
    return render(request, 'hanger/guess.html', {
            'status_message': status_msg,
            'guessing': the_guessing,
            'guessed': already_guessed
    })