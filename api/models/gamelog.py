from django.db import models
from django.contrib.auth import get_user_model
from .player import Player

class GameLog(models.Model):
    game = models.CharField(max_length=100)
    yards = models.CharField(max_length=100)
    touchdowns = models.CharField(max_length=100)

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='gamelogs'
    )

    def __str__(self):
        return f"'{self.game}' - yardage total & touchdowns '{self.yards}' - '{self.touchdowns}'"
