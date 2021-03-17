from django.db import models

class Match(models.Model):
    first_team = models.CharField(max_length=30)
    second_team = models.CharField(max_length=30)
    date = models.CharField(max_length=20, null=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    league = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.first_team} - {self.second_team}"


class League(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name