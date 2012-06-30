from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

class Game(models.Model):
    players = models.ManyToManyField(User, through='Score')
    board = models.ForeignKey(Board)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.board.name + " " + self.created

class Score(models.Model):
    player = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    score = models.IntegerField()

    def __unicode__(self):
        return self.player.username
