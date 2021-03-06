# Generated by Django 3.1.3 on 2020-12-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final_P1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubsCurrentlyIn', models.CharField(max_length=100)),
                ('clubsKnowAbout', models.CharField(max_length=100)),
                ('esportsClub', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favoriteGame', models.CharField(max_length=100)),
                ('favoriteCharacter', models.CharField(max_length=100)),
                ('favoriteGenre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='studentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('lookingforComp', models.BooleanField(default=False)),
                ('lookingforCasual', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='playerfavoritecharacter',
            name='player',
        ),
        migrations.RemoveField(
            model_name='playerinterest',
            name='player',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='PlayerFavoriteCharacter',
        ),
        migrations.DeleteModel(
            name='PlayerInterest',
        ),
    ]
