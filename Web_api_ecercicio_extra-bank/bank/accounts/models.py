from django.db import models


class Account(models.Model):

    owner = models.CharField(max_length=45)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def credit(self, value):
        self.balance += value

    def debit(self, value):
        self.balance -= value

    class Meta:
        ordering = ('owner',)
