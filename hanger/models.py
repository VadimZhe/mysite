from django.db import models

class TheWord(models.Model):
    word = models.CharField(max_length=50) #'abracadabra'
    #guessed = '_'*len(word)
	
    def __str__(self):
        return self.word + ' (' + '_'*len(self.word)+ ')' #guessed
        
    def guessing_string(self):
        return '_'*len(self.word)