from django.db import models
from django.contrib.auth import get_user_model
# from .gamelog import GameLog

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    # gamelog = models.ForeignKey(
    #     GameLog,
    #     on_delete=models.CASCADE,
    #     related_name='GameLog'
    # )

    def __str__(self):
        return f"'{self.name}' plays '{self.position}' and is a member of the '{self.team}'"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'team': self.team
        }
