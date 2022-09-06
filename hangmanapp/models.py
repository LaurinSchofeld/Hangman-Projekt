from datetime import date
from django.db import models

class ListItem(models.Model): 
    createted_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' ' + self.name


# Model fuer zur die Spiel Woerter
class GameWords(models.Model): 
    word = models.CharField(max_length=200)
    difficulty = models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.id) + ' ' + self.word


# Model fuer zur die Spieler
class Player(models.Model): 
    name = models.CharField(max_length=200)
    wins = models.SmallIntegerField(default=0)
    loses = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.id) + ' ' + self.name


# Model fuer Zwischenablage
class AktivWord(models.Model): 
    word = models.CharField(max_length=200)
    hitLocations = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id) + ' ' + self.word

<<<<<<< HEAD
class CheckLetters(models.Model): 
    checkedLetters = models.CharField(max_length=500)
    fails = models.SmallIntegerField(default=0)
=======

# Model fuer Zwischenablage
class AktivWord(models.Model): 
    word = models.CharField(max_length=200)
    hitLocations = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id) + ' ' + self.word

class CheckLetters(models.Model): 
    checkedLetters = models.CharField(max_length=500)
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
    
    def __str__(self):
        return str(self.id) + ' ' + self.checkedLetters