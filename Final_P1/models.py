from django.db import models


class studentInfo(models.Model):
    userName = models.CharField(max_length=100)
    lookingforComp = models.BooleanField(default=False)
    lookingforCasual = models.BooleanField(default=False)

    def __str__(self):
        return self.userName


#
class favorite(models.Model):
    favoriteGame = models.CharField(max_length=100)
    favoriteCharacter = models.CharField(max_length=100)
    favoriteGenre = models.CharField(max_length=100)

    def __str__(self):
        return self.favoriteGame


class clubs(models.Model):
    clubsCurrentlyIn = models.CharField(max_length=100)
    clubsKnowAbout = models.CharField(max_length=100)
    esportsClub = models.BooleanField(default=False)

    def __str__(self):
        return self.clubsCurrentlyIn

# 3 forms first one is  username, grade. and major,
#  second is favorite character, favoirtge game, favorite genra
# Looking for team. Looking for comp, looking for casual
