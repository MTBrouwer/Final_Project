from django.db import models
# Create your models here.

class Player(models.Model):
    Name:   models.CharField(max_length=100)
    UserName: models.CharField(max_length=100)
    Grade: models.DecimalField(max_digits=1)
    Major: models.CharField(max_length=100)

    def __str__(self):
        return self.description

class PlayerInterest(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    interests = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class PlayerFavoriteCharacter(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    favorite_char = models.CharField(max_length=100)

    def __str__(self):
        return self.description