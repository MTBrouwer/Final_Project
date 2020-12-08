from django.db import models

class Player(models.Model):
    Name = models.CharField(max_length=100)
    UserName= models.CharField(max_length=100)
    Grade= models.CharField(max_length=100)
    Major = models.CharField(max_length=100)

    def __str__(self):
        return self.UserName, self.Grade, self.Major

class PlayerInterest(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    interests = models.CharField(max_length=100)

    def __str__(self):
        return self.interests


class PlayerFavoriteCharacter(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    favorite_char = models.CharField(max_length=100)

    def __str__(self):
        return self.favorite_char

