from django.db import models

class TheWord(models.Model):
    word = models.CharField(max_length=50) #'abracadabra'
    #guessed = '_'*len(word)
    max_wrong_attempts = 10
    
    def not__init__(self):
        self.request = 0 #request
        #dummy = TheWord.objects.get(pk=1).word
        #self.word = 'dummy'

    def my_init(self, request):
        self.request = request
        #self.word = word
        self.hint = "_" * len(self.word)
        self.used_letters = ''
        self.wrong_attempts = 0
        
    def check_letter(self, letter):
        letter = letter.upper()
        self.add_used(letter)
        retvalue = letter in self.word.upper()
        if retvalue:
            for i in range(len(self.word)):
                if self.word[i].upper() == letter:
                    self.hint = self.hint[:i] + letter + self.hint[i+1:]
            self.save_hint()
        else:
            self.add_miss()
        return retvalue
        
    def add_miss(self):
        self.wrong_attempts += 1
    
    def solved(self):
        return not "_" in self.hint
        
    def lost(self):
        return self.wrong_attempts >= 10
        
    def finished(self):
        return self.solved() or self.lost()
        
    def attempts_left(self):
        return self.max_wrong_attempts - self.wrong_attempts
    
    def add_used(self, letter):
        self.used_letters += letter
        self.request.session['guessed'] = self.used_letters
    
    def letter_used(self, letter):
        return letter in self.used_letters

    def save_hint(self):
        self.request.session['hint'] = self.hint

    def get_hint(self):
        last_hint = self.request.session.get('hint', False);
        if not last_hint:
            last_hint = '_' * len(self.secret_word)
            request.session['hint'] = last_hint
        return last_hint
        
    def get_answer(self):
        return self.word
	
    def __str__(self):
        return self.word + ' (' + '_'*len(self.word)+ ')' #guessed
        
    def guessing_string(self):
        return '_'*len(self.word)