from django.db import models

class Question(models.Model):

    question_text = models.CharField(max_length=60)
    closed = models.BooleanField(default=False)
    pub_date = models.DateField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(Question, related_name='choices',
                                 on_delete=models.CASCADE,
                                 null=True)
    choice_text = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text