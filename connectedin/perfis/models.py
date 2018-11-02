from django.db import models

class User(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    dt_birth = models.DateField()


class Profile(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='profiles')


class Post(models.Model):
    text = models.CharField(max_length=60)
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='timeline')


class Comment(models.Model):
    text = models.CharField(max_length=60)
    date = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                related_name='comments')


class Reaction(models.Model):
    REACTION_TYPE = (
        ('Curtir' , 1)
        ('Amar' , 2),
        ('HAHA', 3),
        ('HOOOHH', 4),
        ('GR', 5)
    )
    tipo = models.CharField(max_length=60, choices=REACTION_TYPE)
    date = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='messages')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='messages')
    weidht = models.IntegerField()